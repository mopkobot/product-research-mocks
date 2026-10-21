"""Build wireframe mocks as SVG + PNG.

Run: python3 docs/mocks/build.py
PNG output: docs/mocks/png/issue-<n>-<slug>.png at 1.5x.
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import screens_a
import screens_b
import screens_c

SCREENS = [
    (2, "dashboard", screens_a.s002),
    (3, "accounts", screens_a.s003),
    (4, "real-assets-debts", screens_a.s004),
    (5, "net-worth-progress", screens_a.s005),
    (6, "plan-shell", screens_a.s006),
    (9, "other-income", screens_a.s009),
    (11, "typed-expenses", screens_a.s011),
    (13, "flows", screens_a.s013),
    (16, "debt-payoff", screens_a.s016),
    (17, "core-milestones", screens_a.s017),
    (18, "milestone-criteria", screens_a.s018),
    (19, "projection", screens_a.s019),
    (20, "yearly-summary", screens_a.s020),
    (21, "drawdown", screens_a.s021),
    (25, "rmd-roth", screens_b.s025),
    (26, "monte-carlo", screens_b.s026),
    (35, "country-relocation", screens_b.s035),
    (36, "multiple-plans", screens_b.s036),
    (37, "compare-what-if", screens_b.s037),
    (38, "tax-composition", screens_b.s038),
    (39, "tax-brackets", screens_b.s039),
    (43, "gain-harvesting", screens_b.s043),
    (44, "optimizer-engine", screens_b.s044),
    (45, "optimizer-ui", screens_b.s045),
    (46, "estate", screens_b.s046),
    (49, "aca-subsidy", screens_c.s049),
    (51, "decision-variables", screens_c.s051),
    (52, "asset-allocation", screens_c.s052),
    (53, "multi-currency", screens_c.s053),
    (55, "snapshots", screens_c.s055),
    (56, "expense-itemizer", screens_c.s056),
    (58, "variable-rate-loans", screens_c.s058),
    (60, "private-equity", screens_c.s060),
    (61, "mortality", screens_c.s061),
    (62, "safe-to-share", screens_c.s062),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    svg_dir = os.path.join(root, "svg")
    png_dir = os.path.join(root, "png")
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(png_dir, exist_ok=True)
    only = sys.argv[1:] and {int(a) for a in sys.argv[1:]}
    for number, slug, fn in SCREENS:
        if only and number not in only:
            continue
        page = fn()
        base = f"issue-{number:03d}-{slug}"
        svg_path = os.path.join(svg_dir, base + ".svg")
        png_path = os.path.join(png_dir, base + ".png")
        with open(svg_path, "w", encoding="utf-8") as handle:
            handle.write(page.svg())
        subprocess.run(["rsvg-convert", "-z", "1.5", svg_path, "-o", png_path], check=True)
        print(f"{base}  {os.path.getsize(png_path) // 1024} KB  h={page.total_h}")


if __name__ == "__main__":
    main()
