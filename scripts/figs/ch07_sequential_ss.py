"""7장 §2.2 순차제곱합: 같은 SSReg가 변수 순서에 따라 어떻게 나뉘는가 (설명용 도식, 숫자 없음).

새로 그림. 두 막대의 전체 길이는 SSReg(X_1,…,X_p)로 같다.
bmi와 pop이 함께 설명하는 겹치는 부분은 먼저 들어간 변수의 몫이 된다.
나머지 변수는 bmi·pop 뒤에 들어간다고 두어 두 순서에서 길이가 같다.
색: bmi CAT[0], pop CAT[1](두 막대에서 같은 색), 나머지 변수는 무채색. 강조색은 쓰지 않는다.
각 순차제곱합 항이 덮는 범위는 막대 아래 괄호로 표시한다.
용어는 본문 표기(SSReg)를 따른다. 길이는 개념을 보이기 위한 임의 값(설명용).
"""
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

C_BMI, C_POP = CAT[0], CAT[1]
NEUTRAL = "#D9DCE1"

OWN_BMI, SHARED, OWN_POP, REST = 1.4, 1.6, 1.5, 1.4   # 설명용 길이(인치)
TOTAL = OWN_BMI + SHARED + OWN_POP + REST

W, H = 8.2, 3.8
fig, ax = new(W, H)
x0 = 1.8
x1 = x0 + TOTAL
bh = 0.6


def seg(x, y, w, fc, text=None, tc=None, fs=12, bold=True):
    box(ax, x, y, w, bh, fc=fc, ec="white", lw=2, r=0.001, z=2)
    if text:
        label(ax, x + w / 2, y + bh / 2, text, fs=fs, w="bold" if bold else "regular",
              c=tc or on(fc))


def bracket(x, w, y, text, color):
    """막대 아래, 항이 덮는 범위를 표시하는 괄호와 이름."""
    a, b = x + 0.06, x + w - 0.06
    yb = y - 0.13
    ax.plot([a, a, b, b], [yb + 0.07, yb, yb, yb + 0.07], color=color, lw=1.3, zorder=3,
            solid_joinstyle="miter")
    label(ax, (a + b) / 2, yb - 0.22, text, fs=12)


rows = [  # (y, 이름, 설명, 먼저 변수, 나중 변수)
    (2.35, "순서 A", "bmi 먼저", ("bmi", C_BMI, OWN_BMI), ("pop", C_POP, OWN_POP)),
    (0.95, "순서 B", "pop 먼저", ("pop", C_POP, OWN_POP), ("bmi", C_BMI, OWN_BMI)),
]

for y, name, sub, (n1, c1, own1), (n2, c2, own2) in rows:
    label(ax, 0.15, y + bh / 2 + 0.13, name, fs=12.5, w="bold", ha="left")
    label(ax, 0.15, y + bh / 2 - 0.16, sub, fs=11, c=TEXT2, ha="left")
    x = x0
    # 먼저 들어간 변수: 자기 몫 + 겹치는 부분(같은 색의 옅은 단색)
    seg(x, y, own1, c1, n1)
    seg(x + own1, y, SHARED, mix(c1, 0.4), "겹치는 부분", tc=shade(c1, 0.25), fs=11)
    first_w = own1 + SHARED
    bracket(x, first_w, y, rf"$SSReg(\mathrm{{{n1}}})$", c1)
    x += first_w
    # 나중 변수: 자기 몫만
    seg(x, y, own2, c2, n2)
    bracket(x, own2, y, rf"$SSReg(\mathrm{{{n2}}}\mid\mathrm{{{n1}}})$", c2)
    x += own2
    # 나머지 변수
    seg(x, y, REST, NEUTRAL, "나머지 변수", tc=TEXT, fs=11, bold=False)

# 전체 SSReg가 같음
for xx in (x0, x1):
    ax.plot([xx, xx], [0.95, 3.27], color=TEXT2, lw=1, ls="--", zorder=1)
ax.add_patch(mp.FancyArrowPatch((x0, 3.27), (x1, 3.27), arrowstyle="<|-|>", mutation_scale=11,
                                color=TEXT2, lw=1.2, shrinkA=0, shrinkB=0, zorder=3))
box(ax, (x0 + x1) / 2 - 1.85, 3.1, 3.7, 0.34, fc="white", ec="none", z=3)
label(ax, (x0 + x1) / 2, 3.27, r"$SSReg(X_1,\ldots,X_p)$" + " — 두 순서에서 같음", fs=12)

save(fig, "assets/img/ch07/sequential_ss.png")