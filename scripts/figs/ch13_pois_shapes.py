"""3-? §1.2 포아송 분포 — μ = 1, 5, 15일 때의 확률질량함수 P(Y = y).

R 청크 pois-shapes(한 축에 세 분포의 막대를 0.3씩 비켜 그림)를 다시 그림.
실제 포아송 확률(설명용 가상 자료 아님)이며, R 코드와 같이 y = 0..30, 세로축 0–0.4.
세 패널을 위아래로 쌓고 x·y축을 공유해 모양을 바로 비교하게 했다.
μ는 순서가 있는 값이므로 ramp(3) 색. 강조색 없음.
(평균 위치 점선은 정수 μ의 막대에 가려 보이지 않으므로 넣지 않음.)
"""
import math
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

x = np.arange(0, 31)
MUS = [1, 5, 15]
COLS = ramp(3)


def dpois(y, mu):
    return np.array([math.exp(-mu + k * math.log(mu) - math.lgamma(k + 1)) for k in y])


fig, axs = plt.subplots(3, 1, figsize=(8.2, 5.4), sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.22)

for ax, mu, c in zip(axs, MUS, COLS):
    p = dpois(x, mu)
    ax.vlines(x, 0, p, color=c, lw=3.5, zorder=2)
    ax.axhline(0, color="#9AA1AB", lw=0.8, zorder=1)
    ax.text(30, 0.36, rf"$\mu$ = {mu}", ha="right", va="top", fontsize=13,
            fontweight="bold", color=c)
    ax.text(30, 0.26, f"평균 = 분산 = {mu}", ha="right", va="top", fontsize=11, color=TEXT2)
    ax.set_ylim(0, 0.4)
    ax.set_xlim(-0.8, 30.8)
    ax.set_yticks([0, 0.2, 0.4])
    ax.set_yticklabels(["0", "0.2", "0.4"], fontsize=11)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0)

axs[-1].set_xticks(range(0, 31, 5))
axs[-1].tick_params(axis="x", labelsize=11, length=3)
axs[-1].set_xlabel(r"$y$", fontsize=13)
axs[1].set_ylabel(r"$P(Y = y)$", fontsize=12)

save(fig, "assets/img/ch13/pois_shapes.png")