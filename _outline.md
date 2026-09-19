# 3. Linear Regression — 목차 초안 (v0)

원자료: `S_S_2_Linear_regression (GT)` (docx 19개 + PPT/R/data)
매핑 원칙: **docx 1개 = qmd 1장**. 원자료 순서·제목 그대로 유지.

---

## 자료 전환 방침 — GWAS / 오믹스 (2026-09-19 확정)

- 교과서 예제(meddcor, SAT, IMDb …)를 **버리고 생물학 자료로 교체**
  - Part 1~3 → **GWAS** (KNU-Lipid 시뮬레이션 코호트)
  - Part 4 → 로지스틱은 **METABRIC**(실제 유방암 코호트 n=1904), 포아송은 별도 검토
  - Part 5 → 고차원 GWAS + PRS
  - Part 6 → 메틸화(WLS·GAM), eQTL(로버스트), NMR(비선형), CGM(시계열), Visium(공간), 가계 코호트(혈연 LMM)
- 원자료의 **이론 서술·수식·절 구성은 그대로 유지**, 데이터 예제만 교체
- 01~07도 GWAS·유전학 자료로 소급 교체 완료 (2026-09-19)

### 실습 자료

| 파일 | 내용 | 쓰이는 곳 |
|---|---|---|
| `data/gwas_cohort.csv` | KNU-Lipid 코호트 n=1500, 22열 | Part 3~5 |
| `data/gwas_aim_markers.csv` | 조상정보 마커 200개 유전형 | PC 계산 재현용 |
| `data/metabric.csv` | METABRIC n=1904 | Part 4 (로지스틱) |
| `data/rnaseq_counts.csv` | KNU-RNA 카운트 500유전자 × 24시료 | Part 4 (포아송) |
| `data/rnaseq_samples.csv` | 시료 정보 (group/batch/age/lib_size) | Part 4 |
| `data/rnaseq_truth.csv` | 유전자별 참값 (log2FC, dispersion) | Part 4 |
| `data-raw/simulate_cohort.R` | 코호트 생성 (시드 고정) | — |
| `data/gwas_geno_wide.csv.gz` | 유전형 1500 × 2000 (LD 블록 100개) | Part 5 |
| `data/gwas_tc.csv` | 다유전자 형질 총콜레스테롤 | Part 5 |
| `data/gwas_geno_truth.csv` | SNP별 block/maf/beta_true/is_causal | Part 5 |
| `data/methyl_cpg.csv` | KNU-Methyl 혈액 RRBS 400명, CpG 2개 (M/m) | 6-I WLS·GAM |
| `data/eqtl_ldlr.csv` | LDLR eQTL 400명 (라플라스 오차 + 5% 이상치) | 6-I 로버스트 |
| `data/nmr_spectrum.csv` | 1H-NMR 스펙트럼, 로렌츠 피크 4개 | 6-I 비선형 |
| `data/cgm_glucose.csv` | CGM 14일 × 15분 = 1344점 | 6-II 시계열 |
| `data/visium_spots.csv` + `_truth` | Visium 유사 600 spot × 50 유전자 | 6-II 공간 |
| `data/family_cohort.csv` + `family_geno.csv.gz` | KNU-Family 300가계 × 5명, 귀무 SNP 1000개 | 6-II 혼합효과 |
| `data-raw/simulate_rnaseq.R` | RNA-seq 카운트 생성 (시드 고정) | — |
| `data-raw/simulate_genotypes.R` | 고차원 유전형 + tc 생성 (시드 고정) | — |
| `data/gwas_cohort_ext.csv` | KNU-Lipid 확장 — APOE 6유전형, TG, LPL 결핍 1명 | 1-III, 2-II |
| `data-raw/simulate_cohort_ext.R` | 확장 자료 (`set.seed(20260923)`) | — |
| `data-raw/simulate_part6_1.R` | 6-I 자료 (`set.seed(20260921)`) | — |
| `data-raw/simulate_part6_2.R` | 6-II 자료 (`set.seed(20260922)`) | — |

