"""4-I §1.2 Odds와 logit — 확률 p → odds → logit 세 수직선과 대응하는 값 (예시 값).

본문 1.2절 표의 세 값(p = 0.1, 0.5, 0.9 → odds 1/9, 1, 9 → logit −2.20, 0, 2.20)을
세 수직선 위에 찍고 선으로 잇는다. p = 0.5 ↔ odds 1 ↔ logit 0, 그리고 logit이 0을 중심으로
대칭이고 양쪽 끝이 없다는 점을 보여 준다. 수치는 정확한 계산값.
세 값은 대등한 예이므로 CAT 색으로 구분하고 강조색은 쓰지 않는다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

W, H = 8.0, 3.7
fig, ax = new(W, H)

Y_P, Y_O, Y_L = 3.25, 2.0, 0.75          # 세 수직선의 높이
AX_C = "#9AA1AB"

# 좌표 변환
P0, P1 = 2.45, 7.35                       # p 축: 0..1
xp = lambda p: P0 + (P1 - P0) * p
C = xp(0.5)                               # p = 0.5와 logit 0이 놓일 가운데
O0, OS = 2.45, 0.54                       # odds 축: 0에서 시작, 선형 눈금
xo = lambda o: O0 + OS * o
LS = 1.05                                 # logit 축: 0이 가운데
xl = lambda l: C + LS * l

# ── 수직선 ──────────────────────────────────────────────────────────────
# p: 양 끝이 막힌 구간
ax.plot([P0, P1], [Y_P, Y_P], color=AX_C, lw=2, solid_capstyle="butt", zorder=1)
for xe in (P0, P1):
    ax.plot([xe, xe], [Y_P - 0.1, Y_P + 0.1], color=AX_C, lw=2, zorder=1)
label(ax, P0, Y_P - 0.24, "0", fs=11, c=TEXT2)
label(ax, P1, Y_P - 0.24, "1", fs=11, c=TEXT2)

# odds: 0에서 막히고 오른쪽으로 끝없음
ax.plot([O0, O0], [Y_O - 0.13, Y_O + 0.13], color=AX_C, lw=2, zorder=1)
label(ax, O0 - 0.05, Y_O + 0.24, "0", fs=11, c=TEXT2, ha="right")
arrow(ax, O0, Y_O, 7.75, Y_O, color=AX_C, lw=2, ms=13, z=1)
label(ax, 7.84, Y_O, "∞", fs=13, c=TEXT2, ha="left")

# logit: 양쪽으로 끝없음
arrow(ax, C, Y_L, C - 2.85, Y_L, color=AX_C, lw=2, ms=13, z=1)
arrow(ax, C, Y_L, C + 2.85, Y_L, color=AX_C, lw=2, ms=13, z=1)
label(ax, C - 2.93, Y_L, "−∞", fs=13, c=TEXT2, ha="right")
label(ax, C + 2.93, Y_L, "∞", fs=13, c=TEXT2, ha="left")

# ── 왼쪽 이름 칸 ────────────────────────────────────────────────────────
ROWS = [
    (Y_P, "확률 $p$", None, "(0, 1)"),
    (Y_O, "odds", r"$p\,/\,(1-p)$", "(0, ∞)"),
    (Y_L, "logit", r"$\log\,$odds", "(−∞, ∞)"),
]
for y, name, form, rng in ROWS:
    if form is None:
        label(ax, 0.1, y + 0.12, name, fs=13, w="bold", ha="left")
        label(ax, 0.1, y - 0.16, rng, fs=11, c=TEXT2, ha="left")
    else:
        label(ax, 0.1, y + 0.26, name, fs=13, w="bold", ha="left")
        label(ax, 0.1, y - 0.01, form, fs=11, c=TEXT, ha="left")
        label(ax, 0.1, y - 0.27, rng, fs=11, c=TEXT2, ha="left")

# ── 대응하는 값 (본문 표) ────────────────────────────────────────────────
VALS = [  # p, odds 표시, logit 표시, 색
    (0.1, "0.111", "−2.20", CAT[2]),
    (0.5, "1", "0", CAT[0]),
    (0.9, "9", "2.20", CAT[1]),
]
for p, o_txt, l_txt, c in VALS:
    o = p / (1 - p)
    lg = np.log(o)
    pts = [(xp(p), Y_P), (xo(o), Y_O), (xl(lg), Y_L)]
    ax.plot([q[0] for q in pts], [q[1] for q in pts], color=mix(c, 0.7), lw=1.5, zorder=2)
    for (px, py) in pts:
        ax.add_patch(mp.Circle((px, py), 0.075, fc=c, ec="white", lw=1.5, zorder=4))
    # p 값: 선 위
    label(ax, xp(p), Y_P + 0.24, f"{p:g}", fs=12, w="bold", c=c)
    # logit 값: 선 아래
    label(ax, xl(lg), Y_L - 0.24, l_txt, fs=12, w="bold", c=c)
    # odds 값: 선 아래, 나가는 연결선을 피해서
    if p < 0.5:
        label(ax, xo(o) - 0.08, Y_O - 0.24, o_txt, fs=12, w="bold", c=c, ha="right")
    elif p > 0.5:
        label(ax, xo(o) + 0.08, Y_O - 0.22, o_txt, fs=12, w="bold", c=c, ha="left")
    else:
        label(ax, xo(o), Y_O - 0.24, o_txt, fs=12, w="bold", c=c)

label(ax, C, Y_L - 0.58, "logit은 0을 중심으로 좌우 대칭이고, 양쪽 끝이 없다", fs=11, c=TEXT2)

save(fig, "assets/img/ch10/p_odds_logit.png")