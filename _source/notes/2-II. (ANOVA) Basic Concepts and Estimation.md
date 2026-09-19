I.  **Basic Concepts and Estimation**

    1.  Basics of ANOVA

    2.  Estimation method

    3.  Data example I -- Estimation

    4.  Test for equal means

II. **Basic Concepts and Estimation**

    1.  Comparing pairs of means

    2.  Model fit assessment

    3.  ANOVA vs. Simple linear regression

    4.  Data example

```{=html}
<!-- -->
```
1.  **Comparing Pairs of Means**

```{=html}
<!-- -->
```
1)  Tukey method ... Pairwise comparison\
    - H~0~: 두 mean의 차 = 0\
    - sigma: 분산 두 개 합\
    - statistics: studentized range statistic (Q, 여러 개 한 번에 하는 ANOVA는 T)\
    - 분포: studentized range distribution\
    ![](media/image1.png){width="3.0643569553805774in" height="1.4890616797900262in"}\
    ![텍스트, 손목시계이(가) 표시된 사진 자동 생성된 설명](media/image2.png){width="1.0061351706036745in" height="0.5030675853018373in"} ![](media/image3.png){width="1.6809820647419074in" height="0.547736220472441in"}(Honest significant difference)

2)  Difference between ta and qa ... correct for simultaneous inference

> \- q-value \> t-value ... 뭔가 sqrt(n)을 더 곱한 형태\
> ![텍스트, 손목시계이(가) 표시된 사진 자동 생성된 설명](media/image2.png){width="1.0061351706036745in" height="0.5030675853018373in"} ![텍스트, 시계, 손목시계이(가) 표시된 사진 자동 생성된 설명](media/image4.png){width="0.9386504811898513in" height="0.5693460192475941in"}\
> \* q-value = FDR ?!
>
> \- interval도 q-value가 더 큼 (multiplicity correction)\
> e.g. 2개 test C.I. (.95)(.95) ≈ .90 (동시에 비교한다? = 여러 개를 곱)\
> 3개 test C.I. (.95)(..95)(.95) ≈ .86

3)  Example\
    > ![](media/image5.png){width="2.9263812335958006in" height="1.9102865266841644in"}

**\
**

2.  **Model Fit Assessment**

```{=html}
<!-- -->
```
1)  Model & assumption

-   Data: k개 population에서 온 Y\
    > ![](media/image6.png){width="2.140223097112861in" height="0.22699365704286964in"}

-   Model: Y estimator = 각 population의 mean\
    > ![](media/image7.png){width="2.1656441382327207in" height="0.24887357830271217in"}

-   Assumption (linearity만 빼고)

1.  Constant variance assumption ... ![](media/image8.png){width="0.6881189851268591in" height="0.1996609798775153in"}

2.  Independence assumption ... ![](media/image9.png){width="0.6881189851268591in" height="0.2030511811023622in"} independent random

3.  Normality assumption ... ![](media/image10.png){width="1.056205161854768in" height="0.19306977252843394in"}

```{=html}
<!-- -->
```
2)  Residual analysis\
    > ![](media/image11.png){width="1.0148512685914262in" height="0.29664916885389325in"}, ![텍스트, 클립아트이(가) 표시된 사진 자동 생성된 설명](media/image12.png){width="0.88790791776028in" height="0.26732720909886265in"}

```{=html}
<!-- -->
```
1.  0 근처에 randomly scattered

2.  Normality 보는 plot = QQplot & histogram of ${\widehat{\text{ε}}}_{\text{ij}}$

> \- Examples\
> ![](media/image13.png){width="1.6280216535433072in" height="1.3960389326334208in"} ![](media/image14.png){width="1.734407261592301in" height="1.3514851268591426in"} ![](media/image15.png){width="1.6134558180227472in" height="1.3960400262467192in"}
>
> 만약 가정에 안 맞으면 data transform !

**\
**

3.  **"one-way" ANOVA vs Simple Linear Regression**

```{=html}
<!-- -->
```
1)  **ANOVA = 특별한 case의 linear regression (X = categorical)\
    > ( Y estimator = Y mean)**

2)  Simple linear regression vs ANOVA\
    > ![](media/image16.png){width="2.526388888888889in" height="0.7772276902887139in"}![](media/image16.png){width="2.526388888888889in" height="1.0540113735783028in"}\
    > ![https://i.stack.imgur.com/ZYPQm.png](media/image17.png){width="5.59405949256343in" height="2.6372758092738406in"}\
    > *그래서 multiple regression이 ANOVA랑 같은..!*

3)  ANVOA를 linear regression으로 표현하기\
    > ![](media/image18.png){width="2.673865923009624in" height="0.8508661417322835in"}![](media/image18.png){width="2.4042136920384953in" height="0.8828587051618547in"}\
    > *... Y estimator = 각 category의 mean*\
    > ![텍스트이(가) 표시된 사진 자동 생성된 설명](media/image19.png){width="3.653465660542432in" height="1.5263921697287839in"} ![linear independence anova에 대한 이미지 검색결과](media/image20.png){width="1.9405938320209974in" height="1.2064621609798776in"}*\
    > ... categorical X는 dummy variable (k-1)개로 표현\
    > *![](media/image20.png){width="1.9402777777777778in" height="1.20625in"}![](media/image21.png){width="2.7871150481189852in" height="0.7970297462817147in"}![linear independence anova에 대한 이미지 검색결과](media/image20.png){width="1.9405938320209974in" height="1.2064621609798776in"}\
    > ... m0 = 1 추가해서 두 행렬 곱으로 깔끔하게 표현 가능\
    > ... m는 스칼라, categories + errors = V (data estimator)\
    > V는 선형 독립! (data = random variable)\
    > ![](media/image22.png){width="1.4006944444444445in" height="1.8763888888888889in"}![](media/image23.gif){width="1.4944444444444445in" height="1.1979166666666667in"}

**\
**

4.  **Data Example**

```{=html}
<!-- -->
```
1)  Data: survival days \~ cancer type\
    > ![](media/image24.png){width="1.907377515310586in" height="1.881188757655293in"} ... X는 반드시 factor (e.g. cancer type)

2)  Y를 적절히 transformation하면 normal ... **linear랑 다르게 Y가 normal이라고 가정!!**\
    > ![](media/image25.png){width="4.481070647419073in" height="0.6340277777777777in"}\
    > ![](media/image26.png){width="4.222772309711286in" height="1.4704385389326333in"}

3)  ANOVA\
    > ![](media/image27.png){width="4.4847222222222225in" height="0.8531211723534559in"}\
    > ![](media/image28.png){width="2.2013188976377953in" height="0.8613856080489939in"}

4)  Tukey test\
    > ![](media/image29.png){width="2.4306561679790026in" height="1.6666666666666667in"}

5)  Residual analysis\
    > ![](media/image30.png){width="2.576440288713911in" height="1.089109798775153in"}

> ![](media/image31.png){width="3.5322233158355205in" height="3.1089107611548554in"}
