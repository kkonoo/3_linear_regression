"""5-II §1.2 왜 L1은 0을 만들고 L2는 못 만드는가 — 제약영역과 SSE 등고선 (설명용).

R 청크 l1-l2-geometry(제약영역 모양만 그림)를 다시 그림. 본문이 말하는
"SSE의 등고선(타원)이 제약영역에 처음 닿는 점이 해"를 그림에 넣었다.
"""
import numpy as np
from medfig import *

plt.rcParams["mathtext.fontset"] = "dejavusans"

B_HAT = np.array([1.3, 0.3])              # 최소제곱 해 (가상)
A = np.array([[1.0, 0.6], [0.6, 1.0]])    # SSE 이차형식 (가상)
T = 1.0                                    # 제약 크기


def sse(b):
    d = b - B_HAT
    return np.einsum("...i,ij,...j->...", d, A, d)


def solve(boundary):
    """경계 위에서 SSE가 가장 작은 점 = 등고선이 처음 닿는 점."""
    s = sse(boundary)
    return boundary[np.argmin(s)]


th = np.linspace(0, 2 * np.pi, 4001)
circle = np.c_[np.cos(th), np.sin(th)] * T
u = np.linspace(-1, 1, 2001)
diamond = np.r_[np.c_[u, T - abs(u)], np.c_[u, -(T - abs(u))]]

fig, axs = plt.subplots(1, 2, figsize=(8.2, 3.6))
fig.subplots_adjust(wspace=0.18)
gx, gy = np.meshgrid(np.linspace(-1.4, 2.4, 400), np.linspace(-1.3, 1.9, 400))
G = sse(np.dstack([gx, gy]))

for ax, (name, region, fill) in zip(
        axs, [("① L2 (ridge) — 원", circle, CAT[0]), ("② L1 (lasso) — 마름모", diamond, CAT[1])]):
    sol = solve(region)
    level = sse(sol)
    ax.axhline(0, color=LINE, lw=1, zorder=0)
    ax.axvline(0, color=LINE, lw=1, zorder=0)
    if region is circle:
        ax.add_patch(plt.Circle((0, 0), T, fc=mix(fill, 0.18), ec=fill, lw=2, zorder=1))
    else:
        ax.add_patch(plt.Polygon([(T, 0), (0, T), (-T, 0), (0, -T)], closed=True,
                                 fc=mix(fill, 0.18), ec=fill, lw=2, zorder=1))
    # 등고선: 해에서 닿는 것(진하게) + 바깥 둘(옅게)
    ax.contour(gx, gy, G, levels=[level * 0.25, level * 0.6], colors=[TEXT2], linewidths=1,
               linestyles="--", zorder=2)
    ax.contour(gx, gy, G, levels=[level], colors=[TEXT], linewidths=1.6, zorder=2)
    ax.plot(*B_HAT, "o", ms=7, color=TEXT, zorder=4)
    ax.annotate("최소제곱 해", B_HAT, xytext=(B_HAT[0] + 0.35, B_HAT[1] + 0.95), fontsize=11,
                color=TEXT, ha="center", arrowprops=dict(arrowstyle="-", color=TEXT2, lw=1))
    on_axis = abs(sol[0]) < 1e-3 or abs(sol[1]) < 1e-3
    ax.plot(*sol, "o", ms=10, color=ACCENT if on_axis else fill, mec="white", mew=1.5, zorder=5)
    if on_axis:
        ax.annotate("해: β₂ = 0", sol, xytext=(sol[0] + 0.15, sol[1] - 0.85), fontsize=12,
                    fontweight="bold", color=ACCENT_INK,
                    arrowprops=dict(arrowstyle="-", color=ACCENT_INK, lw=1.2))
    else:
        ax.annotate("해: β₁, β₂ ≠ 0", sol, xytext=(-1.3, 1.35),
                    fontsize=11, color=TEXT,
                    arrowprops=dict(arrowstyle="-", color=TEXT2, lw=1))
    ax.text(-1.3, -1.2, "제약영역", fontsize=11, color=fill, fontweight="bold")
    ax.set_xlim(-1.4, 2.4); ax.set_ylim(-1.3, 1.9); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    ax.spines[["left", "bottom"]].set_visible(False)
    ax.text(2.35, -0.1, r"$\beta_1$", fontsize=13, ha="right", va="top", color=TEXT)
    ax.text(0.08, 1.88, r"$\beta_2$", fontsize=13, ha="left", va="top", color=TEXT)
    ax.set_title(name, fontsize=12, fontweight="bold", color=TEXT, loc="left", pad=6)

save(fig, "assets/img/ch16/l1_l2_geometry.png")
