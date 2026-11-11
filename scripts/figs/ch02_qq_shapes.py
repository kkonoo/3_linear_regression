"""2-I §3.3 정규성 가정: QQ-plot의 세 가지 전형 (정규 / 치우침 / 균등).

R 청크 qq-shapes를 다시 그림. 이 그림은 설명용 모의자료다. R 코드와 같은 분포와 표본 크기를 쓴다.
- rnorm(200), rexp(200), runif(200)
- x축은 정규 이론 분위수 ppoints(n) = (i − 0.5)/n
- 기준선은 qqline과 같이 1·3사분위수를 잇는 직선
- 각 패널 왼쪽 위에 작은 히스토그램을 넣음. 막대 수를 줄여 분포 모양이 잘 보이게 함
  (균등분포가 들쭉날쭉하지 않고 평평하게 보이도록)

세 경우는 나란한 항목이므로 CAT 색을 쓰고, 강조색은 쓰지 않는다.
"""
from statistics import NormalDist
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

N = 200
rng = np.random.default_rng(1)
CASES = [
    ("① 정규", rng.normal(size=N)),
    ("② 치우침 (C자)", rng.exponential(size=N)),
    ("③ 균등 (S자)", rng.uniform(size=N)),
]

nd = NormalDist()
p = (np.arange(1, N + 1) - 0.5) / N                 # R ppoints(n), n > 10
q = np.array([nd.inv_cdf(v) for v in p])            # 이론 분위수
xq1, xq3 = nd.inv_cdf(0.25), nd.inv_cdf(0.75)

fig, axs = plt.subplots(1, 3, figsize=(8.2, 3.3))
fig.subplots_adjust(wspace=0.14)
XL = (-3.2, 3.2)

for k, (ax, (name, d)) in enumerate(zip(axs, CASES)):
    c = CAT[k]
    s = np.sort(d)
    # qqline: 1·3사분위수를 지나는 기준선
    y1, y3 = np.quantile(d, [0.25, 0.75])
    slope = (y3 - y1) / (xq3 - xq1)
    icpt = y1 - slope * xq1
    xx = np.array(XL)
    ax.plot(xx, icpt + slope * xx, color=TEXT, lw=1.4, zorder=2)
    ax.scatter(q, s, s=12, color=c, lw=0, zorder=3)

    pad = 0.08 * (s.max() - s.min())
    ax.set_xlim(*XL)
    ax.set_ylim(s.min() - pad, s.max() + pad)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("이론 분위수", fontsize=11)
    if k == 0:
        ax.set_ylabel("잔차", fontsize=11)
    ax.set_title(name, fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

    # 작은 히스토그램 (왼쪽 위: QQ 점이 지나가지 않는 자리)
    ia = ax.inset_axes([0.04, 0.60, 0.34, 0.34])
    ia.hist(d, bins=9, color=mix(c, 0.55), edgecolor="white", linewidth=0.8)
    ia.axhline(0, color=TEXT2, lw=0.8)
    ia.axis("off")

save(fig, "assets/img/ch02/qq_shapes.png")