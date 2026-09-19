I.  **Logistic Regression Basic Concepts and Estimation**

    1.  Introduction

    2.  Data examples

    3.  Model description and estimation

    4.  Data example - Model estimation

II. **Logistic Regression Statistical Inference, Model Assessment and Classification**

    1.  Statistical Inference

    2.  Data example I -- Statistical Inference

    3.  Model Fit Assessment

    4.  Data example II -- Model Fit Assessment

    5.  Classification

III. **Case Study: The Demographics of Obesity**

     1.  Exploratory Data Analysis

     2.  Modeling and Prediction

     3.  Goodness of Fit

IV. **Poisson Regression Basic Concepts and Estimation**

    1.  Introduction

    2.  Data examples

    3.  Model description and estimation

    4.  Data example - Model estimation

V.  **Poisson Regression Statistical Inference, Model Assessment and Classification**

    1.  Statistical Inference

    2.  Data example I -- Statistical Inference

    3.  Model Fit Assessment

    4.  Data example II -- Model Fit Assessment

```{=html}
<!-- -->
```
1.  **Statistical Inference**

```{=html}
<!-- -->
```
1)  Model ... Y일 확률 p (logit) \~ X\
    ![](media/image1.png){width="3.9027777777777777in" height="0.25208552055993in"}\
    ![](media/image2.png){width="2.34292104111986in" height="0.3055555555555556in"}

2)  Parameters: beta\
    ![](media/image3.png){width="0.8125in" height="0.25590004374453196in"}

3)  Approach: **MLE (Maximum likelihood estimation)**

-   Single value의 확률likelihood: Y=1 p, Y=0이면 1-p\
    > ![](media/image4.png){width="2.0416666666666665in" height="0.25013779527559055in"}

-   ML:\
    > ![](media/image5.png){width="4.347163167104112in" height="0.375in"}

-   MLL:\
    > ![](media/image6.png){width="2.7430555555555554in" height="0.2768219597550306in"}![](media/image7.png){width="4.236111111111111in" height="0.4594674103237095in"}

-   non-linear function라서 공식close form은 없음\
    > 그냥 한 parameter에 대해서 미분(dL / d$\text{β}_{p}$)\
    > (p+1) 개 방정식 생김. 미지수도 p+1개\
    > 컴퓨터로 계산

4)  Statistical properties of parameters

    1.  Approximate Sampling Distribution ... normal, **z** statistics\
        > (linear regression이니까 일단 비슷)\
        > ![](media/image8.png){width="0.8333333333333334in" height="0.23569006999125108in"}\
        > ![](media/image9.png){width="2.2836800087489064in" height="0.45592629046369204in"}\
        > *... 평균으로 뭐 만들고 그런 게 없어서 t statistics가 아님?!*

    2.  Normal approximation [large sample size가 아주 중요\
        > ]{.underline}*if small sample size? P(type I error) \> alpha\
        > more type I error (false-positive) than exp !!*

5)  Testing significance of parameters

    1.  Overall regression ... **log-likelihood ratio test**

```{=html}
<!-- -->
```
i.  Full model vs. Reduced/Null model\
    > ![](media/image10.png){width="5.416666666666667in" height="0.2358475503062117in"}\
    > ![](media/image11.png){width="3.2083333333333335in" height="0.22713582677165353in"}

ii. Hypothesis\
    > ![](media/image12.png){width="3.7569444444444446in" height="0.18480861767279091in"}

iii. Statistics\
     > - ML of full model (원하는 predictor q개)\
     > ![](media/image13.png){width="1.9097222222222223in" height="0.22435148731408575in"}\
     > - ML of null model\
     > ![](media/image14.png){width="1.1458333333333333in" height="0.24122812773403324in"}\
     > - **log-likelihood ratio** (dev; lrt) \~ $\chi_{q}^{2}$\
     > ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image15.png){width="1.9652777777777777in" height="0.5033027121609799in"} \* sup = supremum(upper limit)**\
     > ** ![텍스트, 화이트보드이(가) 표시된 사진 자동 생성된 설명](media/image16.png){width="1.7083333333333333in" height="0.3379122922134733in"} logarithm

