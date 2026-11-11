"""1-I §2.5 제곱합 분해 — 한 점에서 본 y_i − ȳ = (ŷ_i − ȳ) + (y_i − ŷ_i), 그리고 SST = SSR + SSE.

설명용 가상 자료. 색: SSR(설명된 부분) CAT[0], SSE(남은 오차) CAT[1], 전체는 무채색.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"
rng = np.random.default_rng(7)
x = np.arange(1, 11, dtype=float)
y = 1.0 + 0.45 * x + rng.normal(0, 0.55, x.size)
i = 7                                   # 강조할 점 (x = 8)
y[i] += 1.1                             # 잔차가 잘 보이도록 (설명용)
b1, b0 = np.polyfit(x, y, 1)
yhat = b0 + b1 * x
ybar = y.mean()
SSR, SSE = ((yhat - ybar) ** 2).sum(), ((y - yhat) ** 2).sum()
C_R, C_E = CAT[0], CAT[1]

fig = plt.figure(figsize=(8.2, 3.9))
gs = fig.add_gridspec(1, 2, width_ratios=[2.7, 1.45], wspace=0.08)
ax = fig.add_subplot(gs[0])

ax.hlines(ybar, 0.3, 10.45, color=TEXT2, lw=1.2, ls="--", zorder=1)
ax.text(10.6, ybar, r"$\bar y$", color=TEXT2, fontsize=13, va="center")
xx = np.array([0.5, 10.5])
ax.plot(xx, b0 + b1 * xx, color=TEXT, lw=1.8, zorder=2)
ax.text(10.6, b0 + b1 * 10.5, "회귀직선", color=TEXT, fontsize=11, va="center")
ax.scatter(np.delete(x, i), np.delete(y, i), s=28, color=mix(TEXT2, 0.55), zorder=3)
ax.scatter([x[i]], [y[i]], s=55, color=TEXT, zorder=5)

# 한 점에서의 분해: 오른쪽에 두 조각, 왼쪽에 전체
xi, yi, yh = x[i], y[i], yhat[i]
ax.plot([xi + 0.18] * 2, [ybar, yh], color=C_R, lw=5, solid_capstyle="butt", zorder=4)
ax.plot([xi + 0.18] * 2, [yh, yi], color=C_E, lw=5, solid_capstyle="butt", zorder=4)
ax.plot([xi - 0.18] * 2, [ybar, yi], color=TEXT2, lw=1.4, zorder=4)
for yy in (ybar, yi):
    ax.plot([xi - 0.28, xi - 0.08], [yy, yy], color=TEXT2, lw=1.4, zorder=4)
ax.text(xi - 0.42, (ybar + yi) / 2, r"$y_i-\bar y$", ha="right", va="center", fontsize=12, color=TEXT)
ax.text(xi + 0.42, (ybar + yh) / 2, r"$\hat y_i-\bar y$" + "\n설명된 부분", ha="left", va="center",
        fontsize=11, color=C_R, linespacing=1.4)
ax.text(xi + 0.42, yi - 0.2, r"$y_i-\hat y_i$" + "  잔차", ha="left", va="center",
        fontsize=11, color=shade(C_E, 0.15))
ax.set_xlim(0.3, 11.6); ax.set_ylim(y.min() - 0.6, y.max() + 0.5)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("x", fontsize=12); ax.set_ylabel("y", fontsize=12, rotation=0, labelpad=10)

# 오른쪽: 모든 점에서 제곱해 더하면
bx = fig.add_subplot(gs[1])
bx.bar([0], [SSR], width=0.8, color=C_R)
bx.bar([0], [SSE], bottom=[SSR], width=0.8, color=C_E)
bx.text(0, SSR / 2, "SSR", ha="center", va="center", color=on(C_R), fontsize=12, fontweight="bold")
bx.text(0, SSR + SSE / 2, "SSE", ha="center", va="center", color=on(C_E), fontsize=12, fontweight="bold")
bx.annotate("", xy=(-0.55, 0), xytext=(-0.55, SSR + SSE),
            arrowprops=dict(arrowstyle="<->", color=TEXT2, lw=1.2))
bx.text(-0.65, (SSR + SSE) / 2, "SST", ha="right", va="center", fontsize=12, fontweight="bold", color=TEXT)
bx.text(0.5, SSR / 2, "자유도 1", ha="left", va="center", fontsize=11, color=TEXT2)
bx.text(0.5, SSR + SSE / 2, "자유도 n − 2", ha="left", va="center", fontsize=11, color=TEXT2)
bx.text(-0.65, (SSR + SSE) / 2 - 0.1 * (SSR + SSE), "자유도 n − 1", ha="right", va="center",
        fontsize=11, color=TEXT2)
bx.set_xlim(-1.9, 1.75); bx.set_ylim(-0.02 * (SSR + SSE), (SSR + SSE) * 1.03)
bx.axis("off")

save(fig, "assets/img/ch01/ss_decomposition.png")
