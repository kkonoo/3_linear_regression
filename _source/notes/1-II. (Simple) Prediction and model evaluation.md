I.  **Estimation and inference**

    1.  Basics

    2.  Estimation method

    3.  Data example I -- Estimation

    4.  Statistical inference

    5.  Data example II -- Inference

II. **Prediction and model evaluation**

    1.  Regression line estimation and prediction

    2.  Data example I -- Regression line estimation and prediction

    3.  Diagnostics

    4.  Outlier and predictive power

    5.  Data example II -- Diagnostics and model evaluation

III. **Data examples**

     1.  Testing the theory of purchasing power parity \#1

     2.  Testing the theory of purchasing power parity \#2

     3.  2000 Elections in Florida

```{=html}
<!-- -->
```
1.  **Regression line estimation and prediction**

```{=html}
<!-- -->
```
1)  ![](media/image1.png){width="1.680077646544182in" height="1.509202755905512in"}Estimation vs. Prediction ... Regression의 목적

> \- prediction: 어떤 것에 대해 미래 or 다른 조건일 때의 response를 예측\
> predictor (x\*) = new observation\
> response (y) = estimated mean response for [one]{.underline} setting
>
> \- estimation: 이미 있는 value를 regression으로 fitting\
> predictor (x\*) = one of observations\
> response (y) = [average]{.underline} estimated mean response for [all]{.underline} settings
>
> \- uncertainty\
> estimation: estimation의 uncertainty\
> prediction: uncertainty in estimation + uncertainty in new observation

2)  Estimation ... Estimating the regression line

```{=html}
<!-- -->
```
1.  Distribution of estimate\
    > ![시계이(가) 표시된 사진 자동 생성된 설명](media/image2.png){width="1.5802996500437445in" height="0.35582895888014in"} ... $\widehat{y}$ \~ normal (∵ b0, b1 \~ normal)\
    > y의 mean, var만 알면 estimation이 가능!

> ![](media/image3.png){width="2.235773184601925in" height="0.7975459317585302in"}\
> ... var = b0 var + b1 var \* x var\
> x\*가 $\overline{x}$에서 멀어질수록 variability ↑

2.  Confidence interval for mean response\
    > ![](media/image4.png){width="2.3104549431321084in" height="0.6071555118110237in"}\
    > ... regression estimator를 사용하므로 t-value 사용!

```{=html}
<!-- -->
```
3)  Prediction

```{=html}
<!-- -->
```
1.  predicting a new response\
    > uncertainty = parameter estimates (of b0 and b1 ) + the new (n+1)th observation\
    > ![](media/image5.png){width="3.611111111111111in" height="0.7209416010498688in"}

2.  confidence interval\
    > ![](media/image6.png){width="3.224701443569554in" height="0.6527777777777778in"}

```{=html}
<!-- -->
```
2.  **Data example I -- Regression line estimation and prediction**

> \- regression: 판매량 \~ 광고비
>
> \- 광고비에 따라 판매량 예측/측정 + C.I.**\
> **![](media/image7.png){width="5.43476924759405in" height="2.2604166666666665in"}**\
> **![](media/image8.png){width="5.370833333333334in" height="2.7824857830271217in"}

3.  **Diagnostics**

```{=html}
<!-- -->
```
1)  simple linear regression (review)

> \- data: bivariate ![](media/image9.png){width="1.6319444444444444in" height="0.2777023184601925in"}
>
> \- model: linear combination b/w X and Y ![](media/image10.png){width="1.8338265529308837in" height="0.2361111111111111in"}
>
> \- assumptions:\
> ![](media/image11.png){width="4.285515091863517in" height="1.2173611111111111in"}

2)  Residual analysis\
    ![](media/image12.png){width="1.6413495188101488in" height="0.28958333333333336in"} ... residuals가 어떻게 생겼는가로 모델 판단

```{=html}
<!-- -->
```
1.  Line 근처에 데이터가 퍼져 있지 않고 몰린 경우 ... 뭔가 random이 아님

> \- X랑 Y가 선형관계가 아님 ... **linearity assumption**\
> ![](media/image13.png){width="2.0476279527559056in" height="1.4880008748906386in"}
>
> \- Error term의 variance != 0 ... **constant variance assumption\
> **![](media/image14.png){width="2.018779527559055in" height="1.4640004374453193in"} ; relationship b/w X and variance
>
> \- Y가 독립이 아님(=X가 독립이 아님) ... **independence assumption\
> **![](media/image15.png){width="2.0879997812773405in" height="1.3064260717410323in"}**\
> ** cluster of residuals (uncorrelated & dependent errors)\
> \* 근데 사실 residual analysis에서는 uncorrelation만 따짐. independence는 human data를 모으면 그 자체로 independence 확보

