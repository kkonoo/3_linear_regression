## ─────────────────────────────────────────────────────────────
## KNU-Lipid 코호트 확장 — APOE 유전형과 중성지방(TG)
##   입력 : gwas_cohort.csv (simulate_cohort.R 결과, 수정하지 않음)
##   출력 : gwas_cohort_ext.csv  iid, apoe, tg, lpl_def
##   용도 : 1-III (TG 로그변환·단일유전자 이상값), 2-II (APOE별 ANOVA)
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260923)

co <- read.csv("gwas_cohort.csv")
n  <- nrow(co)

## ── APOE 유전형 (e2 / e3 / e4, HWE) ─────────────────────────
##   실제로 APOE는 LDL에도 영향을 주지만, 이 가상 코호트의 ldl은
##   APOE 없이 만들어졌으므로 여기서는 TG에만 작용하게 함
allele <- function() sample(c("e2", "e3", "e4"), n, TRUE,
                           prob = c(0.08, 0.80, 0.12))
a1 <- allele(); a2 <- allele()
apoe <- ifelse(a1 <= a2, paste(a1, a2, sep = "/"),
               paste(a2, a1, sep = "/"))

## 유전형별 log(TG) 효과 (참값) — e2/e2는 제3형 고지단백혈증 경향
eff <- c("e2/e2" = 0.70, "e2/e3" = 0.05, "e2/e4" = 0.15,
         "e3/e3" = 0,    "e3/e4" = 0.10, "e4/e4" = 0.20)

## ── 중성지방 (mmol/L): 로그정규 ─────────────────────────────
ltg <- log(1.4) + 0.045 * (co$bmi - 24) + 0.006 * (co$age - 55) +
  0.12 * co$sex + 0.10 * (co$pop == "Group2") + eff[apoe] +
  rnorm(n, 0, 0.38)

## LPL 결핍(가족성 킬로미크론혈증) 1명 — 단일유전자 열성 질환
##   BMI가 평범한 e3/e3 비보인자 중에서 고름 → TG만 약 10배
cand <- which(apoe == "e3/e3" & co$fh_carrier == 0 &
                co$bmi > 21 & co$bmi < 24)
lpl <- sample(cand, 1)
ltg[lpl] <- ltg[lpl] + log(10)
lpl_def <- as.integer(seq_len(n) == lpl)

ext <- data.frame(iid = co$iid, apoe = apoe,
                  tg = round(exp(ltg), 2), lpl_def = lpl_def)
write.csv(ext, "gwas_cohort_ext.csv", row.names = FALSE, quote = FALSE)
cat("n =", n, " LPL:", co$iid[lpl], "\n")
print(table(apoe))
