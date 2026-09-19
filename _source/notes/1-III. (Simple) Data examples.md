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
1.  Testing the theory of purchasing power parity \#1

-   PPP 구매력평가지수: 한 나라의 화폐는 모든 나라에서 동일한 수량의 재화를 구입할 수 있어야 한다는 것을 전제로 한 환율결정이론. e.g. 빅맥지수

-   X는 미국 대비 inflation rate, Y는 환율 변화 (inflation이 커질수록 환율이 올라감)

> ![](media/image1.png){width="3.3168318022747156in" height="1.4640212160979877in"}

-   Fitting 여부: estimate이랑 se랑 R^2^랑 p-value

> ![](media/image2.png){width="3.742574365704287in" height="1.224443350831146in"}

-   P value는 hypothesis testing에서

2.  Testing the theory of purchasing power parity \#2

```{=html}
<!-- -->
```
1)  Fitting 여부

-   Fitting 잘 됐는지 그려보는 plolt. 더 넢은 band가 prediction. 저 구간을 벗어나는 점이 outlier.

> ![](media/image3.png){width="3.5198020559930008in" height="0.5751946631671041in"}
>
> ![](media/image4.png){width="2.930693350831146in" height="1.9040091863517061in"}

2)  Predict(): 새 value를 넣어서 fitting해줌!\
    ![](media/image5.png){width="2.6138615485564305in" height="0.9089359142607174in"}

> ![](media/image6.png){width="4.257425634295713in" height="0.9028040244969379in"}

-   한 나라를 먼저 뽑고 거기서 나올 수 있는 Y라 커짐

3)  Residual analysis

-   Versus predictor: residual이 X랑 상관없이 random처럼 보임 linearity assumption

-   Versus fits: fitted value랑 그려 봄 constant variance(error가 X에 따라 변하지 않음) and uncorrelated error(residual)

-   밑에 두 개 ... normality assumption

> ![](media/image7.png){width="3.8861384514435695in" height="0.7655172790901137in"}
>
> ![](media/image8.png){width="4.475247156605424in" height="2.4664424759405073in"}

4)  Influential points (Brazil \~ hyperinflation)

-   Brazil은 좀 특수한 경우라 그걸 빼고 새로 분석 pvlaue\~0

-   ![](media/image9.png){width="2.886139545056868in" height="1.656988188976378in"}*Constant Variance:* The variance is higher for higher fitted values. Does not hold. (아직도 잘 안 맞음)

-   QQ-plot에서 크게 떨어지는 애 Indonesia

-   아예 developed / developing으로 나눠서 할 수도 있고 (Brazil , indonesia는 outlier)

3.  Elections in Florida

```{=html}
<!-- -->
```
1)  Bush를 찍은 애들이 buch를 찍을지.. 수가 커서 그런지 log()를 해서 비교함

2)  Palm Beach가 outlier라서 빼고 계산\
    여기서 나온 regression으로 fitted value랑 CI 안에 Palm Beach obs가 있는지 확인\
    어림도 없지만 CI랑 차이가 원래 regression(outlier 안 뺴고)으로 했을 때보단 작아짐