### 코호트에 심어 둔 함정

| 함정 | 장치 | 다루는 장 |
|---|---|---|
| 영향점 | FH 보인자 6명 (LDL +4.2~5.8) | 08 §2 |
| 다중공선성 | LD 블록 `snp_LDLR`/`LD1`/`LD2` (r = 0.93, 0.89) | 08 §4 |
| 교란 | 집단층화 — `snp_AIM` MAF 0.12 vs 0.53 | 09 §1 |
| 과적합 | 훈련/검정 분할 PRS | 09 §3 |

---


---

## Part 0. Getting Started

| 파일 | 제목 | 내용 | 원자료 |
|---|---|---|---|
| `index.qmd` | Home | 강의 소개, 전체 syllabus, 평가 | — |
| `chapters/00_setup.qmd` | R 환경과 데이터 | R/RStudio, 패키지, 데이터셋 내려받기, 표기법 | `0_Getting_Started/` |

---

## Part 1. Simple Linear Regression (3장)

**`01_slr_estimation.qmd` — Estimation and Inference** ✅
1. Basics — 강의 자료 소개(KNU-Lipid/KNU-Family/METABRIC/KNU-RNA), **GWAS 단일 SNP 검정 = 단순회귀**, 가법 코딩
2. Estimation method — 4가정, 최소제곱, MSE, 제곱합 분해 (이론 그대로)
3. Data example I — `ldl ~ snp_LDLR` (n=1500), β̂₁ 0.3356 σ̂ 0.757, 공식 직접 계산, 외삽(x=3 없음)
4. Statistical inference — 불편성, t분포, CI·검정 (이론 그대로)
5. Data example II — t 10.79, p 3.6e−26, 99% CI (0.255, 0.416), 참값 0.28 대조, 전장유전체 유의수준 5e−8
- KNU-Lipid 자료 소개 상자(참값·함정 표)가 여기로 옮겨옴

**`02_slr_prediction.qmd` — Prediction and Model Evaluation** ✅
1~2. 추정 vs 예측 — BB(x*=2) 평균 CI (3.49, 3.68) vs 개인 PI (2.10, 5.07), 분산비 230배 → 유전형으로 개인 예측 불가
3. Diagnostics — 잔차 분석, QQ, Box-Cox (이론 그대로)
4~5. Outliers & R² — |r|>2가 48명(정규 기대 68명), n 맞춘 기준 4.15, **|r| 4.6~7.9인 6명(전원 BB) 표시 → 3-III**, R² 0.072 (유의성 ≠ 설명력)

**`03_slr_examples.qmd` — Data Examples** ✅
1~2. PPP → **부모–자녀 LDL 회귀** (KNU-Family 300가계, Galton): H0 β=1 기각(t −7.86), 기울기 = h²,
   FH 가계 추가(=브라질) Cook 1.13 → 빼면 0.571→0.491 (참 0.5), 아버지 0.234·어머니 0.244 (이론 0.25),
   근거 없는 제거(F226) 교훈, 자녀 개별 사용 시 se 과소(0.055→0.048)
3. 대선 → **TG ~ BMI** 로그변환(왜도 2.98→0.06), 4.9%/BMI, **LPL 결핍 KL0719**(=Palm Beach) PI 상한의 4.1배
- 데이터: `family_cohort.csv`, `gwas_cohort.csv`, `gwas_cohort_ext.csv`

---

## Part 2. ANOVA (2장)

**`04_anova_basics.qmd` — Basic Concepts and Estimation** ✅
1~2. ANOVA 개념, pooled variance, MSE 분포 (이론 그대로)
3. Data example — **snp_LDLR 유전형 AA/AB/BB별 LDL** (유전형 모형), 평균 2.938/3.178/3.770, 평균별 CI
4. F-test — F=64.82 (2, 1497), 제곱합 직접 계산, 연습(snp_N1 F=2.29, pop F=t²=176)

