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

    2.  Data example I - Introduction

    3.  Model description and estimation

    4.  Data example II - Model estimation

V.  **Poisson Regression Statistical Inference, Model Assessment and Classification**

    1.  Statistical Inference

    2.  Data example I -- Statistical Inference

    3.  Model Fit Assessment

    4.  Data example II -- Model Fit Assessment

```{=html}
<!-- -->
```
1.  **Introduction**

-   Y (response) = other distribution? 당연히 여러 모델이 가능!

1)  Standard Linear Regression

> ![](media/image1.png){width="4.136805555555555in" height="1.727412510936133in"}

2)  Generalized Linear Model

> ![](media/image2.png){width="4.374268372703412in" height="2.2760739282589677in"}

3)  Y = 지수의 형태로 표현

> ![](media/image3.png){width="2.2873600174978126in" height="0.26630905511811026in"} ... $\theta$*는 Y의 분포, g = link func. = log*
>
> *\
> \* Poisson distribution*
>
> *- random variable =* 단위시간/공간에 발생하는 사건의 수 (count data)\
> - binomial 분포 중 n은 크고 p는 매우 작은 경우 (unit range ≈ 0 p ≈ 0, 1-p ≈ 1)\
> - ![Poisson Distribution \| andymath.com](media/image4.jpeg){width="0.8466262029746282in" height="0.3861111111111111in"}*... x랑 y가 exponential 관계\
> *![Poisson distribution - Wikipedia](media/image5.png){width="1.8367202537182852in" height="1.4171784776902887in"} ![](media/image6.png){width="3.395638670166229in" height="1.0970177165354331in"}

4)  **Poisson regression**

```{=html}
<!-- -->
```
1.  Data\
    > ![](media/image7.png){width="2.8466262029746283in" height="0.23369750656167979in"} ... Y가 Poisson distribution (y mean = y var)

> ... Y = (unit이 있는) count data

2.  Model ... x랑 y가 exponential 관계\
    > ![](media/image8.png){width="3.1226990376202974in" height="0.23767935258092737in"}\
    > ![](media/image9.png){width="2.969226815398075in" height="0.25790791776028in"}

```{=html}
<!-- -->
```
5)  Standard Linear Regression (with log-transformed) vs. Poisson Regression

```{=html}
<!-- -->
```
1.  Standard linear regression

-   ${{E\left( \log(Y)|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right)} = \beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$ ... log(Y)를 estimate

-   V$\left( \log(Y)|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right)$ = constant ... X가 주어질 때 예측되는 logY의 범위는 일정

2.  Poisson Regression

-   ${{\log\left( E(Y|\text{x1,~}\ldots,\text{xp} \right))} = \beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$ ... Y를 estimate하고 log\
    (값 자체는 같을 수 있음 = log(Y))

-   V$\left( \log(Y)|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right)$ = $e^{\beta_{0} + \beta_{1}\text{x1+…+}\beta_{p}\text{xp~}}$ ... = Y estimate ... X에 따라 계속 달라짐

    -   (Poisson해야할 때)\
        그냥 log transformation SLR? variance가 커서 안 맞음\
        SLR을 하고싶으면 variance stabilizing transformation (not log transformation) !\
        (이 때는 Y가 커야 함, 보통 $\mu^{'} \leftarrow$ $\sqrt{\mu + 3/8}$)\
        ... Y가 작으면 Poisson !\
        ![variance stabilizing transformation에 대한 이미지 검색결과](media/image10.jpeg){width="3.524643482064742in" height="2.64417104111986in"}

2.  **Exploratory Data Example I - Introduction**

```{=html}
<!-- -->
```
1)  High School Awards

    -   Y = [1년(unit)]{.underline}에 한 학생이 상 받는 수 (count data)\
        > X = program type, math score

    -   *within*이란 것도 있네...\
        > ![](media/image11.png){width="4.4760553368328955in" height="0.6590605861767279in"}\
        > ![](media/image12.png){width="2.6920559930008747in" height="0.6075470253718285in"}\
        > ![](media/image13.png){width="3.894727690288714in" height="2.68799978127734in"}

2)  Insurance Claims

    -   Y = policyholder 당 자동차 보험 청구 횟수\
        > X = policyholder 거주지, 차 종류, 나이 범위

    -   Y \~ X boxplot (X가 factor라서)\
        > ![](media/image14.png){width="3.6320002187226597in" height="1.935294181977253in"}

**\
**

3.  **Model Description and Estimation**

```{=html}
<!-- -->
```
1)  Model

```{=html}
<!-- -->
```
1.  Data\
    > ![](media/image7.png){width="2.6073622047244096in" height="0.21405511811023623in"}\
    > ... Y가 **Poisson distribution** ([y mean = y var]{.underline}) = (unit이 있는) count data

2.  Poisson distribution\
    > ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image15.png){width="1.0797550306211723in" height="0.3234514435695538in"} ![](media/image16.png){width="1.0920253718285213in" height="0.1734109798775153in"}

3.  Model ... x랑 y가 exponential 관계\
    > ![](media/image17.png){width="2.8957053805774278in" height="0.22274715660542432in"}\
    > ![](media/image18.png){width="3.2208595800524935in" height="0.21339129483814523in"}

```{=html}
<!-- -->
```
2)  Model interpretation

    -   λ (parameter):\
        > predicted response(Y hat)의 mean, 발생률 (단위발생률 \* 시간) ... 이걸 새 Y로 두는 것!\
        > ![](media/image19.png){width="2.2940780839895014in" height="0.20994969378827646in"}

    -   Log rate: 새 Y와의 link function ... 최종 linear regression에서의 Y\
        > ![](media/image20.png){width="1.4233125546806649in" height="0.23002952755905512in"}

    -   Beta의 의미:\
        > Ratio of the rates in one unit , X가 *1 증가 lnY가 1 증가 Y (발생률) e지수배로 증가\
        > *![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image21.png){width="1.2269936570428697in" height="0.3947298775153106in"}

3)  Model estimation

```{=html}
<!-- -->
```
1.  Model\
    > ![](media/image18.png){width="3.1656441382327207in" height="0.2097331583552056in"}

2.  Parameters: beta

3.  Approach by MLE

> ![](media/image22.png){width="2.3128838582677167in" height="0.38749781277340334in"} ... ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image15.png){width="1.0061351706036745in" height="0.30139763779527556in"}
>
> ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image23.png){width="5.147238626421697in" height="0.7778455818022747in"}

4.  **Data example II - Model estimation**

```{=html}
<!-- -->
```
1)  High School Awards

    -   Y = 1년에 받는 상 수

    -   SLR\
        ![](media/image24.png){width="3.9471598862642168in" height="0.40669838145231846in"}![](media/image25.png){width="3.739423665791776in" height="1.7238801399825021in"}\
        residual이 X나 Y랑 연관 있어 보임

    -   Poisson\
        ![](media/image26.png){width="5.126265310586176in" height="0.378251312335958in"}\
        ![](media/image27.png){width="3.5508311461067366in" height="0.985074365704287in"}\
        수학 점수가 1점 오르면 상 받는 정도가 exp(.07) = 1.072배 올라감

2)  Insurance Claims

    -   **Offset**?! : event rate 계산할 때 unit (**exposure**)을 다르게 잡을 수도 있다!\
        ![](media/image28.png){width="3.726266404199475in" height="1.7537314085739282in"}\
        ![](media/image29.png){width="5.18596675415573in" height="0.5935192475940507in"}${{\text{~log}\left( E(Y|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right))} = \beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$+ **log(exposure)**
