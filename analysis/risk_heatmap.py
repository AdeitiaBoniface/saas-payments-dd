"""
risk_heatmap.py
---------------
Generates an investor-ready risk heatmap for the Cross-Border Payments SaaS
M&A due diligence engagement.

Usage:
    python analysis/risk_heatmap.py

Output:
    assets/risk_heatmap_output.png

Part of: saas-payments-dd
Author:  Adeitia K. Boniface — github.com/AdeitiaBoniface
"""

import json
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np

# ── Config ────────────────────────────────────────────────────────────────────

DATA_PATH   = os.path.join(os.path.dirname(__file__), "risk_data.json")
OUTPUT_DIR  = os.path.join(os.path.dirname(__file__), "..", "assets")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "risk_heatmap_output.png")

# Palette
BG          = "#0a0a0f"
SURFACE     = "#111118"
BORDER      = "#2e2e3e"
TEXT_MAIN   = "#e8e8f0"
TEXT_MUTED  = "#6b6b80"
GOLD        = "#c9a84c"
TEAL        = "#2dd4bf"
ROSE        = "#fb7185"

RAG_COLORS  = {
    "green":  "#2dd4bf",
    "amber":  "#c9a84c",
    "red":    "#fb7185",
}

# ── Load data ─────────────────────────────────────────────────────────────────

with open(DATA_PATH) as f:
    data = json.load(f)

engagement   = data["engagement"]
dimensions   = data["dimensions"]
deal_conds   = data["deal_conditions"]

# ── Layout ────────────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 10), facecolor=BG)
gs  = GridSpec(2, 2, figure=fig,
               left=0.05, right=0.97,
               top=0.88,  bottom=0.06,
               hspace=0.45, wspace=0.25)

ax_radar  = fig.add_subplot(gs[0, 0], polar=True)
ax_bar    = fig.add_subplot(gs[0, 1])
ax_conds  = fig.add_subplot(gs[1, 0])
ax_heat   = fig.add_subplot(gs[1, 1])

for ax in [ax_bar, ax_conds, ax_heat]:
    ax.set_facecolor(SURFACE)
    for spine in ax.spines.values():
        spine.set_edgecolor(BORDER)

ax_radar.set_facecolor(SURFACE)

# ── Title block ───────────────────────────────────────────────────────────────

fig.text(0.05, 0.96,
         "M&A TECHNOLOGY DUE DILIGENCE  ·  RISK ASSESSMENT REPORT",
         color=TEXT_MUTED, fontsize=8, fontfamily="monospace")

fig.text(0.05, 0.927,
         engagement["title"],
         color=TEXT_MAIN, fontsize=15, fontweight="bold")

meta = (f"Deal: {engagement['deal_size']}  ·  "
        f"Stage: {engagement['stage']}  ·  "
        f"Geo: {engagement['geography']}  ·  "
        f"Duration: {engagement['engagement_weeks']} weeks")
fig.text(0.05, 0.900, meta,
         color=TEXT_MUTED, fontsize=8, fontfamily="monospace")

fig.text(0.97, 0.900,
         "Adeitia K. Boniface  ·  github.com/AdeitiaBoniface",
         color=TEXT_MUTED, fontsize=7, fontfamily="monospace", ha="right")

# Divider
fig.add_artist(plt.Line2D([0.04, 0.97], [0.892, 0.892],
                           transform=fig.transFigure,
                           color=BORDER, linewidth=0.8))

# ── 1. Radar chart ────────────────────────────────────────────────────────────

labels   = [d["label"] for d in dimensions]
scores   = [d["score"] for d in dimensions]
n        = len(labels)
angles   = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
scores_c = scores + scores[:1]
angles_c = angles + angles[:1]

# Grid rings
for r in [1, 2, 3, 4, 5]:
    ax_radar.plot(angles_c, [r] * (n + 1),
                  color=BORDER, linewidth=0.5, linestyle="--", alpha=0.6)

ax_radar.plot(angles_c, scores_c, color=GOLD, linewidth=1.8)
ax_radar.fill(angles_c, scores_c, color=GOLD, alpha=0.12)

ax_radar.set_xticks(angles)
ax_radar.set_xticklabels(labels, color=TEXT_MUTED, fontsize=7,
                          fontfamily="monospace")
ax_radar.set_yticks([1, 2, 3, 4, 5])
ax_radar.set_yticklabels(["1", "2", "3", "4", "5"],
                          color=TEXT_MUTED, fontsize=6)
ax_radar.set_ylim(0, 5)
ax_radar.grid(color=BORDER, linewidth=0.4)
ax_radar.spines["polar"].set_color(BORDER)
ax_radar.set_title("Overall Risk Profile", color=TEXT_MAIN,
                    fontsize=9, pad=16, fontfamily="monospace")

# ── 2. Score bar chart ────────────────────────────────────────────────────────

bar_labels  = [d["label"].replace("\n", " ") for d in dimensions]
bar_scores  = [d["score"] for d in dimensions]
bar_colors  = [RAG_COLORS[d["rag"]] for d in dimensions]
y_pos       = np.arange(len(bar_labels))

bars = ax_bar.barh(y_pos, bar_scores, color=bar_colors, alpha=0.85,
                   height=0.55)

# Max score ghost bars
ax_bar.barh(y_pos, [5.0] * len(bar_labels),
            color=BORDER, alpha=0.35, height=0.55)