**`05_anova_comparison.qmd` — Comparison and Model Fit** ✅
1. Tukey — q/√2 2.35 vs t 1.96, 3쌍 모두 유의, BB−AB 0.59(참 0.28) 이상
2. Model fit — BB 잔차 SD 1.30 vs 0.68/0.72 → 1-II의 6명 때문 (빼면 0.71)
3. ANOVA = 더미 회귀, **유전형 모형 vs 가법 모형** F=12.43(p=0.0004) → 6명 때문, 3-IV/V에서 F=0.056
4. Case — **APOE 6유전형별 log(TG)**: Shapiro 원척도 p<2e−16 → 로그 0.41, F=7.69(5,1493), Tukey 15쌍 중 6쌍, 참값 대조
- 데이터: `gwas_cohort.csv`, `gwas_cohort_ext.csv`

---

## Part 3. Multiple Linear Regression (4장)

**`06_mlr_estimation.qmd` — Estimation** ✅
1~4. 설계행렬, 교호작용(나이×유전형 F=0.14 → 평행선), hat matrix, 해석 (이론 그대로)
5. Data example — `ldl ~ snp + age + sex + bmi + pop` σ̂ 0.669 R² 0.278, 참값 대조표,
   **marginal vs conditional BMI 0.0583 → 0.0503(집단 보정) → 0.0476** (참 0.042), 행렬 계산 확인

**`07_mlr_inference.qmd` — Statistical Inference and Prediction** ✅
1~2. 분산-공분산, 전체 F, 순차제곱합, partial F (이론 그대로)
3. Data example I — F=115.1(5,1494), 95% CI 참값 포함 여부(snp만 벗어남 → FH),
   **순차제곱합 bmi 51.76(먼저) vs 38.12(pop 뒤)**, partial F(공변량 4개) 106.6
4~5. 예측 — 60세 남성·BMI 27·Group1·BB: CI (3.63, 3.84) vs PI (2.42, 5.05), 행렬 공식, 나이별 띠

**`08_mlr_diagnostics.qmd` — Diagnostics, Evaluation and Multicollinearity** ✅
1. Assumptions and diagnostics — 4가정, error vs residual, hat matrix(멱등·대각합·leverage), standardized residual, 진단 플롯, 변수변환, outlier 3종, Cook's distance
2. Data example I — KNU-Lipid 코호트, scatter matrix, 잔차 4종, **Cook 상위 6 = FH 보인자**, 제거 시 β 0.326 → 0.253
3. Model evaluation — R²/adj R²(귀무 SNP 6개 넣으면 adj R² 하락), 전체 F, 부분 F
4. **Multicollinearity = LD** — 상관 0.935/0.888, 증상 4가지, VIF 11.6 = (se비)², 단독 p<1e-15 → 동시 p=0.92/0.99
5. Data example II — LD 블록, LD pruning·fine-mapping으로 연결

**`09_mlr_casestudy.qmd` — Case Studies** ✅
1. 집단층화와 가짜 연관 — 집단별 MAF·LDL 평균, PC 산점도, `snp_AIM` p 3.5e-15 → **0.994**, `snp_LDLR`은 유지, 10-SNP 스캔 순위 변화, 보정 잔차로 개인 순위(FH 검출), 적합 평가
2. 범주형 X — `as.factor()` 유전형 모형 vs 가법 모형(부분 F = 0.056, p = 0.81), 더미 직접 만들기, 절편 제거 시 해석, Pearson χ²(`snp_AIM` 477.7 vs `snp_LDLR` 3.76)
3. PRS 예측 — 훈련/검정 분할, 단변량 가중치, 검정 R² 0.224 → 0.259, 훈련 0.317(낙관 편향), LD pruning, 95% 예측구간 포함률 94.9%
- 데이터: `data/gwas_cohort.csv`

---

## Part 4. Generalized Linear Models (5장)

