"""
Generate YouTube video thumbnails for each chapter of
"Inference and Intervention" -- one PNG per chapter.

Output: youtube-thumbnails/intro-thumbnail.png, ch01-thumbnail.png ... ch10-thumbnail.png
Style: clean, professional, dark blue background, BKA brand colours.
Size:  1280 x 720 px (YouTube standard).
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# -- Shared constants --------------------------------------------------------

OUT_DIR = os.path.join(os.path.dirname(__file__), "youtube-thumbnails")
THUMB_W = 1280
THUMB_H = 720
DPI = 144
FIG_W = THUMB_W / DPI   # ~8.889
FIG_H = THUMB_H / DPI   # 5.0

# BKA brand colours
BLUE    = "#005CB9"
LBLUE   = "#00A1DF"
GREEN   = "#83BD00"
TEAL    = "#3E9B6E"
RED     = "#E24A3F"
ORANGE  = "#FA7650"
AMBER   = "#F8A623"
YELLOW  = "#FED141"
DARK    = "#333333"
GRAY    = "#888888"
LGRAY   = "#CCCCCC"
WHITE   = "#FFFFFF"

# Darker shade for background gradient
DBLUE   = "#003D7A"


# -- Helpers ------------------------------------------------------------------

def new_thumb(accent_color=BLUE):
    """Create a thumbnail figure with dark blue background and branding."""
    fig = plt.figure(figsize=(FIG_W, FIG_H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor(DBLUE)
    ax.set_facecolor(DBLUE)

    # Gradient overlay: lighter on left, darker on right
    gradient = np.ones((2, 256, 4))
    # Start with BLUE, fade to DBLUE
    r_b, g_b, b_b = int(BLUE[1:3], 16)/255, int(BLUE[3:5], 16)/255, int(BLUE[5:7], 16)/255
    r_d, g_d, b_d = int(DBLUE[1:3], 16)/255, int(DBLUE[3:5], 16)/255, int(DBLUE[5:7], 16)/255
    for i in range(256):
        t = i / 255
        gradient[:, i, 0] = r_b * (1 - t) + r_d * t
        gradient[:, i, 1] = g_b * (1 - t) + g_d * t
        gradient[:, i, 2] = b_b * (1 - t) + b_d * t
        gradient[:, i, 3] = 1.0
    ax.imshow(gradient, aspect="auto", extent=[0, 10, 0, 5.6], zorder=0)

    # Left accent bar
    left_bar = FancyBboxPatch((0, 0), 0.12, 5.6,
                               boxstyle="square", facecolor=accent_color,
                               edgecolor="none", zorder=2)
    ax.add_patch(left_bar)

    # Bottom strip
    strip = FancyBboxPatch((0, 0), 10, 0.55,
                            boxstyle="square", facecolor=accent_color,
                            edgecolor="none", alpha=0.85, zorder=2)
    ax.add_patch(strip)

    # Course name (bottom left)
    ax.text(0.4, 0.27, "INFERENCE & INTERVENTION",
            ha="left", va="center", fontsize=9, fontweight="bold",
            color=WHITE, fontfamily="sans-serif", zorder=3)

    # BK ADVISORS branding (bottom right)
    ax.text(9.6, 0.27, "BK ADVISORS",
            ha="right", va="center", fontsize=9, fontweight="bold",
            color=WHITE, fontfamily="sans-serif", zorder=3)

    return fig, ax


def add_chapter_text(ax, ch_num, title_lines, subtitle="", accent_color=BLUE):
    """Add left-side text block: chapter number + title + subtitle."""
    if ch_num is not None:
        num_text = f"CH {ch_num:02d}" if isinstance(ch_num, int) else str(ch_num)
        ax.text(0.5, 4.9, num_text, ha="left", va="top",
                fontsize=44, fontweight="bold", color=accent_color,
                fontfamily="sans-serif", zorder=5)

    title_y = 3.9 if ch_num is not None else 4.5
    for i, line in enumerate(title_lines):
        ax.text(0.5, title_y - i * 0.6, line.upper(),
                ha="left", va="top", fontsize=26, fontweight="bold",
                color=WHITE, fontfamily="sans-serif", zorder=5)

    if subtitle:
        sub_y = title_y - len(title_lines) * 0.6 - 0.15
        ax.text(0.5, sub_y, subtitle,
                ha="left", va="top", fontsize=13,
                color=LGRAY, fontfamily="sans-serif", zorder=5)


def arrow(ax, x1, y1, x2, y2, color=WHITE, lw=2.5, style="-|>"):
    """Draw an arrow between two points."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw),
                zorder=4)