# Score labels
for bar, score in zip(bars, bar_scores):
    ax_bar.text(score + 0.08, bar.get_y() + bar.get_height() / 2,
                f"{score:.1f}",
                va="center", color=TEXT_MAIN,
                fontsize=8, fontfamily="monospace")

ax_bar.set_yticks(y_pos)
ax_bar.set_yticklabels(bar_labels, color=TEXT_MUTED,
                        fontsize=7.5, fontfamily="monospace")
ax_bar.set_xlim(0, 5.8)
ax_bar.set_xlabel("Score (out of 5.0)", color=TEXT_MUTED,
                   fontsize=7, fontfamily="monospace")
ax_bar.tick_params(colors=TEXT_MUTED)
ax_bar.set_title("Dimension Scores", color=TEXT_MAIN,
                  fontsize=9, fontfamily="monospace")

# Legend
legend_handles = [
    mpatches.Patch(color=RAG_COLORS["green"],  label="Green — Low risk"),
    mpatches.Patch(color=RAG_COLORS["amber"],  label="Amber — Moderate risk"),
    mpatches.Patch(color=RAG_COLORS["red"],    label="Red   — High risk"),
]
ax_bar.legend(handles=legend_handles, loc="lower right",
              fontsize=7, facecolor=BG, labelcolor=TEXT_MUTED,
              framealpha=0.8, edgecolor=BORDER)

# ── 3. Deal conditions table ──────────────────────────────────────────────────

ax_conds.axis("off")
ax_conds.set_title("Deal Conditions", color=TEXT_MAIN,
                    fontsize=9, fontfamily="monospace", pad=12)

status_color = {"agreed": GOLD, "satisfied": TEAL, "open": ROSE}
status_icon  = {"agreed": "◆ Agreed", "satisfied": "✓ Satisfied", "open": "⚠ Open"}

col_x = [0.04, 0.14, 0.72]
headers = ["ID", "Condition", "Status"]

for i, (x, h) in enumerate(zip(col_x, headers)):
    ax_conds.text(x, 0.92, h, transform=ax_conds.transAxes,
                  color=TEXT_MUTED, fontsize=7.5, fontfamily="monospace",
                  fontweight="bold")

ax_conds.axhline(y=0.88, xmin=0.02, xmax=0.98, color=BORDER, linewidth=0.6)

for i, cond in enumerate(deal_conds):
    y = 0.78 - i * 0.18
    ax_conds.text(col_x[0], y, cond["id"],
                  transform=ax_conds.transAxes,
                  color=GOLD, fontsize=7, fontfamily="monospace")
    ax_conds.text(col_x[1], y, cond["description"],
                  transform=ax_conds.transAxes,
                  color=TEXT_MUTED, fontsize=7, fontfamily="monospace",
                  wrap=True)
    sc = cond["status"]
    ax_conds.text(col_x[2], y, status_icon.get(sc, sc),
                  transform=ax_conds.transAxes,
                  color=status_color.get(sc, TEXT_MUTED),
                  fontsize=7, fontfamily="monospace")

# ── 4. RAG summary heatmap grid ───────────────────────────────────────────────

ax_heat.axis("off")
ax_heat.set_title("Risk Summary Heatmap", color=TEXT_MAIN,
                   fontsize=9, fontfamily="monospace", pad=12)

cell_w, cell_h = 0.44, 0.38
positions = [(0.04, 0.54), (0.52, 0.54),
             (0.04, 0.12), (0.52, 0.12),
             (0.04, -0.30),(0.52, -0.30)]

for d, (x, y) in zip(dimensions, positions):
    c   = RAG_COLORS[d["rag"]]
    rect = mpatches.FancyBboxPatch(
        (x, y), cell_w, cell_h,
        boxstyle="round,pad=0.02",
        facecolor=c + "18", edgecolor=c, linewidth=1,
        transform=ax_heat.transAxes, clip_on=False
    )
    ax_heat.add_patch(rect)

    label_clean = d["label"].replace("\n", " ")
    ax_heat.text(x + 0.02, y + cell_h - 0.04, label_clean,
                 transform=ax_heat.transAxes,
                 color=c, fontsize=7.5, fontfamily="monospace",
                 fontweight="bold", clip_on=False)

    ax_heat.text(x + 0.02, y + cell_h - 0.15,
                 f"Score: {d['score']:.1f} / 5.0",
                 transform=ax_heat.transAxes,
                 color=TEXT_MUTED, fontsize=6.5, fontfamily="monospace",
                 clip_on=False)

    # Wrap summary text
    words  = d["summary"].split()
    line, lines_out = "", []
    for w in words:
        if len(line) + len(w) + 1 > 32:
            lines_out.append(line.strip())
            line = w + " "
        else:
            line += w + " "
    if line:
        lines_out.append(line.strip())

    for li, ln in enumerate(lines_out[:2]):
        ax_heat.text(x + 0.02, y + 0.04 + (1 - li) * 0.08, ln,
                     transform=ax_heat.transAxes,
                     color=TEXT_MUTED, fontsize=6, fontfamily="monospace",
                     clip_on=False)

# ── Save ──────────────────────────────────────────────────────────────────────

os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.savefig(OUTPUT_FILE, dpi=180, bbox_inches="tight",
            facecolor=BG, edgecolor="none")
print(f"✅  Risk heatmap saved → {OUTPUT_FILE}")
plt.close()
