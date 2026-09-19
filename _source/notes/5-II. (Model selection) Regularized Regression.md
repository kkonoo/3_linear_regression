I.  **Basics of Variable Selection**

    1.  Introduction

    2.  Data example I

    3.  Prediction Risk Estimation

    4.  Model Search

    5.  Data Example II - Model Search

II. **Regularized Regression**

    1.  Regularized Regression Penalties

    2.  Regularized Regression Approaches

    3.  Data example-- Regularized Regression

III. **Data Analysis Example**

     1.  Emergency Department Healthcare Costs \-- Introduction

     2.  Exploratory Data Analysis

     3.  Multiple Regression Fitted Model and Residual Analysis

     4.  Variable Selection

     5.  Findings

```{=html}
<!-- -->
```
1.  **Regularized Regression: Penalties**

```{=html}
<!-- -->
```
1)  Bias-Variance Tradeoff

-   Prediction Risk: Measure of the Bias-Variance Tradeoff

> ![](media/image1.png){width="3.936767279090114in" height="1.2125207786526684in"}

-   가끔은 full model (unbiased model)보다 MSE가 낮은 게 있을 수도 있음..!

-   Bias를 좀 만들면 MSE가 낮아지는 건 사실!

2)  Biased Regression: Penalties

-   당연히 full model이 제일 좋은 건 아님! **Good biased model**을 찾는 게 목적!

> large (complex) model에는 penalty를 줌! (true가 complex라면 이걸 못 쓰겠지만 그런 경우에는 애초에 찾기도 어려움)

3)  Regularized Regression

-   **penalized sum of squared errors** = MSE + penalty\
    :이걸 기준으로 이제 모델을 잡는 것!

> ![](media/image3.png){width="3.366215004374453in" height="0.40986767279090114in"}

-   $L_{0}$ penalty: ${|\left| \beta \right||}_{0} = \#\{ j:\ \beta_{j} \neq 0\}$ ⇒ Maximizing Q means searching through all submodels.

-   $L_{1}$ penalty: ${|\left| \beta \right||}_{1} = \ \sum_{j = 1}^{p}{|\beta_{j}|}$ ⇒ Maximizing Q forces many $\beta_{j}$'s to be zeros. (*LASSO Regression*)

-   $L_{2}$ penalty: ${|\left| \beta \right||}_{2} = \ \sum_{j = 1}^{p}{\beta_{j}}^{2}$ ⇒ Maximizing Q accounts for multicollinearity. (*Ridge Regression*)

4)  Comparing Penalties

-   $L_{0}$ penalty: provides the best model given a selection criterion but it requires fitting all submodels

-   $L_{1}$ penalty measures sparsity (e.g. Consider the following two vectors of length p)

> ![](media/image4.png){width="3.261920384951881in" height="0.7025448381452318in"}

-   $L_{2}$ penalty is easy to implement but it does not do variable selection

*\
*

2.  **Regularized Regression: Approaches**

```{=html}
<!-- -->
```
1)  Variable Standardization & Notation

-   Rescale the *j*-th predicting variable $x_{j}$ for *j=1,.., p* as follows:

$$\frac{1}{n}\sum_{i = 1}^{n}{x_{\text{ij}} = 0},\frac{1}{n}\sum_{i = 1}^{n}{x_{\text{ij}}^{2} = 1}$$

-   Rescale the response variable as follows

$$\frac{1}{n}\sum_{i = 1}^{n}{Y_{i} = 0},\frac{1}{n}\sum_{i = 1}^{n}{Y_{\text{ij}}^{2} = 1}$$

> \* Use the original scale when fitting the selected model for interpretation of the regression coefficients!

2)  Ridge Regression (under multicolinearity, not for model selection!)

> ![](media/image5.png){width="3.1733092738407698in" height="0.3680982064741907in"} 이게 최소화되는 model

-   estimated regression coefficients: $\widehat{\beta} = {(\mathbf{X}\mathbf{X}^{T} + \mathbf{\lambda}I)}^{- 1}\mathbf{X}^{T}$Y

-   $\lambda$= 0; least squares estimate (low bias, high variance)

-   $\lambda$= 1; $\widehat{\beta}$= 0 (high bias, low variance).

-   Not used for model selection: it does not "force" any ${\widehat{\beta}}_{j} = 0$

3)  Lasso (Least Absolute Shrinkage and Selection) Regression (for model selection)

-   For normal :

-   For GLM: ;l(b) = the log-likelihood function

-   estimated regression coefficients : numerical algorithms (공식 없음)

-   Used for model selection: it does "force" any ${\widehat{\beta}}_{j} = 0$

4)  Choosing lamda: Cross-Validation

```{=html}
<!-- -->
```
1.  Data splitting into train & test

> \- **Training set**: Fit the penalized model [given lamda]{.underline}, i.e. estimate ${\widehat{\beta}}_{0},\ {\widehat{\beta}}_{1}\text{,…},\ {\widehat{\beta}}_{p}$
>
> \- **Testing/Validation set:**

