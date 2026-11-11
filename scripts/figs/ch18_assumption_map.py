"""Part 6 지도 — 선형회귀의 네 가정과, 각 가정이 깨질 때 쓰는 모형.

내용은 6-II §4 "언제 무엇을 쓸 것인가"의 '깨진 가정' 표와 같다.
나란한 네 가정 → CAT 색, 강조색 없음.
"""
from medfig import *

COLS = [  # 가정, [(모형, 조건, 예제·장)]
    ("선형성", [("비선형 회귀", "관계의 구조를 알 때", "NMR 스펙트럼 · 6-I"),
               ("GAM", "구조를 모를 때", "메틸화 ~ 나이·BMI · 6-I")]),
    ("등분산", [("WLS", "관측치마다 분산이 다를 때", "메틸화 coverage · 6-I")]),
    ("독립성", [("시계열 회귀", "시간으로 상관될 때", "CGM · 6-II"),
               ("공간 회귀", "공간으로 상관될 때", "Visium · 6-II"),
               ("혼합효과모형", "반복·군집으로 상관될 때", "가계 GWAS · 6-II")]),
    ("정규성", [("로버스트 회귀", "이상치·두꺼운 꼬리", "LDLR eQTL · 6-I")]),
]

W, H = 8.4, 5.2
fig, ax = new(W, H)
cw, gap = 1.9, 0.16
x0 = (W - (4 * cw + 3 * gap)) / 2
top = H + 0.25
for i, (assume, models) in enumerate(COLS):
    c = CAT[i]
    x = x0 + i * (cw + gap)
    # 가정 칸
    box(ax, x, top - 0.95, cw, 0.55, fc=c, ec="none", r=0.1)
    label(ax, x + cw / 2, top - 0.675, assume, fs=13, w="bold", c=on(c))
    # 깨지면 → 대안 모형들 (대안끼리는 순서가 없으므로 화살표 없이 쌓음)
    arrow(ax, x + cw / 2, top - 0.97, x + cw / 2, top - 1.37, color=mix(c, 0.7), lw=1.4, ms=10)
    label(ax, x + cw / 2 + 0.1, top - 1.17, "깨지면", fs=11, c=TEXT2, ha="left")
    y = top - 1.4
    for name, cond, ex in models:
        hgt = 1.0
        box(ax, x, y - hgt, cw, hgt, fc=mix(c, 0.10), ec=mix(c, 0.55), lw=1.1, r=0.08)
        label(ax, x + cw / 2, y - 0.24, name, fs=12.5, w="bold", c=shade(c, 0.1) if i != 3 else shade(c, 0.45))
        label(ax, x + cw / 2, y - 0.54, cond, fs=11, c=TEXT)
        label(ax, x + cw / 2, y - 0.8, ex, fs=11, c=TEXT2)
        y -= hgt + 0.14

save(fig, "assets/img/ch18/assumption_map.png")
