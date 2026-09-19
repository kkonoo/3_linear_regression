I.  **Other Regression Models (Part 1)**

    1.  Weighted Least Squares Regression

    2.  Robust Regression

    3.  Nonlinear & Nonparametric Regression

II. **Other Regression Models (Part 1)**

    1.  Time Series Regression

    2.  Spatial Regression

    3.  Mixed Effects Models

    4.  Regression Analysis Overview

```{=html}
<!-- -->
```
1.  Time series regression

```{=html}
<!-- -->
```
1)  Independent assumption: if **correlated errors?**

> ***Independence* *Assumption*: {e~1~,..., e~n~} are independent random variables**

-   *Degree of freedom != sample size*

-   *Variability and uncertainty upup*

-   *Less reliable statistical inference*

2)  Time series data 특징

-   **Trend**: 시간에 따른 long-term 증감

-   **Seasonality**: influenced by seasonal factors (e.g. quarter of the year, month, or day of the week)

-   **Periodicity**: 규칙적인 패턴 (seasonal series often called periodic, although they do not exactly repeat themselves)

-   **Cyclical trend**: 올라갔다 내려갔다 (기간은 규칙적이지 않더라도)

-   **Heteroskedasticity**: 시간에 따라 variance가 변화

-   **Correlation**: positive (successive observations are similar) or negative (successive observations are dissimilar)

3)  Examples : GDP, ...

> ![](media/image1.png){width="4.966666666666667in" height="2.2527734033245843in"}

4)  이게 꼭 필요할까?

-   Time series = dependence data redundancy (d.f \< observation), concentrated data sampling

-   Dependence를 무시하면.. too narrow CI poor inference, prediction

5)  Basics

-   **Data**: $Y_{t}$; Y를 time에 대하여 표현 e.g. minute, hour, day, month

-   **Model**: $Y_{t}$ = $m_{t}$+$s_{t}$+$X_{t}
    m_{t}$ : a trend component;, $s_{t}$ : a seasonality component with known periodicity *d* ($s_{t}$=$s_{t + d}$) such that $\sum_{j = 1}^{d}s_{j} = 0,\ X_{t}$ : a stationary component, i.e. its probability distribution does not change when shifted in time

-   **Estimation**\
    i) $m_{t}$, $s_{t}$ *먼저 estimation\
    ii)* $Y_{t}$ - $m_{t}$ - $s_{t}$ = $X_{t}$ (time에 상관없는 X를 남겨서) using time series modeling approaches.

**\
**

2.  **Spatial regression**

```{=html}
<!-- -->
```
1)  똑같이 correlated errors

2)  Spatial data 특징

-   **Trend**: 공간에 따른 거리 증감

-   **Smoothness**: 거리가 멀어질수록 조금씩 달라짐

-   **Heteroskedasticity**: 공간에 따라 분산이 달라짐

-   Continuous vs. Discrete: 각 위치를 numeric value로 observation / 있다 없다로 binary / response count

-   Regular vs. irregular design: the spatial process can be observed within regular or irregular division of the space

3)  Examples:\
    virus 발병 지역 / MRI image ...

> ![](media/image2.png){width="3.425in" height="1.6024562554680666in"}

4)  Basics

-   **Data**: $Y_{s},\ $where *s* indexes space, e.g. voxels, census tract

-   **Model**:\
    > $Y_{s}$ : numeric response vs. point process

> $Y_{s}$ : stationary vs. non-stationary
>
> $Y_{s}$*:* isotropic process
>
> $s \in S$ (S : the space domain), irregular vs regular observation grid
>
> Large scale vs. small-scale spatial dependence

3.  **Mixed effects model**

```{=html}
<!-- -->
```
1)  ANOVA

-   Replicate이 있을 때 (같은 sample에 대한 걸 수도 있고, 같은 환경에서 실험한 것일 수도 있고 그런 경우 작용하는 것은 그 당시의 random effect mean에 random effect로 decomposition)

-   **Data**: Y~ij~ for j = 1，...，n~i~; i = 1,..., k

-   **Model**: Y~ij~ = $\text{μ}_{\text{i}}\text{+}\text{ε}_{\text{ij}}\text{=}$ $\text{μ}\text{+}\text{τ}_{\text{i}}\text{+}\text{ε}_{\text{ij}}\ $\
    > where $\sum_{\text{i=1}}^{\text{k}}{\text{τ}_{\text{i}}\text{=}\text{0}},\ \text{μ}_{\text{i}}$ = i-th group mean decomposed into $\text{μ}_{\text{i}}$=$\text{μ+}\text{τ}_{\text{i}}$

2)  Random effects

-   $\text{ε}_{\text{ij}}\sim\ N\left( 0,\sigma^{2} \right)$*; error term은 원래 linear model 가정대로*

-   $\text{τ}_{\text{i}}\sim\ N\left( 0,\sigma_{r}^{2} \right)$*; random effect도 mean은 0*

-   Fixed effect에서 ANOVA랑 차이점? [여기서는 Y(observation)가 independent가 아님!!!]{.underline}

-   When to use? 우리가 보고있는 것들은 (the same) Larger population에서 보는 것. 우리가 covariate으로 취급하던 걸 random effect로 보는 것 (e.g. cancer 환자의 상태 \~ 다 똑같은 u + r (medical center; 보통은 covariate으로 생각했을.. 같은 medical center끼리의 연관성이 없고 random이라고 보는 것?)

3)  Mixed effects

