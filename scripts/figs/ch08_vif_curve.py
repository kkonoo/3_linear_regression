"""8장 §4.3 Variance Inflation Factor: VIF_j = 1/(1 − R_j²)와 √VIF(표준오차 배수)를 R_j²에 대해 그린 곡선.

자료가 아니라 공식의 곡선이다. 표시한 점은 본문 표의 값이다
(R_j² = 0, 0.5, 0.9, 0.95 → VIF 1, 2, 10, 20; 0.9에서 표준오차 3.2배).
기준선은 본문의 관행적 기준 VIF > 10 (또는 > 5)만 그린다.
강조색은 VIF = 10 기준선 한 곳에만 쓴다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

r2 = np.linspace(0, 0.95, 400)
vif = 1 / (1 - r2)
se = np.sqrt(vif)
C1, C2 = CAT[0], CAT[1]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.2, 3.7))
fig.subplots_adjust(wspace=0.32)

# ① VIF
a1.axhline(5, color=TEXT2, lw=1.1, ls="--", zorder=1)
a1.axhline(10, color=ACCENT_INK, lw=1.4, zorder=1)
a1.text(0.02, 10.5, "기준 VIF > 10", fontsize=11, color=ACCENT_INK, fontweight="bold",
        ha="left", va="bottom")
a1.text(0.02, 5.5, "또는 > 5", fontsize=11, color=TEXT2, ha="left", va="bottom")
a1.plot(r2, vif, color=C1, lw=2.2, zorder=2)
pts = [(0.0, 1), (0.5, 2), (0.9, 10), (0.95, 20)]
for x, v in pts:
    a1.plot(x, v, "o", ms=7, color=C1, mec="white", mew=1.3, zorder=4)
a1.text(0.03, 1.9, "1 (무상관)", fontsize=11, color=TEXT, ha="left", va="bottom")
a1.text(0.5, 3.0, "2배", fontsize=11, color=TEXT, ha="center", va="bottom")
a1.text(0.85, 8.4, "10배", fontsize=11, color=TEXT, ha="right", va="center")
a1.text(0.92, 20, "20배", fontsize=11, color=TEXT, ha="right", va="center")
a1.set_xlim(-0.02, 1.0); a1.set_ylim(0, 21.8)
a1.set_xticks([0, 0.25, 0.5, 0.75, 0.9])
a1.set_yticks([1, 5, 10, 20])
a1.tick_params(labelsize=11)
a1.set_xlabel(r"$R_j^2$", fontsize=13)
a1.set_ylabel(r"$V(\hat\beta_j)$의 배수", fontsize=11)
a1.set_title(r"① $VIF_j = 1/(1-R_j^2)$", fontsize=12, fontweight="bold", color=TEXT,
             loc="left", pad=8)

# ② √VIF
a2.plot(r2, se, color=C2, lw=2.2, zorder=2)
a2.plot(0, 1, "o", ms=7, color=C2, mec="white", mew=1.3, zorder=4)
a2.plot(0.9, np.sqrt(10), "o", ms=7, color=C2, mec="white", mew=1.3, zorder=4)
a2.hlines(np.sqrt(10), -0.02, 0.9, color=mix(C2, 0.5), lw=1, ls=":", zorder=1)
a2.vlines(0.9, 0, np.sqrt(10), color=mix(C2, 0.5), lw=1, ls=":", zorder=1)
a2.text(0.03, 1.12, "1 (무상관)", fontsize=11, color=TEXT, ha="left", va="bottom")
a2.text(0.86, 3.4, "표준오차 3.2배", fontsize=11, color=TEXT, ha="right", va="bottom")
a2.set_xlim(-0.02, 1.0); a2.set_ylim(0, 4.8)
a2.set_xticks([0, 0.25, 0.5, 0.75, 0.9])
a2.set_yticks([1, 2, 3, 4])
a2.tick_params(labelsize=11)
a2.set_xlabel(r"$R_j^2$", fontsize=13)
a2.set_ylabel("표준오차의 배수", fontsize=11)
a2.set_title(r"② $\sqrt{VIF_j}$", fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=8)

save(fig, "assets/img/ch08/vif_curve.png")