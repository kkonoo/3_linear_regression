\#\#3.4 / 3.5

1.  Explanatory analysis; 데이터의 대략적인 거 파악

```{=html}
<!-- -->
```
1)  Data : SAT score \~ takers + income + state ..

> **Attach()**
>
> ![](media/image1.png){width="4.344444444444444in" height="1.3183508311461067in"}
>
> ![](media/image2.png){width="5.166666666666667in" height="0.38352143482064743in"}

2)  각 x에 대해 histogram 그려보면 뭐 하나 동떨어진 게 있으면 그걸 빼야할 수도.. (outlier)

> ![](media/image3.png){width="3.763888888888889in" height="1.3573523622047243in"}

3)  Scatter matrix 그려서도 확인해 봄 & x끼리의 cor

> ![](media/image4.png){width="0.9791666666666666in" height="0.23080380577427823in"} ![](media/image5.png){width="1.788888888888889in" height="0.21371719160104988in"}
>
> ![](media/image6.png){width="1.9241240157480315in" height="1.4722222222222223in"} ![](media/image7.png){width="2.4791666666666665in" height="0.9207130358705162in"}

2.  Regression analysis; Y와 X의 slope를 아는 게 목적?

```{=html}
<!-- -->
```
1)  Overall model에 대하여 & 한 X에 대하여

> ![](media/image8.png){width="6.268055555555556in" height="2.4583333333333335in"}

2)  Partial model에 대하여

-   Controlling factor에 의한 SSR뺴고

-   내가 원하는 predictor 중 하나는 효과가 있다?! TEST

> ![](media/image9.png){width="3.986111111111111in" height="0.2569444444444444in"}
>
> ![](media/image9.png){width="5.430555555555555in" height="0.5694444444444444in"}
>
> ![](media/image10.png){width="2.9583333333333335in" height="2.2406922572178476in"};; 약간 틀린 건가?

3)  Controlling factor를 고려하여 더 나은 ranking 만들기

-   SAT이 필수인 지역은 아무나 다 보기 때문에 필수 아닌 지역 애들(elite)은 rank랑 SAT이 크게 상관 없을 수 있음 그거 고려해서 새 rank 만들어주기

-   근데 왜 residual의 rank를 먹이지? **Residual의 rank**가 왜 중요해서..

> ![](media/image11.png){width="5.170833333333333in" height="1.0140015310586177in"}
>
> ![](media/image12.png){width="3.9652777777777777in" height="1.8135017497812773in"}

3.  Model assesement

```{=html}
<!-- -->
```
1)  필요한 거 : residual , cook's distance(outlier 평가)

> ­![](media/image13.png){width="2.5208333333333335in" height="0.3821314523184602in"}

2)  Check points

```{=html}
<!-- -->
```
1.  Constant Variance & Uncorrelated Errors : Response Variable or Fitted Values vs Residuals

> ![](media/image14.png){width="4.972222222222222in" height="0.927678258967629in"}
>
> ![](media/image15.jpeg){width="5.618055555555555in" height="1.170168416447944in"}
>
> percent of student tested 가 heavy tail..? (사실 그냥 res로 hist 그려봤을 때.. X에 따라 res가 커져서 그런가;;) Transform이 필요해보임!

2.  Linearity: Predicting Variables vs Residuals

3.  Normality: Histogram and QQ normal plot

> ![](media/image16.png){width="2.9027777777777777in" height="0.536431539807524in"}
>
> ![](media/image15.jpeg){width="5.61791447944007in" height="1.3229166666666667in"}

4.  Outliers: Cook Distance Plots

```{=html}
<!-- -->
```
3)  Takers를 log로 바꿔서 했더니 model이 더 좋아졌으나 여전히 heavy tail cook으로 outlier 제거!

> ![](media/image17.png){width="3.9583333333333335in" height="2.0756474190726157in"}

4.  X가 fator인 거 섞여있을 때!

```{=html}
<!-- -->
```
1)  as.factor로 잘 만들기!

> ![](media/image18.png){width="2.0405358705161856in" height="0.9722222222222222in"}; 근데 사실 character로 되어있으면 자동으로 됨
>
> ![](media/image19.png){width="2.7428576115485566in" height="0.1875in"} ![](media/image20.png){width="1.6127755905511811in" height="1.1944444444444444in"}

2)  multicolinearity check하기

> ![](media/image21.png){width="3.0374311023622047in" height="1.9652777777777777in"}

3)  Pearson\'s chi-squrared test : qualitative X 끼리의 correlation 확인할 때

> ![](media/image22.png){width="3.5421456692913385in" height="2.986111111111111in"}

5.  덤

```{=html}
<!-- -->
```
1)  Dummy variable 만들어서 factor X에 대해 regression 연습해보기

> ![](media/image23.png){width="2.51876968503937in" height="2.2083333333333335in"} ![](media/image24.png){width="2.7222222222222223in" height="0.9482228783902013in"}
>
> ![](media/image25.png){width="3.4952941819772527in" height="3.5277777777777777in"}

-   R에서는 factor test 할 때 제일 첫번째걸 baseline으로 잡음! **contr.treatment()** 를 쓰거나 하나하나 다 보고싶으면 dummy value로 만들어서 분석!

-   R에서 intercept 없이 할 때 조심해야함..!! 뭔가 다 유의하게 나오는 걸 해석 잘 해야.. (4개 category dummy 3개로 표현할 수 있고 그 때 하나는 0,0,0으로 intercept랑 같은 의미..)

2)  Marginal vs conditional

-   Conditional : controlling factors 없애고

> ![](media/image26.png){width="5.7125in" height="1.0202252843394575in"}

-   Marginal : 걔 하나만 보는 거; 나머지는 다 control

> X가 category면 anova(model); X가 numeric이면 summary(model)
>
> ![](media/image27.png){width="3.8958333333333335in" height="1.1127263779527559in"}

6.  Prediction

```{=html}
<!-- -->
```
1)  Prediction : **predict(newdata, interval = c(\"prediction\"))**

> ![](media/image28.png){width="6.268055555555556in" height="1.0222222222222221in"}

2)  Prediction accuracy

> ![](media/image29.png){width="2.5999825021872267in" height="1.6736111111111112in"}
>
> ![](media/image30.png){width="2.6572331583552056in" height="1.3888888888888888in"}![](media/image31.png){width="2.5416666666666665in" height="0.6801640419947507in"}
>
> ![](media/image32.png){width="3.611111111111111in" height="1.5608923884514436in"}![](media/image33.png){width="1.842382983377078in" height="1.0830971128608924in"}
>
> ![](media/image34.png){width="5.819444444444445in" height="0.6576367016622923in"}
>
> ![](media/image35.png){width="3.25in" height="0.4894575678040245in"}