def dag_node(ax, x, y, label, color=WHITE, r=0.35, fontsize=10, textcolor=None):
    """Draw a circular DAG node."""
    c = Circle((x, y), r, fill=True, facecolor=color, edgecolor=WHITE,
               linewidth=2, alpha=0.2, zorder=4)
    ax.add_patch(c)
    c2 = Circle((x, y), r, fill=False, edgecolor=color, linewidth=2.5, zorder=4)
    ax.add_patch(c2)
    ax.text(x, y, label, ha="center", va="center",
            fontsize=fontsize, fontweight="bold",
            color=textcolor or WHITE, fontfamily="sans-serif", zorder=5)


def rounded_box(ax, x, y, w, h, text, fc="white", ec=BLUE, lw=2,
                fontsize=11, textcolor=DARK, alpha=1.0):
    """Draw a rounded rectangle with centred text."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.12", facecolor=fc,
                         edgecolor=ec, linewidth=lw, alpha=alpha, zorder=4)
    ax.add_patch(box)
    if text:
        ax.text(x, y, text, ha="center", va="center",
                fontsize=fontsize, fontweight="bold", color=textcolor,
                fontfamily="sans-serif", zorder=5)


def save_thumb(fig, name):
    """Save thumbnail at exact 1280x720."""
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=DPI, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"  Saved {name}")


# == INTRO ====================================================================

def draw_thumb_intro():
    fig, ax = new_thumb(accent_color=LBLUE)

    # Title (centred, no chapter number)
    ax.text(5, 4.8, "INFERENCE &", ha="center", va="top",
            fontsize=36, fontweight="bold", color=WHITE,
            fontfamily="sans-serif", zorder=5)
    ax.text(5, 4.1, "INTERVENTION", ha="center", va="top",
            fontsize=36, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif", zorder=5)
    ax.text(5, 3.4, "Causal Models for Health",
            ha="center", va="top", fontsize=14,
            color=LGRAY, fontfamily="sans-serif", zorder=5)

    # Four-phase flow across the bottom
    phases = [
        ("FOUNDATIONS", "Ch 1-3", LBLUE),
        ("QUANTIFY", "Ch 4-6", TEAL),
        ("DECIDE", "Ch 7-9", GREEN),
        ("DISCOVER", "Ch 10", AMBER),
    ]
    y = 1.8
    x_positions = [1.5, 3.8, 6.2, 8.5]
    bw, bh = 1.8, 1.0

    for i, ((label, sub, color), xp) in enumerate(zip(phases, x_positions)):
        rounded_box(ax, xp, y, bw, bh, "", fc=color, ec=WHITE, lw=2,
                    alpha=0.3)
        ax.text(xp, y + 0.12, label, ha="center", va="center",
                fontsize=11, fontweight="bold", color=WHITE,
                fontfamily="sans-serif", zorder=5)
        ax.text(xp, y - 0.25, sub, ha="center", va="center",
                fontsize=9, color=LGRAY, fontfamily="sans-serif", zorder=5)

        # Arrow to next phase
        if i < len(phases) - 1:
            nx = x_positions[i + 1]
            arrow(ax, xp + bw/2 + 0.05, y, nx - bw/2 - 0.05, y,
                  color=WHITE, lw=2.5)

    save_thumb(fig, "intro-thumbnail.png")


# == CHAPTER 1 ================================================================

def draw_thumb_ch01():
    fig, ax = new_thumb(accent_color=LBLUE)
    add_chapter_text(ax, 1, ["CAUSAL", "THINKING"], "The Ethiopia Paradox", LBLUE)

    # Visual: Correlation =/= Causation
    cx, cy = 7.8, 3.5

    ax.text(cx, cy + 1.2, "Correlation", ha="center", va="center",
            fontsize=16, fontweight="bold", color=LBLUE,
            fontfamily="sans-serif", zorder=5)

    # Big "not equal" symbol
    ax.text(cx, cy, "=/=", ha="center", va="center",
            fontsize=40, fontweight="bold", color=RED,
            fontfamily="sans-serif", zorder=5)

    ax.text(cx, cy - 1.2, "Causation", ha="center", va="center",
            fontsize=16, fontweight="bold", color=GREEN,
            fontfamily="sans-serif", zorder=5)

    # Question mark
    ax.text(cx + 1.3, cy + 0.8, "?", ha="center", va="center",
            fontsize=36, fontweight="bold", color=AMBER, alpha=0.6,
            fontfamily="sans-serif", zorder=4)

    save_thumb(fig, "ch01-thumbnail.png")


# == CHAPTER 2 ================================================================

def draw_thumb_ch02():
    fig, ax = new_thumb(accent_color=TEAL)
    add_chapter_text(ax, 2, ["DRAWING", "CAUSAL MODELS"], "Chains, Forks & Colliders", TEAL)

    # Visual: Three mini DAG triplets
    cx = 7.8
    r = 0.22
    gap = 1.1

    triplets = [
        {"label": "Chain", "y": 4.3, "color": LBLUE,
         "nodes": [(cx - 0.8, 0), (cx, 0), (cx + 0.8, 0)],
         "arrows": [(0, 1), (1, 2)]},
        {"label": "Fork", "y": 3.0, "color": TEAL,
         "nodes": [(cx - 0.8, 0), (cx, 0), (cx + 0.8, 0)],
         "arrows": [(1, 0), (1, 2)]},
        {"label": "Collider", "y": 1.7, "color": AMBER,
         "nodes": [(cx - 0.8, 0), (cx, 0), (cx + 0.8, 0)],
         "arrows": [(0, 1), (2, 1)]},
    ]

    for t in triplets:
        y = t["y"]
        col = t["color"]
        nodes_xy = [(nx, y) for nx, _ in t["nodes"]]

        # Label
        ax.text(cx - 1.5, y, t["label"], ha="right", va="center",
                fontsize=10, fontweight="bold", color=col,
                fontfamily="sans-serif", zorder=5)

        # Nodes
        labels = ["A", "B", "C"]
        for i, (nx, ny) in enumerate(nodes_xy):
            c = Circle((nx, ny), r, fill=True, facecolor=col,
                       edgecolor=WHITE, linewidth=1.5, alpha=0.3, zorder=4)
            ax.add_patch(c)
            c2 = Circle((nx, ny), r, fill=False, edgecolor=col,
                        linewidth=2, zorder=4)
            ax.add_patch(c2)
            ax.text(nx, ny, labels[i], ha="center", va="center",
                    fontsize=9, fontweight="bold", color=WHITE,
                    fontfamily="sans-serif", zorder=5)

        # Arrows
        for frm, to in t["arrows"]:
            x1, y1 = nodes_xy[frm]
            x2, y2 = nodes_xy[to]
            dx = x2 - x1
            dy = y2 - y1
            dist = np.sqrt(dx**2 + dy**2)
            x1s = x1 + (r + 0.05) * dx / dist
            x2s = x2 - (r + 0.05) * dx / dist
            arrow(ax, x1s, y1, x2s, y2, color=col, lw=2)

    save_thumb(fig, "ch02-thumbnail.png")


# == CHAPTER 3 ================================================================

def draw_thumb_ch03():
    fig, ax = new_thumb(accent_color=GREEN)
    add_chapter_text(ax, 3, ["THE DIAGNOSTIC", "CASE"], "Building Models from Interviews", GREEN)

    # Visual: Magnifying glass with DAG inside
    cx, cy = 7.6, 3.2
    lens_r = 1.2

    # Magnifying glass circle (lens)
    lens = Circle((cx, cy), lens_r, fill=True, facecolor=GREEN,
                  edgecolor=WHITE, linewidth=3, alpha=0.15, zorder=4)
    ax.add_patch(lens)
    lens_border = Circle((cx, cy), lens_r, fill=False,
                         edgecolor=GREEN, linewidth=3, zorder=4)
    ax.add_patch(lens_border)

    # Handle
    hx = cx + lens_r * 0.7
    hy = cy - lens_r * 0.7
    ax.plot([hx, hx + 0.8], [hy, hy - 0.8],
            color=GREEN, linewidth=5, solid_capstyle="round", zorder=4)

    # Mini DAG inside lens
    nr = 0.18
    nodes_inside = [
        (cx - 0.4, cy + 0.5, WHITE),
        (cx + 0.5, cy + 0.4, YELLOW),
        (cx, cy - 0.3, LBLUE),
        (cx - 0.5, cy - 0.1, WHITE),
    ]
    for nx, ny, nc in nodes_inside:
        c = Circle((nx, ny), nr, fill=True, facecolor=nc,
                   edgecolor=WHITE, linewidth=1.5, alpha=0.7, zorder=5)
        ax.add_patch(c)

    # Arrows inside lens
    mini_arrows = [(0, 2), (1, 2), (3, 2)]
    for frm, to in mini_arrows:
        x1, y1, _ = nodes_inside[frm]
        x2, y2, _ = nodes_inside[to]
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        arrow(ax, x1 + (nr + 0.03) * dx/dist, y1 + (nr + 0.03) * dy/dist,
              x2 - (nr + 0.03) * dx/dist, y2 - (nr + 0.03) * dy/dist,
              color=WHITE, lw=1.5)

    save_thumb(fig, "ch03-thumbnail.png")


# == CHAPTER 4 ================================================================

def draw_thumb_ch04():
    fig, ax = new_thumb(accent_color=LBLUE)
    add_chapter_text(ax, 4, ["ARROWS TO", "NUMBERS"], "Probability & Bayes' Rule", LBLUE)

    # Visual: DAG arrow with number label + lookup table
    cx, cy = 7.8, 3.8

    # Two nodes connected by arrow
    dag_node(ax, cx - 0.9, cy, "A", color=LBLUE, r=0.3, fontsize=11)
    dag_node(ax, cx + 0.9, cy, "B", color=LBLUE, r=0.3, fontsize=11)
    arrow(ax, cx - 0.55, cy, cx + 0.55, cy, color=LBLUE, lw=3)

    # Probability label on the arrow
    ax.text(cx, cy + 0.35, "55 out of 100", ha="center", va="bottom",
            fontsize=10, fontweight="bold", color=YELLOW,
            fontfamily="sans-serif", zorder=5)

    # Lookup table below
    ty = 2.0
    tw, th = 1.6, 0.8
    # Table outline
    ax.plot([cx - tw/2, cx + tw/2], [ty + th/2, ty + th/2],
            color=LGRAY, lw=1.5, zorder=4)
    ax.plot([cx - tw/2, cx + tw/2], [ty, ty],
            color=LGRAY, lw=1.5, zorder=4)
    ax.plot([cx - tw/2, cx + tw/2], [ty - th/2, ty - th/2],
            color=LGRAY, lw=1.5, zorder=4)
    ax.plot([cx, cx], [ty + th/2, ty - th/2],
            color=LGRAY, lw=1.5, zorder=4)
    ax.plot([cx - tw/2, cx - tw/2], [ty + th/2, ty - th/2],
            color=LGRAY, lw=1.5, zorder=4)
    ax.plot([cx + tw/2, cx + tw/2], [ty + th/2, ty - th/2],
            color=LGRAY, lw=1.5, zorder=4)

    # Table labels
    ax.text(cx - tw/4, ty + th/4, "Low", ha="center", va="center",
            fontsize=8, color=LGRAY, fontfamily="sans-serif", zorder=5)
    ax.text(cx + tw/4, ty + th/4, "High", ha="center", va="center",
            fontsize=8, color=LGRAY, fontfamily="sans-serif", zorder=5)
    ax.text(cx - tw/4, ty - th/4, "55", ha="center", va="center",
            fontsize=10, fontweight="bold", color=AMBER,
            fontfamily="sans-serif", zorder=5)
    ax.text(cx + tw/4, ty - th/4, "45", ha="center", va="center",
            fontsize=10, fontweight="bold", color=AMBER,
            fontfamily="sans-serif", zorder=5)

    ax.text(cx, ty - th/2 - 0.25, "Lookup Table", ha="center", va="top",
            fontsize=9, color=LGRAY, fontfamily="sans-serif", zorder=5)

    save_thumb(fig, "ch04-thumbnail.png")


# == CHAPTER 5 ================================================================

def draw_thumb_ch05():
    fig, ax = new_thumb(accent_color=ORANGE)
    add_chapter_text(ax, 5, ["SITUATIONAL", "ANALYSIS"], "Forward & Backward Reasoning", ORANGE)

    # Visual: Two big arrows (predict down, diagnose up)
    cx = 7.8

    # Predict arrow (down) - blue
    ax.annotate("", xy=(cx - 0.6, 1.5), xytext=(cx - 0.6, 4.8),
                arrowprops=dict(arrowstyle="-|>", color=LBLUE, lw=4),
                zorder=4)
    ax.text(cx - 1.1, 3.2, "PREDICT", ha="center", va="center",
            fontsize=11, fontweight="bold", color=LBLUE,
            fontfamily="sans-serif", rotation=90, zorder=5)

    # Diagnose arrow (up) - orange
    ax.annotate("", xy=(cx + 0.6, 4.8), xytext=(cx + 0.6, 1.5),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=4),
                zorder=4)
    ax.text(cx + 1.1, 3.2, "DIAGNOSE", ha="center", va="center",
            fontsize=11, fontweight="bold", color=ORANGE,
            fontfamily="sans-serif", rotation=270, zorder=5)

    # Small nodes between arrows
    for ny in [2.2, 3.2, 4.2]:
        c = Circle((cx, ny), 0.15, fill=True, facecolor=WHITE,
                   edgecolor=WHITE, linewidth=1.5, alpha=0.3, zorder=4)
        ax.add_patch(c)

    save_thumb(fig, "ch05-thumbnail.png")


# == CHAPTER 6 ================================================================

def draw_thumb_ch06():
    fig, ax = new_thumb(accent_color=RED)
    add_chapter_text(ax, 6, ["SIMPSON'S", "PARADOX"], "When Combined Data Misleads", RED)

    # Visual: Crossing trend lines
    cx = 7.5
    x_range = np.linspace(cx - 1.3, cx + 1.3, 50)

    # "Each group" lines going UP (green)
    for offset in [0.5, -0.5]:
        y_up = 2.5 + offset + 0.6 * (x_range - cx + 1.3) / 2.6
        ax.plot(x_range, y_up, color=GREEN, lw=3, alpha=0.7, zorder=4)

    # "Combined" line going DOWN (red)
    y_down = 3.8 - 0.8 * (x_range - cx + 1.3) / 2.6
    ax.plot(x_range, y_down, color=RED, lw=3.5, zorder=4)

    # Labels (positioned inside the chart area)
    ax.text(cx + 1.0, 4.2, "Each group", ha="center", va="center",
            fontsize=9, fontweight="bold", color=GREEN,
            fontfamily="sans-serif", zorder=5)
    ax.text(cx + 1.0, 1.8, "Combined", ha="center", va="center",
            fontsize=9, fontweight="bold", color=RED,
            fontfamily="sans-serif", zorder=5)

    # Big question mark at intersection
    ax.text(cx, 3.15, "?!", ha="center", va="center",
            fontsize=36, fontweight="bold", color=YELLOW, alpha=0.8,
            fontfamily="sans-serif", zorder=5)

    save_thumb(fig, "ch06-thumbnail.png")


# == CHAPTER 7 ================================================================

def draw_thumb_ch07():
    fig, ax = new_thumb(accent_color=AMBER)
    add_chapter_text(ax, 7, ["WATCHING", "VS DOING"], "Graph Surgery", AMBER)

    # Visual: Scissors cutting a DAG arrow
    cx, cy = 7.8, 3.2

    # Three DAG nodes
    n1x, n2x, n3x = cx - 1.2, cx, cx + 1.2
    nr = 0.28

    dag_node(ax, n1x, cy + 0.8, "A", color=AMBER, r=nr, fontsize=11)
    dag_node(ax, n2x, cy + 0.8, "B", color=AMBER, r=nr, fontsize=11)
    dag_node(ax, n3x, cy + 0.8, "C", color=AMBER, r=nr, fontsize=11)

    # Arrow A->B (being cut - dashed red)
    ax.plot([n1x + nr + 0.05, n2x - nr - 0.05],
            [cy + 0.8, cy + 0.8],
            color=RED, lw=2.5, linestyle="--", alpha=0.7, zorder=4)

    # Arrow B->C (intact)
    arrow(ax, n2x + nr + 0.05, cy + 0.8, n3x - nr - 0.05, cy + 0.8,
          color=AMBER, lw=2.5)

    # Scissors (two lines crossing as X)
    sx = (n1x + n2x) / 2
    sy = cy + 0.8
    scissors_len = 0.4
    ax.plot([sx - scissors_len, sx + scissors_len],
            [sy - scissors_len, sy + scissors_len],
            color=RED, lw=3.5, solid_capstyle="round", zorder=5)
    ax.plot([sx - scissors_len, sx + scissors_len],
            [sy + scissors_len, sy - scissors_len],
            color=RED, lw=3.5, solid_capstyle="round", zorder=5)

    # Labels below
    ax.text(cx - 0.5, cy - 0.5, "WATCH", ha="center", va="center",
            fontsize=12, fontweight="bold", color=LBLUE,
            fontfamily="sans-serif", zorder=5)
    ax.text(cx + 0.9, cy - 0.5, "DO", ha="center", va="center",
            fontsize=12, fontweight="bold", color=AMBER,
            fontfamily="sans-serif", zorder=5)

    # Arrow between watch and do
    ax.annotate("", xy=(cx + 0.4, cy - 0.5), xytext=(cx + 0.05, cy - 0.5),
                arrowprops=dict(arrowstyle="-|>", color=WHITE, lw=2),
                zorder=4)

    save_thumb(fig, "ch07-thumbnail.png")


# == CHAPTER 8 ================================================================

def draw_thumb_ch08():
    fig, ax = new_thumb(accent_color=TEAL)
    add_chapter_text(ax, 8, ["RESOURCE", "ALLOCATION"], "Four Countries, One Budget", TEAL)

    # Visual: Central budget circle with 4 country circles
    cx, cy = 7.8, 3.0

    # Central budget circle
    budget = Circle((cx, cy), 0.5, fill=True, facecolor=TEAL,
                    edgecolor=WHITE, linewidth=2.5, alpha=0.5, zorder=4)
    ax.add_patch(budget)
    ax.text(cx, cy, "BUDGET", ha="center", va="center",
            fontsize=8, fontweight="bold", color=WHITE,
            fontfamily="sans-serif", zorder=5)

    # Country circles
    countries = [
        (cx - 1.3, cy + 1.2, "ET", LBLUE, 0.35),
        (cx + 1.3, cy + 1.2, "RW", GREEN, 0.30),
        (cx - 1.3, cy - 1.2, "KE", AMBER, 0.32),
        (cx + 1.3, cy - 1.2, "TZ", TEAL, 0.33),
    ]

    for ccx, ccy, label, color, r in countries:
        c = Circle((ccx, ccy), r, fill=True, facecolor=color,
                   edgecolor=WHITE, linewidth=2, alpha=0.4, zorder=4)
        ax.add_patch(c)
        c2 = Circle((ccx, ccy), r, fill=False,
                    edgecolor=color, linewidth=2.5, zorder=4)
        ax.add_patch(c2)
        ax.text(ccx, ccy, label, ha="center", va="center",
                fontsize=10, fontweight="bold", color=WHITE,
                fontfamily="sans-serif", zorder=5)

        # Arrow from budget to country
        dx = ccx - cx
        dy = ccy - cy
        dist = np.sqrt(dx**2 + dy**2)
        arrow(ax, cx + 0.55 * dx/dist, cy + 0.55 * dy/dist,
              ccx - (r + 0.05) * dx/dist, ccy - (r + 0.05) * dy/dist,
              color=color, lw=2)

    save_thumb(fig, "ch08-thumbnail.png")


# == CHAPTER 9 ================================================================

def draw_thumb_ch09():
    fig, ax = new_thumb(accent_color=GREEN)
    add_chapter_text(ax, 9, ["GAME", "THEORY"], "The Free-Rider Trap", GREEN)

    # Visual: Simplified 2x2 payoff grid
    cx, cy = 7.8, 3.0
    cw, ch = 1.2, 0.9

    # Grid lines
    for i in range(3):
        ax.plot([cx - cw, cx + cw], [cy - ch + i * ch, cy - ch + i * ch],
                color=LGRAY, lw=1.5, alpha=0.6, zorder=4)
    for j in range(3):
        ax.plot([cx - cw + j * cw, cx - cw + j * cw], [cy - ch, cy + ch],
                color=LGRAY, lw=1.5, alpha=0.6, zorder=4)

    # Cell fills
    cells = [
        (-0.5, 0.5, GREEN, 0.3),   # top-left: cooperate-cooperate (good)
        (0.5, 0.5, RED, 0.25),     # top-right: cooperate-freeride (trap!)
        (-0.5, -0.5, LGRAY, 0.1),  # bottom-left
        (0.5, -0.5, LGRAY, 0.15),  # bottom-right
    ]
    for dx, dy, color, alpha in cells:
        rect = FancyBboxPatch((cx + dx * cw - cw/2 + 0.03,
                               cy + dy * ch - ch/2 + 0.03),
                              cw - 0.06, ch - 0.06,
                              boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor="none",
                              alpha=alpha, zorder=4)
        ax.add_patch(rect)

    # Cell labels
    ax.text(cx - cw/2, cy + ch/2, "WIN-\nWIN", ha="center", va="center",
            fontsize=9, fontweight="bold", color=GREEN,
            fontfamily="sans-serif", zorder=5)
    ax.text(cx + cw/2, cy + ch/2, "TRAP!", ha="center", va="center",
            fontsize=9, fontweight="bold", color=RED,
            fontfamily="sans-serif", zorder=5)

    # Axis labels
    ax.text(cx, cy + ch + 0.2, "Cooperate    Free-Ride", ha="center",
            va="center", fontsize=8, color=LGRAY,
            fontfamily="sans-serif", zorder=5)
    ax.text(cx - cw - 0.15, cy, "Player", ha="right", va="center",
            fontsize=8, color=LGRAY, fontfamily="sans-serif",
            rotation=90, zorder=5)

    # Nash equilibrium pointer
    ax.text(cx + cw/2, cy - ch/2, "NE", ha="center", va="center",
            fontsize=8, fontweight="bold", color=AMBER,
            fontfamily="sans-serif", zorder=5)

    save_thumb(fig, "ch09-thumbnail.png")


# == CHAPTER 10 ===============================================================

def draw_thumb_ch10():
    fig, ax = new_thumb(accent_color=AMBER)
    add_chapter_text(ax, 10, ["STRUCTURE", "LEARNING"], "Expert + Algorithm + Data", AMBER)

    # Visual: Triangle with 3 nodes + cycle arrows
    cx, cy = 7.8, 3.0
    r = 0.4
    # Triangle vertices
    top = (cx, cy + 1.3)
    bl = (cx - 1.1, cy - 0.7)
    br = (cx + 1.1, cy - 0.7)

    nodes = [
        (*top, "Expert", LBLUE),
        (*bl, "Algo", ORANGE),
        (*br, "Data", TEAL),
    ]

    for nx, ny, label, color in nodes:
        c = Circle((nx, ny), r, fill=True, facecolor=color,
                   edgecolor=WHITE, linewidth=2, alpha=0.3, zorder=4)
        ax.add_patch(c)
        c2 = Circle((nx, ny), r, fill=False,
                    edgecolor=color, linewidth=2.5, zorder=4)
        ax.add_patch(c2)
        ax.text(nx, ny, label, ha="center", va="center",
                fontsize=9, fontweight="bold", color=WHITE,
                fontfamily="sans-serif", zorder=5)

    # Cycle arrows
    edges = [(top, bl, LBLUE), (bl, br, ORANGE), (br, top, TEAL)]
    for (x1, y1), (x2, y2), ec in edges:
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)
        rr = r + 0.08
        arrow(ax, x1 + rr * dx/dist, y1 + rr * dy/dist,
              x2 - rr * dx/dist, y2 - rr * dy/dist,
              color=ec, lw=2.5)

    # Center label
    ax.text(cx, cy + 0.15, "DAG", ha="center", va="center",
            fontsize=11, fontweight="bold", color=AMBER,
            fontfamily="sans-serif", zorder=5)

    save_thumb(fig, "ch10-thumbnail.png")


# == MAIN =====================================================================

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Generating YouTube thumbnails to {OUT_DIR}")

    draw_thumb_intro()
    draw_thumb_ch01()
    draw_thumb_ch02()
    draw_thumb_ch03()
    draw_thumb_ch04()
    draw_thumb_ch05()
    draw_thumb_ch06()
    draw_thumb_ch07()
    draw_thumb_ch08()
    draw_thumb_ch09()
    draw_thumb_ch10()

    print("Done -- 11 thumbnails generated.")
