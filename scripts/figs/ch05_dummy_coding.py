"""3-? §3.3 ANOVA를 회귀식으로 표현하기 — 3수준 유전형(geno)을 더미변수 2개로 바꾸는 과정.

새로 그림(도식, 축 없음). 수준 이름·변수 이름(AA 기준, genoAB, genoBB)과 숫자
(AA 평균 2.938, genoBB = 0.831)는 본문의 R 결과와 같다. 가상 자료 없음.
나란한 세 유전형 → CAT 색, 강조색 없음.
"""
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

LEVELS = ["AA", "AB", "BB"]
DUMMY = [(0, 0), (1, 0), (0, 1)]          # (genoAB, genoBB)
MEANING = [
    (r"$\beta_0$ = 절편", "= 기준 범주(AA) 평균 2.938"),
    (r"$\beta_1$ (genoAB)", "= AB 평균 − AA 평균"),
    (r"$\beta_2$ (genoBB)", "= BB 평균 − AA 평균 = 0.831"),
]

W, H = 8.2, 4.4
fig, ax = new(W, H)

rh, rgap = 0.62, 0.06
top = 3.3
lx, lw_ = 0.2, 1.15                        # 유전형 칸
tx0, cw = 1.75, 0.95                       # 표
rx = 5.05                                  # 계수의 뜻
cx_all = 3.6                               # 그린 내용의 가로 중심 (0.2 … ~7.0)

# 머리글
label(ax, lx + lw_ / 2, 3.62, "유전형 (geno)", fs=11, c=TEXT2)
heads = ["(Intercept)", "genoAB", "genoBB"]
maths = ["1", r"$x_{i1}$", r"$x_{i2}$"]
for j in range(3):
    cx = tx0 + j * cw + cw / 2
    label(ax, cx, 3.75, heads[j], fs=11, w="bold", c=TEXT2 if j == 0 else TEXT)
    label(ax, cx, 3.47, maths[j], fs=12, c=TEXT2 if j == 0 else TEXT)
label(ax, rx, 3.62, "계수의 뜻", fs=11, c=TEXT2, ha="left")

# 더미 두 열 묶음 표시
y_b = 4.0
ax.plot([tx0 + cw + 0.06, tx0 + 3 * cw - 0.06], [y_b, y_b], color=TEXT2, lw=1.2)
for xx in (tx0 + cw + 0.06, tx0 + 3 * cw - 0.06):
    ax.plot([xx, xx], [y_b, y_b - 0.08], color=TEXT2, lw=1.2)
label(ax, tx0 + 2 * cw, y_b + 0.17, "더미 2개 = k − 1", fs=11, c=TEXT2)

for i, lev in enumerate(LEVELS):
    c = CAT[i]
    y1 = top - i * (rh + rgap)
    y0 = y1 - rh
    yc = (y0 + y1) / 2
    # 유전형 칸
    box(ax, lx, y0, lw_, rh, fc=c, ec="none", r=0.08)
    label(ax, lx + lw_ / 2, yc, lev + (" (기준)" if i == 0 else ""), fs=13 if i else 12,
          w="bold", c=on(c))
    arrow(ax, lx + lw_ + 0.06, yc, tx0 - 0.07, yc, color=mix(c, 0.7), lw=1.4, ms=10)
    # 표의 한 행
    vals = [1] + list(DUMMY[i])
    for j, v in enumerate(vals):
        x = tx0 + j * cw
        if j == 0:
            fc, ec, tc, wt = FAINT, "none", TEXT2, "regular"
        elif v == 1:
            fc, ec, tc, wt = mix(c, 0.28), "none", shade(c, 0.25), "bold"
        else:
            fc, ec, tc, wt = "white", LINE, TEXT2, "regular"
        box(ax, x + 0.04, y0 + 0.03, cw - 0.08, rh - 0.06, fc=fc, ec=ec, r=0.06)
        label(ax, x + cw / 2, yc, str(v), fs=13, w=wt, c=tc)
    arrow(ax, tx0 + 3 * cw + 0.05, yc, rx - 0.1, yc, color=mix(c, 0.7), lw=1.4, ms=10)
    # 계수의 뜻
    l1, l2 = MEANING[i]
    label(ax, rx, yc + 0.14, l1, fs=12, w="bold", c=c, ha="left")
    label(ax, rx, yc - 0.15, l2, fs=11, c=TEXT, ha="left")

# 아래: 회귀식과 k − 1개인 이유 (표 바로 아래로 당기고 내용 중심에 맞춤)
label(ax, cx_all, 0.98, r"$Y_i=\beta_0+\beta_1 x_{i1}+\beta_2 x_{i2}+\varepsilon_i$", fs=13)
label(ax, cx_all, 0.6,
      "AA 더미는 두지 않음: 세 더미를 다 넣으면 그 합이 절편 열(1, …, 1)과 같아 선형종속",
      fs=11, c=TEXT2)

save(fig, "assets/img/ch05/dummy_coding.png")