-   그래서 fixed effect로 두고 싶은 건 그렇게 두고, random effect로 두고 싶은 것도 둠! (medical center는 fixed effect로 생각할 수도 있을 것.)

-   그런 경우, covariance matrix : 엄청 복잡. 그러니까 컴퓨터

-   **Model**: Y~ij~ = $\text{μ}\text{+τ}_{\text{i}}\text{+}\alpha\text{~}X_{\text{ij}}\text{~+}\text{ε}_{\text{ij}}$

-   $\text{ε}_{\text{ij}}\sim\ N\left( 0,\sigma^{2} \right)$

-   $\text{τ}_{\text{i}}\sim\ N\left( 0,\sigma_{a}^{2} \right)$*; random으로 두고 싶은 것에 대한 random effect*

-   $X_{\text{ij}} = j,\ j = 1,\ldots,\ 7$ in this example

4.  **Overview**

+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
|                | data                    | model                                                                                                                                                                                  | assumptions            | estimation                        | Properties of beta     |
+================+=========================+========================================================================================================================================================================================+========================+===================================+========================+
| Simple         | {(X~1~, Y~1~)},..       | Y~i~ = b0 +\                                                                                                                                                                           | \- E(e~i~) = 0         | Minimum\                          | E($\widehat{b}$) = b   |
|                |                         | b~1~X~i~ +\                                                                                                                                                                            |                        | Least square                      |                        |
|                |                         | e~i~                                                                                                                                                                                   | \- V(e~i~) = s2        |                                   | V($\widehat{b}$) = s2? |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- ei : independent    |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- e \~ normal         |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| ANOVA          | {Yij},..                | Y~ij~ = $\text{μ}_{\text{i}} + \text{ε}_{\text{ij}}$                                                                                                                                   | \- V(e~ij~) = s2       |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- e~ij~ : independent |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- e~ij~ \~ normal     |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| Multiple       | {(x~n1~,..,x~np~ ),\    | Y~i~ = b~0~ + b~1~x~i1~ + ..+ b~p~x~ip~ + e~i~                                                                                                                                         | \- E(e~i~) = 0         | Projection matrix                 | E($\widehat{b}$) = b   |
|                | Y~n~},..                |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- V(e~i~) = s2        |                                   | V($\widehat{b}$) = ∑   |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- ei : independent    |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- e \~ normal         |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| Logistic       | {(x~n1~,..,x~np~ ),\    | \-$\text{p~=~p}\left( \text{x}\text{1}\text{,…}\text{,}\text{x}\text{p} \right)\text{~}\text{=~P}\{\text{Y=1}|\text{x}\text{1},\ldots,\text{x}\text{p}\}$                              | \- linearity\          | MLE                               |                        |
|                | Y~n~}; binary Y         |                                                                                                                                                                                        | - independent Y        |                                   |                        |
|                |                         | -g(p) = b~0~ + b~1~x~i1~ + ..+ b~p~x~ip~ + e~i~                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | (no\_error\_term)      |                                   |                        |
|                |                         | -g(p) = link = logit = ln(p/1-p)                                                                                                                                                       |                        |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| Poission       | {(x~n1~,..,x~np~ ),\    | ${{\log\left( E(Y|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right))} = \beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$                                 | \- linearity\          |                                   |                        |
|                | Y~n~}; count Y          |                                                                                                                                                                                        | - independent Y        |                                   |                        |
|                |                         | \- link = log(E(Y)) = log($\widehat{Y}$)                                                                                                                                               |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | (no\_error\_term)      |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- E(Y) = V(Y)         |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| GLM (linear)   | {(x~n1~,..,x~np~ ),\    | $- {{g\left( E(Y|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right))}{= g\left( \widehat{Y} \right) = \ }\beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$ |                        |                                   |                        |
|                | Y~n~}; exponential Y    |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         | $- {{E\left( Y|\text{x}\text{1}\text{,~}\ldots,\text{x}\text{p} \right)} = {Y = \ g}^{- 1}(\beta}_{0} + \beta_{1}\text{x}\text{1}$+...+$\beta_{p}\text{x}\text{p}$)                    |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         | Y의 분포에 따라 g/g^-1^                                                                                                                                                                |                        |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| Weighted       | {(x~n1~,..,x~np~ ),\    | Y~i~ = b~0~ + b~1~x~i1~ + ..+ b~p~x~ip~ + e~i~                                                                                                                                         | \- E(e~i~) = 0         |                                   |                        |
|                | Y~n~},..                |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- V(e~i~) = **∑**     |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- ei : independent    |                                   |                        |
|                |                         |                                                                                                                                                                                        |                        |                                   |                        |
|                |                         |                                                                                                                                                                                        | \- e \~ normal         |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
| GAM (additive) | Y~i~=f(x~i1~,...,x~ip~) | f(x~1~,...,x~p~) = ${\alpha + \ f}_{1}$(x~1~)+ ...+ $f_{p}$(x~p~)\                                                                                                                     |                        | Backfitting algorithm             |                        |
|                |                         | f: unknown smooth function                                                                                                                                                             |                        |                                   |                        |
|                | \+ e~i~\                |                                                                                                                                                                                        |                        | (error가 특정 값에 수렴할 때까지) |                        |
|                | (non-linear)            |                                                                                                                                                                                        |                        |                                   |                        |
+----------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------------------+------------------------+
