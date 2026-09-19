## ─────────────────────────────────────────────────────────────
## 가상 지질 코호트 (KNU-Lipid Cohort) 생성 스크립트
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260918)

n1 <- 900; n2 <- 600; n <- n1 + n2
pop <- factor(c(rep("Group1", n1), rep("Group2", n2)))

## ── 유전형 생성 (HWE) ────────────────────────────────────────
draw_snp <- function(maf_vec) {            # 집단별 MAF
  maf <- ifelse(pop == "Group1", maf_vec[1], maf_vec[2])
  rbinom(n, 1, maf) + rbinom(n, 1, maf)
}

## 인과 SNP — 두 집단에서 MAF 동일
snp_LDLR <- draw_snp(c(0.27, 0.27))

## LD로 묶인 이웃 SNP 2개 (인과 SNP에서 일부만 재조합)
flip <- function(g, r) {                    # r = 불일치 확률
  idx <- runif(n) < r
  g2 <- g; g2[idx] <- draw_snp(c(0.27, 0.27))[idx]; g2
}
snp_LD1 <- flip(snp_LDLR, 0.06)
snp_LD2 <- flip(snp_LDLR, 0.11)

## 조상정보 SNP — 집단 간 MAF가 크게 다름, 참 효과는 0
snp_AIM <- draw_snp(c(0.12, 0.52))

## 귀무 SNP 6개
null_snps <- replicate(6, draw_snp(c(0.3, 0.3)))
colnames(null_snps) <- paste0("snp_N", 1:6)

## ── 공변량 ───────────────────────────────────────────────────
age <- round(pmin(pmax(rnorm(n, 55, 9), 30), 80), 0)
sex <- rbinom(n, 1, 0.48)                         # 1 = 남성
bmi <- round(rnorm(n, 23.8 + 0.6 * (pop == "Group2"), 3.1), 1)

## ── 형질: LDL 콜레스테롤 (mmol/L) ────────────────────────────
##   snp_AIM 은 계수 0 — 그런데 집단 평균 차이 때문에 겉보기 연관이 생김
ldl <- 2.55 +
  0.28 * snp_LDLR +
  0.013 * (age - 55) +
  0.33 * sex +
  0.042 * (bmi - 24) +
  0.52 * (pop == "Group2") +
  rnorm(n, 0, 0.62)

## 가족성 고콜레스테롤혈증(FH) 보인자 4명 — 단일유전자 기전
##   (영향점 효과를 보여주기 위해 위험 대립유전자 동형접합자 중에서 고름)
fh <- sample(which(snp_LDLR == 2), 6)
ldl[fh] <- ldl[fh] + runif(6, 4.2, 5.8)
fh_carrier <- as.integer(seq_len(n) %in% fh)

ldl <- round(ldl, 2)

## ── 이분형 형질 (Part 4 용) ─────────────────────────────────
lp <- -3.55 + 0.72 * ldl + 0.035 * (age - 55) + 0.45 * sex
disease <- rbinom(n, 1, 1 / (1 + exp(-lp)))

## ── 조상정보 마커 200개 → 주성분 ────────────────────────────
aim_maf <- cbind(runif(200, 0.05, 0.5), runif(200, 0.05, 0.5))
aim_maf[1:70, 2] <- pmin(aim_maf[1:70, 1] + runif(70, 0.20, 0.35), 0.95)
G <- sapply(1:200, function(j) draw_snp(aim_maf[j, ]))
colnames(G) <- sprintf("aim%03d", 1:200)
pcs <- prcomp(G, center = TRUE, scale. = TRUE)$x[, 1:4]
colnames(pcs) <- paste0("PC", 1:4)

cohort <- data.frame(
  iid = sprintf("KL%04d", 1:n),
  pop = pop, age = age, sex = sex, bmi = bmi,
  ldl = ldl, disease = disease, fh_carrier = fh_carrier,
  snp_LDLR = snp_LDLR, snp_LD1 = snp_LD1, snp_LD2 = snp_LD2,
  snp_AIM = snp_AIM, null_snps,
  round(pcs, 4)
)

write.csv(cohort, "gwas_cohort.csv", row.names = FALSE, quote = FALSE)
write.csv(data.frame(iid = cohort$iid, G), "gwas_aim_markers.csv",
          row.names = FALSE, quote = FALSE)
cat("n =", nrow(cohort), " cols =", ncol(cohort), "\n")
