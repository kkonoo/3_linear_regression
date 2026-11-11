"""2-? §4.1 회귀에서의 이상치: Outlier · Leverage point · Influential point (설명용 가상 자료).

새로 그림. 세 패널은 같은 기본 점을 쓰고, 패널마다 특별한 점 하나만 더한다.
실선 = 그 점을 넣고 적합한 직선, 점선 = 그 점을 빼고 적합한 직선.
나란한 세 종류는 CAT 색. 강조색은 회귀선을 실제로 끌고 가는 influential point 한 곳에만 쓴다.
"""
import numpy as np
from matplotlib.lines import Line2D
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"
rng = np.random.default_rng(3)
x = np.sort(rng.uniform(1, 8, 12))
y = 1.0 + 0.5 * x + rng.normal(0, 0.45, x.size)
xbar = x.mean()
b1, b0 = np.polyfit(x, y, 1)            # 특별한 점을 뺀 적합 (세 패널 공통)

def line_at(v):
    return b0 + b1 * v

PANELS = [
    ("① Outlier", (xbar + 0.1, line_at(xbar + 0.1) + 4.2), CAT[0],
     "잔차는 크지만\n기울기는 거의 그대로", "br"),
    ("② Leverage point", (14.0, line_at(14.0)), CAT[2],
     "두 직선이 겹침:\n해롭지 않음", "br"),
    ("③ Influential point", (14.0, -1.0), ACCENT,
     "기울기를 끌어당김", "tl"),
]

XL, YL = (0, 15), (-2.2, 9.6)
fig, axs = plt.subplots(1, 3, figsize=(8.2, 3.1), sharey=True)
fig.subplots_adjust(wspace=0.08)
xx = np.array(XL, dtype=float)

for ax, (name, (px, py), c, note, pos) in zip(axs, PANELS):
    ax.axvline(xbar, color=LINE, lw=1.2, ls=":", zorder=0)
    ax.text(xbar, YL[0] - 0.25, r"$\bar x$", ha="center", va="top", fontsize=12, color=TEXT2)

    xa, ya = np.append(x, px), np.append(y, py)
    c1, c0 = np.polyfit(xa, ya, 1)
    ax.plot(xx, c0 + c1 * xx, color=TEXT, lw=1.8, zorder=2)
    ax.plot(xx, b0 + b1 * xx, color=TEXT2, lw=1.4, ls="--", zorder=3)   # 겹쳐도 점선이 보이게 위에

    ax.scatter(x, y, s=22, color=mix(TEXT2, 0.55), zorder=4)
    ax.scatter([px], [py], s=80, color=c, edgecolors="white" if c != ACCENT else ACCENT_INK,
               linewidths=1.2, zorder=5)

    is_acc = c == ACCENT
    tc = ACCENT_INK if is_acc else TEXT
    if pos == "br":
        ax.text(14.6, YL[0] + 0.4, note, ha="right", va="bottom", fontsize=11, color=tc,
                linespacing=1.35)
    else:
        ax.text(0.5, YL[1] - 0.3, note, ha="left", va="top", fontsize=11, color=tc,
                fontweight="bold" if is_acc else "regular")

    ax.set_xlim(*XL); ax.set_ylim(*YL)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("x", fontsize=12, labelpad=16)
    ax.set_title(name, fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

axs[0].set_ylabel("y", fontsize=12, rotation=0, labelpad=10)

handles = [Line2D([], [], color=TEXT, lw=1.8, label="그 점을 넣고 적합"),
           Line2D([], [], color=TEXT2, lw=1.4, ls="--", label="그 점을 빼고 적합")]
fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=2,
           frameon=False, fontsize=11, handlelength=2.4, columnspacing=2.0)

save(fig, "assets/img/ch02/outlier_leverage.png")