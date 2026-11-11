"""4-I §1.2 '왜 분산을 보는가' — 같은 집단 평균, 다른 집단 내 산포 (설명용 가상 자료).

callout의 내용을 그림으로 옮김: 집단 평균의 차이(집단 간 변동)를 집단 안의 산포
(집단 내 변동)와 견주어 판단한다. 두 패널의 집단 평균은 똑같고 산포만 다르다.
나란한 세 집단 → CAT[0..2], 강조색 없음.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

rng = np.random.default_rng(11)
MEANS = [4.0, 5.5, 7.0]            # 세 집단 평균 (두 패널 공통, 가상)
N = 12
Z = []
for _ in MEANS:
    z = rng.normal(size=N)
    Z.append((z - z.mean()) / z.std())          # 집단 평균을 정확히 MEANS로 맞춤
JIT = [rng.uniform(-0.13, 0.13, N) for _ in MEANS]
GRAND = float(np.mean(MEANS))

PANELS = [("① 집단 안이 촘촘함", 0.35, "F 큼 — 차이가 의미 있음"),
          ("② 집단 안이 넓게 퍼짐", 1.55, "F 작음 — 우연일 수 있음")]

fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.9))
fig.subplots_adjust(wspace=0.12, bottom=0.18)

for ax, (name, sd, verdict) in zip(axs, PANELS):
    # 전체 평균
    ax.hlines(GRAND, -0.1, 4.3, color=TEXT2, lw=1.2, ls="--", zorder=1)
    ax.text(4.3, GRAND - 0.3, "전체 평균", ha="right", va="top", fontsize=11, color=TEXT2)

    lows, highs = [], []
    for g, (m, z, jit) in enumerate(zip(MEANS, Z, JIT)):
        c = CAT[g]
        yv = m + sd * z
        lows.append(yv.min()); highs.append(yv.max())
        ax.scatter(g + 1 + jit, yv, s=30, color=mix(c, 0.8), edgecolor="white", lw=0.6, zorder=3)
        ax.hlines(m, g + 1 - 0.3, g + 1 + 0.3, color=shade(c, 0.25), lw=3, zorder=4)

    # 집단 간 변동: 전체 평균 → 집단 3 평균
    ax.annotate("", xy=(3.38, MEANS[2]), xytext=(3.38, GRAND),
                arrowprops=dict(arrowstyle="<->", color=TEXT, lw=1.4, shrinkA=0, shrinkB=0))
    ax.text(3.48, (GRAND + MEANS[2]) / 2, "집단 간", ha="left", va="center", fontsize=11,
            fontweight="bold", color=TEXT)

    # 집단 내 변동: 집단 1의 퍼짐
    bx, lo, hi = 0.66, lows[0], highs[0]
    ax.plot([bx, bx], [lo, hi], color=TEXT, lw=1.4, zorder=4)
    for yy in (lo, hi):
        ax.plot([bx, bx + 0.08], [yy, yy], color=TEXT, lw=1.4, zorder=4)
    ax.text(bx - 0.08, MEANS[0], "집단 내", ha="right", va="center", fontsize=11,
            fontweight="bold", color=TEXT)

    ax.set_xlim(-0.35, 4.35); ax.set_ylim(0.2, 9.9)
    ax.set_xticks([1, 2, 3]); ax.set_xticklabels(["집단 1", "집단 2", "집단 3"], fontsize=11)
    ax.tick_params(axis="x", length=0)
    for lab, c in zip(ax.get_xticklabels(), CAT):
        lab.set_color(shade(c, 0.1))
    ax.set_yticks([])
    ax.spines[["left", "bottom"]].set_visible(False)
    ax.set_title(name, fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)
    ax.text(0.5, -0.14, verdict, transform=ax.transAxes, ha="center", va="top",
            fontsize=12, fontweight="bold", color=TEXT)

save(fig, "assets/img/ch04/between_within.png")