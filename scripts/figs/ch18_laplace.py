"""6-I §2.2 두꺼운 꼬리 분포 — 분산이 같은 정규분포와 라플라스 분포 (R 청크 laplace-plot을 다시 그림).

R 코드와 같은 분포·모수: 정규 N(0, 1), 라플라스 μ = 0, 척도 b = 1/√2 (분산 1).
① 전체 모양(-4..4), ② 오른쪽 꼬리(y ≥ 2.5)를 확대. 두 곡선은 y ≈ 2.35에서 만나므로
확대 구간을 2.5부터 잡아 그 안에서는 라플라스가 늘 위에 있게 했다.
데이터가 아닌 밀도함수 그대로라 축 눈금을 남김. 나란한 두 분포 → CAT[0], CAT[1]. 강조색 없음.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

b = 1 / np.sqrt(2)                       # 분산 1이 되는 척도 (R 코드와 같음)
Z0 = 2.5                                 # 꼬리 확대 시작점


def dnorm(y):
    return np.exp(-y ** 2 / 2) / np.sqrt(2 * np.pi)


def dlap(y):
    return np.exp(-np.abs(y) / b) / (2 * b)


C_N, C_L = CAT[0], CAT[1]
xx = np.linspace(-4, 4, 801)

fig = plt.figure(figsize=(8.2, 3.7))
gs = fig.add_gridspec(1, 2, width_ratios=[1.55, 1], wspace=0.24)
ax = fig.add_subplot(gs[0])
tx = fig.add_subplot(gs[1])

# ① 전체
ax.axvspan(Z0, 4, color=mix(TEXT2, 0.10), lw=0, zorder=0)
ax.plot(xx, dnorm(xx), color=C_N, lw=2.2, zorder=3)
ax.plot(xx, dlap(xx), color=C_L, lw=2.2, zorder=3)
ax.annotate("라플라스 분포", (0.15, dlap(0.15)), xytext=(0.75, 0.66), fontsize=12,
            fontweight="bold", color=C_L, va="center",
            arrowprops=dict(arrowstyle="-", color=C_L, lw=1))
ax.annotate("정규분포", (0.9, dnorm(0.9)), xytext=(1.45, 0.43), fontsize=12,
            fontweight="bold", color=C_N, va="center",
            arrowprops=dict(arrowstyle="-", color=C_N, lw=1))
ax.text((Z0 + 4) / 2, 0.72, "②", fontsize=12, fontweight="bold", color=TEXT2,
        ha="center", va="top")
ax.set_xlim(-4, 4); ax.set_ylim(0, 0.75)
ax.set_xticks([-4, -2, 0, 2, 4]); ax.set_yticks([0, 0.2, 0.4, 0.6])
ax.tick_params(labelsize=11)
ax.set_xlabel(r"$y$", fontsize=13); ax.set_ylabel("밀도", fontsize=12)
ax.set_title("① 전체", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

# ② 오른쪽 꼬리 확대 (y ≥ 2.5)
tt = np.linspace(Z0, 4, 401)
tx.fill_between(tt, dnorm(tt), dlap(tt), color=mix(C_L, 0.22), lw=0, zorder=1)
tx.plot(tt, dnorm(tt), color=C_N, lw=2.2, zorder=3)
tx.plot(tt, dlap(tt), color=C_L, lw=2.2, zorder=3)
tx.annotate("라플라스 분포\n꼬리가 더 두꺼움", (3.25, dlap(3.25)), xytext=(3.05, 0.0175),
            fontsize=11, color=C_L, va="center", linespacing=1.3,
            arrowprops=dict(arrowstyle="-", color=C_L, lw=1))
tx.annotate("정규분포", (2.75, dnorm(2.75)), xytext=(2.55, 0.0032), fontsize=12,
            fontweight="bold", color=C_N, va="center",
            arrowprops=dict(arrowstyle="-", color=C_N, lw=1))
tx.set_xlim(Z0, 4); tx.set_ylim(0, 0.022)
tx.set_xticks([2.5, 3, 3.5, 4]); tx.set_yticks([0, 0.01, 0.02])
tx.tick_params(labelsize=11)
tx.set_xlabel(r"$y$", fontsize=13)
tx.set_title("② 오른쪽 꼬리 확대", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

save(fig, "assets/img/ch18/laplace.png")