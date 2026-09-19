I.  **Estimation and inference**

    1.  Objectives and Data Examples

    2.  Basic Concepts

    3.  Estimation Method

    4.  Model Interpretation

    5.  Estimation Data Examples

II. **Statistical Inference and Prediction**

    1.  Statistical Inference

    2.  Testing for Subsets of Coefficients

    3.  Data example I -- Statistical Inference

    4.  Regression Line Estimation & Prediction

    5.  Data example II -- Regression Line Estimation & Prediction

III. **Model Diagnostics, Evaluation and Multicolinearity**

     1.  Assumptions and Diagnostics

     2.  Data example I -- Assumptions and Diagnostics

     3.  Model Evaluation and Multicollinearity

     4.  Data example II -- Model Evaluation and Multicollinearity

IV. **Case Study: Ranking States by SAT Performance**

    1.  Exploratory Analysis

    2.  Analysis

    3.  States by SAT

    4.  Model Fit Assessment

V.  **Case Study: Prediction of IMDb Movie Ratings**

    1.  Exploratory Analysis

    2.  Regression Analysis

    3.  Prediction and Findings

```{=html}
<!-- -->
```
1.  **Statistical inference**

```{=html}
<!-- -->
```
1)  Regression estimator

> \- model by design matrix\
> ![](media/image1.png){width="3.3161614173228346in" height="1.1584164479440069in"}
>
> \- estimation ... MSE\
> ![](media/image2.png){width="3.5940594925634297in" height="0.8768132108486439in"}\
> ![](media/image3.png){width="2.6756517935258093in" height="0.37313429571303586in"}

2)  Beta (regression estimations)의 특성\
    ![](media/image4.png){width="1.9925371828521434in" height="0.7164173228346457in"}\
    ... 전체 variability에 각자 X의 특성(variability)이 더해진 느낌\
    ... variance-covariance matrix of b (beta/X 간의 관계성)

```{=html}
<!-- -->
```
1.  Estimates of beta\
    beta (parameter)로 이루어진 vector. 모수 beta의 unbiased estimator\
    ![](media/image5.png){width="1.3035706474190727in" height="0.45959208223972003in"}\
    ![](media/image6.png){width="1.9925371828521434in" height="0.5469706911636045in"}... Y를 X와 e로 표현\
    ![](media/image7.png){width="2.6268657042869643in" height="0.5669499125109362in"} ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image8.png){width="1.6481036745406825in" height="0.3339293525809274in"}\
    ... ![](media/image9.png){width="0.6258694225721785in" height="0.2537314085739283in"} by linear 가정 or ![](media/image10.png){width="2.296372484689414in" height="0.221580271216098in"} ... ![](media/image11.png){width="0.7935323709536308in" height="0.24626859142607174in"}

2.  Distribution of beta (parameter는 항상 추정하는 것 항상 분포/분산 제시!)\
    e~i~ \~ N (0,sigma^2^) ![](media/image12.png){width="0.9107141294838145in" height="0.32114720034995625in"}**\
    **

3.  **variance-covariance matrix (b) of the OLS estimator**\
    (\* OLS, ordinary least squares: MSE를 행렬 미분으로 구하는 방법)

> \- V(b) = 편차/error 제곱 합의 평균\
> = ![](media/image13.png){width="1.373134295713036in" height="0.31180555555555556in"}
>
> \- sigma = 상수\
> ![](media/image14.png){width="0.9198184601924759in" height="0.5370374015748032in"} ... esimated by data Y
>
> \- beta estimator\
> ![](media/image6.png){width="1.9909241032370955in" height="0.27787073490813646in"}
>
> \- V(b) estimator\
> ![](media/image15.png){width="3.723279746281715in" height="0.5527580927384077in"}... (AB)' = B'A'**\
> **![](media/image13.png){width="3.7531310148731407in" height="0.31227580927384074in"}... X는 정해진 값**\
> **![](media/image16.png){width="3.5298501749781277in" height="0.7328762029746282in"}**\
> **![](media/image17.png){width="4.864469597550306in" height="1.1159120734908137in"}\
> \
> \* covariance ... X 편차, Y 편차 곱의 평균\
> ![](media/image18.png){width="1.631868985126859in" height="1.1590715223097112in"}\
> \* correlation ... cov를 s.d.로 표준화\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image19.png){width="1.2348632983377077in" height="0.4212970253718285in"}\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image20.png){width="1.7243580489938757in" height="0.3981474190726159in"}

4.  OLS standard errors = too big or too small?\
    Weighted Least Squares / Robust standard errors\
    e.g. Robust (Huber of White) Standard Errors (OLS의 s.e.)\
    ![](media/image13.png){width="3.4722222222222223in" height="0.28890310586176726in"}\
    ![](media/image21.png){width="3.0462970253718287in" height="0.5749846894138233in"}\
    ![](media/image22.png){width="3.9212970253718287in" height="0.9662051618547681in"}\
    ![](media/image23.png){width="2.361111111111111in" height="0.8638210848643919in"}

```{=html}
<!-- -->
```
3)  sampling distribution (sigma)의 특성 ... df = n- (p+1), t-distribution\
    ![](media/image24.png){width="3.6435192475940505in" height="1.6800721784776902in"}

4)  C.I. estimation (t-interval)\
    ![](media/image25.png){width="3.7083333333333335in" height="1.3344411636045495in"}\
    *이 사이에 0이 있으면 유의하지 않음!*

5)  Testing significance

