"""Wireframe screens, part 3 (issues 49-62)."""

from wirelib import (Page, txt, rrect, line, pill, btn, field, select, tabs, toggle,
                     table, kpi, line_chart, bars, donut, gauge, warn, empty, card, circle, polyline, para,
                     INK, INK_SOFT, MUTED, FAINT, FILL, SURFACE, BORDER, HAIR)

L, W = 272, 1136
LW, GAP, RW = 716, 20, 400


def s049():
    p = Page(49, "Strategy · ACA subsidy", "Benchmark, subsidy, cliff, and reconciliation.", "Strategy",
             crumb="Plans / Plan For Retirement / Strategy / ACA", premium=True, actions=["Run plan"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 250, "ACA Marketplace · 2027")
    for i, (lab, val, note) in enumerate([("Benchmark premium", "$14,400 / yr", "second-lowest silver"),
                                          ("Subsidy", "$9,120 / yr", "63% of benchmark"),
                                          ("Net premium", "$5,280 / yr", "$440 / mo")]):
        p.add(txt(L + 18 + i * 228, iy + 14, lab.upper(), size=9.5, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(L + 18 + i * 228, iy + 44, val, size=18, weight=600, family="Menlo, monospace"))
        p.add(txt(L + 18 + i * 228, iy + 64, note, size=10.5, fill=FAINT))
    p.add(line(L + 18, iy + 88, L + LW - 18, iy + 88, stroke=HAIR))
    p.add(txt(L + 18, iy + 116, "Household MAGI $62,000 · 400% FPL · 2 people", size=11.5, fill=INK_SOFT))
    p.add(txt(L + 18, iy + 152, "Income cap at the cliff: $1 above 400% FPL removes the subsidy.", size=11, fill=FAINT))
    p.add(warn("Strategy target: cap income at 400% FPL to keep the subsidy.", L + 18, iy + 176, LW - 36, tone="info"))
    ix2, iy2, iw2 = p.card(L, 450, LW, 386, "Subsidy and cliff")
    p.add(line_chart(L + 18, iy2 + 10, LW - 36, 270,
                     [{"name": "Subsidy $ / yr", "values": [9.1, 9.1, 9.1, 9.1, 0, 0], "area": True}],
                     x_labels=["100%", "200%", "300%", "400%", "401%", "500%"], y_max=12, y_ticks=2,
                     milestone_x=[(3, "Cliff")]))
    p.add(txt(L + 18, iy2 + 320, "The cliff is a step, not a slope. The engine applies the FPL rule for the year.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Reconciliation")
    for i, (lab, val) in enumerate([("Advance credit received", "100%"), ("Final MAGI", "$66,400"), ("Final subsidy", "$6,900"), ("Repayment next year", "$2,220")]):
        y = iy3 + 10 + i * 50
        p.add(txt(x + 20, y + 14, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 14, val, size=12, weight=600 if i == 3 else 400, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 30, x + RW - 18, y + 30, stroke=HAIR))
    p.add(txt(x + 18, iy3 + 232, "Repayment appears in the next-year tax balance.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "Strategy cap")
    p.add(select(x + 18, iy4 + 6, RW - 36, "Cap income at", "400% FPL")[0])
    p.add(toggle(x + 18, iy4 + 76, True, "Adjust drawdown to hold the cap"))
    p.add(txt(x + 18, iy4 + 116, "Income after cap", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 140, "$62,000", size=18, weight=600, family="Menlo, monospace"))
    p.add(txt(x + 18, iy4 + 178, "Subsidy preserved", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 202, "$9,120 / yr", size=18, weight=600, family="Menlo, monospace"))
    p.add(warn("Below 138% FPL the plan is assumed Medicaid-eligible and shows no marketplace cost.", x + 18, iy4 + 240, RW - 36, tone="info"))
    p.markers([(1, L + 18, 216), (2, L + 18, 490), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Benchmark premium, subsidy, and net premium are separate values. The subsidy is a dollar amount, not a percentage the UI derives."),
        (2, "The FPL cliff is a step at 400%. Above it the subsidy is reduced or removed, and the chart shows the drop."),
        (3, "An advance credit reconciled against final MAGI creates a repayment in the next-year tax balance."),
        (4, "A strategy targeting 400% FPL caps income below the cliff; the engine adjusts drawdown, not the client."),
    ])


def s051():
    p = Page(51, "Decision variables", "Inputs reference variables instead of copying values.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Variables", actions=["Add variable"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 320, "Variables")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Name", 170), ("Type", 100), ("Value", 250), ("Used by", 160)],
                [["retirementAge", "number", "55", "Retirement, salary end"],
                 ["inflation", "percent", "2.5%", "12 inputs"],
                 ["lifeExpectancy", "number", "85", "Mortality, FI metrics"],
                 ["retireYear", "expression", "birthYear + retirementAge", "Retirement"]], row_h=48)[0])
    p.add(txt(L + 18, iy + 258, "An input that references a variable updates when the variable changes.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 520, LW, 316, "References for retirementAge")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Input", 300), ("Current value", 160)],
                [["Retirement milestone · target age", "55"],
                 ["Salary · end age", "55"],
                 ["Roth conversion window · start age", "{{retirementAge}} + 1"]], row_h=44)[0])
    p.add(para(L + 18, iy2 + 196, "One save moves every reference. No copied value is left behind.", LW - 36, size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 360, "Edit variable")
    p.add(field(x + 18, iy3 + 6, RW - 36, "Name", "retirementAge")[0])
    p.add(select(x + 18, iy3 + 72, RW - 36, "Type", "Number")[0])
    p.add(field(x + 18, iy3 + 138, RW - 36, "Value", "60", hint="Was 55 · 3 references update", focus=True)[0])
    b1, w1 = btn(x + 18, iy3 + 218, "Cancel", variant="secondary")
    b2, w2 = btn(x + 18 + w1 + 10, iy3 + 218, "Save and update references")
    p.add(b1 + b2)
    ix4, iy4, iw4 = p.card(x, 560, RW, 276, "Validation")
    p.add(warn("Unknown variable 'retireAge' referenced by Salary · end age.", x + 18, iy4 + 8, RW - 36))
    p.add(txt(x + 18, iy4 + 76, "code: INPUT_INVALID_REFERENCE", size=11, family="Menlo, monospace", fill=INK_SOFT))
    p.add(txt(x + 18, iy4 + 100, "field: plan.inputs.salary.endAge", size=11, family="Menlo, monospace", fill=MUTED))
    p.add(para(x + 18, iy4 + 140, "The API rejects the run. The UI shows the problem detail and links to the field.", RW - 36, size=11, fill=FAINT))
    p.markers([(1, L + 18, 216), (2, L + 18, 560), (3, x + 18, 216), (4, x + 18, 600)])
    return p.footer([
        (1, "Variables have a name, a type, and a value. Types are number, percent, date, or expression."),
        (2, "The reference list proves a change is not copied: two inputs show 55 and one shows an expression."),
        (3, "Saving retirementAge as 60 updates both references in one save. The hint states how many references move."),
        (4, "A missing or invalid reference fails validation with a stable code and offending field; the engine never falls back silently."),
    ])


def s052():
    p = Page(52, "Asset allocation", "Plan mix, account overrides, and a glide path.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Allocation", actions=["Save"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 300, "Plan mix")
    p.add(donut(L + 110, iy + 100, 72, [("Stocks", 0.6), ("Bonds", 0.4)], thickness=20,
                center_top="60 / 40", center_bottom="at age 40"))
    p.add(txt(L + 230, iy + 30, "Stocks", size=12, weight=600))
    p.add(txt(L + 230, iy + 50, "60%", size=13, family="Menlo, monospace"))
    p.add(txt(L + 360, iy + 30, "Bonds", size=12, weight=600))
    p.add(txt(L + 360, iy + 50, "40%", size=13, family="Menlo, monospace"))
    p.add(txt(L + 230, iy + 96, "Glide path", size=11.5, weight=600))
    p.add(txt(L + 230, iy + 116, "60/40 at 40 → 40/60 at 60", size=11, fill=MUTED))
    p.add(txt(L + 230, iy + 136, "Linear interpolation between points", size=11, fill=FAINT))
    p.add(txt(L + 230, iy + 172, "Age 50 uses 50/50 within 0.01%.", size=11.5, fill=INK_SOFT))
    ix2, iy2, iw2 = p.card(L, 500, LW, 336, "Glide path")
    p.add(line_chart(L + 18, iy2 + 10, LW - 36, 250,
                     [{"name": "Stocks %", "values": [60, 58, 50, 42, 40], "area": True}],
                     x_labels=["40", "45", "50", "55", "60"], y_max=80, y_ticks=2))
    p.add(txt(L + 18, iy2 + 286, "Dated points interpolate; an account override does not change the plan curve.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Account overrides")
    p.add(table(x + 18, iy3 + 6, RW - 36,
                [("Account", 180), ("Mix", 150)],
                [["Taxable brokerage", "100% bonds"], ["401(k)", "Plan mix"], ["Roth IRA", "Plan mix"]], row_h=44)[0])
    p.add(txt(x + 18, iy3 + 186, "An override applies to that account only.", size=11, fill=FAINT))
    b, bw = btn(x + 18, iy3 + 212, "Add override", variant="secondary")
    p.add(b)
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "Validation")
    p.add(warn("Total is 105%. A mix must total exactly 100% before save.", x + 18, iy4 + 8, RW - 36))
    p.add(txt(x + 18, iy4 + 76, "code: ALLOCATION_NOT_100", size=11, family="Menlo, monospace", fill=INK_SOFT))
    p.add(txt(x + 18, iy4 + 100, "field: plan.allocation[2027].stocks", size=11, family="Menlo, monospace", fill=MUTED))
    p.add(field(x + 18, iy4 + 132, RW - 36, "Stocks", "65%", error="Stocks + bonds must equal 100%")[0])
    p.add(txt(x + 18, iy4 + 220, "Save stays disabled until the server accepts the mix.", size=11, fill=FAINT))
    p.markers([(1, L + 18, 216), (2, L + 18, 540), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "The plan holds a stock and bond mix. Each dated point changes it over time."),
        (2, "The glide path interpolates between dated points; the client renders the returned curve."),
        (3, "Account overrides are per account and are listed with the mix applied."),
        (4, "Validation rejects any mix that does not total 100%, with a stable code and the offending field."),
    ])


def s053():
    p = Page(53, "Settings · Multi-currency", "Each amount keeps its currency and a stored rate.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Currency", actions=["Rerun plan"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 320, "Amounts")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Item", 200), ("Native", 150), ("Rate · date", 170), ("Display (USD)", 160)],
                [["Rental income", "€2,000 / mo", "1.10 · Aug 26 2026", "$2,200"],
                 ["UK pension", "£1,200 / mo", "1.27 · Aug 26 2026", "$1,524"],
                 ["Swiss account", "CHF 40,000", "1.12 · Aug 26 2026", "$44,800"]], row_h=48)[0])
    p.add(txt(L + 18, iy + 214, "Displayed values use the stored rate and date. No live feed is requested.", size=11, fill=FAINT))
    p.add(warn("Rate change requires a rerun. Results never mix old and new rates.", L + 18, iy + 240, LW - 36, tone="info"))
    ix2, iy2, iw2 = p.card(L, 520, LW, 316, "Rate history · EUR/USD")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Date", 160), ("Rate", 140), ("Source", 180), ("Used by", 160)],
                [["Aug 26 2026", "1.10", "Manual", "Current run"],
                 ["Jun 30 2026", "1.08", "Manual", "Run v11"],
                 ["Jan 02 2026", "1.04", "Manual", "Run v9"]], row_h=44)[0])
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 260, "Display currency")
    p.add(select(x + 18, iy3 + 6, RW - 36, "Currency", "USD ($)")[0])
    p.add(para(x + 18, iy3 + 82, "Amounts are converted for display only. Each source keeps its own currency.", RW - 36, size=11, fill=MUTED))
    ix4, iy4, iw4 = p.card(x, 460, RW, 376, "Change rate")
    p.add(field(x + 18, iy4 + 6, RW - 36, "EUR/USD rate", "1.05", focus=True, hint="Was 1.10")[0])
    p.add(field(x + 18, iy4 + 86, RW - 36, "Effective date", "Aug 26 2026")[0])
    p.add(warn("Results are stale. Rerun to apply 1.05.", x + 18, iy4 + 156, RW - 36))
    p.add(txt(x + 18, iy4 + 224, "After rerun", size=11, weight=600, fill=MUTED))
    p.add(txt(x + 18, iy4 + 252, "€2,000 / mo → $2,100", size=15, weight=600, family="Menlo, monospace"))
    p.add(txt(x + 18, iy4 + 276, "Down $100 per month from 1.10", size=11, fill=FAINT))
    b, bw = btn(x + 18, iy4 + 306, "Rerun with new rate")
    p.add(b)
    p.markers([(1, L + 18, 216), (2, L + 18, 560), (3, x + 18, 216), (4, x + 18, 500)])
    return p.footer([
        (1, "Every foreign amount stores its currency, a rate, and a rate date. Display converts with that stored pair."),
        (2, "Rate history is versioned with the run that used it, so a past result keeps its original conversion."),
        (3, "Display currency formats only. A cross-currency account converts contributions and withdrawals consistently."),
        (4, "Changing EUR/USD from 1.10 to 1.05 marks results stale and requires a rerun before the new value shows."),
    ])


