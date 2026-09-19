## ─────────────────────────────────────────────────────────────
## Part 6-I 실습 자료 생성 — WLS · 로버스트 · 비선형 · GAM
##   입력 : gwas_cohort.csv (simulate_cohort.R 결과, eQTL 참여자 추출용)
##   출력 : methyl_cpg.csv    KNU-Methyl 혈액 RRBS, 400명 x CpG 2개
##          eqtl_ldlr.csv     LDLR 발현 eQTL, 400명 (두꺼운 꼬리 오차)
##          nmr_spectrum.csv  1H-NMR 스펙트럼 구간, 로렌츠 피크 4개
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260921)

## ══ 1. KNU-Methyl — CpG 메틸화 비율 ═════════════════════════
n   <- 400
age <- round(runif(n, 20, 85))
sex <- rbinom(n, 1, 0.5)                          # 1 = 남성
bmi <- round(rnorm(n, 24, 3.5), 1)

## CpG마다 read depth(coverage)가 사람마다 크게 다름
draw_cov <- function() {
  pmin(pmax(round(exp(rnorm(n, log(35), 0.85))), 5), 400)
}
cov_A <- draw_cov()
cov_B <- draw_cov()

## cgA — 나이에 선형 (WLS 예제)
pi_A <- 0.30 + 0.006 * (age - 50) + 0.02 * sex + rnorm(n, 0, 0.015)
## cgB — 나이·BMI에 비선형 (GAM 예제)
f_age <- function(a) 0.18 * tanh((a - 40) / 15)
f_bmi <- function(b) 0.10 / (1 + exp(-(b - 27) / 1.5))
pi_B <- 0.45 + f_age(age) + f_bmi(bmi) + 0.02 * sex +
  rnorm(n, 0, 0.015)

clip <- function(p) pmin(pmax(p, 0.001), 0.999)
meth_A <- rbinom(n, cov_A, clip(pi_A))
meth_B <- rbinom(n, cov_B, clip(pi_B))

methyl <- data.frame(
  iid = sprintf("KM%03d", 1:n), age = age, sex = sex, bmi = bmi,
  cov_A = cov_A, meth_A = meth_A, cov_B = cov_B, meth_B = meth_B)

## ══ 2. LDLR eQTL — 두꺼운 꼬리 오차 ═════════════════════════
co <- read.csv("gwas_cohort.csv")
co <- co[co$fh_carrier == 0, ]
ids <- sort(sample(nrow(co), 400))
eq <- co[ids, c("iid", "age", "sex", "snp_LDLR")]
m  <- nrow(eq)

## 라플라스 오차 (원자료의 heavy-tailed 예제 분포)
rlaplace <- function(k, b) {
  sample(c(-1, 1), k, TRUE) * rexp(k, 1 / b)
}
e <- rlaplace(m, 0.30)
## 5% 시료는 RNA 분해·시료 뒤바뀜 등으로 크게 튄 값
out <- sample(m, 20)
e[out] <- e[out] + sample(c(-1, 1), 20, TRUE) * runif(20, 2.5, 4.5)

eq$expr <- round(6.0 - 0.30 * eq$snp_LDLR + 0.008 * (eq$age - 55) +
                   0.10 * eq$sex + e, 3)
eq$outlier_true <- as.integer(seq_len(m) %in% out)

## ══ 3. 1H-NMR 스펙트럼 — 로렌츠 피크의 합 ══════════════════
ppm  <- round(seq(0.95, 1.55, by = 0.0015), 4)
peak <- data.frame(
  metabolite = c("valine", "3HB", "lactate", "alanine"),
  mu = c(1.04, 1.20, 1.33, 1.48),
  A  = c(0.60, 0.35, 1.00, 0.45))
tau <- 0.006
lor <- function(x, A, mu) A / ((x - mu)^2 / tau^2 + 1)
signal <- rowSums(sapply(1:4, function(l)
  lor(ppm, peak$A[l], peak$mu[l])))
nmr <- data.frame(ppm = ppm,
                  intensity = round(signal + rnorm(length(ppm), 0,
                                                   0.015), 4))

write.csv(methyl, "methyl_cpg.csv", row.names = FALSE, quote = FALSE)
write.csv(eq, "eqtl_ldlr.csv", row.names = FALSE, quote = FALSE)
write.csv(nmr, "nmr_spectrum.csv", row.names = FALSE, quote = FALSE)
cat("methyl n =", n, " eqtl n =", m, " nmr points =", nrow(nmr), "\n")