```{=html}
<!-- -->
```
1.  ![](media/image26.png){width="1.2916666666666667in" height="0.7287609361329834in"}가설 ... b가 0(no effect)인가 아닌가(significant effect)\
    ![](media/image27.png){width="1.9626870078740157in" height="0.3798753280839895in"}

2.  Statistic ... t 절대값이 클수록 0이랑 유의하게 떨어져 있다!

```{=html}
<!-- -->
```
2.  **Testing for Subsets of Coefficients**

```{=html}
<!-- -->
```
1)  Overall regression ... **ANOVA**로 testing for multiple regression

```{=html}
<!-- -->
```
1.  Data summary\
    ![](media/image28.png){width="4.119402887139108in" height="0.8584755030621173in"}\
    - total은 실제 Y에 대한 거니까 n-1\
    - Regression은 X 개수\
    - 여기서 나오는 residual은 \[각 X의 평균(regression)\]으로 설명하고 남은 거

2.  SSReg (between-group var) / SST (within-group var)\
    ![](media/image29.png){width="3.723279746281715in" height="0.3073173665791776in"}

3.  가설\
    ![](media/image30.png){width="1.7537314085739282in" height="0.2595767716535433in"} ... ***어떤 X는 Y랑 연관이 있다!*** (reject H~0~)

4.  Statistic for test\
    **F-statistics** = 그룹(각 X)로 설명되는 거; between-group\
    / 각 개체(Y)로 설명되는 거; within group\
    = explained variance\
    ![](media/image31.png){width="1.5043853893263341in" height="0.1985356517935258in"}

```{=html}
<!-- -->
```
2)  Testing subsets of coefficients ... *covariate 순서가 중요한 이유*\
    ![](media/image32.png){width="4.559101049868766in" height="0.7940288713910761in"}

```{=html}
<!-- -->
```
1.  SSReg(X~1~) ... Y를 예측(Y의 variance를 설명)할 때 X~1~으로 설명되는 SS

2.  SSReg(X~2~ \| X~1~) ... X1하고 나서 남은 것 중에 X~2~로 설명되는 SS

3.  SSReg(X~3~ \| X~1~, X~2~) ... X~1~, X~2~하고 나서

4.  SSReg(X~p~ \| X~1~, X~2~, ..., X~p-1~) ... 다 하고 남은 것 중에 X~p~로 설명되는 SS

```{=html}
<!-- -->
```
3)  General expression

```{=html}
<!-- -->
```
1.  Model ... p개는 controlling factors, q개는 explanatory factors\
    ![](media/image33.png){width="4.455223097112861in" height="0.34157042869641296in"}

2.  가설 ... q에 대해서\
    ![](media/image34.png){width="4.014924540682415in" height="0.290909886264217in"}

3.  Statistic\
    ![](media/image35.png){width="3.059701443569554in" height="0.603406605424322in"} ... X로 설명되는 SSE 중에 얼마나?\
    ![](media/image36.png){width="1.970148731408574in" height="0.29161089238845145in"} ... 적어도 한 X~k~는 다르다

4.  [F \> 2]{.underline}면 대충 도움된다고 할 수 있음

**\
**

3.  **Statistical Inference Data Examples\
    **![](media/image37.png){width="5.504385389326334in" height="2.631719160104987in"}

```{=html}
<!-- -->
```
1)  C.I.\
    ![](media/image38.png){width="3.186567147856518in" height="0.6714884076990376in"}

2)  Condition 차이 (partial F test)

> ![](media/image39.png){width="4.0894520997375325in" height="1.425372922134733in"}
>
> ![](media/image40.png){width="3.0223873578302713in" height="0.8763112423447069in"}
>
> ![](media/image41.png){width="3.4166666666666665in" height="0.6412401574803149in"}

**\
**

4.  **Regression Line: Estimation & Prediction**

```{=html}
<!-- -->
```
1)  Estimating the Regression Line\
    ![](media/image42.png){width="4.0526312335958in" height="0.3731146106736658in"}

2)  Y estimator:\
    X랑 b로 regression했을 때 예측할 수 있는 값들의 평균값 (normal, T-distribution)

3)  Var(y estimate):\
    ![](media/image43.png){width="2.5166666666666666in" height="0.31646544181977254in"}... ![](media/image44.png){width="0.7666666666666667in" height="0.25824584426946634in"} (chi-squared distribution)

4)  C.I. for regression line

> \- x가 정해졌을 때 가질 수 있는 y의 평균값 / 선 위에 있는 값\
> (the regression line or mean response for one instance of predicting variables x\*)\
> ![](media/image45.png){width="2.911111111111111in" height="0.5699015748031496in"}
>
> \- y가 가질 수 있는 모든 p+1개의 값\
> (all possible instances of the predicting variables) *\
> *![](media/image46.png){width="3.911111111111111in" height="0.38651793525809275in"}

5)  prediction

```{=html}
<!-- -->
```
1.  Y estimate의 variation:\
    > ![](media/image47.png){width="1.283581583552056in" height="0.28969706911636045in"}

2.  New measurement에 대한 variance (Y hat의 sampling variance):\
    > ![](media/image48.png){width="0.271910542432196in" height="0.21641841644794402in"}

3.  Predicted value Y에 대한 total variation

> ![](media/image49.png){width="2.0223873578302713in" height="0.4247014435695538in"}

4.  1개 값에 대한 prediction:\
    > ![](media/image50.png){width="2.8504975940507435in" height="0.4585553368328959in"}

5.  M개 값에 대한 prediction:\
    > ![](media/image51.png){width="3.34328302712161in" height="0.3300317147856518in"} ... M 개만큼 분산이 커짐

```{=html}
<!-- -->
```
5.  **Estimation & Prediction Data Examples**