**`10_logistic_basics.qmd` — Logistic: Basic Concepts and Estimation** ✅
1. Introduction — 0/1에 lm을 쓰면 확률이 음수(100명), odds·logit·시그모이드, 3가정, 오차항이 없는 이유
2. Data example — METABRIC, 반응변수는 **5년 유방암 특이 사망**(n=1675, 사건 314), 경쟁위험·중도절단 처리, 경험적 logit이 직선
3. Model description & estimation — odds ratio(≠risk ratio), MLE 로그가능도, 닫힌 해 없음·IRLS
4. Data example — NPI OR 2.304, ER+ OR 0.262(=2×2 표와 일치), optim으로 MLE 재현, 다변량 OR 표

**`11_logistic_inference.qmd` — Logistic: Inference, Fit, Classification** ✅
1. Statistical inference — t가 아니라 z인 이유, OR의 CI, LRT(이탈도 차) D=239.41(df 7), Wald, Hauck-Donner
2. Data example I — 순차 이탈도(순서 의존), 유전자발현 3개 추가 partial LRT p=0.0085
3. Model fit — 잔차 4종, **반복 없는 0/1은 이탈도 GOF 불가**, 집계 후 dev 16.92(df 14, p=0.26), HL 8.98(p=0.34), 과산포, logit/probit/cloglog
4. Data example II — **Simpson's paradox**: ERBB2 단변량 +0.166 → HER2 보정 −0.171 (층별 기울기는 −0.245/+0.401 → 상호작용)
5. Classification — 0.5 오분류율 0.173 vs 기저율 0.187, 임계값·민감도/특이도, ROC·AUC 0.772, 10-fold CV AUC 0.764

**`12_logistic_casestudy.qmd` — Case Study: 케이스-컨트롤 GWAS** ✅
1. EDA — KNU-Lipid `disease` (n=1494, 사례 386), mosaicplot, 케이스-컨트롤에서 절편이 해석 불가한 이유
2. Modeling — SNP 스캔 OR 1.411(Bonferroni 0.005), 가법 vs 유전형 LRT p=0.82, PC 보정, **매개변수 과보정**(LDL 넣으면 OR 1.436→1.158, p=0.14), 교란/매개/충돌 구분표
3. Prediction — AUC 0.629→0.639(SNP)→0.693(LDL): **유의성 ≠ 예측력**
4. GOF — 집계 dev 17.22(df 17, p=0.44), **HL이 G에 따라 p 0.02~0.80으로 흔들림**, 보정도 그림

**`13_poisson_basics.qmd` — Poisson: Basic Concepts and Estimation** ✅
1. Introduction — GLM 한 틀(분포+연결함수), 포아송 분포(평균=분산), log link, **log 변환 lm vs 포아송**(E(logY) vs logE(Y), y=0 문제)
2. Data example — KNU-RNA 카운트, 평균-분산 그림(대부분 선 위 = 과산포 예고), 라이브러리 크기 4.3배 차이
3. Model & estimation — rate ratio = fold change, **offset**(=log lib_size, 계수 1로 고정), MLE 점수방정식
4. Data example — G0001 log2FC 1.203(참 1.2), **offset 빼면 0.508로 붕괴**, log(lib)를 변수로 넣으면 계수 1.018, 다중회귀(batch/age), optim 재현

**`14_poisson_inference.qmd` — Poisson: Inference and Model Assessment** ✅
1. Statistical inference — Wald z, 이탈도 차 검정, 전체 회귀
2. Data example I — G0001 RR·CI, batch 부분검정 p=0.73
3. Model fit — 잔차, GOF(개별 관측치 단위로 가능), **과산포 φ**, quasi-Poisson vs 음이항
4. Data example II — **같은 참 log2FC 1.2, 다른 산포**: G0001 φ=0.88 vs G0021 φ=680, quasi se 26배, NB dispersion 0.253(참 0.20)
5. 전체 스캔 500유전자 — Bonferroni 위양성 **포아송 315/441, quasi 0, NB 3** → edgeR/DESeq2가 NB를 쓰는 이유, p-value 히스토그램, volcano
6. 비선형 — G0061 이차항 0.305(참 0.312), quasi-Poisson은 F-검정, `mgcv::gam` edf 2.90
- 데이터: `data/metabric.csv`, `data/gwas_cohort.csv`, `data/rnaseq_*.csv`

