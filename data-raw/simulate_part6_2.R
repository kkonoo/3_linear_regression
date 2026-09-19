## ─────────────────────────────────────────────────────────────
## Part 6-II 실습 자료 생성 — 시계열 · 공간 · 혼합효과
##   출력 : cgm_glucose.csv       연속혈당측정(CGM) 14일, 15분 간격
##          visium_spots.csv      Visium 유사 공간전사체 600 spot x 50 유전자
##          visium_truth.csv      유전자별 참값
##          family_cohort.csv     KNU-Family 300가계 x 5명
##          family_geno.csv.gz    가계 코호트 귀무 SNP 1000개
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260922)

## ══ 1. CGM — 한 사람의 14일 혈당 ════════════════════════════
per   <- 96                                  # 하루 96점 (15분)
n_day <- 14
tt    <- 0:(n_day * per - 1)
day   <- tt / per                            # 경과 일수
hour  <- (tt %% per) / 4                     # 시각 (0 ~ 23.75)
dayn  <- floor(day) + 1
wkend <- as.integer(dayn %in% c(6, 7, 13, 14))

## 추세: 식이 조절 시작 후 하루 1.2 mg/dL씩 감소
tr_trend <- 150 - 1.2 * day
## 불규칙 순환: 6~8일째 감기(스트레스 고혈당) — 주기 없음
tr_cycle <- 14 * exp(-((day - 7) / 0.8)^2)
## 계절성(하루 주기): 새벽 현상 + 식후 반응 (시각·크기가 매일 조금씩 다름)
meal <- numeric(length(tt))
for (d in 1:n_day) {
  idx <- which(dayn == d)
  t0  <- c(7.5, 12.5, 18.5) + rnorm(3, 0, 0.4)
  A   <- c(35, 45, 55) * exp(rnorm(3, 0, 0.2)) *
    ifelse(d %in% c(6, 7, 13, 14), 1.3, 1)
  for (k in 1:3) {
    dt <- hour[idx] - t0[k]
    meal[idx] <- meal[idx] +
      ifelse(dt > 0, A[k] * (dt / 0.9) * exp(1 - dt / 0.9), 0)
  }
}
dawn <- 8 * exp(-((hour - 6) / 1.5)^2)
tr_season <- dawn + meal
## 정상 성분: AR(1), 식후에 분산이 커짐 (이분산)
phi <- 0.8
sdt <- 3 * (1 + meal / 30)
x <- numeric(length(tt)); x[1] <- rnorm(1, 0, 5)
for (i in 2:length(tt)) x[i] <- phi * x[i - 1] + sdt[i] * rnorm(1)
glucose <- round(tr_trend + tr_cycle + tr_season + x +
                   rnorm(length(tt), 0, 2))

cgm <- data.frame(t = tt, day = round(day, 4), dayn = dayn,
                  hour = hour, weekend = wkend, glucose = glucose,
                  true_trend = round(tr_trend, 3),
                  true_cycle = round(tr_cycle, 3),
                  true_season = round(tr_season, 3))

## ══ 2. Visium 유사 공간전사체 — 피질 절편 ═══════════════════
nr <- 25; nc <- 24
gd <- expand.grid(col = 0:(nc - 1), row = 0:(nr - 1))
sx <- gd$col + 0.5 * (gd$row %% 2)           # 육각 격자
sy <- gd$row * sqrt(3) / 2                   # spot 중심 간격 = 1
ns <- nrow(gd)
depth  <- sy                                 # 연질막(0)에서 백질 방향
region <- ifelse(depth > 0.8 * max(depth), "WM", "GM")
D <- as.matrix(dist(cbind(sx, sy)))
gp <- function(s2, rho) {
  as.vector(t(chol(s2 * exp(-D / rho))) %*% rnorm(ns))
}

G <- matrix(0, ns, 50)
colnames(G) <- sprintf("g%02d", 1:50)
vt <- data.frame(gene = colnames(G), is_svg = 0L, trend = 0,
                 sigma2_sp = 0, range = NA_real_, tau2_gm = 0.25,
                 tau2_wm = 0.25)
