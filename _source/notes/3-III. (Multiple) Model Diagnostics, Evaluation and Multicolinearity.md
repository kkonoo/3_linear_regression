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
1.  **Assumptions and Diagnostics**

```{=html}
<!-- -->
```
1)  Assumption

```{=html}
<!-- -->
```
1.  Linearity Assumption ... X랑 Y는 선형 관계 (Y를 X의 선형결합으로 표현)

2.  Constant Variance Assumption ... Var(e~i~) = s^2\
    ^(모든 X에 대해, error var는 동일; error estimator인 residual의 var는 다름!)

3.  Independence Assumption ... e들은 independent

4.  Normality Assumption ... e는 normal (exp(ei) = 0 , var(ei) = sigma\^2)

```{=html}
<!-- -->
```
2)  Error (true)와 residuals (estimated)의 properties

    1.  Error (true): 가정에 맞게\
        ![](media/image1.png){width="1.4505489938757656in" height="0.25345581802274714in"}

    2.  Residuals (estimated, ![](media/image2.png){width="0.571428258967629in" height="0.15555555555555556in"}) ... n가 한 번에 vector 형태로

```{=html}
<!-- -->
```
i.  ![](media/image3.png){width="1.6701388888888888in" height="0.8055555555555556in"}![](media/image4.png){width="1.5159339457567804in" height="0.19485017497812773in"} ... 전체 평균도 0, 각자 분포 평균도 0\
    > ∵ E(Y-bx) = E(Y) -- E(bx) = E(Y) -- Ybar = 0

ii. ![](media/image5.png){width="2.3076924759405073in" height="0.22805883639545058in"}\
    > ... (n x n) matrix 형태로; 한 샘플은 대각 성분; *X(b)에 의해 변함!*\
    > ∵![](media/image6.png){width="0.7472528433945756in" height="0.24740157480314962in"} ![](media/image7.png){width="1.9554483814523185in" height="0.3499540682414698in"}\
    > ![](media/image8.png){width="1.8366327646544183in" height="0.24549103237095363in"} ![](media/image9.png){width="1.3680555555555556in" height="0.2912095363079615in"}\
    > V(e hat) = V(**\[1-H\]**\*Y) = (1-H)\* V(Y)

> \* **Hat matrix** (= projection matrix, influence matrix):\
> Y를 fitted Y로 만들어주는 matrix (Y를 X 공간으로 projection)\
> ![](media/image10.png){width="1.2692300962379703in" height="0.22916666666666666in"}(its eigenvalues are 0 and 1)\
> ![enter image description here](media/image11.png){width="2.0736187664041994in" height="1.2430380577427822in"} ![enter image description here](media/image12.png){width="1.987729658792651in" height="1.356991469816273in"}
>
> \* diag element: leverage of i-th obs (sample)\
> ![](media/image13.png){width="1.4494728783902013in" height="0.34065944881889765in"} ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image14.png){width="2.283333333333333in" height="0.2473753280839895in"}
>
> \* residual marker matrix: y를 residual로 만들어주는 matrix. 1-H\
> (1-H)Y = e

1.  Standardized residual:\
    error는 var가 같지만 residual은 X에 따라 var가 달라짐\
    X가 여러 개인 걸 감안하여 residual을 standardize\
    ![](media/image15.png){width="0.8814304461942257in" height="0.45604440069991253in"} ... var(e~i~) = sigma^2^ \* (1-h~ii~)

```{=html}
<!-- -->
```
3)  Diagnosis

    1.  Linearity ... error \~ X (↓)\
        ![](media/image16.png){width="1.6703291776027998in" height="1.2703455818022746in"} ![](media/image17.png){width="1.6923075240594925in" height="1.1542005686789152in"}

    2.  Constant Variance ... residual (not error)은 X에 따라 달라짐

    3.  Independence ... X \~ error\
        ![](media/image18.png){width="1.4660050306211723in" height="1.0054943132108487in"}

    4.  Normality of residuals ... hist or qqplot of residuals\
        ![](media/image19.png){width="1.4079768153980752in" height="2.104395231846019in"}

4)  Fitting 팁

    1.  Predicting Variable Transformation\
        ![](media/image20.png){width="0.7142847769028872in" height="0.2756200787401575in"} ![](media/image21.png){width="2.895604768153981in" height="1.0692497812773403in"}

    2.  Outliers

        i.  종류

> \- Outliers: x나 y가 평균 X나 평균 Y랑 크게 떨어져 있는 것
>
> \- Leverage points: x가 크게 다른 것
>
> \- Influential point: (x, y)가 둘 다 멀리 떨어져 있는 것

ii. Upshot: outlier등을 빼고 분석하는 것

iii. Cook's distance: outlier를 빼고 했을 때 분석 성능 비교\
     > ![](media/image22.png){width="1.6898151793525809in" height="0.5446095800524935in"}\
     > ... = sample I 뺀 뒤 estimate\
     > ... fitted value $\widehat{Y}$ *: X 다 넣고 estimate\
     > *![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image24.png){width="2.5208333333333335in" height="0.3821314523184602in"}*; reduced.line = lm() object*

```{=html}
<!-- -->
```
3.  Controlling factor를 고려하여 더 나은 ranking 만들기

> \- residual의 순서로 re-order..?

**\
**

2.  **Data examples**