---

## Part 5. Variable Selection (3장)

**`15_varsel_basics.qmd` — Basics of Variable Selection** ✅
1. Introduction — 고차원/다중공선성/설명vs예측, **주의사항 6가지**, no magic bullet, 표기 S
2. Data example I — KNU-Lipid 확장판 (n=1494, p=2000, 인과 40개, h²=0.385), 공변량 잔차화, **p>n이면 lm 계수 1001개가 NA**
3. Prediction risk — 편향-분산, 훈련 R² 0.088→0.997 vs 검정 R² 정점 0.227(k=50) → −34.5(k=990), Cp/AIC/BIC/LOOCV 공식과 leverage 닫힌식
4. Model search — 2^2000은 602자리, forward/backward/both, stepwise의 문제
5. Data example II — `leaps` 후보 15개 전수탐색(BIC k=8, **8개 전부 인과**), `step()` 200개 forward(39개 중 21개 인과),
   LD 블록에서 하나만 선택, **순열검사로 선택편향 정량화**(y를 섞어도 훈련 R²=0.135)

**`16_regularized.qmd` — Regularized Regression** ✅
1. Penalties — L0/L1/L2/EN 비교표, L1이 0을 만드는 기하적 이유 (제약영역 그림)
2. Approaches — 표준화 필수(비표준화 시 흔한 변이로 쏠림: 평균 MAF 0.351 vs 0.277),
   Ridge 닫힌 해 **(X'X + nλI)⁻¹X'y가 glmnet과 6.1e-06 일치**, 연성임계 그림,
   Lasso 한계(최대 n개=910, 묶음 문제), Elastic Net, lambda.min vs lambda.1se
3. Data examples — 계수경로·CV 곡선, 성능표(lasso 163개 0.267 / EN 193개 0.261 / ridge 2000개 0.104),
   **LD 블록에서 lasso는 snp_LDLR 하나(0.123), ridge는 넷에 분산, EN은 둘**, `MASS::lm.ridge`, `glmnet` binomial

**`17_varsel_casestudy.qmd` — Case Study: Polygenic Risk Score** ✅
1. Introduction — PRS 정의, **실제 GWAS는 요약통계만 공개**, 훈련1000/검증247/검정247 3분할
2. GWAS 요약통계 — Manhattan·QQ, λ_GC=1.151, **r = Z/√(N+Z²)로 개체자료 없이 상관 복원**(오차 2.6e-05)
3. C+T — clumping(2000→789), 문턱 조율, 검증 최적 T=0.01(45 SNP) → 검정 증가 R² 0.171
4. **lassosum 직접 구현** — 목적함수 (1−s)β'Rβ−2β'r+s‖β‖²+2λ‖β‖₁, 좌표하강 갱신식,
   **한 블록 s=0에서 glmnet과 5.8e-05 일치**, 격자 조율 → s=0.2, λ=0.06 (143 SNP) → 검정 0.230
5. 개체수준 Lasso — 163 SNP → 0.274 (상한선)
6. Findings — C+T 0.171 < lassosum 0.230 < 개체 Lasso 0.274 (참 h²=0.385),
   요약통계만으로 개체자료 성능의 84% 회수, PRS 이식성·해석 주의
- 데이터: `data/gwas_geno_wide.csv.gz`, `data/gwas_tc.csv`, `data/gwas_geno_truth.csv`

---

## Part 6. Other Regression Models (2장)

**`18_other_models_1.qmd` — WLS, Robust, Nonlinear/Nonparametric** ✅
1. **WLS** — 원자료 발병률 D/m ↔ **CpG 메틸화 비율 M/m** (KNU-Methyl 400명, coverage 5~400),
   잔차 깔때기(SD 0.140 → 0.041), 성별 효과 OLS 0.0118(p=0.18) vs **WLS 0.0212(p=0.00097)** (참 0.02),
   닫힌 해 = `lm(weights)` 1e-16, 1000회 반복 효율 1.66/1.86, 분산함수 기울기 −0.81,
   R `weights` = 원자료 w의 역수(표기 주의), **limma-voom = lowess 가중치 WLS** (KNU-RNA)
2. **Robust** — FH 6명: OLS 0.326 vs Huber 0.269·LAD 0.292 (지우지 않고), 라플라스 = LAD의 MLE,
   LDLR eQTL(참 −0.30): OLS −0.215(se 0.070) vs **LAD −0.282(0.029)**, Huber −0.271(0.027),
   IRLS(1/|r|) = `rq`, 효율 Var(LAD)/Var(OLS) 정규 1.58(π/2) · 라플라스 0.64
3. **Nonlinear/GAM** — NMR 로렌츠 피크 4개 `nls`(9개 모수 복원, 10차 다항식 R² 0.24),
   μ·τ 알면 lm, 나쁜 시작값 → 실패/국소해, 차원의 저주 300^(9/5)=28762,
   메틸화 cgB ~ s(age)+s(bmi) edf 4.52/3.96, **backfitting 직접 구현 ↔ mgcv 상관 0.9999**
- 데이터: `methyl_cpg.csv`, `eqtl_ldlr.csv`, `nmr_spectrum.csv`, `rnaseq_*.csv`, `gwas_cohort.csv`

**`19_other_models_2.qmd` — Time Series, Spatial, Mixed Effects** ✅
1. **Time series = CGM 14일** — 6가지 특징 전부, Y = m + s + X, `decompose()` = 중심이동평균+시각별 평균 직접 계산,
   AR(1) φ̂ 0.78(참 0.8), 추세 OLS −1.03(se 0.083, CI가 참 −1.2 벗어남) vs **GLS −1.05(se 0.260)**,
   n_eff 149, Prais–Winsten = gls, 추세 없는 자료 500회 OLS 1종 오류 54% vs FGLS 4.8%
2. **Spatial = Visium 600 spot** — 깊이 추세·GP 장·백질 이분산, OLS 잔차 Moran's I 0.41, 준변동도,
   GP 가능도 직접 구현 = `gls(corExp)` (logLik −480.89), 깊이 OLS 0.122(se 0.0042) vs **GLS 0.125(0.0142)** (참 0.10),
   `gam(s(x,y))`, Moran's I SVG 스캔 10/10 검출·위양성 0
3. **Mixed = KNU-Family 300가계×5** — ANOVA(가계 고정) → 임의효과(ANOVA 추정량 = REML) → 혼합,
   관계별 잔차 상관(배우자 −0.05, 부모-자녀 0.22, 형제 0.24) → **혈연행렬 LMM**, 고유분해 회전 = WLS (GEMMA),
   REML h² 0.46(참 0.5), 귀무 SNP 1000개 λ_GC OLS 1.52 → 임의절편 1.14 → **혈연 LMM 1.07**, GRM이 혈연 0.5 복원
4. **Overview** — 모형 선택표(반응 유형 / 깨진 가정), 전체 모형 정리표
- 데이터: `cgm_glucose.csv`, `visium_spots.csv`, `visium_truth.csv`, `family_cohort.csv`, `family_geno.csv.gz`

---

## Part 7. 부록

**`chapters/A1_cheatsheet.qmd` — 부록 A. 통계량 치트시트** ✅
1. 가설검정의 절차, 1·2종 오류, 강의에서 반복된 주의점 (유의성 ≠ 예측력 등)
2. 검정 선택 흐름도 (mermaid) + Y·X 유형별 표
3. 일반 검정표 — 평균(z, t, 대응, Welch), 비율, 분산(F, Bartlett, Brown–Forsythe), 카이제곱 계열, 비모수
4. 이 강의의 검정표 — t, F·Tukey, Wald z, LRT·이탈도·HL·과산포, 다중검정(Bonferroni·BH·5e−8·λ_GC·순열), 가정 점검, 모형 비교 기준 (장 링크)
5. 분포 관계 — t² = F(1, ν), χ²/k = F(k, ∞), 분위수로 확인
6. 흔한 검정 = 선형모형 — 단일·두 표본·대응 t, 상관 검정이 lm과 완전히 같음, χ² 독립성 = 포아송 로그선형 Pearson X² (477.73), Mann–Whitney·Kruskal–Wallis ≈ 순위 lm

**`chapters/A2_r_reference.qmd` — 부록 B. R 함수 레퍼런스** ✅
1. R 기초 (벡터, 데이터프레임, apply, 도움말) — 원자료 R intro 요약
2. 공식 문법, 적합 함수 12종 / 3. 결과·추론 / 4. 예측 / 5. 진단 (VIF 정의대로) /
6. 선택·정규화·CV (regsubsets·cv.glmnet 실행) / 7. 행렬 계산 (optim으로 glm 재현) / 8. base 그래픽 / 9. 패키지 표
- 모든 표에 "쓰인 장" 링크

**`chapters/00_setup.qmd` — R 환경과 데이터** ✅
- 설치, RStudio, 저장소 받기·작업 디렉터리, 패키지 7개와 설치 스크립트, 실습 자료 18개 표, 불러오기 주의점,
  시뮬레이션 스크립트 6개(시드·입출력·실행 순서), 표기법

---

## _quarto.yml sidebar 초안

```yaml
  sidebar:
    style: "floating"
    search: true
    contents:
      - text: "Home"
        href: index.qmd
      - chapters/00_setup.qmd
      - section: "Part 1. Simple Linear Regression"
        contents:
          - chapters/01_slr_estimation.qmd
          - chapters/02_slr_prediction.qmd
          - chapters/03_slr_examples.qmd
      - section: "Part 2. ANOVA"
        contents:
          - chapters/04_anova_basics.qmd
          - chapters/05_anova_comparison.qmd
      - section: "Part 3. Multiple Linear Regression"
        contents:
          - chapters/06_mlr_estimation.qmd
          - chapters/07_mlr_inference.qmd
          - chapters/08_mlr_diagnostics.qmd
          - chapters/09_mlr_casestudy.qmd
      - section: "Part 4. Generalized Linear Models"
        contents:
          - chapters/10_logistic_basics.qmd
          - chapters/11_logistic_inference.qmd
          - chapters/12_logistic_casestudy.qmd
          - chapters/13_poisson_basics.qmd
          - chapters/14_poisson_inference.qmd
      - section: "Part 5. Variable Selection"
        contents:
          - chapters/15_varsel_basics.qmd
          - chapters/16_regularized.qmd
          - chapters/17_varsel_casestudy.qmd
      - section: "Part 6. Other Regression Models"
        contents:
          - chapters/18_other_models_1.qmd
          - chapters/19_other_models_2.qmd
      - section: "부록"
        contents:
          - chapters/A1_cheatsheet.qmd
          - chapters/A2_r_reference.qmd
```

## 그밖에 바꿔야 할 것 (템플릿 잔재) — 정리 완료 (2026-09-19)

- `_quarto.yml`: 제목·GitHub 링크 교체 완료, `01_intro.qmd` 제외 줄 삭제
- `index.qmd`: 강의 소개·Syllabus(장별 링크·실습 자료)·함정 표·읽는 법으로 새로 씀
- `chapters/01_intro.qmd`: **삭제**
- git remote: `kkonoo/2_linear_algebra` → `kkonoo/3_linear_regression` (원격 저장소는 비어 있음, 첫 push 필요)
- 남은 것: `README.md`는 여전히 AI 강의 템플릿 설명 (Cloudflare Worker 설정 안내)
