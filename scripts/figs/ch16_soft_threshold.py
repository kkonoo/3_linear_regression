"""5-II §2.3 Lasso — 연성임계(soft-thresholding)와 ridge 축소를 OLS와 비교 (R 청크 soft-threshold 다시 그림).

R 코드와 같은 함수와 λ를 쓴다. 직교 설계에서
  OLS: z,  Lasso: S(z, λ) = sign(z)(|z| − λ)_+,  Ridge: z / (1 + λ),  λ = 1.
데이터가 아니라 함수 그래프다. 강조색은 한 곳, 계수가 정확히 0이 되는 띠 |z| ≤ λ에만 쓴다.
색은 l1_l2_geometry와 맞춘다: Ridge(L2) CAT[0], Lasso(L1) CAT[1].
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

LAM = 1.0
z = np.linspace(-3, 3, 400)
soft = lambda z, l: np.sign(z) * np.maximum(np.abs(z) - l, 0)
ols, lasso, ridge = z, soft(z, LAM), z / (1 + LAM)
C_RIDGE, C_LASSO = CAT[0], CAT[1]

fig, ax = plt.subplots(figsize=(6.6, 4.3))

# 정확히 0이 되는 띠 |z| ≤ λ  (강조색: 그림에서 한 곳)
ax.axvspan(-LAM, LAM, color=mix(ACCENT, 0.30), lw=0, zorder=0)
ax.axhline(0, color=LINE, lw=1, zorder=1)
ax.axvline(0, color=LINE, lw=1, zorder=1)

ax.plot(z, ols, color=TEXT2, lw=1.5, ls="--", zorder=2)
ax.plot(z, ridge, color=C_RIDGE, lw=2.4, zorder=3)
ax.plot(z, lasso, color=C_LASSO, lw=2.6, zorder=4)

# 띠 안 설명 (곡선과 겹치지 않는 아래쪽)
label(ax, 0, -2.35, "정확히 0", fs=12.5, w="bold", c=ACCENT_INK)
ax.text(0, -2.8, r"$|z|\leq\lambda$", fontsize=12, color=ACCENT_INK, ha="center", va="center")

# 큰 계수는 λ만큼 평행이동
xa = -2.5
ax.annotate("", xy=(xa, soft(xa, LAM)), xytext=(xa, xa),
            arrowprops=dict(arrowstyle="<->", color=shade(C_LASSO, 0.15), lw=1.3, shrinkA=0, shrinkB=0))
ax.text(xa - 0.12, (xa + soft(xa, LAM)) / 2, r"$\lambda$", fontsize=13, color=shade(C_LASSO, 0.15),
        ha="right", va="center")

# 곡선 끝 이름표 (범례 대신)
ax.text(3.12, 3.0, "OLS", fontsize=12, color=TEXT2, va="center", clip_on=False)
ax.text(3.12, soft(3, LAM), r"Lasso  $S(z,\lambda)$", fontsize=12, color=shade(C_LASSO, 0.15),
        fontweight="bold", va="center", clip_on=False)
ax.text(3.12, 3 / (1 + LAM) - 0.12, r"Ridge  $z/(1+\lambda)$", fontsize=12, color=C_RIDGE,
        fontweight="bold", va="center", clip_on=False)

ax.set_xlim(-3.1, 3.1); ax.set_ylim(-3.15, 3.2)
ax.set_xticks([-LAM, 0, LAM]); ax.set_xticklabels([r"$-\lambda$", "0", r"$\lambda$"], fontsize=12)
ax.set_yticks([0]); ax.set_yticklabels(["0"], fontsize=12)
ax.set_xlabel("z (OLS 추정)", fontsize=12)
ax.set_ylabel("벌점 추정치", fontsize=12)

save(fig, "assets/img/ch16/soft_threshold.png")