```{=html}
<!-- -->
```
1)  Scatter plot matrix \~ **plot**(Y, X~1~, X~2~, X~3~, ...)\
    ![](media/image25.png){width="3.25in" height="2.05456583552056in"} Y와 다양한 X 간의 linearity를 한 번에 파악

2)  Residual analysis

```{=html}
<!-- -->
```
1.  X \~ residual로 linearity 파악\
    *plot(meddcor\[,2\],resids,xlab=\"Adv Expenditure\",ylab=\"Residuals\")\
    *![](media/image26.png){width="3.1296303587051617in" height="1.810650699912511in"}

2.  기타 (Y hat & residuals)\
    ![](media/image27.png){width="1.8461537620297463in" height="0.5339774715660542in"} ![](media/image28.png){width="1.3241754155730534in" height="0.1527898075240595in"}\
    *- plot(fits, resids, xlab=\"Fitted Values\",ylab=\"Residuals\"); abline(0,0,col=\"red\")\
    - qqPlot(resids, ylab=\"Residuals\", main = \"\")*\
    *- hist(resids, xlab=\"Residuals\", main = \"\",nclass=10,col=\"orange\")\
    - plot(cook,type=\"h\",lwd=3,col=\"red\", ylab = \"Cook's Distance\")\
    *![](media/image29.png){width="2.8652777777777776in" height="1.7957983377077866in"}

```{=html}
<!-- -->
```
3.  **Model evaluation**

```{=html}
<!-- -->
```
1)  Coefficient of Determination (결정 계수)\
    ![](media/image30.png){width="1.2032961504811899in" height="0.2588484251968504in"}; ![](media/image31.png){width="0.7252744969378828in" height="0.37085629921259844in"} ![](media/image31.png){width="1.0321008311461068in" height="0.39832895888013997in"}\
    SSE: model로 설명하지 못하는 나머지들 R^2^ = model로 설명되는 Y의 variability

2)  ANOVA로 evaluation

```{=html}
<!-- -->
```
1.  Total model에 대하여 F-test (k = p+1 ... b~0~도 있어서)\
    ![](media/image32.png){width="1.5824168853893263in" height="0.29486001749781277in"}\
    ![](media/image33.png){width="1.1373622047244094in" height="0.225667104111986in"}\
    ![](media/image34.png){width="1.2252744969378828in" height="0.6969860017497813in"} ![multiple regression F에 대한 이미지 검색결과](media/image35.gif){width="1.560554461942257in" height="0.7692300962379702in"} F(k, n-k-1)\
    각 X에 대하여 fitted Y의 평균은 y hat =sum(x\*beta hat)\
    ... **SSR** = (그룹 Y mean -- Y mean) = (Y hat -- Y mean) = **fitted value로 설명하는 variance**\
    ... **SSE** = (실제 Y -- 그룹 Y mean) = (실제 Y -- Y hat) = **residuals (모델로 설명 불가)**

2.  Partial model에 대하여\
    ![](media/image36.png){width="2.5274715660542433in" height="0.25285870516185477in"}\
    ![](media/image37.png){width="1.2692300962379703in" height="0.8012817147856518in"}

**\
**

4.  **Multicolinearity**

```{=html}
<!-- -->
```
1)  Correlation coefficient\
    ![](media/image38.png){width="1.631868985126859in" height="1.1590715223097112in"} ![](media/image39.png){width="1.6084853455818022in" height="0.5486898512685914in"}

2)  Multicollinearity diagnosis\
    ![](media/image40.png){width="1.3901093613298339in" height="0.3431649168853893in"}

> \- collinearity\
> X(column) 중에 correlation 있는 게 있다? X^T^X가 역행렬이 없음 var(b) = 무한대
>
> \- near collinearity

1.  var($\widehat{\beta}$)가 엄청 큼

2.  X가 조금 바뀌어도 beta는 엄청 크게 바뀜 (= var가 크다)

3.  F = 보통 sig, partial (t-statistic) = insig 가능\
    (Y랑 엄청 연관 있는 X1, 그 X1이랑 비슷한 X2, X3, ...\
    당연히 전체모델로 보면 누군가 하나는 연관이 있기 때문에 overall F는 sig\
    ... but partial F는 X1이 다 가져가고 X2, X3는 sig하게 안 나올 수 있음)

4.  당연히 prediction도 안 좋을 것

```{=html}
<!-- -->
```
3)  variance inflation factor(VIF) ... X 마다 나오는 값\
    ![](media/image41.png){width="0.9058814523184602in" height="0.423076334208224in"}\
    (X가 전부 완전 uncorrelated일 때의 한 beta에 대해서 proportional increase,\
    독립변수 X~j~를 다른 독립변수로 회귀한 성능)

```{=html}
<!-- -->
```
1.  전부 uncorrelated\
    VIF = 1

2.  조금 있을 때 1-R^2^ (현재 보이고 있는 proportional increase)\
    VIF = 1 + (R^2^ / 1-R^2^)

3.  ![](media/image42.png){width="1.6339752843394575in" height="0.4120877077865267in"}\
    VIF는 엄청 크지 않기 때문에 X끼리 colinearity가 그렇게 크지 않다고 할 수 있음

```{=html}
<!-- -->
```
4)  data examples\
    ![](media/image43.png){width="5.8277777777777775in" height="2.44255249343832in"}