i.  MSE for normal regression

ii. classification error rate for logistic regression

iii. (General) scoring rule depending on the regression problem

> \- K-fold cross-validation (KCV) : data splitting method
>
> ![](media/image8.png){width="3.329405074365704in" height="1.223905293088364in"}

5)  Lasso vs Ridge Regression

> ![](media/image9.png){width="3.795663823272091in" height="1.9226432633420822in"}

6)  LASSO: Limitations

```{=html}
<!-- -->
```
1.  p \> n: n개까지만 선택됨

2.  n \> p: x끼리 correlation 높으면 ridge regression이 performance가 더 좋음

> Lasso는 variable을 1개만 선택하는 경향이 있음

7)  Elastic Net (Lasso + Ridge)

-   $L_{1}$ penalty a sparse model

-   $L_{2}$ penalty (lasso의) selected variable 수 제한 없앰 + group effect도 고려 + L1 regularization path의 안정화

\* [ Reference]{.underline}*:* Zou, Hui, and Trevor Hastie. \"Regularization and variable selection via the elastic net.\" *Journal of the Royal Statistical Society: Series B* 67.2 (2005): 301-320.

3.  **Data example-- Regularized Regression**

```{=html}
<!-- -->
```
1)  Ridge regression; **library(MASS)**

```{=html}
<!-- -->
```
1.  Scaling\
    ![](media/image11.png){width="3.7914107611548555in" height="0.5124660979877516in"}

2.  ridge regression for a range of penalty constants\
    ![](media/image12.png){width="3.7145636482939635in" height="1.5889577865266842in"}

> GCV : generalized CV score. 최소화하는 lambda고르기
>
> ![](media/image13.png){width="3.433128827646544in" height="1.7546008311461068in"}

2)  Lasso Regression; variable selection **library(lars)**

```{=html}
<!-- -->
```
1.  Scaling\
    ![](media/image11.png){width="3.7914107611548555in" height="0.5124660979877516in"}

2.  Lasso Regression

> ![](media/image14.png){width="3.3103094925634298in" height="2.073619860017498in"}
>
> ![](media/image15.png){width="3.4785269028871393in" height="1.479511154855643in"}

-   Malow로는 4번째가 들어감..? 이게 stepwise인가

-   Lasso variable selection을 하고 나면 ordinary least squares with the selected predicting variables!

3)  Lasso & Elastic Net; ***library(glmnet) ...** 아 elastic net이 lasso + Ridge같은 거니까*

```{=html}
<!-- -->
```
1.  Data\
    ![](media/image16.png){width="3.907975721784777in" height="0.21172134733158354in"}

2.  Find the optimal lambda using 10-fold CV\
    ![](media/image17.png){width="3.7465824584426946in" height="0.19882655293088364in"}

3.  Fit lasso model with 100 values for lambda\
    ![](media/image18.png){width="3.9613068678915138in" height="0.21505030621172352in"}

4.  Extract coefficients at optimal lambda\
    ![](media/image19.png){width="3.331288276465442in" height="1.7165758967629046in"}\
    ![](media/image20.png){width="2.870449475065617in" height="1.6064052930883639in"}

-   Selected predictors: log(takers), rank, years & expend using Lasso & penalty selected using 10-fold CV

4)  Elastic Net *\#\# alpha = 1 lasso, alpha=0 ridge*

```{=html}
<!-- -->
```
1.  Data\
    ![](media/image21.png){width="4.182166447944007in" height="0.23862314085739283in"}

2.  Find the optimal lambda using 10-fold CV\
    ![](media/image22.png){width="4.544129483814523in" height="0.25424212598425194in"}

3.  Fit lasso model with 100 values for lambda\
    ![](media/image23.png){width="4.54375in" height="0.23811132983377079in"}

4.  Extract coefficients at optimal lambda\
    ![](media/image24.png){width="4.036809930008749in" height="1.6646358267716534in"}

> ![](media/image25.png){width="3.421292650918635in" height="1.8220866141732284in"}

-   Selected predictors: Takers, rank, income, years & expend using Lasso & penalty selected using 10-fold CV

5)  Overview of All Selection Approaches

> ![](media/image26.png){width="4.441718066491688in" height="2.249892825896763in"}

-   Rank, Years & Expend : 다 뽑힘

-   Takers : 뽑힌 데도 있고 아닌 데도

-   Income : 다 안 뽑힘

6)  파산 문제

-   Lasso

> ![](media/image27.png){width="4.682378608923885in" height="2.398772965879265in"}\
> ![](media/image28.png){width="2.9831233595800524in" height="1.668711723534558in"}

-   Elastic net\
    > ![](media/image29.png){width="3.826337489063867in" height="2.0047364391951006in"}\
    > ![](media/image30.png){width="3.4662576552930884in" height="1.681284995625547in"}

-   Overview of All Selection Approaches\
    > ![](media/image31.png){width="4.122699037620298in" height="1.9718252405949257in"}
