"""Wireframe screens, part 2 (issues 25-46)."""

from wirelib import (Page, txt, rrect, line, pill, btn, field, select, tabs, toggle,
                     table, kpi, line_chart, bars, donut, gauge, warn, empty, card, circle, polyline, para, stacked_bars,
                     INK, INK_SOFT, MUTED, FAINT, FAINT_FILL, FILL, SURFACE, BORDER, HAIR)

L, W = 272, 1136
LW, GAP, RW = 716, 20, 400


def s025():
    p = Page(25, "Strategy · RMD and Roth conversion", "Mandatory withdrawals and voluntary conversions.", "Strategy",
             crumb="Plans / Plan For Retirement / Strategy / Withdrawals", actions=["Run plan"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 244, "Required minimum distribution")
    p.add(pill(L + LW - 130, 200, "MANDATORY", fg=INK_SOFT)[0])
    for i, (lab, val) in enumerate([("IRA balance", "$1,000,000"), ("Owner age", "73"), ("Life-expectancy factor", "26.5"), ("RMD this year", "$37,736")]):
        p.add(txt(L + 18 + i * 172, iy + 14, lab.upper(), size=10, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(L + 18 + i * 172, iy + 42, val, size=17, weight=600, family="Menlo, monospace"))
    p.add(line(L + 18, iy + 64, L + LW - 18, iy + 64, stroke=HAIR))
    p.add(txt(L + 18, iy + 90, "The RMD is withdrawn before any discretionary drawdown in that year.", size=11.5, fill=MUTED))
    p.add(txt(L + 18, iy + 128, "Inherited IRA treatment", size=12, weight=600))
    for i, lab in enumerate(["10-year rule", "Stretch"]):
        p.add(rrect(L + 18 + i * 160, iy + 142, 148, 40, r=8, fill=INK if i == 0 else SURFACE, stroke=None if i == 0 else BORDER))
        p.add(txt(L + 18 + i * 160 + 74, iy + 167, lab, size=11.5, weight=600, anchor="middle", fill="#FFFFFF" if i == 0 else INK_SOFT))
    p.add(txt(L + 18, iy + 206, "Distributions follow the selected schedule for every inherited account.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 436, LW, 400, "Roth conversion")
    p.add(field(L + 18, iy2 + 6, 200, "Amount", "$50,000")[0])
    p.add(field(L + 18, iy2 + 78, 200, "Year", "2027")[0])
    p.add(select(L + 238, iy2 + 6, 236, "Target", "Fill 22% bracket")[0])
    p.add(toggle(L + 238, iy2 + 78, True, "Stop at bracket ceiling"))
    p.add(line(L + 18, iy2 + 128, L + LW - 18, iy2 + 128, stroke=HAIR))
    p.add(table(L + 18, iy2 + 148, LW - 36,
                [("Effect in 2027", 300), ("Baseline", 160), ("With conversion", 200)],
                [["Ordinary income", "$186,400", "$236,400"],
                 ["Federal tax", "$38,220", "$49,170"],
                 ["Roth balance (end)", "$138,500", "$188,500"],
                 ["IRA balance (end)", "$1,012,000", "$962,000"]], row_h=40)[0])
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Conversion effect")
    for i, (lab, val) in enumerate([("Ordinary income", "+ $50,000"), ("Roth balance", "+ $50,000"), ("Tax this year", "+ $10,950")]):
        y = iy3 + 10 + i * 56
        p.add(txt(x + 20, y + 14, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 14, val, size=13, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 32, x + RW - 18, y + 32, stroke=HAIR))
    p.add(txt(x + 18, iy3 + 208, "Tax impact lands in the conversion year.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "RMD by year")
    p.add(line_chart(x + 18, iy4 + 8, RW - 36, 190,
                     [{"name": "RMD", "values": [0, 0, 37.7, 41.2, 46.0, 52.1], "area": True}],
                     x_labels=["2029", "2032", "2035", "2038", "2041", "2044"], y_max=60, y_ticks=2))
    p.add(txt(x + 18, iy4 + 258, "Owners before RMD age show $0 and no RMD line.", size=11, fill=FAINT))
    p.markers([(1, L + 18, 216), (2, L + 18, 500), (3, x + 18, 216), (4, x + 18, 560)])
    return p.footer([
        (1, "RMD is computed from the applicable life-expectancy factor and is mandatory once the owner reaches RMD age."),
        (2, "A manual conversion raises taxable income in the conversion year and moves the same amount into the Roth balance."),
        (3, "The effect cards are the API's baseline and modified values, so the tax delta and the balance delta always agree."),
        (4, "Strategy-driven conversions ship later. This form is manual only, with an optional bracket ceiling."),
    ])


def s026():
    p = Page(26, "Monte Carlo", "Seeded trials with a chosen sampling method.", "Monte Carlo",
             crumb="Plans / Plan For Retirement / Monte Carlo", actions=["Run trials"], premium=True, frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 236, "Configuration")
    p.add(field(L + 18, iy + 6, 200, "Seed", "1234")[0])
    p.add(field(L + 18, iy + 72, 200, "Trials", "100")[0])
    p.add(select(L + 238, iy + 6, 460, "Sampling method", "Historical · random restart")[0])
    p.add(field(L + 238, iy + 72, 220, "Block length", "5", placeholder=True)[0])
    p.add(txt(L + 238 + 232, iy + 96, "Only used by block bootstrap", size=10.5, fill=FAINT))
    p.add(txt(L + 18, iy + 150, "The same seed and method must return the same success rate and the same percentiles.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 428, LW, 408, "Outcome distribution")
    p.add(line_chart(L + 18, iy2 + 8, LW - 36, 300,
                     [{"name": "Median", "values": [1.9, 2.4, 2.9, 3.2, 3.4, 3.5], "dash": None},
                      {"name": "p10", "values": [1.2, 1.5, 1.8, 2.0, 2.1, 2.1], "dash": "5 4"}],
                     x_labels=["2026", "2036", "2046", "2056", "2066", "2075"], y_max=4.4,
                     band=([1.2, 1.5, 1.8, 2.0, 2.1, 2.1], [2.7, 3.4, 4.0, 4.3, 4.4, 4.5])))
    x = L + LW + GAP
    for i, (lab, val, note) in enumerate([("Success rate", "86%", "86 of 100 trials funded"),
                                          ("p10 net worth", "$2.1M", "at 2075"),
                                          ("p50 net worth", "$3.5M", "at 2075"),
                                          ("p90 net worth", "$4.5M", "at 2075")]):
        p.add(kpi(x + (i % 2) * 204, 176 + (i // 2) * 108, 196, lab, val, delta=note, h=96))
    ix3, iy3, iw3 = p.card(x, 404, RW, 240, "Trial paths")
    p.add(table(x + 18, iy3 + 6, RW - 36,
                [("Trial", 80), ("End value", 140), ("Failed year", 130)],
                [["001", "$2,940,112", "—"], ["002", "$1,204,880", "2068"], ["003", "$3,551,002", "—"]], row_h=40)[0])
    p.add(para(x + 18, iy3 + 168, "Each trial stores its yearly path and is replayable from the result.", RW - 36, size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 660, RW, 176, "Run status")
    p.add(pill(x + 18, 690, "COMPLETE · 100 / 100 TRIALS", fg=INK_SOFT)[0])
    p.add(txt(x + 18, iy4 + 64, "Duration 4.2 s · seed 1234 · historical random restart", size=11.5, fill=MUTED))
    p.add(txt(x + 18, iy4 + 92, "Cancel stops the job and discards partial statistics.", size=11, fill=FAINT))
    p.markers([(1, L + 18, 216), (2, L + 18, 470), (3, x + 18, 446), (4, x + 18, 700)])
    return p.footer([
        (1, "Seed, trial count, and method are stored with the run. Repeating seed 1234 with 100 trials returns identical metrics."),
        (2, "The band is p10 to p90 from the backend. The median line is drawn from the stored percentile values, never from sampled client data."),
        (3, "Trial rows open the stored yearly path for that trial, including failed trials."),
        (4, "Success rate and every percentile come from one response, so the KPI row and the chart cannot disagree."),
    ])


def s035():
    p = Page(35, "Settings · Country and relocation", "Presets, custom mode, and dated relocation.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Country", actions=["Save"], frame_h=880)
    presets = [("United States", "USD · Federal + state", True), ("Canada", "CAD · Federal + province", False),
               ("United Kingdom", "GBP · UK income tax", False), ("France", "EUR · nearest preset", False),
               ("Other", "Custom tax mode", False)]
    ix, iy, iw = p.card(L, 176, LW, 300, "Country preset")
    for i, (name, note, active) in enumerate(presets):
        x = L + 18 + (i % 3) * 228
        y = iy + 6 + (i // 3) * 92
        p.add(rrect(x, y, 212, 80, r=10, fill=FILL if active else SURFACE, stroke=INK if active else BORDER, sw=2 if active else 1))
        p.add(txt(x + 14, y + 28, name, size=12.5, weight=600))
        p.add(txt(x + 14, y + 48, note, size=10.5, fill=MUTED))
        if name == "France":
            p.add(pill(x + 14, y + 74, "UNSUPPORTED", fg=INK_SOFT)[0])
    p.add(txt(L + 18, iy + 206, "Selecting a preset sets currency, locale, account types, and tax. Other is labeled custom.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 492, LW, 344, "Relocation milestone")
    p.add(select(L + 18, iy2 + 6, 200, "From", "New York")[0])
    p.add(select(L + 238, iy2 + 6, 200, "To", "Florida")[0])
    p.add(field(L + 458, iy2 + 6, 220, "Year", "2035")[0])
    p.add(txt(L + 18, iy2 + 82, "Jurisdiction by year", size=11.5, weight=600))
    for i in range(8):
        x = L + 18 + i * 84
        yr = 2032 + i
        active = yr >= 2035
        p.add(rrect(x, iy2 + 96, 76, 54, r=8, fill=FILL if active else SURFACE, stroke=BORDER))
        p.add(txt(x + 38, iy2 + 118, str(yr), size=10.5, fill=MUTED, anchor="middle"))
        p.add(txt(x + 38, iy2 + 138, "FL" if active else "NY", size=11.5, weight=600, anchor="middle"))
    p.add(txt(L + 18, iy2 + 176, "2034 keeps New York tax. 2035 and later use Florida. No earlier year changes.", size=11.5, fill=INK_SOFT))
    p.add(warn("Dual residency is out of scope. One jurisdiction per year.", L + 18, iy2 + 204, LW - 36, tone="info"))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Locale")
    p.add(select(x + 18, iy3 + 6, RW - 36, "Currency", "USD ($)")[0])
    p.add(select(x + 18, iy3 + 72, RW - 36, "Locale", "en-US")[0])
    p.add(select(x + 18, iy3 + 138, RW - 36, "Account types", "US retirement accounts")[0])
    p.add(select(x + 18, iy3 + 204, RW - 36, "Tax preset", "US federal + state")[0])
    ix4, iy4, iw4 = p.card(x, 492, RW, 344, "Custom mode")
    p.add(toggle(x + 18, iy4 + 6, False, "Use custom tax mode"))
    p.add(field(x + 18, iy4 + 44, RW - 36, "Currency code", "EUR", placeholder=True)[0])
    p.add(field(x + 18, iy4 + 110, RW - 36, "Ordinary rate", "—", placeholder=True)[0])
    p.add(field(x + 18, iy4 + 176, RW - 36, "Capital-gains rate", "—", placeholder=True)[0])
    p.add(warn("A custom mode is labeled on every result screen.", x + 18, iy4 + 246, RW - 36, tone="info"))
    p.markers([(1, L + 18, 216), (2, L + 18, 532), (3, x + 18, 216), (4, x + 18, 690)])
    return p.footer([
        (1, "A preset updates currency, locale, account types, and tax together. France maps to the nearest preset, or Other with a warning."),
        (2, "Relocation takes effect from its completion year. 2034 stays on New York tax; 2035 onward uses Florida."),
        (3, "Locale changes formatting only. Amounts and rates still come from the backend."),
        (4, "Other is always labeled as custom on results, so no one mistakes it for a supported jurisdiction."),
    ])


def s036():
    p = Page(36, "Plans", "Clone, rename, reorder, and delete.", "Plans",
             crumb="Home / Plans", actions=["New plan"], plan_badge="3 plans", frame_h=840)
    ix, iy, iw = p.card(L, 176, LW, 300, "All plans")
    for i, (name, created, note, active) in enumerate([("Plan For Retirement", "Jan 2026", "Primary", True),
                                                       ("Retire at 55", "Aug 2026", "Clone of Plan For Retirement", False),
                                                       ("Sandbox · Recent Grad", "Nov 2025", "Sandbox persona", False)]):
        y = iy + 6 + i * 84
        p.add(rrect(L + 18, y, LW - 36, 72, r=10, fill=FILL if active else SURFACE, stroke=BORDER))
        p.add(txt(L + 34, y + 40, "≡", size=14, fill=FAINT))
        p.add(rrect(L + 60, y + 22, 28, 28, r=7, fill=SURFACE, stroke=BORDER))
        p.add(txt(L + 96, y + 30, name, size=12.5, weight=600))
        p.add(txt(L + 96, y + 50, f"Created {created} · {note}", size=11, fill=MUTED))
        for j, act in enumerate(["Rename", "Clone", "Delete"]):
            bw = 74 if act != "Rename" else 84
            bx = L + LW - 36 - (3 - j) * 86
            p.add(rrect(bx, y + 22, bw, 28, r=6, fill=SURFACE, stroke=BORDER))
            p.add(txt(bx + bw / 2, y + 41, act, size=10.5, anchor="middle", fill=INK_SOFT))
    p.add(txt(L + 18, iy + 264, "Drag to reorder. The order is saved per user and appears in the plan switcher.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 496, LW, 340, "Delete plan")
    p.add(txt(L + 20, iy2 + 16, "Permanently delete \"Retire at 55\"?", size=13, weight=600))
    p.add(txt(L + 20, iy2 + 38, "Its snapshots are deleted with it. This cannot be undone.", size=11.5, fill=MUTED))
    p.add(field(L + 20, iy2 + 70, 320, "Type the plan name to confirm", "", placeholder=True)[0])
    for i, (lab, variant) in enumerate([("Cancel", "secondary"), ("Delete plan", "primary")]):
        b, bw = btn(L + 20 + i * 122, iy2 + 148, lab, variant=variant)
        p.add(b)
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 660, "Clone plan")
    p.add(txt(x + 18, iy3 + 14, "Source", size=10.5, weight=600, fill=MUTED))
    p.add(txt(x + 18, iy3 + 38, "Plan For Retirement", size=13, weight=600))
    p.add(line(x + 18, iy3 + 58, x + RW - 18, iy3 + 58, stroke=HAIR))
    p.add(field(x + 18, iy3 + 76, RW - 36, "New name", "Retire at 55")[0])
    p.add(txt(x + 18, iy3 + 158, "Icon", size=10.5, weight=600, fill=MUTED, ls=0.4))
    for i in range(5):
        p.add(rrect(x + 18 + i * 44, iy3 + 168, 32, 32, r=8, fill=FILL if i == 1 else SURFACE, stroke=INK if i == 1 else BORDER))
    p.add(field(x + 18, iy3 + 226, RW - 36, "Notes", "", placeholder=True)[0])
    p.add(warn("The clone gets a new plan id with the same accounts and events.", x + 18, iy3 + 328, RW - 36, tone="info"))
    p.add(txt(x + 18, iy3 + 396, "Independent data", size=11.5, weight=600))
    for i, lab in enumerate(["New plan id", "Copied accounts and events", "Own name, icon, notes"]):
        p.add(circle(x + 26, iy3 + 422 + i * 26, 3, fill=INK, stroke=None))
        p.add(txt(x + 40, iy3 + 426 + i * 26, lab, size=11, fill=MUTED))
    b, bw = btn(x + 18, iy3 + 508, "Create clone")
    p.add(b)
    p.markers([(1, L + 18, 216), (2, L + 18, 536), (3, x + 18, 216), (4, x + 18, 420)])
    return p.footer([
        (1, "A clone copies accounts, events, and settings, then assigns a new plan id. Editing the clone never edits the source."),
        (2, "Delete needs the plan name typed. On confirm the plan is permanently removed with its snapshots."),
        (3, "Rename, icon, and notes update the sidebar and plan header immediately after save."),
        (4, "The cloned plan opens with an independent name, icon, and notes; its accounts and events start as copies."),
    ])


def s037():
    p = Page(37, "Compare and what-if", "Baseline versus modified, with line-item deltas.", "Compare",
             crumb="Plans / Plan For Retirement / Compare", actions=["Revert", "Keep changes"], frame_h=880)
    p.add(pill(L, 168, "WHAT-IF · NOT SAVED")[0])
    p.add(txt(L + 220, 166, "Baseline: retire at 60 · Modified: retire at 55", size=11.5, fill=MUTED))
    ix, iy, iw = p.card(L, 200, LW, 356, "Net worth")
    p.add(line_chart(L + 18, iy + 10, LW - 36, 270,
                     [{"name": "Baseline", "values": [1.55, 2.2, 2.9, 3.3, 3.2, 2.9], "dash": "6 4"},
                      {"name": "Modified", "values": [1.55, 2.4, 3.1, 3.6, 3.5, 3.2], "dash": None}],
                     x_labels=["2026", "2036", "2046", "2056", "2066", "2075"], y_max=4.0,
                     milestone_x=[(3, "Retire 55")]))
    ix2, iy2, iw2 = p.card(L, 576, LW, 260, "Line-item deltas")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Metric", 260), ("Baseline", 150), ("Modified", 150), ("Delta", 120)],
                [["Net worth at 85", "$2,881,400", "$3,293,400", "+ $412,000"],
                 ["FI date", "2042", "2039", "3 yr earlier"],
                 ["Lifetime taxes", "$1,204,000", "$1,120,000", "− $84,000"]], row_h=44)[0])
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 200, RW, 300, "What-if inputs")
    p.add(field(x + 18, iy3 + 6, RW - 36, "Retirement age", "55", hint="Baseline 60")[0])
    p.add(field(x + 18, iy3 + 76, RW - 36, "Life expectancy", "85")[0])
    p.add(field(x + 18, iy3 + 146, RW - 36, "Living expenses", "$8,000 / mo")[0])
    p.add(para(x + 18, iy3 + 222, "Changing any input reruns the projection against the saved baseline.", RW - 36, size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 520, RW, 316, "Compare with another plan")
    p.add(select(x + 18, iy4 + 6, RW - 36, "Plan", "Second Opinion")[0])
    p.add(txt(x + 18, iy4 + 80, "Same overlay, saved plans on both sides.", size=11, fill=MUTED))
    for i, (lab, val) in enumerate([("Net worth delta", "− $240,000"), ("FI date", "2044 (−2 yr)"), ("Lifetime taxes", "+ $61,000")]):
        y = iy4 + 112 + i * 46
        p.add(txt(x + 20, y + 14, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 14, val, size=11.5, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 28, x + RW - 18, y + 28, stroke=HAIR))
    p.markers([(1, L + 18, 236), (2, L + 18, 616), (3, x + 18, 246), (4, x + 18, 560)])
    return p.footer([
        (1, "What-if overlays a modified line on the saved baseline. The baseline is dashed and never mutated by previewing."),
        (2, "Deltas are line items from the API. Lowering retirement age from 60 to 55 adds $412,000 of net worth at 85 in this example."),
        (3, "Keep changes saves the modified plan; Revert restores retirement age 60 and discards the overlay."),
        (4, "Two saved plans use the same overlay, so a plan-to-plan comparison and a what-if comparison behave identically."),
    ])


def s038():
    p = Page(38, "Tax analytics", "Composition and rates from completed results.", "Tax analytics",
             crumb="Plans / Plan For Retirement / Tax analytics", premium=True, actions=["Customize metrics"], frame_h=880)
    metrics = [("Legacy", "$25.8M", "net at 2075"), ("Average effective tax rate", "30.29%", "lifetime"),
               ("Withdrawal rate", "1.69%", "of portfolio"), ("Lifetime taxes", "$2,041,000", "2026–2075")]
    card_w = (W - 3 * 16) // 4
    for i, (lab, val, note) in enumerate(metrics):
        cx = L + i * (card_w + 16)
        p.add(rrect(cx, 176, card_w, 108, r=12, fill=SURFACE, stroke=BORDER))
        p.add(txt(cx + 16, 200, lab.upper(), size=9.5, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(cx + 16, 238, val, size=23, weight=600, family="Menlo, monospace"))
        p.add(txt(cx + 16, 262, note, size=10.5, fill=FAINT))
    p.add(tabs(L, 306, ["Income", "Rates"], active=0)[0])
    ix, iy, iw = p.card(L, 356, LW, 480, "Income composition by year")
    years = ["2026", "2036", "2046", "2056", "2066", "2075"]
    series = [("Salary", [220, 234, 0, 0, 0, 0], INK),
              ("Taxable Social Security", [0, 0, 18, 22, 24, 24], INK_SOFT),
              ("RMDs", [0, 0, 42, 61, 74, 88], MUTED),
              ("Roth conversions", [0, 50, 30, 0, 0, 0], FAINT_FILL)]
    p.add(stacked_bars(L + 18, iy + 10, LW - 36, 320, years, series, y_max=340, y_ticks=3))
    p.add(txt(L + 18, iy + 370, "Stacked bars use the same tax result as the Brackets view.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 356, RW, 250, "Income by type · 2036")
    for i, (lab, val) in enumerate([("Salary", "$234,604"), ("Taxable Social Security", "$0"), ("RMDs", "$0"), ("Roth conversion", "$50,000")]):
        y = iy2 + 8 + i * 42
        p.add(txt(x + 20, y + 12, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 12, val, size=11.5, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 26, x + RW - 18, y + 26, stroke=HAIR))
    ix3, iy3, iw3 = p.card(x, 626, RW, 210, "Rates view")
    p.add(txt(x + 18, iy3 + 12, "Income by effective rate", size=12, weight=600))
    p.add(bars(x + 18, iy3 + 34, RW - 36,
               [("0 – 12%", 42, "$42K"), ("12 – 22%", 118, "$118K"), ("22 – 24%", 64, "$64K"), ("24%+", 11, "$11K")],
               row_h=22, gap=10, max_val=118, label_w=100, value_w=70))
    p.markers([(1, L + 16, 200), (2, L + 18, 330), (3, x + 18, 396), (4, x + 18 + 284, 200)])
    return p.footer([
        (1, "Four metrics: legacy $25.8M, average effective tax rate 30.29%, withdrawal rate 1.69%, and lifetime taxes."),
        (2, "Income and Rates are views of one tax result, not separate calculations."),
        (3, "Selecting a year changes the composition detail. Values stay in sync with the chart."),
        (4, "Customize metrics persists per user and reorders or hides cards without changing the underlying result."),
    ])


def s039():
    p = Page(39, "Tax analytics · Brackets", "Marginal brackets and income by bracket.", "Tax analytics",
             crumb="Plans / Plan For Retirement / Tax analytics / Brackets", premium=True, frame_h=860)
    p.add(select(L, 166, 190, "Year", "2036")[0])
    for i, lab in enumerate(["Federal", "State", "Local"]):
        p.add(rrect(L + 214 + i * 88, 174, 80, 36, r=8, fill=INK if i == 0 else SURFACE, stroke=None if i == 0 else BORDER))
        p.add(txt(L + 214 + i * 88 + 40, 197, lab, size=11.5, weight=600, anchor="middle", fill="#FFFFFF" if i == 0 else INK_SOFT))
    p.add(tabs(L, 232, ["Brackets", "Effective brackets", "Selected year"], active=0)[0])
    ix, iy, iw = p.card(L, 282, LW, 554, "Marginal brackets · Federal · 2036")
    rows = [["10%", "$23,850", "$2,385"], ["12%", "$73,100", "$8,772"], ["22%", "$97,000", "$21,340"],
            ["24%", "$40,654", "$9,757"], ["32%", "$0", "$0"], ["35%", "$0", "$0"], ["37%", "$0", "$0"]]
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Rate", 120), ("Amount taxed at rate", 280), ("Tax from bracket", 220)], rows, row_h=42, highlight=2)[0])
    p.add(txt(L + 18, iy + 372, "Total federal tax 2036: $75,102. Brackets sum to the yearly total, to the dollar.", size=11.5, fill=INK_SOFT))
    p.add(rrect(L + 18, iy + 400, 300, 96, r=8, fill=SURFACE, stroke=INK, sw=2))
    p.add(txt(L + 32, iy + 424, "22% bracket", size=12, weight=600))
    p.add(txt(L + 32, iy + 446, "$97,000 taxed → $21,340", size=11, fill=MUTED))
    p.add(txt(L + 32, iy + 466, "Hover shows the amount and the tax", size=10.5, fill=FAINT))
    p.add(txt(L + 18, iy + 520, "Hover tooltip anchored to the 22% row (shown left).", size=10.5, fill=FAINT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 282, RW, 250, "Effective brackets")
    p.add(bars(x + 18, iy2 + 10, RW - 36,
               [("Ordinary income", 24, "24.0%"), ("Qualified dividends", 15, "15.0%"), ("Long-term gains", 15, "15.0%")],
               row_h=30, gap=12, max_val=30, label_w=130, value_w=64))
    ix3, iy3, iw3 = p.card(x, 556, RW, 280, "Selected year")
    p.add(txt(x + 18, iy3 + 14, "2036 · Federal filter", size=12, weight=600))
    for i, (lab, val) in enumerate([("Taxable income", "$234,604"), ("Ordinary taxable", "$186,400"), ("Capital gains", "$48,204"), ("Federal tax", "$75,102")]):
        y = iy3 + 40 + i * 42
        p.add(txt(x + 20, y + 12, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 12, val, size=11.5, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 26, x + RW - 18, y + 26, stroke=HAIR))
    p.markers([(1, L + 18, 320), (2, L + 18, 330), (3, x + 18, 320), (4, x + 18, 590)])
    return p.footer([
        (1, "Each bracket row shows rate, amount taxed at that rate, and tax from that bracket, for the selected year."),
        (2, "Hovering 22% shows $97,000 taxed and $21,340 of tax. Bracket rows sum to the yearly federal tax."),
        (3, "The Federal, State, and Local filters change the view only; no recalculation happens in the client."),
        (4, "Changing the selected year reloads brackets and the detail from the same tax result."),
    ])


def s043():
    p = Page(43, "Strategy · Gain harvesting", "Realize gains inside a chosen bracket, then rebuy.", "Strategy",
             crumb="Plans / Plan For Retirement / Strategy / Gain harvesting", premium=True, actions=["Run plan"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 260, "Setting")
    p.add(toggle(L + 18, iy + 8, True, "Enable gain harvesting"))
    p.add(select(L + 18, iy + 52, 220, "Capital-gains bracket", "0%")[0])
    p.add(field(L + 258, iy + 52, 200, "From year", "2027")[0])
    p.add(field(L + 478, iy + 52, 200, "To year", "2035")[0])
    p.add(txt(L + 18, iy + 132, "Gains are realized only up to the top of the chosen bracket, then the asset is rebought and basis resets.", size=11, fill=FAINT))
    p.add(warn("Harvesting never pushes income past the selected bracket ceiling.", L + 18, iy + 158, LW - 36, tone="info"))
    ix2, iy2, iw2 = p.card(L, 460, LW, 376, "Harvest by year")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Year", 100), ("Asset", 210), ("Gains realized", 150), ("Basis reset", 150)],
                [["2027", "Taxable brokerage", "$20,000", "+ $20,000"],
                 ["2028", "Taxable brokerage", "$18,400", "+ $18,400"],
                 ["2029", "Crypto", "$6,200", "+ $6,200"]], row_h=44, highlight=0)[0])
    p.add(txt(L + 18, iy2 + 200, "Total gains harvested", size=11.5, fill=MUTED))
    p.add(txt(L + 18, iy2 + 232, "$44,600", size=22, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 240, iy2 + 232, "Next year's taxable gain falls by the same amount.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Effect on tax")
    for i, (lab, val) in enumerate([("Baseline tax", "$75,102"), ("With harvesting", "$72,102"), ("Tax saved", "$3,000")]):
        y = iy3 + 10 + i * 56
        p.add(txt(x + 20, y + 14, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 14, val, size=13, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 32, x + RW - 18, y + 32, stroke=HAIR))
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "Empty state", dash="6 5")
    p.add(txt(x + 18, iy4 + 14, "No harvestable accounts", size=12.5, weight=600))
    p.add(txt(x + 18, iy4 + 36, "Turn on harvesting after adding a taxable or crypto account.", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 66, "Total gains harvested", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 96, "$0", size=22, weight=600, family="Menlo, monospace"))
    p.add(warn("Zero state is explicit, not an error.", x + 18, iy4 + 120, RW - 36, tone="info"))
    p.markers([(1, L + 18, 216), (2, L + 18, 500), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Harvesting is enabled per plan with a bracket and a year range. Outside the range nothing is realized."),
        (2, "Each harvest sells and immediately rebuys, so the asset stays owned and the basis rises by the realized gain."),
        (3, "Tax effect uses the same result pipeline: baseline and harvesting runs are compared by the backend."),
        (4, "With no taxable or crypto account the total is $0 and the empty state explains why."),
    ])


def s044():
    p = Page(44, "Strategy · Optimizer", "Generate candidates, score them, honor depth.", "Strategy",
             crumb="Plans / Plan For Retirement / Strategy / Optimizer", premium=True, actions=["Run again"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 300, "Search space")
    p.add(select(L + 18, iy + 6, 330, "Objective", "Lower lifetime taxes")[0])
    p.add(txt(L + 366, iy + 12, "Depth", size=10.5, weight=600, fill=MUTED, ls=0.4))
    for i, lab in enumerate(["Quick", "Standard", "Deep", "Extreme"]):
        active = i == 2
        p.add(rrect(L + 366 + i * 80, iy + 20, 74, 30, r=7, fill=INK if active else SURFACE, stroke=None if active else BORDER))
        p.add(txt(L + 366 + i * 80 + 37, iy + 40, lab, size=10.5, weight=600, anchor="middle", fill="#FFFFFF" if active else INK_SOFT))
    p.add(txt(L + 18, iy + 76, "Candidates combine", size=11.5, weight=600))
    for i, (lab, count) in enumerate([("Brackets", "18 boundaries"), ("IRMAA tiers", "6 tiers"), ("FPL multiples", "5 caps"), ("Module combinations", "12")]):
        x = L + 18 + i * 172
        p.add(rrect(x, iy + 92, 160, 62, r=8, fill=FILL, stroke=None))
        p.add(txt(x + 14, iy + 116, lab, size=11.5, weight=600))
        p.add(txt(x + 14, iy + 136, count, size=10.5, fill=MUTED))
    p.add(line(L + 18, iy + 176, L + LW - 18, iy + 176, stroke=HAIR))
    p.add(txt(L + 18, iy + 202, "Deep evaluates more bracket boundaries and drawdown presets than Quick.", size=11, fill=FAINT))
    p.add(txt(L + 18, iy + 224, "Estimated candidates: 66", size=11.5, fill=INK_SOFT))
    ix2, iy2, iw2 = p.card(L, 500, LW, 336, "Run")
    p.add(txt(L + 18, iy2 + 16, "Completed 66 of 66 candidates", size=12.5, weight=600))
    p.add(rrect(L + 18, iy2 + 34, LW - 36, 12, r=6, fill=FILL, stroke=None))
    p.add(rrect(L + 18, iy2 + 34, LW - 36, 12, r=6, fill=INK, stroke=None))
    p.add(txt(L + 18, iy2 + 72, "100% · 4.2 s · ranking is final · safe to leave this page", size=11, fill=MUTED))
    p.add(table(L + 18, iy2 + 96, LW - 36,
                [("Rank", 80), ("Candidate", 280), ("Lifetime tax", 160)],
                [["1", "Fill 22% · IRMAA 2 · FPL 400%", "$1,380,000"],
                 ["2", "Fill 24% · no IRMAA cap", "$1,412,000"],
                 ["3", "Fill 22% · no modules", "$1,455,000"]], row_h=40)[0])
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Depth comparison")
    p.add(txt(x + 18, iy3 + 12, "Candidates evaluated", size=11.5, fill=MUTED))
    p.add(bars(x + 18, iy3 + 30, RW - 36,
               [("Quick", 18, "18"), ("Standard", 34, "34"), ("Deep", 66, "66")],
               row_h=24, gap=12, max_val=66, label_w=110, value_w=54))
    p.add(txt(x + 18, iy3 + 168, "A deeper search costs more time and finds more bracket edges.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "Cancel behaviour")
    p.add(txt(x + 18, iy4 + 14, "Cancel stops the job.", size=12.5, weight=600))
    for i, lab in enumerate(["Partial results are not applied", "The saved strategy is unchanged", "Results list keeps the last complete run"]):
        p.add(circle(x + 26, iy4 + 44 + i * 28, 3, fill=INK, stroke=None))
        p.add(txt(x + 40, iy4 + 48 + i * 28, lab, size=11, fill=MUTED))
    p.add(warn("Job status is read from the API after navigation, so no duplicate job starts.", x + 18, iy4 + 148, RW - 36, tone="info"))
    p.markers([(1, L + 18, 216), (2, L + 18, 540), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Candidates are generated from brackets, IRMAA tiers, FPL multiples, and module combinations, then ranked by the chosen objective."),
        (2, "Depth changes search breadth: Quick 18, Standard 34, Deep 66 candidates in this example. The setting is stored with the run."),
        (3, "The ranking table updates as results arrive, ranked by cumulative lifetime tax with the winner first."),
        (4, "Cancel stops the job and applies nothing. Resuming is not automatic; the last complete run stays available."),
    ])


def s045():
    p = Page(45, "Optimizer results", "Best strategy, baseline, and deltas. Apply writes the plan.", "Strategy",
             crumb="Plans / Plan For Retirement / Strategy / Optimizer results", premium=True,
             actions=["Back to optimizer", "Apply winner"], frame_h=880)
    p.add(pill(L, 168, "COMPLETE · 66 CANDIDATES · DEEP")[0])
    p.add(txt(L + 250, 166, "Job 8f21 · completed 14:22 · safe to navigate", size=11, fill=MUTED))
    ix, iy, iw = p.card(L, 200, LW, 200, "Winner")
    p.add(txt(L + 20, iy + 34, "Fill 22% · IRMAA tier 2 · FPL 400% · drawdown cash-first", size=15, weight=600))
    p.add(txt(L + 20, iy + 58, "Rank 1 of 66", size=11, fill=MUTED))
    p.add(txt(L + 20, iy + 104, "$222,288", size=30, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 20, iy + 126, "taxes saved vs baseline", size=11, fill=MUTED))
    p.add(txt(L + 260, iy + 104, "$726,256", size=30, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 260, iy + 126, "net legacy added", size=11, fill=MUTED))
    b, bw = btn(L + LW - 172, iy + 84, "Apply winner")
    p.add(b)
    ix2, iy2, iw2 = p.card(L, 420, LW, 416, "Winner vs baseline")
    p.add(line_chart(L + 18, iy2 + 10, LW - 36, 300,
                     [{"name": "Baseline", "values": [1.55, 2.2, 2.9, 3.3, 3.1, 2.9], "dash": "6 4"},
                      {"name": "Winner", "values": [1.55, 2.4, 3.2, 3.7, 3.6, 3.4], "dash": None}],
                     x_labels=["2026", "2036", "2046", "2056", "2066", "2075"], y_max=4.0))
    p.add(txt(L + 18, iy2 + 350, "Applying writes the winning target and modules to the plan strategy.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 200, RW, 340, "Ranked candidates")
    for i, (rank, name, saved, active) in enumerate([("1", "Fill 22% · IRMAA 2 · FPL 400%", "$222,288", True),
                                                     ("2", "Fill 24% · no IRMAA cap", "$186,400", False),
                                                     ("3", "Fill 22% · no modules", "$151,900", False)]):
        y = iy3 + 6 + i * 90
        p.add(rrect(x + 18, y, RW - 36, 78, r=10, fill=FILL if active else SURFACE, stroke=INK if active else BORDER, sw=2 if active else 1))
        p.add(txt(x + 34, y + 30, f"#{rank}", size=12, weight=700, fill=INK_SOFT))
        p.add(txt(x + 66, y + 30, name, size=11.5, weight=600))
        p.add(txt(x + 66, y + 52, f"{saved} taxes saved", size=11, fill=MUTED))
        p.add(txt(x + RW - 34, y + 44, "Preview", size=11, fill=INK_SOFT, anchor="end"))
    p.add(txt(x + 18, iy3 + 300, "Selecting a candidate previews its chart and metrics.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 560, RW, 276, "Run states")
    p.add(warn("Running: 62% · navigation stays open.", x + 18, iy4 + 8, RW - 36, tone="info"))
    p.add(warn("Failed: API error shown, Retry available, plan strategy unchanged.", x + 18, iy4 + 66, RW - 36))
    b, bw = btn(x + 18, iy4 + 126, "Retry", variant="secondary")
    p.add(b)
    p.add(para(x + 18, iy4 + 194, "Progress and failure states read from the job API, not local timers.", RW - 36, size=11, fill=FAINT))
    p.markers([(1, L + 18, 240), (2, L + 18, 470), (3, x + 18, 240), (4, x + 18, 600)])
    return p.footer([
        (1, "Winner card: $222,288 of tax saved and $726,256 of added net legacy against the baseline, both from the job result."),
        (2, "The chart overlays the saved baseline and the selected candidate. Previewing another candidate changes only this overlay."),
        (3, "Ranked candidates are ordered by the objective. Selecting one previews it without applying anything."),
        (4, "Apply writes the winning target and modules to the plan. A failed job leaves the plan strategy unchanged and offers Retry."),
    ])


def s046():
    p = Page(46, "Estate", "Gross estate, estate drag, and net legacy.", "Estate",
             crumb="Plans / Plan For Retirement / Estate", premium=True, actions=["Run plan"], frame_h=880)
    for i, (lab, val, note) in enumerate([("Gross estate", "$37.84M", "at 2075"), ("Estate drag", "$12.03M", "32% of gross"), ("Net legacy", "$25.81M", "68% of gross")]):
        p.add(rrect(L + i * 376, 176, 360, 108, r=12, fill=SURFACE, stroke=BORDER))
        p.add(txt(L + i * 376 + 16, 200, lab.upper(), size=9.5, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(L + i * 376 + 16, 238, val, size=23, weight=600, family="Menlo, monospace"))
        p.add(txt(L + i * 376 + 16, 262, note, size=10.5, fill=FAINT))
    p.add(rrect(L, 300, LW, 54, r=10, fill=SURFACE, stroke=BORDER))
    p.add(txt(L + 16, 324, "Estate composition", size=11.5, weight=600))
    seg = [("Taxable brokerage", 0.33, INK), ("401(k) / IRA", 0.31, INK_SOFT), ("Roth", 0.14, MUTED), ("House", 0.22, FAINT_FILL)]
    cx = L
    for lab, frac, shade in seg:
        p.add(rrect(cx, 334, LW * frac, 10, r=3, fill=shade, stroke=None))
        cx += LW * frac
    lx = L
    for lab, frac, shade in seg:
        p.add(rrect(lx, 356, 9, 9, r=2, fill=shade, stroke=None))
        p.add(txt(lx + 15, 364, f"{lab} {int(frac*100)}%", size=10, fill=MUTED))
        lx += 190
    ix, iy, iw = p.card(L, 396, LW, 440, "Breakdown")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Account", 210), ("Gross", 140), ("Deferred tax", 140), ("Costs", 110), ("Net", 140)],
                [["Taxable brokerage", "$12,400,000", "—", "$210,000", "$12,190,000"],
                 ["401(k) / IRA", "$11,700,000", "$2,808,000", "—", "$8,892,000"],
                 ["Roth IRA", "$5,300,000", "—", "—", "$5,300,000"],
                 ["House", "$8,440,000", "—", "$250,000", "$8,190,000"]], row_h=44)[0])
    p.add(line(L + 18, iy + 262, L + LW - 18, iy + 262, stroke=HAIR))
    p.add(txt(L + 18, iy + 290, "Distributable estate", size=11.5, fill=MUTED))
    p.add(txt(L + 18, iy + 322, "$37,840,000 gross → $25,810,000 net", size=14, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 18, iy + 358, "Charity 10% receives $2,581,000. Heirs receive $23,229,000.", size=11.5, fill=INK_SOFT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 396, RW, 440, "Settings")
    p.add(field(x + 18, iy2 + 6, RW - 36, "Deferred-tax rate", "24%")[0])
    p.add(toggle(x + 18, iy2 + 78, True, "Step-up basis on death"))
    p.add(toggle(x + 18, iy2 + 114, True, "Liquidate to pay costs"))
    p.add(field(x + 18, iy2 + 152, RW - 36, "Admin costs", "$180,000")[0])
    p.add(field(x + 18, iy2 + 218, RW - 36, "Charitable gift", "10%")[0])
    p.add(line(x + 18, iy2 + 292, x + RW - 18, iy2 + 292, stroke=HAIR))
    p.add(warn("Changing a setting reruns the estate result. The UI never recomputes tax.", x + 18, iy2 + 310, RW - 36, tone="info"))
    p.add(txt(x + 18, iy2 + 380, "Liabilities exceeding assets raise a warning on this page.", size=11, fill=FAINT))
    p.markers([(1, L + 16, 200), (2, L + 18, 440), (3, x + 18, 440), (4, x + 18, 470)])
    return p.footer([
        (1, "Gross estate $37.84M, estate drag $12.03M at 32%, net legacy $25.81M at 68%."),
        (2, "The breakdown ties each account to gross, deferred tax, costs, and net."),
        (3, "Settings cover deferred-tax rate, step-up basis, liquidation, admin costs, and charity. Each change reruns the backend."),
        (4, "Charity is shown separately from the heirs' share, so a 10% gift is visible in both totals."),
    ])