iv. P-value for statistics[\
    > ]{.underline}- lrt의 분포: **카이제곱분포 (df = q)** ... *(ML 제곱 -- ML 제곱 = 카이제곱)\
    > *- p-value: P($\chi_{q}^{2} >$ Dev)

    1.  Partial testing for parameters ... **Wald test**

```{=html}
<!-- -->
```
i.  Hypothesis\
    > - two-tailed: z가 0에서 먼 가\
    > ![](media/image17.emf){width="1.7708333333333333in" height="0.20253718285214348in"}\
    > - one-tailed: z가 얼마나 큰가 / 작은가\
    > ![](media/image18.png){width="1.8472222222222223in" height="0.20524715660542434in"} ![](media/image19.png){width="1.9236111111111112in" height="0.21427602799650045in"}

ii. Statistics: Z-value\
    > ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image20.png){width="1.125in" height="0.5264774715660543in"}

> \* [Wald statistic]{.underline}: statistical parameter가 가정한 value와의 차이\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image21.png){width="1.0833333333333333in" height="0.5575043744531933in"}\~ $\chi^{2}$ ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image22.png){width="1.0in" height="0.5512817147856518in"}\~ Z\
> - θ : likelihood function을 maximizing하는 argument\
> - (pseudo) t-ratio랑 비슷, linear regression에서는 t 맞음

iii. P-value for statistics\
     > - two-tailed\
     > ![](media/image23.png){width="1.7847222222222223in" height="0.18786526684164478in"}\
     > - one-tailed\
     > ![](media/image24.png){width="1.6736111111111112in" height="0.21178477690288713in"} ![](media/image25.png){width="1.5694444444444444in" height="0.1955686789151356in"}

iv. Significance\
    > ![](media/image26.png){width="1.1180555555555556in" height="0.39460739282589674in"}\
    > - Normal approximation large sample size가 아주 중요\
    > - if small sample size?  P(type I error) \> alpha\
    > more type I error (false-positive) than exp. !!

```{=html}
<!-- -->
```
2.  **Data example I -- Statistical Inference**

> ![](media/image27.png){width="5.34542104111986in" height="2.28125in"}

3.  **Model fit assessment**

```{=html}
<!-- -->
```
1)  Data: Y = 0/1 (binary)\
    ![](media/image28.png){width="2.0274726596675414in" height="0.19317804024496937in"}

2)  Assumption

    1.  Linearity Assumption:\
        > $\text{g}{\text{\{p}\left( \text{x1,…,xp} \right)}\text{\}~=~}\text{β}_{0} + \text{β}_{1}\text{x1}$ +...+${\ \text{β}}_{p}\text{xp}$

    2.  Independence Assumption:\
        > Y~1~,.., Y~n~ are independent random variables

    3.  Logit link function:\
        > ${\text{g}\left( \text{p} \right)\text{~=~ln}}\left( \frac{\text{p}}{\text{1}\text{-}\text{p}} \right)$ ... *No error term!!*

3)  Residuals in logistic ... 일반적인 linear에서 한 건 *response residuals* !

    1.  Logistic Regression without replications

> \- p개 X Y 1개 : binomial 시행 1번\
> ![](media/image29.png){width="2.656715879265092in" height="0.2554527559055118in"}\
> ![](media/image29.png){width="1.0447758092738408in" height="0.2548611111111111in"}![](media/image30.png){width="1.8059700349956256in" height="0.2315343394575678in"}

2.  Logistic Regression with replications