def s055():
    p = Page(55, "Snapshots", "Stored plan state with label and date.", "Snapshots",
             crumb="Plans / Plan For Retirement / Snapshots", premium=True, actions=["New snapshot"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 260, "Snapshot list")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Label", 260), ("Created", 170), ("Age", 100), ("Net worth", 150)],
                [["Before retirement at age 55", "Aug 26 2026", "55", "$2.10M"],
                 ["After sale at age 60", "Aug 22 2026", "60", "$2.60M"],
                 ["Baseline (auto)", "Jan 2026", "36", "$1.55M"]], row_h=44)[0])
    p.add(para(L + 18, iy + 184, "Ordered newest first. Stored plan state and progress, never a reference to changing data.", LW - 36, size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 460, LW, 376, "Compare snapshots")
    p.add(txt(L + 20, iy2 + 14, "Before retirement at age 55", size=12, weight=600))
    p.add(txt(L + 300, iy2 + 14, "vs", size=11, fill=FAINT))
    p.add(txt(L + 340, iy2 + 14, "After sale at age 60", size=12, weight=600))
    p.add(table(L + 18, iy2 + 40, LW - 36,
                [("Metric", 240), ("Age 55", 160), ("Age 60", 160), ("Delta", 120)],
                [["Net worth", "$2.10M", "$2.60M", "+ $500K"],
                 ["FI date", "2041", "2039", "2 yr earlier"],
                 ["Lifetime taxes", "$1,204,000", "$1,310,000", "+ $106,000"]], row_h=46)[0])
    p.add(txt(L + 18, iy2 + 234, "Deltas are computed by the backend from the two stored snapshots.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 320, "Restore")
    p.add(txt(x + 18, iy3 + 16, "Restore as a new plan", size=13, weight=600))
    p.add(txt(x + 18, iy3 + 40, "The original plan and later snapshots stay intact.", size=11.5, fill=MUTED))
    p.add(field(x + 18, iy3 + 78, RW - 36, "New plan name", "Before retirement · restored")[0])
    b, bw = btn(x + 18, iy3 + 158, "Restore as new plan", variant="secondary")
    p.add(b)
    p.add(warn("Restore never overwrites later data.", x + 18, iy3 + 232, RW - 36, tone="info"))
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "New snapshot")
    p.add(field(x + 18, iy4 + 6, RW - 36, "Label", "Before retirement", focus=True)[0])
    p.add(txt(x + 18, iy4 + 82, "Stores", size=11, weight=600, fill=MUTED))
    for i, lab in enumerate(["Plan state", "Progress points", "Last completed result id"]):
        p.add(circle(x + 26, iy4 + 108 + i * 26, 3, fill=INK, stroke=None))
        p.add(txt(x + 40, iy4 + 112 + i * 26, lab, size=11, fill=MUTED))
    b, bw = btn(x + 18, iy4 + 210, "Create snapshot")
    p.add(b)
    p.markers([(1, L + 18, 216), (2, L + 18, 480), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Every snapshot has a label and a creation date and is ordered newest first."),
        (2, "Comparison shows net worth and FI metrics from both snapshots with deltas."),
        (3, "Restoring creates a new plan or revision. The source plan and any later snapshots stay unchanged."),
        (4, "A snapshot stores plan state, progress points, and the last completed result id, so it is reproducible."),
    ])


def s056():
    p = Page(56, "Expense itemizer", "Templates create editable line items.", "Expenses & flows",
             crumb="Plans / Plan For Retirement / Expenses / Itemizer", actions=["Save as living expense"], frame_h=860)
    ix, iy, iw = p.card(L, 176, LW, 190, "Templates")
    for i, lab in enumerate(["Housing", "Food", "Transport", "Utilities", "Full living"]):
        tw = 120 if i < 4 else 150
        p.add(rrect(L + 18 + i * 134, iy + 8, tw, 36, r=18, fill=FILL if i == 4 else SURFACE, stroke=BORDER))
        p.add(txt(L + 18 + i * 134 + tw / 2, iy + 31, lab, size=11.5, anchor="middle", fill=INK_SOFT))
    p.add(txt(L + 18, iy + 70, "Applying a template adds one editable line per category. Amounts stay editable.", size=11, fill=FAINT))
    b, bw = btn(L + 18, iy + 96, "Apply template", variant="secondary")
    p.add(b)
    ix2, iy2, iw2 = p.card(L, 392, LW, 442, "Line items")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Category", 220), ("Line item", 220), ("Amount", 150), ("Edit", 70)],
                [["Housing", "Rent / mortgage", "$2,400 / mo", "Edit"],
                 ["Food", "Groceries and dining", "$900 / mo", "Edit"],
                 ["Transport", "Car and transit", "$420 / mo", "Edit"],
                 ["Utilities", "Power, water, internet", "$280 / mo", "Edit"]], row_h=48, highlight=1)[0])
    p.add(line(L + 18, iy2 + 226, L + LW - 18, iy2 + 226, stroke=HAIR))
    p.add(txt(L + 18, iy2 + 254, "Total", size=12, weight=600, fill=MUTED))
    p.add(txt(L + LW - 36, iy2 + 254, "$4,000 / mo", size=16, weight=600, family="Menlo, monospace", anchor="end"))
    p.add(txt(L + 18, iy2 + 292, "Food changed from $800 to $900. The total and the plan expense update on save.", size=11, fill=FAINT))
    p.add(warn("Deleting a line lowers the total and the plan expense. The save is one request.", L + 18, iy2 + 320, LW - 36, tone="info"))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Edit line")
    p.add(field(x + 18, iy3 + 6, RW - 36, "Category", "Food")[0])
    p.add(field(x + 18, iy3 + 72, RW - 36, "Amount", "$900 / mo", focus=True)[0])
    p.add(field(x + 18, iy3 + 138, RW - 36, "Note", "Groceries and dining")[0])
    b1, w1 = btn(x + 18, iy3 + 208, "Delete line", variant="secondary")
    b2, w2 = btn(x + 18 + w1 + 10, iy3 + 208, "Apply")
    p.add(b1 + b2)
    ix4, iy4, iw4 = p.card(x, 500, RW, 336, "Saved as")
    p.add(txt(x + 18, iy4 + 16, "Living-expense event", size=12, weight=600))
    p.add(txt(x + 18, iy4 + 40, "$4,000 / mo from 2026", size=15, family="Menlo, monospace"))
    p.add(line(x + 18, iy4 + 64, x + RW - 18, iy4 + 64, stroke=HAIR))
    p.add(para(x + 18, iy4 + 92, "One total feeds the engine. The itemized lines stay as the audit trail.", RW - 36, size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 130, "Annual", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 156, "$48,000", size=18, weight=600, family="Menlo, monospace"))
    p.markers([(1, L + 18, 216), (2, L + 18, 436), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Templates offer categories; applying one creates editable line items, not an opaque total."),
        (2, "Editing food to $900 updates the total and stores that total as the living-expense event."),
        (3, "Deleting a line removes it from the total. One request saves the items and the resulting total."),
        (4, "The plan still reads one living-expense event; the itemization is the audit trail behind it."),
    ])


