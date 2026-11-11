"""1-I §2.2 오차에 대한 네 가지 가정: 회귀직선 위에 같은 정규분포를 옆으로 눕혀 그림 (설명용 가상 자료).

여러 x에서 Y의 분포를 그린다. 중심은 직선 위에 있고(평균 0), 폭은 모두 같고(등분산),
모양은 종 모양이다(정규성). 즉 Y_i ~ N(β0 + β1 x_i, σ²)를 그림으로 보인다.
독립성은 그림으로 나타낼 수 없으므로 캡션에서 다룬다.
네 분포는 같은 분포이므로 한 색(CAT[0])을 쓰고, 등분산 표시는 CAT[1]로 칠한다. 강조색은 쓰지 않는다.
설명 라벨 셋은 오른쪽 빈 곳에 모아 두어 지시선이 점·막대·곡선을 가로지르지 않게 한다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"
rng = np.random.default_rng(11)

B0, B1, SIG = 1.0, 0.5, 0.6          # 가상의 모수
XS = [2.0, 4.0, 6.0, 8.0]            # 분포를 그릴 x 위치
WID = 1.1                            # 눕힌 밀도곡선의 최대 폭(그림 단위)
ZMAX = 2.8                           # 곡선을 그릴 범위(±ZMAX·σ)
C_D, C_V = CAT[0], CAT[1]

fig, ax = plt.subplots(figsize=(8.2, 3.9))

# 회귀직선 E(Y) = β0 + β1 x
xx = np.array([0.5, 10.5])
ax.plot(xx, B0 + B1 * xx, color=TEXT, lw=1.8, zorder=3)
ax.text(10.65, B0 + B1 * 10.5, r"$E(Y)=\beta_0+\beta_1 x$", fontsize=13, color=TEXT,
        va="center", ha="left")

z = np.linspace(-ZMAX, ZMAX, 300)
for xk in XS:
    mu = B0 + B1 * xk
    yy = mu + z * SIG
    curve = xk + WID * np.exp(-z ** 2 / 2)
    # 기준선과 눕힌 정규분포 (모두 같은 분포)
    ax.plot([xk, xk], [yy[0], yy[-1]], color=TEXT2, lw=0.9, ls=(0, (3, 3)), zorder=1)
    ax.fill_betweenx(yy, xk, curve, color=mix(C_D, 0.16), lw=0, zorder=1)
    ax.plot(curve, yy, color=C_D, lw=1.8, zorder=2)
    # ±σ 막대: 어느 x에서나 같은 길이
    bx = xk - 0.2
    ax.plot([bx, bx], [mu - SIG, mu + SIG], color=C_V, lw=2.2, solid_capstyle="butt", zorder=4)
    for yv in (mu - SIG, mu + SIG):
        ax.plot([bx - 0.08, bx + 0.08], [yv, yv], color=C_V, lw=2.2, zorder=4)
    # 표본점 몇 개
    e = np.clip(rng.normal(0, SIG, 6), -2.4 * SIG, 2.4 * SIG)
    ax.scatter(np.full(6, xk), mu + e, s=24, color=TEXT, zorder=5, edgecolor="white", lw=0.6)

# 설명 라벨: 마지막 분포(x = 8) 오른쪽 빈 곳에 모음
x8, mu8 = 8.0, B0 + B1 * 8.0
LX = 9.75
# 평균 0 → 곡선의 꼭짓점(중심)이 직선 높이에 있음
ax.annotate("평균 0: 중심이 직선 위", xy=(x8 + WID + 0.03, mu8 - 0.03), xytext=(LX, 4.25),
            fontsize=12, color=TEXT, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=TEXT2, lw=1, shrinkA=3, shrinkB=1,
                            relpos=(0.0, 0.5)))
# 정규성 → 곡선의 아래쪽 어깨
tx, ty = x8 + WID * np.exp(-0.5), mu8 - SIG
ax.annotate("정규성: 종 모양", xy=(tx + 0.03, ty), xytext=(LX, 3.45),
            fontsize=12, color=shade(C_D, 0.1), ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=mix(C_D, 0.8), lw=1, shrinkA=3, shrinkB=1,
                            relpos=(0.0, 0.5)))
# 등분산 → 막대 색과 같은 글자색
ax.text(LX, 2.65, r"등분산: 폭 $\sigma$가 모두 같음", fontsize=12, color=shade(C_V, 0.15),
        ha="left", va="center")

# 위·아래 꼬리가 잘리지 않도록 범위를 곡선 끝보다 넉넉히
ylo = B0 + B1 * XS[0] - ZMAX * SIG - 0.2
yhi = B0 + B1 * XS[-1] + ZMAX * SIG + 0.2
ax.set_xlim(0.2, 13.9)
ax.set_ylim(ylo, yhi)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("Y", fontsize=12, rotation=0, labelpad=10)

save(fig, "assets/img/ch01/error_assumptions.png")