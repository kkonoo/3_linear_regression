"""5-I §2.3 LAD의 추정: 손실함수 ρ(r)와 IRLS 가중치 v(r) (설명용).

제곱손실 r²(OLS), 절대손실 |r|(LAD), Huber(|r| ≤ c에서는 r², 바깥에서는 직선)를 비교한다.
본문에 Huber 상수가 없으므로 c는 숫자 없이 표시한다(그림에서는 c = 1.5로 그림).
Huber는 r² 쪽에 맞춘 꼴(c 바깥에서 2c|r| − c²)로 그려 0 근처에서 OLS와 겹치게 했다.
오른쪽 패널은 본문의 IRLS 가중치 v = 1/|r|(LAD), OLS = 1, Huber = min(1, c/|r|).
OLS와 Huber가 v = 1에서 겹치는 구간은 OLS를 점선으로 위에 그려 둘 다 보이게 했다.
나란한 세 방법은 CAT[0..2]. 강조색은 "큰 잔차에서 벌점 차이" 한 곳에만 쓴다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

C = 1.5                                   # Huber 경계 (설명용, 숫자는 표시하지 않음)
C_OLS, C_LAD, C_HUB = CAT[0], CAT[1], CAT[2]
r = np.linspace(-3, 3, 1201)

rho_ols = r ** 2
rho_lad = np.abs(r)
rho_hub = np.where(np.abs(r) <= C, r ** 2, 2 * C * np.abs(r) - C ** 2)

fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.6))
fig.subplots_adjust(wspace=0.5)

# ── ① 손실함수 ───────────────────────────────────────────────
ax = axs[0]
for c_ in (-C, C):
    ax.axvline(c_, color=LINE, lw=1, ls=":", zorder=0)
ax.plot(r, rho_ols, color=C_OLS, lw=2.2, zorder=3)
ax.plot(r, rho_hub, color=C_HUB, lw=2.2, zorder=3)
ax.plot(r, rho_lad, color=C_LAD, lw=2.2, zorder=3)
ax.text(3.08, 9.0, r"$r^2$  OLS", fontsize=11.5, color=C_OLS, va="center", fontweight="bold")
ax.text(3.08, 2 * C * 3 - C ** 2, "Huber", fontsize=11.5, color=shade(C_HUB, 0.2),
        va="center", fontweight="bold")
ax.text(3.08, 3.0, r"$|r|$  LAD", fontsize=11.5, color=C_LAD, va="center", fontweight="bold")

# 큰 잔차에서 벌점 차이 (강조색 한 곳)
xa = 2.5
ax.annotate("", xy=(xa, xa), xytext=(xa, xa ** 2),
            arrowprops=dict(arrowstyle="<->", color=ACCENT_INK, lw=1.5), zorder=4)
ax.text(xa - 0.15, 7.2, "잔차가 크면\n제곱손실이 훨씬 큼", ha="right", va="center",
        fontsize=11, color=ACCENT_INK, fontweight="bold", linespacing=1.3)

ax.set_xlim(-3.2, 3.2); ax.set_ylim(0, 9.6)
ax.set_xticks([-C, 0, C]); ax.set_xticklabels(["−c", "0", "c"], fontsize=11)
ax.set_yticks([])
ax.set_xlabel(r"잔차 $r$", fontsize=12)
ax.set_ylabel(r"손실 $\rho(r)$", fontsize=12)
ax.set_title("① 손실함수", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

# ── ② IRLS 가중치 ────────────────────────────────────────────
bx = axs[1]
rr = r[np.abs(r) > 1e-3]
w_lad = np.minimum(1 / np.abs(rr), 50)
w_hub = np.minimum(1, C / np.abs(rr))
for c_ in (-C, C):
    bx.axvline(c_, color=LINE, lw=1, ls=":", zorder=0)
bx.plot(rr, w_hub, color=C_HUB, lw=2.6, zorder=3)
bx.plot([-3, 3], [1, 1], color=C_OLS, lw=2.2, zorder=4, dashes=(4, 3))   # Huber 위에 점선
neg, pos = rr < 0, rr > 0
bx.plot(rr[neg], w_lad[neg], color=C_LAD, lw=2.2, zorder=3)
bx.plot(rr[pos], w_lad[pos], color=C_LAD, lw=2.2, zorder=3)

bx.text(-2.95, 1.1, "OLS", fontsize=11.5, color=C_OLS, ha="left", va="bottom", fontweight="bold")
bx.text(0.8, 2.05, r"LAD:  $v = 1/|r|$", fontsize=11.5, color=C_LAD, ha="left", va="center",
        fontweight="bold")
bx.text(3.08, C / 3 + 0.08, "Huber", fontsize=11.5, color=shade(C_HUB, 0.2), ha="left",
        va="center", fontweight="bold")

bx.set_xlim(-3.2, 3.2); bx.set_ylim(0, 2.6)
bx.set_xticks([-C, 0, C]); bx.set_xticklabels(["−c", "0", "c"], fontsize=11)
bx.set_yticks([0, 1]); bx.set_yticklabels(["0", "1"], fontsize=11)
bx.set_xlabel(r"잔차 $r$", fontsize=12)
bx.set_ylabel(r"가중치 $v$", fontsize=12)
bx.set_title("② IRLS 가중치", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

save(fig, "assets/img/ch18/loss_functions.png")