> \- p개 X Y n개: binomial 시행 n번\
> ![](media/image31.png){width="3.156715879265092in" height="0.22418088363954505in"}
>
> \- residuals 여러 번 반복 시행해야 생김
>
> \- probability sample (one X set)마다 하나씩 있음\
> ![](media/image32.png){width="2.611940069991251in" height="0.6120909886264218in"}
>
> i\) **Pearson Residuals:** from *binomial r \~ N(0,1)\
> *![](media/image33.png){width="0.9179101049868766in" height="0.4881364829396325in"}
>
> ii\) **Deviance Residuals**: likelihood ratio (saturated model vs fitted)의 제곱\
> r \~ N(0,1) (*likelihood function 성질때문에*)\
> ![](media/image34.png){width="3.783581583552056in" height="0.3542136920384952in"}\
> 이거 제곱한 D가 deviance residual\
> \
> **\[types of residuals\] ...** 무슨 residuals 간에 $\chi_{\text{df}}^{2}$ *분포*\
> **•response residuals**: 우리가 일반적으로 아는 거; y -- y hat\
> ![](media/image35.png){width="0.9626859142607174in" height="0.2682895888013998in"}\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image36.png){width="2.8879768153980754in" height="0.593241469816273in"}\
> **•working residuals**: y hat으로 표준화\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image37.png){width="0.9625in" height="0.43889982502187225in"}\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image38.png){width="2.783581583552056in" height="0.5998512685914261in"}\
> **•Pearson residuals**: sqrt(y hat)으로 표준화\
> ![](media/image39.png){width="0.8880588363954506in" height="0.5115223097112861in"}\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image40.png){width="2.8879768153980754in" height="0.5949770341207349in"}\
> **•deviance residuals**: likelihood ratio (saturated vs proposed model)의 제곱\
> saturated는 모든 샘플이 완벽하게 들어맞는 model (parameter를 엄청나게 많이)\
> proposed는 원하는 parameter를 넣고 만든 model\
> ![](media/image41.png){width="2.4179101049868765in" height="0.25230424321959755in"}\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image42.png){width="2.7611931321084864in" height="1.3369280402449695in"} Poisson 계산

4)  Model Goodness of Fit (GOF) ... model assumption이 잘 지켜지는가

    1.  GOF Visual Analytics

> \- Normal Probability plot & Histogram of the Residuals
>
> \- Residuals vs predictors ... Linearity & Independence Assumption
>
> \- Logit of success rate vs predictors ... Linearity Assumptions

2.  Hypothesis Testing Procedure

> \- statistic: D = $\sum_{i = 1}^{n}d_{i}^{2}
> $- D\~$\chi_{\text{df}}^{2}$ with [df = n-p-1]{.underline} (model 만들 때 parameter는 p+1개니까\
> - 여기서는 **[p가 커야함]{.underline}**

5)  Goodness of Fit vs. Predictive Power

> \- GOF: model assumption이 잘 지켜진다 = model이 데이터에 잘 맞다
>
> \- predictive power: X가 Y를 잘 예측한다 (model assumption이 한 두 개 안 맞아도)\
> ![](media/image43.png){width="2.7637357830271214in" height="1.4342246281714786in"}\
> ↑(왼) not fitted, high predictive power (오) GOF (s-shaped), low power
>
> \- logistic regression은 p에 굉장히 민감하기 때문에 몇몇 데이터 포인트는 안 맞을 수 있음\
> (≠ predictive power가 떨어진다)

6)  If no GOF?

    1.  X를 선별 or X/Y 변환 (log취한다든지) linearity ↑

    2.  outlier, leverage points 빼기

    3.  binomial 분포 자체가 안 맞는 경우

```{=html}
<!-- -->
```
i.  **overdispersion** (correction 해야함)\
    > binomial의 variance보다 훨씬 큼 (heterogeneity in the success p)\
    > 혹은 X끼리 correlation

ii. **logit function이 틀린 경우\
    > **link function으로 S-shape function 사용 (probit, c-log-log)\
    > ![](media/image44.png){width="4.861081583552056in" height="2.761194225721785in"}

> \* **probit**: 표준 정규분포 누적확률을 역수한 것 (inverse of the CDF of a standard normal distribution) ... 가장 데이터가 모여져 있는 경우, small range\
> y가 1일 확률을 역수..?!
>
> \* **complementary-log-log**
>
> ![On the Predictive Analytics of the Probit and Logit Link Functions \| Semantic Scholar](media/image45.png){width="3.5055555555555555in" height="1.5447769028871392in"}
>
> [* 사실 뭐 여러가지 이유에서 logit이 좋고 그래서 다들 많이 씀*]{.underline}

