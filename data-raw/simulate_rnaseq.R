## ─────────────────────────────────────────────────────────────
## 가상 RNA-seq 실험 (KNU-RNA) 카운트 행렬 생성 스크립트
## 시드 고정 — 실행할 때마다 동일한 데이터가 만들어짐
## ─────────────────────────────────────────────────────────────
set.seed(20260919)

n_s <- 24                                   # 시료 수
G   <- 500                                  # 유전자 수

## ── 시료 정보 ────────────────────────────────────────────────
group <- factor(rep(c("Control", "Treated"), each = 12),
                levels = c("Control", "Treated"))
batch <- factor(rep(rep(c("B1", "B2"), each = 6), 2))
age   <- round(runif(n_s, 22, 68))
## 라이브러리 크기(총 read 수)는 시료마다 4배 넘게 차이 남
lib   <- round(exp(runif(n_s, log(8e6), log(35e6))))

samples <- data.frame(
  sample_id = sprintf("S%02d", 1:n_s),
  group = group, batch = batch, age = age, lib_size = lib)

## ── 유전자별 참값 ────────────────────────────────────────────
base_lcpm <- rnorm(G, 4, 1.8)               # 대조군 log2 CPM

lfc <- rep(0, G)                            # 참 log2 fold change
de  <- 1:60
lfc[de] <- sample(c(-1, 1), 60, TRUE) * runif(60, 0.6, 2.5)

beff <- rep(0, G)                           # 배치 효과 (log2)
bg   <- sample(G, 100)
beff[bg] <- rnorm(100, 0, 0.5)

## 과산포 — 발현량이 낮을수록 크다 (edgeR/DESeq2가 쓰는 평균-분산 관계)
disp <- 0.03 + 6 / (2^base_lcpm)
disp[1:20] <- 1e-8                          # 거의 포아송인 유전자 20개

age_eff <- rep(0, G)                        # 나이 비선형 반응 표시

## ── 본문 예제용 대표 유전자 4개는 성질을 고정 ────────────────
##   G0001 포아송 · DE        G0002 포아송 · 비DE
##   G0021 과산포 · DE (효과크기는 G0001과 동일)
##   G0061 나이에 비선형 반응
base_lcpm[1]  <- 6.5; lfc[1]  <- 1.2; beff[1]  <- 0; disp[1]  <- 1e-8
base_lcpm[2]  <- 5.0; lfc[2]  <- 0.0; beff[2]  <- 0; disp[2]  <- 1e-8
base_lcpm[21] <- 6.5; lfc[21] <- 1.2; beff[21] <- 0; disp[21] <- 0.20
base_lcpm[61] <- 6.5; lfc[61] <- 0.0; beff[61] <- 0; disp[61] <- 0.05
age_eff[61]   <- 1

## ── 카운트 생성 ──────────────────────────────────────────────
trt <- as.integer(group == "Treated")
b2  <- as.integer(batch == "B2")
agz <- (age - 45) / 10

counts <- matrix(0L, nrow = G, ncol = n_s)
for (g in 1:G) {
  log2_cpm <- base_lcpm[g] + lfc[g] * trt + beff[g] * b2
  if (age_eff[g] == 1) log2_cpm <- log2_cpm + 0.45 * agz^2
  mu <- lib / 1e6 * 2^log2_cpm
  counts[g, ] <- if (disp[g] < 1e-6) rpois(n_s, mu)
                 else rnbinom(n_s, size = 1 / disp[g], mu = mu)
}

gene_id <- sprintf("G%04d", 1:G)
dimnames(counts) <- list(gene_id, samples$sample_id)

truth <- data.frame(
  gene_id = gene_id, base_lcpm = round(base_lcpm, 4),
  true_lfc = round(lfc, 4), batch_effect = round(beff, 4),
  dispersion = signif(disp, 4),
  is_de = as.integer(lfc != 0),
  is_poisson = as.integer(disp < 1e-6),
  age_nonlinear = age_eff)

write.csv(data.frame(gene_id = gene_id, counts),
          "rnaseq_counts.csv", row.names = FALSE, quote = FALSE)
write.csv(samples, "rnaseq_samples.csv", row.names = FALSE, quote = FALSE)
write.csv(truth, "rnaseq_truth.csv", row.names = FALSE, quote = FALSE)
cat("genes =", G, " samples =", n_s,
    " total reads =", format(sum(counts), big.mark = ","), "\n")