def s058():
    p = Page(58, "Debts · Variable-rate loan", "Dated rate changes, resets, and a cap.", "Assets & debts",
             crumb="Plans / Plan For Retirement / Assets & debts / Mortgage", actions=["Add rate change"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 200, "Adjustable mortgage")
    for i, (lab, val) in enumerate([("Balance", "$420,000"), ("Current rate", "5.00%"), ("Rate cap", "8.00%"), ("Payment", "$2,255 / mo")]):
        p.add(txt(L + 18 + i * 172, iy + 14, lab.upper(), size=10, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(L + 18 + i * 172, iy + 42, val, size=17, weight=600, family="Menlo, monospace"))
    p.add(line(L + 18, iy + 64, L + LW - 18, iy + 64, stroke=HAIR))
    p.add(pill(L + 18, iy + 100, "5.00% FIXED 2026–2030", fg=INK_SOFT)[0])
    p.add(txt(L + 250, iy + 98, "Then resets on each dated change.", size=11, fill=MUTED))
    ix2, iy2, iw2 = p.card(L, 400, LW, 434, "Rate schedule")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("From", 120), ("Market rate", 150), ("Applied rate", 150), ("Payment", 160), ("Note", 120)],
                [["Jan 2026", "5.00%", "5.00%", "$2,255", "Initial"],
                 ["Jan 2031", "6.00%", "6.00%", "$2,686", "Reset"],
                 ["Jan 2033", "7.00%", "7.00%", "$3,027", "Reset"],
                 ["Jan 2035", "9.00%", "8.00%", "$3,265", "Capped"]], row_h=48, highlight=3)[0])
    p.add(txt(L + 18, iy2 + 264, "A market rate above the cap uses the cap. The table shows both values.", size=11, fill=FAINT))
    p.add(txt(L + 18, iy2 + 300, "Changes after payoff have no effect.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Payment by reset")
    p.add(line_chart(x + 18, iy3 + 10, RW - 36, 190,
                     [{"name": "Payment", "values": [2255, 2686, 3027, 3265], "area": True}],
                     x_labels=["2026", "2031", "2033", "2035"], y_max=3600, y_ticks=2))
    p.add(txt(x + 18, iy3 + 222, "Payment recalculates at each reset.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 500, RW, 334, "Add rate change")
    p.add(field(x + 18, iy4 + 6, RW - 36, "Effective date", "Jan 2035")[0])
    p.add(field(x + 18, iy4 + 72, RW - 36, "Market rate", "9.00%", hint="Capped at 8.00% when applied")[0])
    p.add(field(x + 18, iy4 + 152, RW - 36, "Cap", "8.00%")[0])
    b, bw = btn(x + 18, iy4 + 224, "Save rate change")
    p.add(b)
    p.markers([(1, L + 18, 216), (2, L + 18, 450), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "The loan stores dated rate changes: 5% for five years, then 6%, then 7%."),
        (2, "Interest and payment recalculate at each reset. A 9% market rate with an 8% cap applies 8%."),
        (3, "The payment chart follows the applied rate, not the market rate."),
        (4, "Adding a rate change after payoff is stored but has no effect on the result."),
    ])


def s060():
    p = Page(60, "Private equity and VC", "Commitment, capital calls, distributions.", "Assets & debts",
             crumb="Plans / Plan For Retirement / Assets & debts / Private equity", premium=True, frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 210, "Fund")
    p.add(txt(L + 20, iy + 26, "Growth Fund III", size=15, weight=600))
    p.add(pill(L + LW - 150, iy + 12, "ILLIQUID", fg=INK_SOFT)[0])
    for i, (lab, val) in enumerate([("Commitment", "$100,000"), ("Called", "$40,000"), ("Distributed", "$0"), ("NAV", "$46,000")]):
        p.add(txt(L + 18 + i * 172, iy + 68, lab.upper(), size=9.5, weight=700, fill=MUTED, ls=0.4))
        p.add(txt(L + 18 + i * 172, iy + 96, val, size=17, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 18, iy + 138, "20% called per year for five years. Distributions start in year six.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 410, LW, 424, "Capital calls and distributions")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Year", 110), ("Event", 160), ("Amount", 150), ("Cash", 150), ("Invested", 150)],
                [["2026", "Capital call", "$20,000", "− $20,000", "$20,000"],
                 ["2027", "Capital call", "$20,000", "− $20,000", "$40,000"],
                 ["2031", "Distribution", "$12,000", "+ $12,000", "$40,000"],
                 ["2032", "Distribution", "$18,000", "+ $18,000", "$40,000"]], row_h=48)[0])
    p.add(txt(L + 18, iy2 + 268, "Each call lowers cash and raises invested capital. A distribution returns cash.", size=11, fill=FAINT))
    p.add(txt(L + 18, iy2 + 300, "The fund counts in net worth and is excluded from liquid net worth.", size=11.5, fill=INK_SOFT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Net worth split")
    p.add(txt(x + 18, iy3 + 14, "Liquid", size=11, fill=MUTED))
    p.add(txt(x + 18, iy3 + 40, "$1,550,000", size=17, weight=600, family="Menlo, monospace"))
    p.add(txt(x + 18, iy3 + 78, "Illiquid", size=11, fill=MUTED))
    p.add(txt(x + 18, iy3 + 104, "$46,000", size=17, weight=600, family="Menlo, monospace"))
    p.add(rrect(x + 18, iy3 + 130, RW - 36, 18, r=4, fill=FILL, stroke=None))
    p.add(rrect(x + 18, iy3 + 130, (RW - 36) * 0.97, 18, r=4, fill=INK_SOFT, stroke=None))
    p.add(rrect(x + 18 + (RW - 36) * 0.97, iy3 + 130, (RW - 36) * 0.03, 18, r=4, fill=INK, stroke=None))
    p.add(txt(x + 18, iy3 + 170, "Illiquid value is visible but never counted as spendable cash.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 500, RW, 334, "Add call or distribution")
    p.add(select(x + 18, iy4 + 6, RW - 36, "Event", "Capital call")[0])
    p.add(field(x + 18, iy4 + 72, RW - 36, "Year", "2028")[0])
    p.add(field(x + 18, iy4 + 138, RW - 36, "Amount", "$20,000")[0])
    b, bw = btn(x + 18, iy4 + 210, "Save event")
    p.add(b)
    p.markers([(1, L + 18, 216), (2, L + 18, 450), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "A fund stores its commitment, dated capital calls, and distributions."),
        (2, "A call raises invested capital and lowers cash; a distribution returns cash and records realized value."),
        (3, "The fund is included in net worth but marked illiquid and excluded from liquid net worth."),
        (4, "Calls beyond the commitment are rejected with a validation error, not silently trimmed."),
    ])


def s061():
    p = Page(61, "Mortality and life expectancy", "Overlay for survivor paths and horizon.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Mortality", actions=["Rerun plan"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 260, "Mortality overlay")
    p.add(toggle(L + 18, iy + 8, True, "Model mortality"))
    p.add(field(L + 18, iy + 56, 260, "Life expectancy variable", "85", hint="Was 85 · changed to 90 updates horizon", focus=True)[0])
    p.add(txt(L + 18, iy + 140, "Life expectancy is a variable, not a copy. The horizon and FI metrics read it.", size=11, fill=FAINT))
    p.add(warn("With mortality off, the deterministic life-expectancy milestone drives the end of the projection.", L + 18, iy + 168, LW - 36, tone="info"))
    ix2, iy2, iw2 = p.card(L, 460, LW, 374, "Horizon")
    p.add(line_chart(L + 18, iy2 + 10, LW - 36, 260,
                     [{"name": "Net worth · LE 85", "values": [1.55, 2.2, 2.9, 3.2, 2.9, 2.4], "dash": "6 4"},
                      {"name": "Net worth · LE 90", "values": [1.55, 2.2, 2.9, 3.2, 3.0, 2.6], "dash": None}],
                     x_labels=["2026", "2036", "2046", "2056", "2066", "2076"], y_max=4.0,
                     milestone_x=[(4, "LE 85"), (5, "LE 90")]))
    p.add(txt(L + 18, iy2 + 318, "Changing life expectancy from 85 to 90 extends the projection five years and moves FI metrics.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Household")
    p.add(txt(x + 18, iy3 + 14, "You", size=12, weight=600))
    p.add(txt(x + 18, iy3 + 36, "Born Mar 1990 · age 36", size=11, fill=MUTED))
    p.add(txt(x + 18, iy3 + 62, "Life expectancy 90", size=11, family="Menlo, monospace", fill=INK_SOFT))
    p.add(line(x + 18, iy3 + 84, x + RW - 18, iy3 + 84, stroke=HAIR))
    p.add(txt(x + 18, iy3 + 110, "Partner", size=12, weight=600))
    p.add(txt(x + 18, iy3 + 132, "Born Jul 1992 · age 34", size=11, fill=MUTED))
    p.add(txt(x + 18, iy3 + 158, "Life expectancy 88", size=11, family="Menlo, monospace", fill=INK_SOFT))
    p.add(warn("First death in 2045. Survivor keeps the household assets.", x + 18, iy3 + 196, RW - 36))
    ix4, iy4, iw4 = p.card(x, 500, RW, 334, "Survivor filing status")
    for i, (yr, status, active) in enumerate([("2044", "Married filing jointly", False), ("2045", "Single", True)]):
        y = iy4 + 8 + i * 70
        p.add(rrect(x + 18, y, RW - 36, 58, r=10, fill=FILL if active else SURFACE, stroke=BORDER))
        p.add(txt(x + 34, y + 22, yr, size=11, family="Menlo, monospace", fill=MUTED))
        p.add(txt(x + 34, y + 42, status, size=12, weight=600))
    p.add(para(x + 18, iy4 + 170, "Filing status changes from the year of death, and assets stay with the survivor.", RW - 36, size=11, fill=FAINT))
    p.markers([(1, L + 18, 216), (2, L + 18, 500), (3, x + 18, 216), (4, x + 18, 540)])
    return p.footer([
        (1, "Mortality is an overlay on the deterministic plan. Turning it on adds survivor paths; turning it off leaves the milestone horizon."),
        (2, "Life expectancy is a variable. Changing 85 to 90 extends the horizon five years and updates FI metrics."),
        (3, "A couple models the first death and the survivor's filing status from that year."),
        (4, "The survivor keeps household assets, and filing status becomes single from the year of death."),
    ])


def s062():
    p = Page(62, "Safe-to-share", "Read-only, redacted, revocable.", "Data & sharing",
             crumb="Plans / Plan For Retirement / Share", actions=["Revoke link"], frame_h=860)
    ix, iy, iw = p.card(L, 176, LW, 260, "Share link")
    p.add(field(L + 18, iy + 6, 380, "Link", "plan.app/s/7f2c9d", hint="Read-only · expires never")[0])
    p.add(field(L + 420, iy + 6, 200, "Status", "Active")[0])
    b1, w1 = btn(L + 18, iy + 84, "Copy link", variant="secondary")
    b2, w2 = btn(L + 18 + w1 + 10, iy + 84, "Revoke link")
    p.add(b1 + b2)
    p.add(txt(L + 18, iy + 150, "Revoking makes the link return 404 on the next open. Existing recipients are not notified.", size=11, fill=FAINT))
    p.add(warn("The recipient cannot edit, export, or discover the original plan.", L + 18, iy + 176, LW - 36, tone="info"))
    ix2, iy2, iw2 = p.card(L, 460, LW, 374, "Recipient preview")
    p.add(rrect(L + 18, iy2 + 8, LW - 36, 40, r=8, fill=FILL, stroke=None))
    p.add(txt(L + 32, iy2 + 33, "Read-only shared plan · owner redacted amounts", size=11.5, fill=INK_SOFT))
    p.add(txt(L + 32, iy2 + 76, "Plan For Retirement", size=16, weight=600))
    p.add(txt(L + 32, iy2 + 100, "Net worth ███████ · Legacy ███████", size=12.5, family="Menlo, monospace", fill=MUTED))
    p.add(txt(L + 32, iy2 + 140, "Allocation", size=11.5, weight=600))
    p.add(bars(L + 32, iy2 + 158, LW - 64,
               [("Stocks", 60, "60%"), ("Bonds", 40, "40%")], row_h=28, gap=10, max_val=60, label_w=90, value_w=60))
    p.add(txt(L + 32, iy2 + 244, "Milestones · Retirement 2045 · FI 2042 · Life expectancy 2075", size=11.5, fill=MUTED))
    p.add(txt(L + 32, iy2 + 286, "No edit action. No export action. No account details.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 360, "Redaction")
    p.add(select(x + 18, iy3 + 6, RW - 36, "Amounts", "Hidden")[0])
    p.add(select(x + 18, iy3 + 72, RW - 36, "Percentages", "Visible")[0])
    p.add(toggle(x + 18, iy3 + 146, True, "Show plan shape"))
    p.add(toggle(x + 18, iy3 + 182, False, "Show account names"))
    p.add(txt(x + 18, iy3 + 228, "Amounts are hidden or scaled. Percentages and shape remain.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 560, RW, 274, "Access")
    p.add(txt(x + 18, iy4 + 14, "Opened 3 times · last Aug 26 2026", size=11.5, fill=MUTED))
    p.add(txt(x + 18, iy4 + 42, "Recipient can view only", size=12.5, weight=600))
    for i, lab in enumerate(["View plan shape", "No edit, export, or original-plan discovery"]):
        p.add(circle(x + 26, iy4 + 72 + i * 26, 3, fill=INK, stroke=None))
        p.add(txt(x + 40, iy4 + 76 + i * 26, lab, size=11, fill=MUTED))
    p.markers([(1, L + 18, 216), (2, L + 18, 500), (3, x + 18, 216), (4, x + 18, 600)])
    return p.footer([
        (1, "A share link opens a read-only, redacted view with a stable URL that the owner can revoke at any time."),
        (2, "The recipient sees the plan shape, percentages, and milestones. Dollar amounts are hidden or scaled."),
        (3, "Redaction is a server-side setting, so the payload never contains the hidden values."),
        (4, "The recipient cannot edit, export, or discover the original plan; revoking returns 404 on the next open."),
    ])
