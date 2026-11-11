"""4.2 Marginal vs. Conditional — 교란 그림: 그룹을 무시한 기울기와 그룹 안의 기울기 (설명용).

6장 예제(BMI와 LDL)의 분위기를 따른 가상 자료. Group2가 BMI도 높고 LDL도 높아서,
BMI만 넣은 단순회귀(marginal) 기울기가 Group을 함께 넣은 회귀(conditional) 기울기보다 가파르다.
색: Group1 CAT[0], Group2 CAT[1], marginal 직선은 TEXT. 나란한 두 집단이므로 강조색 없음.
축 눈금 숫자는 가상 자료라 숨긴다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"
rng = np.random.default_rng(11)

n = 40
x1 = rng.normal(22, 1.4, n)            # Group1: BMI 낮음
x2 = rng.normal(28, 1.4, n)            # Group2: BMI 높음
y1 = 100 + 1.5 * x1 + rng.normal(0, 5, n)
y2 = 130 + 1.5 * x2 + rng.normal(0, 5, n)   # Group2는 LDL도 높음 (가상)

x = np.r_[x1, x2]
y = np.r_[y1, y2]
g = np.r_[np.zeros(n), np.ones(n)]

# marginal: BMI 하나만 넣은 단순회귀
bm, am = np.polyfit(x, y, 1)
# conditional: BMI + Group을 함께 넣은 회귀 (공통 기울기, 그룹별 절편)
X = np.c_[np.ones_like(x), x, g]
c0, cb, cg = np.linalg.lstsq(X, y, rcond=None)[0]

C1, C2 = CAT[0], CAT[1]
fig, ax = plt.subplots(figsize=(7.6, 4.4))

ax.scatter(x1, y1, s=26, color=mix(C1, 0.75), edgecolor="white", lw=0.5, zorder=3)
ax.scatter(x2, y2, s=26, color=mix(C2, 0.75), edgecolor="white", lw=0.5, zorder=3)

# conditional 직선 (그룹마다, 그 그룹 범위에서)
ends = []
for xs, gi, c in [(x1, 0, C1), (x2, 1, C2)]:
    xx = np.array([xs.min() - 0.4, xs.max() + 0.4])
    ax.plot(xx, c0 + cb * xx + cg * gi, color=shade(c, 0.1), lw=2.4, zorder=4)
    ends.append((xx[1], c0 + cb * xx[1] + cg * gi))

# marginal 직선 (전체)
xm = np.array([x.min() - 0.3, x.max() + 0.6])
ax.plot(xm, am + bm * xm, color=TEXT, lw=2.2, ls="--", zorder=5)

# 직선 라벨
ax.text(xm[1] + 0.35, am + bm * xm[1], "marginal\nBMI만 넣은 회귀", fontsize=12,
        color=TEXT, ha="left", va="center", linespacing=1.35, fontweight="bold")
ax.text(ends[0][0] + 0.35, ends[0][1], "conditional\nGroup을 함께 넣은 회귀", fontsize=12,
        color=shade(C1, 0.1), ha="left", va="center", linespacing=1.35, fontweight="bold")
ax.text(ends[1][0] + 0.35, ends[1][1], "conditional", fontsize=12,
        color=shade(C2, 0.15), ha="left", va="center", fontweight="bold")

# 그룹 이름: 점선이 지나지 않는 쪽(Group1은 왼쪽 위, Group2는 오른쪽 아래)
ax.text(x1.min(), y1.max() + 1, "Group1", fontsize=12, fontweight="bold",
        color=C1, ha="left", va="bottom")
ax.text(x2.max(), y2.min() - 2.5, "Group2", fontsize=12, fontweight="bold",
        color=shade(C2, 0.1), ha="right", va="top")

ax.set_xlim(x.min() - 1.0, x.max() + 6.2)
ax.set_ylim(min(y.min(), am + bm * xm[0]) - 5, max(y.max(), am + bm * xm[1]) + 6)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("BMI", fontsize=12)
ax.set_ylabel("LDL", fontsize=12, rotation=0, labelpad=16)

save(fig, "assets/img/ch06/marginal_conditional.png")