## g01: 깊이 추세 + 공간장 + 영역별 이분산
tau_g01 <- ifelse(region == "WM", 0.6, 0.35)
G[, 1] <- 1.5 + 0.10 * depth + gp(0.30, 3) + rnorm(ns, 0, tau_g01)
vt[1, 2:7] <- list(1L, 0.10, 0.30, 3, 0.35^2, 0.6^2)
## g02 ~ g10: 공간변이 유전자 (SVG)
for (j in 2:10) {
  s2 <- runif(1, 0.10, 0.40); rho <- runif(1, 1.5, 5)
  G[, j] <- 1 + gp(s2, rho) + rnorm(ns, 0, 0.4)
  vt[j, 2:7] <- list(1L, 0, round(s2, 4), round(rho, 3),
                     0.16, 0.16)
}
## g11 ~ g50: 공간 패턴 없음
for (j in 11:50) G[, j] <- 1 + rnorm(ns, 0, 0.5)

vis <- data.frame(spot = sprintf("S%03d", 1:ns), row = gd$row,
                  col = gd$col, x = round(sx, 4), y = round(sy, 4),
                  depth = round(depth, 4), region = region,
                  round(G, 3))

## ══ 3. KNU-Family — 핵가족 300가계 ══════════════════════════
nf <- 300; fs <- 5; nfam <- nf * fs
role <- rep(c("father", "mother", "child", "child", "child"), nf)
fid  <- rep(sprintf("F%03d", 1:nf), each = fs)
iid  <- sprintf("%s_%d", fid, rep(1:fs, nf))
pat  <- ifelse(role == "child", sprintf("%s_1", fid), "0")
mat  <- ifelse(role == "child", sprintf("%s_2", fid), "0")
fa <- which(role == "father"); mo <- which(role == "mother")
ch <- which(role == "child")
par_f <- rep(fa, each = 3); par_m <- rep(mo, each = 3)

## 멘델 전달: 창시자 대립유전자 2개 → 자녀는 부모에게서 하나씩
transmit <- function(maf) {
  h1 <- h2 <- integer(nfam)
  fd <- c(fa, mo)
  h1[fd] <- rbinom(length(fd), 1, maf)
  h2[fd] <- rbinom(length(fd), 1, maf)
  pick <- function(p) ifelse(runif(length(p)) < 0.5, h1[p], h2[p])
  h1[ch] <- pick(par_f); h2[ch] <- pick(par_m)
  h1 + h2
}
snp_LDLR <- transmit(0.27)
Gn <- sapply(runif(1000, 0.05, 0.5), transmit)
colnames(Gn) <- sprintf("rs%04d", 1:1000)

## 다유전자 배경 (무한소 모형): 자녀 = 부모 평균 + 멘델 표집 편차
s2g <- 0.19; s2e <- 0.19                     # h2 = 0.5
gpoly <- numeric(nfam)
gpoly[c(fa, mo)] <- rnorm(2 * nf, 0, sqrt(s2g))
gpoly[ch] <- (gpoly[par_f] + gpoly[par_m]) / 2 +
  rnorm(length(ch), 0, sqrt(s2g / 2))

sex <- ifelse(role == "father", 1L,
              ifelse(role == "mother", 0L, rbinom(nfam, 1, 0.5)))
age <- round(ifelse(role == "father", rnorm(nfam, 60, 6),
                    ifelse(role == "mother", rnorm(nfam, 57, 6),
                           rnorm(nfam, 31, 5))))
bmi <- round(rnorm(nfam, 24, 3.1), 1)
ldl <- round(2.55 + 0.28 * snp_LDLR + 0.013 * (age - 55) + 0.33 * sex +
               0.042 * (bmi - 24) + gpoly +
               rnorm(nfam, 0, sqrt(s2e)), 2)

fam <- data.frame(fid = fid, iid = iid, father = pat, mother = mat,
                  role = role, sex = sex, age = age, bmi = bmi,
                  snp_LDLR = snp_LDLR, ldl = ldl)

write.csv(cgm, "cgm_glucose.csv", row.names = FALSE, quote = FALSE)
write.csv(vis, "visium_spots.csv", row.names = FALSE, quote = FALSE)
write.csv(vt, "visium_truth.csv", row.names = FALSE, quote = FALSE)
write.csv(fam, "family_cohort.csv", row.names = FALSE, quote = FALSE)
gz <- gzfile("family_geno.csv.gz", "w")
write.csv(data.frame(iid = iid, Gn), gz, row.names = FALSE,
          quote = FALSE)
close(gz)
cat("cgm", nrow(cgm), " visium", ns, "x 50  family", nfam, "\n")