3)  **Normality assumption** ... by QQ-plot + histogram![](media/image16.png){width="2.0395833333333333in" height="1.8923611111111112in"}

> normal probability plot
>
> x = exp (residual의 normal 상에서 probability)\
> y = residual (error \~ normal)
>
> ![](media/image17.png){width="3.5694444444444446in" height="1.5490048118985127in"}

1.  Normality ... 딱 선에 맞고 histogram도 종 모양\
    > ![](media/image18.png){width="3.216000656167979in" height="1.4868569553805775in"}

2.  skewed (여기선 right-/positively-) ... C-shaped & histogram도 쏠려 있음\
    > ![](media/image19.png){width="3.136000656167979in" height="1.44500656167979in"}... 예상보다 residual이 적은 게 많다

3.  uniform distribution... S-shaped\
    > ![](media/image20.png){width="3.0720002187226596in" height="1.414494750656168in"}

```{=html}
<!-- -->
```
4)  ![](media/image21.png){width="0.8888888888888888in" height="0.3125in"}![](media/image22.png){width="3.9375in" height="1.5298611111111111in"}Variable transformation\
    Residual analysis를 했는데 여러 가정에 안 맞는다?\
    Y를 변형하면 linear regression 가능!\
    **BoX-Cox Transformation\
    \
    \
    **

```{=html}
<!-- -->
```
4.  **Outlier and predictive power**

```{=html}
<!-- -->
```
1)  Outliers in regression ... **car::outlierTest()**

```{=html}
<!-- -->
```
1.  **Outliers**: data point far from the majority of the data (X, Y 둘 중 하나)

2.  **Leverage points**: data points far from the mean **X\
    **far from = 2\*s.d. (commonly)

3.  **Influential points**: data points far from the both mean X & mean Y\
    제일 문제

```{=html}
<!-- -->
```
2)  Upshot ... excluding outliers

```{=html}
<!-- -->
```
1.  Checking for outliers\
    - **standardized residuals\
    **![](media/image23.png){width="1.4477602799650044in" height="0.6258880139982502in"}**... MSE를 그냥 y의 variance랑 같다고 가정하니까**

> \- outlier = +- 2\*s.r. (1x 할 때도 있음)

2.  Predictive power

```{=html}
<!-- -->
```
i.  **coefficient of determination\
    > - 만든 model의 fitness 정도 판단 기준\
    > **![선형회귀의 적합성 평가와 과적합을 판단하는 방법](media/image24.png){width="3.160004374453193in" height="1.6458333333333333in"} ![텍스트, 시계이(가) 표시된 사진 자동 생성된 설명](media/image25.png){width="0.9027777777777778in" height="0.43545713035870515in"}**\
    > R^2^ = SSR/SST = 1-SSE/SST\
    > ** 전체 Y의 variability 중 (X로 regression) fitted value로 설명되는 비율\
    > (= fitted로 예측하나 real로 예측하나 비슷하다)\
    > *[= 이게 y,]{.underline}* $\widehat{y}$*[의 correlation이랑 같음?!\
    > ]{.underline}*

**\
**

ii. **correlation coefficient\
    > **![](media/image26.png){width="3.7531310148731407in" height="0.7813134295713036in"}**... b1 = Sxy / Sxx\
    > b1^2^(S~XX~) =** $\sum_{}^{}{(bx - b\overline{x}})2$**=** $\sum_{}^{}{(\widehat{y} - \overline{y}})2$ **= SSR\
    > S~YY~ = SST\
    > ** ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image27.png){width="0.9029265091863518in" height="0.3055555555555556in"} = SSR/SST

iii. **Coefficient of variation (CV = relative standard deviation, RSD)\
     > **![Coefficient of Variation (Definition, Formula)\| How to Calculate?](media/image28.jpeg){width="3.6805555555555554in" height="0.4513888888888889in"}**\
     > **![Statistics - How to calculate the coefficient of variation - YouTube](media/image29.jpeg){width="3.6180555555555554in" height="1.0277777777777777in"}

> **여러 데이터셋을 한 번에 비교하고 싶을 때 표준화**

5.  **Data example II -- Diagnostics and model evaluation**

> \- residual analysis 해보기\
> ![](media/image30.png){width="4.201388888888889in" height="2.344912510936133in"}
>
> \- outlier 찾기 & explained variability 측정하기 (R^2^)\
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image31.png){width="4.111940069991251in" height="1.6277373140857392in"}

그냥 참고... abline에 그냥 lm model을 넣어도 그림 그려짐\
![](media/image32.png){width="2.313888888888889in" height="0.3611111111111111in"}\
![](media/image33.png){width="3.3731342957130357in" height="0.6277548118985127in"}\
![](media/image34.png){width="2.5833333333333335in" height="2.0137773403324584in"}
