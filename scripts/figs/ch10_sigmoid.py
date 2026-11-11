"""3-I(10장) §1.3 로지스틱(시그모이드) 곡선 — 기울기 β₁이 클수록 가파름 (설명용 함수 그림).

R 청크 sigmoid를 다시 그림. R 코드와 같은 기울기 0.5, 1, 3을 쓰고 β₀ = 0으로 두었다
(z = β₁x). 기울기에 순서가 있으므로 옅은 색 → 진한 색 순서로 칠한다(완만 → 가파름).
범례 대신 왼쪽 위 빈 곳에 직접 표시한다. p = 0.5(z = 0)는 점선과 점으로 표시하고,
강조색은 쓰지 않는다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

BETAS = [0.5, 1, 3]                       # R 코드와 같은 값
cols = [CAT[3], CAT[1], PRIMARY]          # 완만 → 가파름: 옅은 올리브 → 올리브 → 진한 초록
x = np.linspace(-6, 6, 400)

fig, ax = plt.subplots(figsize=(7.4, 3.8))

for yy in (0, 1):
    ax.axhline(yy, color=LINE, lw=1, ls=":", zorder=0)
ax.axhline(0.5, color=TEXT2, lw=1.1, ls="--", zorder=1)

for b, c in zip(BETAS, cols):
    ax.plot(x, 1 / (1 + np.exp(-b * x)), color=c, lw=2.6, zorder=3)

# 모든 곡선이 지나는 점
ax.plot(0, 0.5, "o", ms=7, color=TEXT, mec="white", mew=1.2, zorder=5)
ax.text(0.45, 0.38, r"$z = 0$  →  $p = 0.5$", fontsize=12, color=TEXT, ha="left", va="center")

# 직접 표시 (가파른 순서로 위에서 아래로)
lx, ly = -5.8, 0.93
for k, (b, c) in enumerate(sorted(zip(BETAS, cols), key=lambda t: -t[0])):
    yy = ly - k * 0.12
    ax.plot([lx, lx + 0.7], [yy, yy], color=c, lw=2.6, solid_capstyle="butt")
    tc = shade(c, 0.35) if b == 0.5 else c
    ax.text(lx + 0.9, yy, rf"$\beta_1 = {b:g}$", fontsize=12, color=tc,
            va="center", ha="left")

ax.set_xlim(-6.2, 6.0); ax.set_ylim(-0.06, 1.06)
ax.set_xticks([0]); ax.set_yticks([0, 0.5, 1])
ax.set_yticklabels(["0", "0.5", "1"], fontsize=11)
ax.set_xticklabels(["0"], fontsize=11)
ax.set_xlabel(r"$x$   ($z = \beta_1 x$,  $\beta_0 = 0$)", fontsize=12)
ax.set_ylabel(r"$p(x)$", fontsize=12)

save(fig, "assets/img/ch10/sigmoid.png")