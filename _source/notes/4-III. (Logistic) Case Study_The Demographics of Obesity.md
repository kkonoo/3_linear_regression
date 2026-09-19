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
1.  **Exploratory Data Analysis**

```{=html}
<!-- -->
```
1)  Data

> Y (obese) \~ age group (factor) + education (factor) + gender (factor)
>
> Training data (4314) + testing (1000)

2)  **vcd::mosaicplot** (factor끼리 관계를 보는 것)

> ![](media/image1.png){width="2.906593394575678in" height="0.5158836395450569in"}
>
> ![](media/image2.png){width="4.0631332020997375in" height="2.697801837270341in"}

3)  Response vs Predictors

> ![](media/image3.png){width="3.1256944444444446in" height="0.7493908573928258in"}
>
> ![](media/image4.png){width="2.384615048118985in" height="1.55294072615923in"} ![](media/image5.png){width="2.246660104986877in" height="1.4010990813648294in"}

2.  Modeling and Prediction

```{=html}
<!-- -->
```
1)  model

> ![](media/image6.png){width="3.219780183727034in" height="0.2978630796150481in"}
>
> ![](media/image7.png){width="3.003454724409449in" height="1.813186789151356in"}
>
> ... edu는 age, gender를 condition하면 거의 설명 X

2)  test for overall

-   null deviance vs residual deviance

> ![](media/image8.png){width="4.179902668416448in" height="1.1373632983377078in"}

3)  Predictive Power ... Model 만들어서 10-fold cross-validation

```{=html}
<!-- -->
```
1.  Model ... library(**boot**)

> ![](media/image9.png){width="2.880142169728784in" height="0.9780227471566054in"}

2.  Classification error for 10-fold

> ![](media/image10.png){width="3.373626421697288in" height="0.5789654418197725in"}
>
> \- cost function: classification threshold 넣어서 (이미 만든 model로 생성되는) p에 따라 Y 판정하는 함수
>
> \- delta: error term
>
> \- threshold에 따라(cost0.3, cost0.35...) error rate 그림 그려 봄
>
> ![](media/image11.png){width="3.0153083989501313in" height="1.3108869203849518in"}
>
> ... 0.5는 넘어야 accuracy가 높아짐 쓸모가 없음. 사람들이 다 obese가 아니면 어쩔건데 (Y = 0이 많은 경우)

3.  **Goodness of Fit (Logistic regression with replications)**

```{=html}
<!-- -->
```
1)  aggregate data

> ![](media/image12.png){width="3.928571741032371in" height="0.7290441819772528in"}

2)  Fit a logistic regression model

> ![](media/image13.png){width="3.7692311898512685in" height="0.3027580927384077in"}

3)  Test for GOF: Using deviance residuals

> ![](media/image14.png){width="3.148351924759405in" height="0.31357939632545934in"}

4)  Without replications랑 비교

> ![](media/image15.png){width="2.425051399825022in" height="1.829669728783902in"}\
> ... 각 X에 대한 regression coefficient는 같음\
> ... null, residual deviance가 다름! (아까 GOF에서 p= 0.899로 좋았음)

5)  (deviance) Residual 분석

> ![](media/image16.png){width="3.8076924759405073in" height="1.0909251968503937in"}
>
> ![](media/image17.png){width="4.038461286089239in" height="2.087687007874016in"}

6)  결론

-   Gender, age group은 Y의 variability를 설명하는 significant factor지만 fitted model은 딱히 prediction을 잘 하진 않음 (error rate 0.5)

-   factor aggregation하고 나면 (replication이니까) GOF할 수 있음

-   GOF의 deviance p가 높았음 model이 data에 잘 fit

-   Residual test residual normality는 좀 아님\
    > [(근데 이게 GOF에서 온 거다.. Y가 normal이 아니다 보니까 residual도 좀 따라가는 경향이 있다는 말?)]{.underline}

-   결과는 없었지만 다른 link function은 그닥 좋아지지 X

-   Sample size는 충분

-   **[개선 방향: X를 더 넣거나, X끼리의 interaction을 넣거나]{.underline}**