4.  **Data example II -- Model Fit Assessment**

```{=html}
<!-- -->
```
1)  GOF hypothesis test \~ 모델이 데이터에 맞는지

```{=html}
<!-- -->
```
1.  Deviance Test for GOF (deviance residuals)

> ![](media/image46.png){width="3.478021653543307in" height="0.3710761154855643in"}\
> ... D statistics와 p-value ... not good

2.  GOF test using Pearson residuals

> ![](media/image47.png){width="3.0165179352580926in" height="0.701492782152231in"}\
> ... Pearson residuals로도 볼 수 있음 ... not good

2)  Linearity assumption

-   Linear fit (logit \~ X)\
    > ![](media/image48.png){width="5.092230971128609in" height="0.41805227471566053in"}

> ![](media/image49.png){width="1.5936132983377078in" height="1.3846150481189852in"} ... (logit \~ age) linear는 아닌 것 같고 이차식quadratic

3)  Improving fit

-   그림 그려보니 logit \~ X가 이차식? X' = X^2^도 추가해서

> ![](media/image50.png){width="4.531792432195975in" height="2.0645614610673664in"}

-   Weight: replication이 있을 때 trials로 나누는 건데.. quasi-likelihood 로 다루게 됨..?\
    > (over-dispersion인 경우, 일반적 distribution만으로 해결 안 될 때)

-   이렇게 하고 GOF하면 좋아지고 residual 분석도 괜찮아 보임\
    > ![](media/image51.png){width="3.8406594488188976in" height="0.98207895888014in"}

4)  Residual plots\
    ![](media/image52.png){width="3.2825415573053367in" height="1.2692300962379703in"} ![](media/image53.png){width="3.8491601049868764in" height="2.087911198600175in"}

5)  X에 factor가 들어있을 경우\
    ![](media/image54.png){width="3.683876859142607in" height="1.8880588363954505in"}

> factor의 각 dummy value별로 나옴.. 근데 이렇게 하니까 GOF가 더 좋아짐 ..

6)  Link를 probit으로도 해보고 GOF도 보고

7)  Simpson's paradox:\
    marginal model에서랑 conditional model에서 effect 부호가 달라져 버리는 것

```{=html}
<!-- -->
```
5.  **Classification**

```{=html}
<!-- -->
```
1)  Classification Objective:\
    logistic으로 model 만들어서 새 Y가 왔을 때 Y가 1일 확률을 예측 해보기\
    ![](media/image55.png){width="2.390109361329834in" height="0.5049529746281715in"}

-   1로 판정할 확률 threshold는 내가 정하지만 0.5보단 커야 그럴 듯할 것

2)  Classification Error Rate

-   Training error rate: 모델 만든 다음에 틀리게 예측한 거 비율

-   True error rate: training에 사용한 거 말고 새 데이터를 넣어서 error rate을 estimation

-   Classification error rate\
    > ![](media/image56.png){width="1.574627077865267in" height="0.23034886264216972in"} ... h는 classifier

3)  Cross Validation

```{=html}
<!-- -->
```
1.  Model의 true error rate을 찾기 위한 방법

2.  Data = training set + testing/validation set

    -   Random subsampling; training, testing에 들어갈 거 새로 뽑기

    -   K-fold cross-validation (KCV): k 묶음으로 나누기 (K↑ = bias ↓ variance ↑)\
        > ![ML\] Cross validation과 GridSearch하는 방법](media/image57.png){width="3.684032152230971in" height="2.261194225721785in"}

    -   Leave-one-out Cross-Validation: 하나씩 빼는 거 (k가 n인 KCV)

3.  Error rate (performance): data set별(m개)로 하고 평균 내기\
    ![](media/image58.png){width="3.240582895888014in" height="0.387749343832021in"}

    -   random에서는 (random으로 만든 묶음)\*N에서 error rate 평균

    -   KCV에서는 m번 해서 나온 error rate 평균

    -   사실 random이 KCV랑 비교해서 error rate을 정확하게 구하는 것도 아니라 KCV를 많이 함
