## ─────────────────────────────────────────────────────────────
## KNU-Lipid 코호트 확장 — 고차원 유전형 패널과 다유전자 형질
##   입력 : data/gwas_cohort.csv (simulate_cohort.R 결과)
##   출력 : gwas_geno_wide.csv.gz  유전형 1500 x 2000
##          gwas_geno_truth.csv    SNP별 참값
##          gwas_tc.csv            총콜레스테롤 형질
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260920)

co <- read.csv("gwas_cohort.csv")
n  <- nrow(co)

## ── LD 블록 생성 ─────────────────────────────────────────────
##   블록 안에서는 AR(1) 잠재변수로 이웃일수록 강한 LD를 만듦
make_block <- function(n, m, maf, rho) {
  hap <- function() {
    z <- matrix(0, n, m)
    z[, 1] <- rnorm(n)
    if (m > 1) for (j in 2:m) {
      z[, j] <- rho * z[, j - 1] + sqrt(1 - rho^2) * rnorm(n)
    }
    matrix(as.integer(z < rep(qnorm(maf), each = n)), n, m)
  }
  hap() + hap()
}

n_block  <- 100
blk_size <- 20                              # 100 x 20 = 2000
n_new    <- n_block * blk_size - 4          # 기존 SNP 4개 자리를 뺌

G <- matrix(0L, n, n_new)
blk_id <- integer(n_new)
maf_all <- numeric(n_new)
pos <- 0
for (b in 1:n_block) {
  m   <- if (b == 1) blk_size - 4 else blk_size
  maf <- runif(m, 0.05, 0.5)
  rho <- runif(1, 0.55, 0.95)               # 블록마다 LD 강도가 다름
  G[, pos + seq_len(m)] <- make_block(n, m, maf, rho)
  blk_id[pos + seq_len(m)]  <- b
  maf_all[pos + seq_len(m)] <- maf
  pos <- pos + m
}
colnames(G) <- sprintf("rs%04d", seq_len(n_new))

## ── 기존에 쓰던 SNP 4개를 그대로 합침 ────────────────────────
known <- c("snp_LDLR", "snp_LD1", "snp_LD2", "snp_AIM")
K <- as.matrix(co[, known])
geno <- cbind(G, K)
blk_id  <- c(blk_id, rep(0L, 4))            # 블록 0 = 기존 LDLR 부위
maf_all <- c(maf_all, colMeans(K) / 2)

## ── 다유전자 형질: 총콜레스테롤 (mmol/L) ────────────────────
p <- ncol(geno)
beta <- numeric(p)
names(beta) <- colnames(geno)

## 큰 효과 4개 + 중간 효과 36개 = 인과 SNP 40개
big  <- sample(n_new, 4)
mid  <- sample(setdiff(seq_len(n_new), big), 35)
beta[big] <- sample(c(-1, 1), 4, TRUE) * runif(4, 0.30, 0.42)
beta[mid] <- sample(c(-1, 1), 35, TRUE) * runif(35, 0.09, 0.18)
beta["snp_LDLR"] <- 0.24                    # Part 3의 그 변이도 인과

gscore <- as.numeric(geno %*% beta)
tc <- 5.20 + gscore - mean(gscore) +
  0.011 * (co$age - 55) + 0.24 * co$sex +
  0.031 * (co$bmi - 24) + 0.35 * (co$pop == "Group2") +
  rnorm(n, 0, 0.80)
tc <- round(tc, 2)

truth <- data.frame(
  snp = colnames(geno), block = blk_id,
  maf = round(maf_all, 4), beta_true = round(beta, 4),
  is_causal = as.integer(beta != 0))

## ── 저장 ─────────────────────────────────────────────────────
gz <- gzfile("gwas_geno_wide.csv.gz", "w")
write.csv(data.frame(iid = co$iid, geno), gz,
          row.names = FALSE, quote = FALSE)
close(gz)
write.csv(truth, "gwas_geno_truth.csv", row.names = FALSE, quote = FALSE)
write.csv(data.frame(iid = co$iid, tc = tc), "gwas_tc.csv",
          row.names = FALSE, quote = FALSE)

cat("n =", n, " p =", p, " causal =", sum(beta != 0), "\n")
cat("var(genetic) =", round(var(gscore), 3),
    " var(tc) =", round(var(tc), 3),
    " h2 =", round(var(gscore) / var(tc), 3), "\n")
