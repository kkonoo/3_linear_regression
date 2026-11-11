"""3-II §3.4 과산포: 포아송의 평균–분산 관계 V(Y) = μ와 과산포 V(Y) = φμ, 그리고 평균이 같은 두 분포의 퍼짐 (설명용).

새로 그림. 수치는 모두 설명용 가상값이다(μ = 5, φ = 3).
본문 §3.4는 과산포 모수 φ(추정값 φ̂)만 다루고 특정 대안 분포를 이름 짓지 않는다. 그래서
그림과 캡션에서는 "과산포"와 "분산 φμ"로만 부른다. ② 패널의 과산포 분포는 μ = 5에서 분산이
φμ = 15가 되도록 음이항 확률로 계산했지만(θ = μ²/(φμ − μ) = 2.5), 그림 안에서는 그 이름을 쓰지 않는다.
색: 포아송 CAT[0], 과산포 CAT[1]로 두 패널에서 같게 둔다. 강조색은 한 곳에만 쓴다:
포아송이 놓치는 분산의 차이.
"""
import math
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

MU, PHI = 5.0, 3.0                      # 설명용
C_P, C_O = CAT[0], CAT[1]               # 포아송, 과산포

fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.2, 3.6))
fig.subplots_adjust(wspace=0.22)

# ── ① 평균–분산 관계 ────────────────────────────────────────────────
m = np.linspace(0, 10.5, 200)
ax.plot(m, m, color=C_P, lw=2.2, zorder=3)
ax.plot(m, PHI * m, color=C_O, lw=2.2, zorder=3)
ax.vlines(MU, 0, PHI * MU, color=LINE, lw=1.2, ls="--", zorder=1)
ax.plot([MU], [MU], "o", ms=7, color=C_P, mec="white", mew=1.2, zorder=5)
ax.plot([MU], [PHI * MU], "o", ms=7, color=C_O, mec="white", mew=1.2, zorder=5)

# 포아송이 놓치는 변동 (강조색 한 곳)
ax.annotate("", xy=(MU + 0.22, MU + 0.3), xytext=(MU + 0.22, PHI * MU - 0.3),
            arrowprops=dict(arrowstyle="<->", color=ACCENT_INK, lw=1.6), zorder=4)
ax.text(MU + 0.45, 11.6, "포아송이\n놓치는 변동", fontsize=11, fontweight="bold",
        color=ACCENT_INK, ha="left", va="center", linespacing=1.3)

ax.text(10.3, 6.6, "포아송\n$V(Y) = \\mu$", fontsize=12, color=C_P, ha="right", va="top",
        fontweight="bold", linespacing=1.35)
ax.text(7.5, 31.3, "과산포\n$V(Y) = \\phi\\mu$, $\\phi > 1$", fontsize=12, color=shade(C_O, 0.1),
        ha="right", va="top", fontweight="bold", linespacing=1.35)

ax.set_xlim(0, 10.5); ax.set_ylim(0, 32)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("평균  $\\mu$", fontsize=12)
ax.set_ylabel("분산  $V(Y)$", fontsize=12)
ax.set_title("① 평균과 분산", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

# ── ② 같은 평균, 다른 퍼짐 ─────────────────────────────────────────
k = np.arange(0, 21)
pois = np.array([math.exp(-MU + y * math.log(MU) - math.lgamma(y + 1)) for y in k])
theta = MU ** 2 / (PHI * MU - MU)       # 2.5 → 분산 = φμ = 15
p = theta / (theta + MU)
over = np.array([math.exp(math.lgamma(y + theta) - math.lgamma(theta) - math.lgamma(y + 1)
                          + theta * math.log(p) + y * math.log(1 - p)) for y in k])

bw = 0.4
bx.bar(k - bw / 2, pois, width=bw, color=C_P, zorder=3)
bx.bar(k + bw / 2, over, width=bw, color=C_O, zorder=3)
top = max(pois.max(), over.max())
bx.vlines(MU, 0, top * 1.12, color=TEXT2, lw=1.2, ls="--", zorder=2)
bx.text(MU + 0.25, top * 1.13, "같은 평균 $\\mu$", fontsize=11, color=TEXT2, ha="left", va="bottom")

bx.text(7.0, pois[6] + 0.012, "포아송", fontsize=12, fontweight="bold", color=C_P,
        ha="left", va="bottom")
bx.text(11.0, over[11] + 0.03, "과산포\n(분산 $\\phi\\mu$, $\\phi = 3$)", fontsize=11.5,
        fontweight="bold", color=shade(C_O, 0.1), ha="left", va="bottom", linespacing=1.35)

bx.set_xlim(-0.8, 20.8); bx.set_ylim(0, top * 1.3)
bx.set_xticks([0, 5, 10, 15, 20]); bx.set_yticks([])
bx.tick_params(labelsize=11)
bx.set_xlabel("개수  $y$", fontsize=12)
bx.set_ylabel("확률", fontsize=12)
bx.set_title("② 같은 평균, 다른 퍼짐", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

save(fig, "assets/img/ch14/overdispersion.png")