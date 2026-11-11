"""6-II §3.2 Random effects — 가계 효과 τ_i ~ N(0, σ_a²)와 가계 내 흩어짐 σ², 그리고 ICC (설명용).

새로 그림. 설명용 가상 자료(고정 시드): 가계 6개, 가계마다 구성원 5명(본문의 n0 = 5와 같은 균형자료).
본문 결과값(0.08128, ICC 0.15)은 그림에 넣지 않는다. 축 눈금은 의미가 없으므로 숨김.
색: 가계 간 변동(σ_a², 가계 평균 μ + τ_i) CAT[0], 가계 내 변동(σ²) CAT[1], 구성원은 무채색.
나란한 가계는 모두 같은 색으로 두고 강조색은 쓰지 않는다.
ICC는 한 줄 분수로 씀(\frac은 분자·분모가 작아져 페이지 폭에서 11pt 아래로 줄어듦).
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

rng = np.random.default_rng(19)
SA, S = 1.0, 0.6                                   # σ_a, σ (가상)
TAU = np.array([-1.3, 0.6, -0.3, 1.4, 0.1, -0.8])  # 가계 효과 (가상)
N0 = 5
C_A, C_W = CAT[0], CAT[1]
YLO, YHI = -4.1, 3.4
Y_LAB, Y_ICC = -2.75, -3.7                         # 가계 이름 줄, 공식 줄

fig = plt.figure(figsize=(8.2, 4.2))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 4.6], wspace=0.04)
lx = fig.add_subplot(gs[0])
ax = fig.add_subplot(gs[1], sharey=lx)

# ── 왼쪽: 가계 효과의 분포 N(0, σ_a²), 옆으로 눕힘 ──────────────────────────
yy = np.linspace(-3.0, 3.0, 400)
dens = np.exp(-yy ** 2 / (2 * SA ** 2)) / (SA * np.sqrt(2 * np.pi))
lx.fill_betweenx(yy, 0, dens, color=mix(C_A, 0.16), lw=0)
lx.plot(dens, yy, color=C_A, lw=1.8)
lx.plot([0, 0], [-3.0, 3.0], color=TEXT2, lw=1)
lx.axhline(0, color=TEXT2, lw=1.1, ls="--", zorder=1)
for t in TAU:                                      # 뽑힌 τ_i
    lx.plot([0, 0.05], [t, t], color=C_A, lw=2.4, solid_capstyle="butt", zorder=4)
lx.annotate("", xy=(0.085, -SA), xytext=(0.085, SA),
            arrowprops=dict(arrowstyle="<->", color=C_A, lw=1.4))
lx.text(0.25, 0.0, r"$\sigma_a^2$" + "\n가계 간", ha="center", va="center", fontsize=12,
        color=shade(C_A, 0.05), fontweight="bold", linespacing=1.3)
lx.text(0.2, Y_ICC, r"$\tau_i \sim N(0,\sigma_a^2)$", ha="center", va="center",
        fontsize=12, color=TEXT)
lx.set_xlim(0.46, -0.01)                           # 뒤집어서 기준선이 오른쪽(가계 쪽)
lx.set_ylim(YLO, YHI)
lx.axis("off")

# ── 오른쪽: 가계별 구성원 ───────────────────────────────────────────────
ax.axhline(0, color=TEXT2, lw=1.1, ls="--", zorder=1)
ax.text(7.25, 0.0, r"$\mu$", ha="right", va="bottom", fontsize=13, color=TEXT2)
offs = np.array([-0.16, -0.08, 0.0, 0.08, 0.16])
for k, t in enumerate(TAU, start=1):
    eps = np.clip(rng.normal(0, S, N0), -1.8 * S, 1.8 * S)
    ax.scatter(k + rng.permutation(offs), t + eps, s=30, color=mix(TEXT2, 0.6),
               zorder=3, linewidths=0)
    ax.plot([k - 0.3, k + 0.3], [t, t], color=C_A, lw=3, solid_capstyle="butt", zorder=4)
    ax.text(k, Y_LAB, f"가계 {k}", ha="center", va="center", fontsize=11, color=TEXT2)

# μ + τ_i 이름표 (가계 4)
ax.annotate(r"$\mu+\tau_i$", (4.3, TAU[3]), xytext=(4.95, 2.75), fontsize=13, color=C_A,
            va="center", arrowprops=dict(arrowstyle="-", color=mix(C_A, 0.7), lw=1))

# σ² 괄호 (가계 6)
k, t = 6, TAU[5]
ax.annotate("", xy=(k + 0.38, t - S), xytext=(k + 0.38, t + S),
            arrowprops=dict(arrowstyle="<->", color=C_W, lw=1.4))
ax.text(k + 0.5, t, r"$\sigma^2$" + "\n가계 내", ha="left", va="center", fontsize=12,
        color=shade(C_W, 0.15), fontweight="bold", linespacing=1.3)

# ICC (가계 이름 아래 한 줄, 설명은 공식 바로 옆)
ax.text(0.55, Y_ICC, r"$\mathrm{ICC}=\sigma_a^2\,/\,(\sigma_a^2+\sigma^2)$",
        ha="left", va="center", fontsize=13, color=TEXT)
ax.text(3.05, Y_ICC, "같은 가계 두 관측치의 상관", ha="left", va="center", fontsize=11, color=TEXT2)

ax.set_xlim(0.4, 7.3)
ax.set_ylim(YLO, YHI)
ax.axis("off")
ax.text(0.45, 3.2, r"$Y_{ij}$", ha="left", va="center", fontsize=13, color=TEXT)

save(fig, "assets/img/ch19/random_effects.png")