"""5-II §2.6 λ는 어떻게 고르는가 — K-fold 교차검증으로 CV 오차 곡선을 만들고
lambda.min / lambda.1se를 고르는 과정 (설명용 도식, 숫자 없음).

왼쪽: 자료를 K조각으로 나눠 한 조각씩 검증, 나머지로 훈련 → 검증 오차 e_1..e_K.
오른쪽: λ마다 K개 오차를 평균한 CV 곡선(가상의 모양)과 두 관행.
나란한 두 관행은 CAT 색, 강조색 없음.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

W, H = 8.2, 3.8
fig, ax = new(W, H)

C_VAL = PRIMARY
C_TR = mix(PRIMARY, 0.14)
C_MIN, C_1SE = CAT[1], CAT[2]
MONO = "DejaVu Sans Mono"

# ── 왼쪽: K-fold 격자 ───────────────────────────────────────────────────────
bw, bg, rh = 0.55, 0.06, 0.42
gx0 = 0.55
cols = ["1", "2", "3", "⋯", "K"]
for j, c in enumerate(cols):
    label(ax, gx0 + j * (bw + bg) + bw / 2, 3.62, c, fs=11, c=TEXT2)

rows = [(3.0, 0, r"$e_1$"), (2.46, 1, r"$e_2$"), (1.92, 2, r"$e_3$"), (1.0, 4, r"$e_K$")]
for y0, vj, e in rows:
    for j in range(5):
        x = gx0 + j * (bw + bg)
        if j == vj:
            box(ax, x, y0, bw, rh, fc=C_VAL, ec="none", r=0.05)
            label(ax, x + bw / 2, y0 + rh / 2, "검증", fs=11, w="bold", c=on(C_VAL))
        else:
            box(ax, x, y0, bw, rh, fc=C_TR, ec="none", r=0.05)
    label(ax, gx0 + 5 * bw + 4 * bg + 0.25, y0 + rh / 2, e, fs=13, c=TEXT, ha="left")
gx1 = gx0 + 5 * bw + 4 * bg
label(ax, (gx0 + gx1) / 2, 1.66, "⋮", fs=14, c=TEXT2)
label(ax, gx1 + 0.37, 1.66, "⋮", fs=14, c=TEXT2)

# 범례
box(ax, gx0, 0.47, 0.26, 0.2, fc=C_TR, ec="none", r=0.03)
label(ax, gx0 + 0.34, 0.57, "훈련: 나머지 K − 1조각으로 적합", fs=11, c=TEXT, ha="left")
label(ax, gx0, 0.2, r"$e_k$" + ": k번째 조각의 검증 오차", fs=11, c=TEXT2, ha="left")

# 묶음 → 평균
bxl = gx1 + 0.78
ytop, ybot = 3.0 + rh / 2, 1.0 + rh / 2
ax.plot([bxl, bxl], [ybot, ytop], color=TEXT2, lw=1.3, zorder=3)
for yy in (ytop, ybot):
    ax.plot([bxl - 0.1, bxl], [yy, yy], color=TEXT2, lw=1.3, zorder=3)
ymid = (ytop + ybot) / 2

# ── 오른쪽: CV 곡선 (가상의 모양) ──────────────────────────────────────────
cx0, cx1, cy0, cy1 = 5.6, 8.1, 1.0, 3.15
arrow(ax, bxl, ymid, cx0 - 0.1, ymid, color=TEXT2, lw=1.5)
label(ax, (bxl + cx0) / 2 - 0.05, ymid + 0.2, "K개 평균", fs=11, c=TEXT)
label(ax, (bxl + cx0) / 2 - 0.05, ymid - 0.2, "λ마다 한 점", fs=11, c=TEXT2)

def f(u):
    return 0.3 + 1.2 * (u - 0.35) ** 2 + 2.0 * np.maximum(u - 0.55, 0) ** 2

def X(u):
    return cx0 + 0.12 + u * (cx1 - cx0 - 0.24)

def Y(v):
    return cy0 + (v - 0.18) / 1.1 * (cy1 - cy0)

SE = 0.1
us = np.round(np.arange(0.05, 0.96, 0.075), 3)
fs_ = f(us)
u_min = us[np.argmin(fs_)]
u_1se = us[fs_ <= fs_.min() + SE].max()

arrow(ax, cx0, cy0, cx1, cy0, color=TEXT2, lw=1.2, ms=10)
arrow(ax, cx0, cy0, cx0, cy1, color=TEXT2, lw=1.2, ms=10)
label(ax, cx0 - 0.15, cy0 + 0.45, "CV 오차", fs=11, c=TEXT, rotation=90)
label(ax, (cx0 + cx1) / 2, cy0 - 0.25, r"$\log\lambda$" + "  (클수록 단순한 모형)",
      fs=11, c=TEXT)

uu = np.linspace(0.05, 0.95, 200)
ax.plot(X(uu), Y(f(uu)), color=mix(TEXT2, 0.5), lw=1.2, zorder=3)
for u, v in zip(us, fs_):
    ax.plot([X(u)] * 2, [Y(v - SE), Y(v + SE)], color=mix(TEXT2, 0.7), lw=1, zorder=3)
ax.scatter(X(us), Y(fs_), s=16, color=TEXT, zorder=4)

# 최소 + 1 표준오차 수평선
ax.plot([X(u_min), X(u_1se)], [Y(fs_.min() + SE)] * 2, color=TEXT2, lw=1, ls=":", zorder=3)

for u, c, name, desc, ha, dx in [(u_min, C_MIN, "lambda.min", "CV 오차 최소", "right", 0.06),
                                (u_1se, C_1SE, "lambda.1se", "1 표준오차 안 최대 λ", "left", -0.06)]:
    ax.plot([X(u)] * 2, [cy0, cy1], color=c, lw=1.4, ls="--", zorder=2)
    ax.scatter([X(u)], [Y(f(u))], s=55, color=c, ec="white", lw=1.2, zorder=5)
    xt = X(u) + dx
    ax.text(xt, cy1 + 0.42, name, fontsize=11, fontweight="bold", family=MONO,
            color=shade(c, 0.1), ha=ha, va="center")
    label(ax, xt, cy1 + 0.17, desc, fs=11, c=TEXT2, ha=ha)

save(fig, "assets/img/ch16/kfold_cv.png")