"""Wireframe screens, part 1 (issues 2-21)."""

from wirelib import (Page, txt, rrect, line, pill, btn, field, select, tabs, toggle,
                     table, kpi, line_chart, bars, donut, gauge, warn, empty, card, circle, polyline, para,
                     INK, INK_SOFT, MUTED, FAINT, FAINT_FILL, FILL, BG, SURFACE, BORDER, HAIR)

L, W = 272, 1136
LW, GAP, RW = 716, 20, 400


def s002():
    p = Page(2, "Dashboard", "First run: onboarding, then the empty plan state.", "Dashboard",
             crumb="Home", actions=["Add finances"], plan_badge="No plan yet", frame_h=820)
    for i, (lab, val, hint) in enumerate([
            ("Net worth", "$0.00", "from Postgres"), ("Assets", "$0.00", None),
            ("Liabilities", "$0.00", None), ("Plans", "0", "No plans yet")]):
        p.add(kpi(L + i * 284, 176, 268, lab, val, hint=hint))
    ix, iy, iw = p.card(L, 292, LW, 250, "Finish setting up")
    steps = [("Profile", "Birth month/year, state, currency", "done"),
             ("Walkthrough", "Normal or Sandbox", "done"),
             ("Current finances", "Add accounts, assets, debts", "next"),
             ("Create a plan", "Then run the first projection", "todo")]
    for i, (name, desc, state) in enumerate(steps):
        y = iy + i * 46
        p.add(circle_mark(L + 18 + 14, y + 8, state))
        p.add(txt(L + 62, y + 12, name, size=12.5, weight=600 if state != "todo" else 400))
        p.add(txt(L + 190, y + 12, desc, size=11.5, fill=MUTED))
        if state == "next":
            b, bw = btn(L + LW - 130, y - 10, "Start", w=88, h=28, variant="secondary")
            p.add(b)
        if state == "done":
            p.add(txt(L + LW - 24, y + 12, "Done", size=11, fill=FAINT, anchor="end"))
    p.add(empty(L, 558, LW, 210, "No plans yet", "A plan projects your money year by year.", "New plan"))
    xr = L + LW + GAP
    ix, iy, iw = p.card(xr, 292, RW, 476, "Walkthrough mode")
    p.add(txt(xr + 18, iy + 12, "Normal", size=12.5, weight=600))
    p.add(txt(xr + 18, iy + 30, "Collects your own birth date, state, and currency.", size=11.5, fill=MUTED))
    p.add(rrect(xr + 14, iy + 42, RW - 28, 48, r=8, fill=FILL, stroke=None))
    p.add(circle(xr + 34, iy + 66, 8))
    p.add(circle(xr + 34, iy + 66, 4, fill=INK, stroke=None))
    p.add(txt(xr + 54, iy + 70, "Individual or couple · state · currency", size=11.5, fill=INK_SOFT))
    p.add(txt(xr + 18, iy + 128, "Sandbox", size=12.5, weight=600))
    p.add(txt(xr + 18, iy + 146, "Pick a persona. Lands on a populated dashboard.", size=11.5, fill=MUTED))
    for i, persona in enumerate(["Recent Grad · Single", "Mid-career · Couple", "Retired · Couple"]):
        y = iy + 166 + i * 44
        p.add(rrect(xr + 14, y, RW - 28, 36, r=8, fill=SURFACE, stroke=BORDER))
        p.add(circle(xr + 34, y + 18, 7))
        p.add(txt(xr + 52, y + 22, persona, size=12, fill=INK_SOFT))
    p.add(txt(xr + 18, iy + 320, "Sandbox data is labeled and excluded from paid runs.", size=11, fill=FAINT))
    p.markers([(1, L + 128, 176), (2, L + 132, 498), (3, xr + 14, 300), (4, xr + 14, 470)])
    return p.footer([
        (1, "KPI row reads the profile and finances from Postgres, not from client state. Reload restores the same values."),
        (2, "Empty state is explicit: 'No plans yet' plus one New plan action. No invented numbers."),
        (3, "Normal walkthrough collects individual/couple, birth month and year, US state, and currency before the dashboard."),
        (4, "Sandbox selects a persona (for example Recent Grad, Single) and lands on a populated dashboard without personal data."),
    ])


def circle_mark(cx, cy, state):
    if state == "done":
        return rrect(cx - 9, cy - 9, 18, 18, r=5, fill=INK, stroke=None) + txt(cx, cy + 4, "✓", size=10, weight=700, fill="#FFFFFF", anchor="middle")
    if state == "next":
        return rrect(cx - 9, cy - 9, 18, 18, r=5, fill=SURFACE, stroke=INK, sw=2) + rrect(cx - 3, cy - 3, 6, 6, r=2, fill=INK, stroke=None)
    return rrect(cx - 9, cy - 9, 18, 18, r=5, fill=SURFACE, stroke=BORDER, dash="3 2")


def s003():
    p = Page(3, "Current finances", "Accounts the engine reads for taxes and drawdown.", "Current Finances",
             crumb="Home / Current finances", actions=["Add account"], frame_h=860)
    p.add(tabs(L, 162, ["Overview", "Investments", "Assets & debts", "Progress"], active=1)[0])
    for i, (lab, val, hint) in enumerate([("Investments", "$511,111", "4 accounts"),
                                          ("Cost basis", "$210,278", "taxable only"),
                                          ("Net worth", "$511,111", "after save")]):
        p.add(kpi(L + i * 240, 218, 224, lab, val, hint=hint, h=84))
    ix, iy, iw = p.card(L, 318, LW, 340, "Investments")
    cols = [("Account", 226), ("Owner", 92), ("Balance", 132), ("Cost / contributions", 200)]
    rows = [["Savings", "You", "$92,000", "—"],
            ["401(k)", "You", "$511,111", "—"],
            ["Roth IRA", "You", "$120,000", "Contributions $84,000"],
            ["Taxable brokerage", "Joint", "$420,555", "Cost $210,278"],
            ["HSA", "You", "$18,500", "—"]]
    p.add(table(L + 18, iy, LW - 36, cols, rows, row_h=38, highlight=1)[0])
    p.add(txt(L + 18, iy + 32 + 38 * 5 + 24, "Row editor: type, balance, owner, cost basis or contributions.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 318, RW, 396, "Add account")
    p.add(select(x + 18, iy2 + 4, RW - 36, "Type", "401(k)")[0])
    p.add(field(x + 18, iy2 + 70, RW - 36, "Balance", "$511,111")[0])
    p.add(select(x + 18, iy2 + 136, RW - 36, "Owner", "You")[0])
    p.add(field(x + 18, iy2 + 202, RW - 36, "Cost basis", "$210,278", hint="Used by capital-gains estimates")[0])
    p.add(toggle(x + 18, iy2 + 272, True, "Employer-sponsored"))
    b1, w1 = btn(x + 18, iy2 + 310, "Cancel", variant="secondary")
    b2, w2 = btn(x + 18 + w1 + 10, iy2 + 310, "Save account")
    p.add(b1 + b2)
    p.add(warn("Cost basis is required for taxable accounts and crypto.", x + 18, iy2 + 356, RW - 36, tone="info"))
    p.markers([(1, L + LW + GAP + 18, 366), (2, L + 18 + 226, 392), (3, x + 18, 528), (4, L + 258, 218)])
    return p.footer([
        (1, "Add account covers savings, taxable, 401(k), Roth 401(k), IRA, Roth IRA, HSA, and 529. One form, type-specific fields."),
        (2, "Mixed owners stay visible per row: You, Partner, or Joint. No owner is inferred."),
        (3, "Cost basis edits persist and feed capital-gains estimates. The row shows Cost or Contributions, never both."),
        (4, "Saving the 401(k) at $511,111 raises the Investments total and net worth by the same amount without a reload."),
    ])


def s004():
    p = Page(4, "Current finances · Assets & debts", "Assets and liabilities stay separate so net worth is auditable.", "Current Finances",
             crumb="Home / Current finances / Assets & debts", actions=["Add asset", "Add debt"], frame_h=890)
    p.add(tabs(L, 162, ["Overview", "Investments", "Assets & debts", "Progress"], active=2)[0])
    for i, (lab, val, note) in enumerate([("Assets", "$289,000", "House + car"), ("Liabilities", "$56,974", "Mortgage only"), ("Net worth", "$232,026", "Assets − Liabilities")]):
        p.add(rrect(L + i * 376, 218, 360, 120, r=12, fill=SURFACE, stroke=BORDER))
        p.add(gauge(L + i * 376 + 180, 286, 54, [0.62, 0.24, 0.82][i], lab, val))
    ix, iy, iw = p.card(L, 356, LW, 180, "Real assets")
    p.add(table(L + 18, iy + 8, LW - 36,
                [("Asset", 220), ("Owner", 96), ("Value", 130), ("Financed", 120)],
                [["House", "You", "$289,000", "Yes · mortgage"],
                 ["Car", "Joint", "$18,000", "No"]], row_h=38)[0])
    ix, iy, iw = p.card(L, 556, LW, 300, "Debts")
    p.add(table(L + 18, iy + 8, LW - 36,
                [("Debt", 190), ("Balance", 120), ("APR", 74), ("Payment", 110), ("Term", 96)],
                [["Mortgage", "$56,974", "6.00%", "$1,702 / mo", "27 yr left"],
                 ["Student loan", "$30,000", "6.00%", "$333 / mo", "10 yr"]], row_h=38)[0])
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 356, RW, 520, "Add financed asset")
    p.add(select(x + 18, iy2 + 4, RW - 36, "Asset type", "House")[0])
    p.add(field(x + 18, iy2 + 70, RW - 36, "Value", "$289,000")[0])
    p.add(select(x + 18, iy2 + 136, RW - 36, "Owner", "You")[0])
    p.add(toggle(x + 18, iy2 + 202, True, "Financed"))
    p.add(line(x + 18, iy2 + 226, x + RW - 18, iy2 + 226, stroke=HAIR))
    p.add(field(x + 18, iy2 + 250, RW - 36, "Mortgage balance", "$56,974")[0])
    p.add(field(x + 18, iy2 + 316, RW - 36, "APR", "6.00%")[0])
    p.add(field(x + 18, iy2 + 382, (RW - 46) / 2, "Payment", "$1,702")[0])
    p.add(field(x + 18 + (RW - 46) / 2 + 10, iy2 + 382, (RW - 46) / 2, "Term", "27 yr")[0])
    b, bw = btn(x + 18, iy2 + 432, "Save asset and liability")
    p.add(b)
    p.markers([(1, L + 18 + 130, 410), (2, L + 18 + 190, 642), (3, x + 18, 470), (4, x + 18, 560)])
    return p.footer([
        (1, "A financed asset writes two rows: the asset value here and a liability below. The house shows $289,000; the mortgage $56,974."),
        (2, "Debt rows carry balance, APR, payment, and term. Payoff behaviour ships in a later slice (#15)."),
        (3, "Turning Financed on reveals mortgage fields without a second form. Turning it off removes the liability row on save."),
        (4, "Gauges and the header agree: Assets $289,000 − Liabilities $56,974 = Net worth $232,026."),
    ])


def s005():
    p = Page(5, "Current finances · Net worth", "Three gauges plus dated progress points.", "Current Finances",
             crumb="Home / Current finances", actions=["Add progress point"], frame_h=840)
    p.add(tabs(L, 162, ["Overview", "Investments", "Assets & debts", "Progress"], active=0)[0])
    for i, (lab, val, note) in enumerate([("Net worth", "$1.55M", "Assets − Liabilities"), ("Assets", "$1.61M", "5 accounts · 2 assets"), ("Liabilities", "$56.97K", "1 mortgage")]):
        p.add(rrect(L + i * 376, 218, 360, 132, r=12, fill=SURFACE, stroke=BORDER))
        p.add(txt(L + i * 376 + 18, 240, lab.upper(), size=10.5, weight=700, fill=MUTED, ls=0.6))
        p.add(txt(L + i * 376 + 18, 292, val, size=30, weight=600, family="Menlo, monospace"))
        p.add(txt(L + i * 376 + 18, 318, note, size=11.5, fill=MUTED))
        p.add(txt(L + i * 376 + 18, 336, "Aug 26 2026", size=10.5, fill=FAINT))
    p.add(line(L, 370, L + W, 370, stroke=HAIR))
    p.add(txt(L, 396, "Net worth = Assets − Liabilities. The header uses the same response.", size=11.5, fill=MUTED))
    ix, iy, iw = p.card(L, 418, LW, 386, "Progress points", sub="Newest first · 12 per page")
    p.add(table(L + 18, iy + 14, LW - 36,
                [("Date", 190), ("Net worth", 140), ("Assets", 140), ("Liabilities", 130)],
                [["Aug 26 2026", "$1.60M", "$1.61M", "$56.97K"],
                 ["Aug 8 2026", "$1.50M", "$1.55M", "$52.00K"],
                 ["Nov 30 2025", "$1.30M", "$1.32M", "$18.40K"]], row_h=40, highlight=0)[0])
    p.add(txt(L + 18, iy + 210, "Each save of a finance change writes one dated point.", size=11, fill=FAINT))
    for i, lab in enumerate(["1", "2", "3", "…"]):
        p.add(rrect(L + 18 + i * 34, iy + 236, 28, 28, r=6, fill=FILL if i == 0 else SURFACE, stroke=BORDER))
        p.add(txt(L + 18 + i * 34 + 14, iy + 255, lab, size=11, anchor="middle", fill=INK_SOFT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 418, RW, 230, "Overlay on projection")
    p.add(txt(x + 18, iy2 + 12, "Show actual progress points against a fixed-date plan.", size=11.5, fill=MUTED))
    p.add(toggle(x + 18, iy2 + 36, True, "Overlay actual points"))
    p.add(line_chart(x + 18, iy2 + 72, RW - 36, 116,
                     [{"name": "Projection", "values": [1.55, 1.9, 2.4, 2.9, 3.4], "dash": None}],
                     x_labels=["2026", "2030", "2034", "2038", "2042"], y_max=4.0, y_ticks=2))
    p.add(warn("Actual points snap to the nearest projection year.", x + 18, iy2 + 192, RW - 36, tone="info"))
    p.markers([(1, L + 18, 240), (2, L + 18, 470), (3, x + 18, 462), (4, x + 18, 676)])
    return p.footer([
        (1, "Gauges read one API response. Assets $1.61M and liabilities $56.97K must equal net worth $1.55M exactly, to the cent."),
        (2, "Progress points are dated snapshots of net worth, assets, and liabilities, newest first, paginated with a stable cursor."),
        (3, "Overlay places actual points on an existing fixed-date projection. This slice forecasts nothing."),
        (4, "A saved finance change writes exactly one progress point. Editing without saving writes none."),
    ])


def s006():
    p = Page(6, "Plans", "Create a plan from current finances or from a frozen date.", "Plans",
             crumb="Home / Plans", actions=["New plan"], plan_badge="2 plans", frame_h=840)
    ix, iy, iw = p.card(L, 176, LW, 216, "Your plans")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Plan", 280), ("Started", 170), ("Mode", 180), ("Updated", 130)],
                [["Plan For Retirement", "Jan 2026", "Fixed date", "Aug 26 2026"],
                 ["Second Opinion", "Aug 2026", "Current finances", "Aug 12 2026"]], row_h=40)[0])
    p.add(txt(L + 18, iy + 132, "Plan name, icon, and notes appear in the sidebar and plan header.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 176, RW, 664, "Create plan")
    p.add(field(x + 18, iy2 + 4, RW - 36, "Plan name", "Plan For Retirement")[0])
    p.add(txt(x + 18, iy2 + 92, "Icon", size=10.5, weight=600, fill=MUTED, ls=0.4))
    for i in range(6):
        p.add(rrect(x + 18 + i * 44, iy2 + 102, 32, 32, r=8, fill=FILL if i == 0 else SURFACE, stroke=INK if i == 0 else BORDER))
        p.add(rrect(x + 28 + i * 44, iy2 + 112, 12, 12, r=3, fill=INK if i == 0 else FAINT_FILL, stroke=None))
    p.add(field(x + 18, iy2 + 168, RW - 36, "Notes", "Long-term plan, review each January", placeholder=True)[0])
    p.add(txt(x + 18, iy2 + 262, "Starting point", size=10.5, weight=600, fill=MUTED, ls=0.4))
    p.add(rrect(x + 18, iy2 + 272, RW - 36, 86, r=10, fill=SURFACE, stroke=BORDER))
    p.add(circle(x + 40, iy2 + 302, 8))
    p.add(txt(x + 60, iy2 + 306, "From current finances", size=12.5, weight=600))
    p.add(txt(x + 60, iy2 + 324, "Follows later finance edits.", size=11, fill=MUTED))
    p.add(rrect(x + 18, iy2 + 370, RW - 36, 120, r=10, fill=FILL, stroke=INK, sw=2))
    p.add(circle(x + 40, iy2 + 400, 8) + circle(x + 40, iy2 + 400, 4, fill=INK, stroke=None))
    p.add(txt(x + 60, iy2 + 404, "From a fixed date", size=12.5, weight=600))
    p.add(txt(x + 60, iy2 + 422, "Frozen starting balances.", size=11, fill=MUTED))
    p.add(txt(x + 60, iy2 + 448, "Jan 2026", size=12, family="Menlo, monospace"))
    p.add(pill(x + RW - 106, iy2 + 404, "FROZEN", fg=INK_SOFT)[0])
    p.add(field(x + 18, iy2 + 512, 150, "Start date", "2026-01-01")[0])
    b, bw = btn(x + 18, iy2 + 570, "Create plan")
    p.add(b)
    p.markers([(1, L + 18, 240), (2, x + 18, 232), (3, x + 18, 452), (4, x + 18, 700)])
    return p.footer([
        (1, "Plans show name, icon, mode, and updated date. Icon, notes, and name appear in the sidebar and plan header."),
        (2, "Name and notes persist as typed. Validation is UX-only; the backend is authoritative."),
        (3, "Fixed date freezes the starting point. After Jan 2026, balance edits in Current Finances leave this plan's start balances untouched."),
        (4, "Current-finances mode follows later edits, so the same finance change moves this plan's starting conditions."),
    ])


def s009():
    p = Page(9, "Income · Other income", "Pension, Social Security, rental, and inheritance.", "Income",
             crumb="Plans / Plan For Retirement / Income", actions=["Add income"], frame_h=880)
    p.add(tabs(L, 162, ["Salary", "Social Security", "Pension", "Rental", "Inheritance"], active=1)[0])
    ix, iy, iw = p.card(L, 218, LW, 300, "Income sources")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Source", 180), ("Owner", 90), ("Amount", 150), ("Starts", 140), ("Tax treatment", 120)],
                [["Social Security", "You", "$30,000 / yr", "Age 67 · 2057", "Provisional"],
                 ["Pension", "You", "$24,000 / yr", "Jan 2038", "Ordinary"],
                 ["Rental", "Joint", "$2,500 / mo", "2026", "Schedule E"],
                 ["Inheritance", "You", "$150,000", "2041", "Not income"]], row_h=44)[0])
    p.add(txt(L + 18, iy + 208, "Rental is 50% rented: only the rental share enters cash flow and tax.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 534, LW, 270, "Social Security estimate", sub="Computed by the backend, never in the browser")
    for i, (lab, val) in enumerate([("Benefit at 67", "$30,000 / yr"), ("Other income", "$20,000"), ("Provisional income", "$35,000"), ("Taxable Social Security", "$5,350")]):
        y = iy2 + 8 + i * 44
        p.add(txt(L + 20, y + 12, lab, size=11.5, fill=MUTED))
        p.add(txt(L + LW - 36, y + 12, val, size=12.5, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(L + 18, y + 26, L + LW - 18, y + 26, stroke=HAIR))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 218, RW, 586, "Add income")
    p.add(select(x + 18, iy3 + 4, RW - 36, "Type", "Social Security")[0])
    p.add(select(x + 18, iy3 + 70, RW - 36, "Owner", "You")[0])
    p.add(field(x + 18, iy3 + 136, RW - 36, "Annual amount", "$30,000")[0])
    p.add(field(x + 18, iy3 + 202, (RW - 46) / 2, "Start age", "67")[0])
    p.add(field(x + 18 + (RW - 46) / 2 + 10, iy3 + 202, (RW - 46) / 2, "Start year", "2057")[0])
    p.add(select(x + 18, iy3 + 268, RW - 36, "Tax treatment", "Provisional income")[0])
    p.add(warn("Taxable Social Security depends on other income. The engine estimates it each year.", x + 18, iy3 + 348, RW - 36, tone="info"))
    b, bw = btn(x + 18, iy3 + 420, "Save income")
    p.add(b)
    p.markers([(1, L + 18, 262), (2, L + 18, 570), (3, x + 18, 276), (4, x + 18, 626)])
    return p.footer([
        (1, "Each source stores timing, amount, owner, and tax treatment. The pension row starts exactly in its payout year."),
        (2, "Provisional income and taxable Social Security come from the backend. The UI shows the estimate and its inputs, never the formula."),
        (3, "Amount and start fields switch by type: pension asks payout start; inheritance asks year only; rental asks rent and rented share."),
        (4, "Tax treatment is explicit per source so later tax slices do not reopen this form."),
    ])


def s011():
    p = Page(11, "Expenses · Healthcare, childcare, charity", "Typed expenses that carry tax meaning.", "Expenses & flows",
             crumb="Plans / Plan For Retirement / Expenses", actions=["Add expense"], frame_h=880)
    p.add(tabs(L, 162, ["Living", "Healthcare", "Childcare & education", "Charity"], active=1)[0])
    ix, iy, iw = p.card(L, 218, LW, 336, "Typed expenses")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Expense", 170), ("Amount", 130), ("Starts", 110), ("Ends", 100), ("Tax treatment", 150)],
                [["Medicare", "$2,900 / yr", "Jan 2055", "—", "Medical"],
                 ["ACA Marketplace", "$9,600 / yr", "2026", "2054", "Premium tax credit"],
                 ["Childcare", "$1,800 / mo", "2026", "2031", "Not deductible"],
                 ["Charitable gifts (QCD)", "$5,000 / yr", "2030", "—", "QCD exclusion"]], row_h=44)[0])
    p.add(txt(L + 18, iy + 250, "Subtype drives the tax fields. One row per typed expense.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 570, LW, 234, "Healthcare line by year", sub="Medicare starts Jan 2055 at $2,900, then rises with healthcare inflation")
    p.add(line_chart(L + 18, iy2 + 6, LW - 36, 130,
                     [{"name": "$ / yr", "values": [0, 0, 0, 2900, 3300, 3800, 4300], "area": True}],
                     x_labels=["2049", "2052", "2055", "2058", "2061", "2064", "2067"], y_max=5200, y_ticks=2))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 218, RW, 500, "Add expense")
    p.add(select(x + 18, iy3 + 4, RW - 36, "Type", "Healthcare")[0])
    p.add(select(x + 18, iy3 + 70, RW - 36, "Subtype", "Medicare")[0])
    p.add(field(x + 18, iy3 + 136, RW - 36, "Amount", "$2,900 / yr")[0])
    p.add(field(x + 18, iy3 + 202, (RW - 46) / 2, "Start", "Jan 2055")[0])
    p.add(field(x + 18 + (RW - 46) / 2 + 10, iy3 + 202, (RW - 46) / 2, "End", "—")[0])
    p.add(select(x + 18, iy3 + 268, RW - 36, "Inflation", "Healthcare 4.5%")[0])
    p.add(toggle(x + 18, iy3 + 350, True, "Eligibility-based start"))
    b, bw = btn(x + 18, iy3 + 396, "Save expense")
    p.add(b)
    p.markers([(1, L + 18, 262), (2, L + 18, 606), (3, x + 18, 330), (4, x + 18, 486)])
    return p.footer([
        (1, "Typed expenses keep the subtype and its tax fields. Medicare is $0 before 2055 and $2,900 in 2055, rising with healthcare inflation."),
        (2, "The preview line comes from the backend run, so it matches the projection. No client-side inflation math."),
        (3, "Childcare ends automatically at the set end date (5 years in the example), and the row stops contributing."),
        (4, "Charitable treatment follows the chosen form: cash, securities, QCD, or DAF. ACA reconciliation ships in #48."),
    ])


def s013():
    p = Page(13, "Flows", "Transfers, debt payments, and leftover income.", "Expenses & flows",
             crumb="Plans / Plan For Retirement / Flows", actions=["Add flow"], frame_h=860)
    p.add(tabs(L, 162, ["Living", "Flows", "Leftover income"], active=1)[0])
    ix, iy, iw = p.card(L, 218, LW, 316, "Flows")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Flow", 210), ("From", 120), ("To", 130), ("Amount", 130), ("Frequency", 90)],
                [["Monthly savings", "Checking", "Taxable brokerage", "$500", "Monthly"],
                 ["Debt payment", "Checking", "Mortgage", "$1,702", "Monthly"],
                 ["Annual gift", "Taxable brokerage", "529 plan", "$6,000", "Yearly"]], row_h=44)[0])
    p.add(txt(L + 18, iy + 214, "A transfer moves money. Net worth is unchanged by the transfer itself.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 550, LW, 254, "Leftover income", sub="Anything left after expenses, debt, and savings flows")
    p.add(rrect(L + 18, iy2 + 4, LW - 36, 62, r=8, fill=FILL, stroke=None))
    p.add(circle(L + 40, iy2 + 34, 8) + circle(L + 40, iy2 + 34, 4, fill=INK, stroke=None))
    p.add(txt(L + 60, iy2 + 38, "Save", size=12.5, weight=600))
    p.add(txt(L + 120, iy2 + 38, "route to cash", size=11.5, fill=MUTED))
    p.add(circle(L + 40, iy2 + 80, 8))
    p.add(txt(L + 60, iy2 + 84, "Spend", size=12.5))
    p.add(txt(L + 120, iy2 + 84, "discretionary spending", size=11.5, fill=MUTED))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 218, RW, 336, "This month", sub="Transfer preview · backend result")
    for i, (lab, val) in enumerate([("Checking", "− $500"), ("Taxable brokerage", "+ $500"), ("Net worth", "$0 change")]):
        y = iy3 + 10 + i * 54
        p.add(txt(x + 20, y + 12, lab, size=12, fill=INK_SOFT))
        p.add(txt(x + RW - 20, y + 12, val, size=13, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 30, x + RW - 18, y + 30, stroke=HAIR))
    p.add(warn("Yearly total: savings −$6,000, taxable +$6,000.", x + 18, iy3 + 196, RW - 36, tone="info"))
    p.add(warn("Mandatory payment $1,702 could not be met in 2038. Shortfall recorded and warned.", x + 18, 586, RW - 36))
    p.markers([(1, L + 18, 262), (2, L + 18 + 210, 350), (3, x + 18, 272), (4, x + 18, 586)])
    return p.footer([
        (1, "Each flow stores source, destination, amount, and frequency. Frequency supports monthly, yearly, and one-off dates."),
        (2, "A $500 monthly transfer lowers savings and raises taxable by $500; net worth does not move."),
        (3, "The preview is a backend result for the selected month, so the UI never computes balances itself."),
        (4, "A mandatory payment that cannot be met becomes an explicit shortfall with a warning, never a silent negative balance."),
    ])


def s016():
    p = Page(16, "Debts · Extra payments", "Dated extra payments shorten payoff and cut interest.", "Assets & debts",
             crumb="Plans / Plan For Retirement / Assets & debts", actions=["Add extra payment"], frame_h=860)
    ix, iy, iw = p.card(L, 176, LW, 190, "Student loan")
    for i, (lab, val) in enumerate([("Balance", "$30,000"), ("APR", "6.00%"), ("Payment", "$333 / mo"), ("Term", "10 yr")]):
        p.add(txt(L + 18 + i * 172, iy + 14, lab.upper(), size=10, weight=700, fill=MUTED, ls=0.5))
        p.add(txt(L + 18 + i * 172, iy + 42, val, size=17, weight=600, family="Menlo, monospace"))
    p.add(line(L + 18, iy + 62, L + LW - 18, iy + 62, stroke=HAIR))
    p.add(txt(L + 18, iy + 88, "Baseline payoff", size=11, fill=MUTED))
    p.add(txt(L + 18, iy + 108, "Jan 2036", size=13, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 190, iy + 88, "With extra payment", size=11, fill=MUTED))
    p.add(txt(L + 190, iy + 108, "Aug 2031", size=13, weight=600, family="Menlo, monospace"))
    p.add(txt(L + 362, iy + 88, "Interest saved", size=11, fill=MUTED))
    p.add(txt(L + 362, iy + 108, "$3,140", size=13, weight=600, family="Menlo, monospace"))
    ix2, iy2, iw2 = p.card(L, 388, LW, 300, "Extra payments")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Amount", 150), ("Starts", 130), ("Ends", 120), ("Frequency", 130), ("Type", 130)],
                [["$200 / mo", "Sep 2026", "Payoff", "Monthly", "Fixed"],
                 ["$100 / mo", "Jan 2028", "Dec 2029", "Monthly", "Fixed"]], row_h=44)[0])
    p.add(txt(L + 18, iy2 + 172, "Payments stop automatically when the balance reaches zero.", size=11, fill=FAINT))
    p.add(warn("A percentage-of-balance extra payment recalculates as the balance falls.", L + 18, iy2 + 200, LW - 36, tone="info"))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 300, "Payoff comparison")
    for i, (lab, frac, val) in enumerate([("Baseline", 1.0, "2036"), ("Extra $200", 0.68, "2031")]):
        y = iy3 + 14 + i * 66
        p.add(txt(x + 18, y + 12, lab, size=12, fill=INK_SOFT))
        p.add(rrect(x + 18, y + 24, RW - 106, 18, r=4, fill=FILL, stroke=None))
        p.add(rrect(x + 18, y + 24, (RW - 106) * frac, 18, r=4, fill=INK_SOFT if i == 0 else INK, stroke=None))
        p.add(txt(x + RW - 20, y + 39, val, size=11.5, family="Menlo, monospace", anchor="end"))
    p.add(txt(x + 18, iy3 + 158, "Interest: $9,960 baseline → $6,820 with extra.", size=11, fill=FAINT))
    ix4, iy4, iw4 = p.card(x, 498, RW, 300, "Add extra payment")
    p.add(field(x + 18, iy4 + 4, RW - 36, "Amount", "$200 / mo")[0])
    p.add(field(x + 18, iy4 + 70, (RW - 46) / 2, "Start", "Sep 2026")[0])
    p.add(field(x + 18 + (RW - 46) / 2 + 10, iy4 + 70, (RW - 46) / 2, "End", "Payoff")[0])
    p.add(select(x + 18, iy4 + 136, RW - 36, "Frequency", "Monthly")[0])
    b, bw = btn(x + 18, iy4 + 208, "Save extra payment")
    p.add(b)
    p.markers([(1, L + 18, 240), (2, L + 18, 448), (3, x + 18, 250), (4, x + 18, 556)])
    return p.footer([
        (1, "A $30,000 student loan at 6% with $333/month pays off in 2036. Adding $200/month moves payoff to 2031 and lowers total interest."),
        (2, "Extra payments are dated and repeat on a chosen frequency. The editor rejects an end date before the start date."),
        (3, "The comparison reads two backend results: baseline and modified. The UI does not model amortization."),
        (4, "Payments stop at a zero balance, and cash flow updates in that year."),
    ])


def s017():
    p = Page(17, "Milestones", "Four defaults every plan needs.", "Milestones",
             crumb="Plans / Plan For Retirement / Milestones", actions=["Add milestone"], frame_h=860)
    cards = [("Retirement", "2045 · age 55", "Stops salary", "On chart"),
             ("Life Expectancy", "2075 · age 85", "Ends projection", "On chart"),
             ("Financial Independence", "25× spending", "Completes 2042", "On chart"),
             ("Debt Free", "Total debt $0", "Completes 2036", "On chart")]
    for i, (name, target, note, toggle_lab) in enumerate(cards):
        x = L + (i % 2) * (LW / 2 + 8)
        y = 176 + (i // 2) * 150
        p.add(rrect(x, y, LW / 2 - 8, 134, r=12, fill=SURFACE, stroke=BORDER))
        p.add(rrect(x + 18, y + 18, 32, 32, r=8, fill=FILL, stroke=BORDER))
        p.add(txt(x + 62, y + 32, name, size=13.5, weight=600))
        p.add(txt(x + 62, y + 52, target, size=11.5, fill=MUTED))
        p.add(txt(x + 18, y + 84, note, size=11.5, fill=INK_SOFT))
        p.add(toggle(x + 18, y + 98, True, "Shown on chart", size=11.5))
    p.add(warn("Retirement can stop income. Life expectancy ends the projection. Both are used by every run.", L, 486, LW))
    ix, iy, iw = p.card(L, 550, LW, 254, "Chart markers", sub="Retirement 2045 · Debt free 2036 · FI 2042 · Life expectancy 2075")
    p.add(line_chart(L + 18, iy + 4, LW - 36, 150,
                     [{"name": "Net worth", "values": [1.55, 2.1, 2.8, 3.1, 3.0, 2.7, 2.4], "area": True}],
                     x_labels=["2026", "2034", "2042", "2050", "2058", "2066", "2075"], y_max=3.6, y_ticks=2,
                     milestone_x=[(1, "Debt free"), (3, "FI"), (2, "Retire"), (6, "End")]))
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 176, RW, 628, "Retirement")
    p.add(select(x + 18, iy2 + 4, RW - 36, "Target", "Age 55")[0])
    p.add(field(x + 18, iy2 + 70, RW - 36, "Year", "2045", hint="Derived from birth year and target age")[0])
    p.add(toggle(x + 18, iy2 + 140, True, "Stops salary income"))
    p.add(toggle(x + 18, iy2 + 176, False, "Starts Social Security early"))
    p.add(line(x + 18, iy2 + 208, x + RW - 18, iy2 + 208, stroke=HAIR))
    p.add(txt(x + 18, iy2 + 234, "Criteria", size=12, weight=600))
    p.add(txt(x + 18, iy2 + 254, "Age is 55. Custom criteria and actions ship in #17.", size=11, fill=MUTED))
    p.add(txt(x + 18, iy2 + 292, "Appears in", size=12, weight=600))
    for i, lab in enumerate(["Chart", "Yearly summary", "What-if"]):
        p.add(rrect(x + 18 + i * 118, iy2 + 304, 108, 30, r=8, fill=FILL, stroke=None))
        p.add(txt(x + 18 + i * 118 + 54, iy2 + 323, lab, size=11, anchor="middle", fill=INK_SOFT))
    b, bw = btn(x + 18, iy2 + 372, "Save milestone")
    p.add(b)
    p.markers([(1, L + 18, 312), (2, L + 18, 606), (3, x + 18, 252), (4, x + 18, 560)])
    return p.footer([
        (1, "The four defaults are always available: Retirement, Life Expectancy, Financial Independence, and Debt Free."),
        (2, "Markers come from the run result. Retirement at 2045 (age 55) places a marker and stops salary in that year."),
        (3, "Financial Independence completes at 25× spending: the first year net worth crosses the target."),
        (4, "Life Expectancy 2075 (age 85) ends the chart at 2075. Changing it changes the projection horizon."),
    ])


def s018():
    p = Page(18, "Milestone criteria and actions", "Criteria combine metrics with AND or OR.", "Milestones",
             crumb="Plans / Plan For Retirement / Milestones / Retirement", actions=["Delete"], frame_h=880)
    ix, iy, iw = p.card(L, 176, LW, 348, "Criteria")
    rows = [["Age", "≥", "55", "Target year"], ["Net worth", "≥", "$1,000,000", "Target year"]]
    p.add(table(L + 18, iy + 6, LW - 36, [("Metric", 210), ("Comparator", 130), ("Value", 180), ("Timing", 150)], rows, row_h=44)[0])
    p.add(txt(L + 18, iy + 130, "Match", size=11, weight=600, fill=MUTED))
    for i, lab in enumerate(["AND", "OR"]):
        p.add(rrect(L + 70 + i * 74, iy + 116, 64, 28, r=6, fill=INK if i == 0 else SURFACE, stroke=None if i == 0 else BORDER))
        p.add(txt(L + 102 + i * 74, iy + 135, lab, size=11.5, weight=600, anchor="middle", fill="#FFFFFF" if i == 0 else INK_SOFT))
    p.add(txt(L + 18, iy + 176, "Completion is checked each year. A before-age or before-year criterion can complete early.", size=11, fill=FAINT))
    p.add(line(L + 18, iy + 196, L + LW - 18, iy + 196, stroke=HAIR))
    p.add(txt(L + 18, iy + 222, "Result", size=12, weight=600))
    p.add(txt(L + 18, iy + 246, "Age 55 (2045): net worth $900,000 → not complete.", size=11.5, fill=INK_SOFT))
    p.add(txt(L + 18, iy + 266, "2047: net worth reaches $1,000,000 → completes in 2047.", size=11.5, weight=600))
    ix2, iy2, iw2 = p.card(L, 548, LW, 290, "Actions when complete")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Action", 220), ("Value", 210), ("Starts", 130)],
                [["Stop salary", "—", "Completion year"],
                 ["Increase spending", "$9,000 / mo", "Completion year"],
                 ["Relocate", "Florida", "Completion year"]], row_h=44)[0])
    p.add(txt(L + 18, iy2 + 170, "An action applies from the completion year, never earlier.", size=11, fill=FAINT))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 420, "Add action")
    p.add(select(x + 18, iy3 + 4, RW - 36, "Action", "Relocate")[0])
    p.add(select(x + 18, iy3 + 70, RW - 36, "Destination", "Florida")[0])
    p.add(field(x + 18, iy3 + 136, RW - 36, "Tax treatment from", "2035")[0])
    p.add(toggle(x + 18, iy3 + 206, True, "Apply state tax change"))
    b, bw = btn(x + 18, iy3 + 260, "Add action")
    p.add(b)
    ix4, iy4, iw4 = p.card(x, 618, RW, 220, "Timeline")
    for i, (yr, lab, frac) in enumerate([("2045", "Not complete", 0.5), ("2047", "Completes · relocation", 1.0)]):
        y = iy4 + 6 + i * 66
        p.add(txt(x + 18, y + 12, yr, size=11.5, family="Menlo, monospace"))
        p.add(txt(x + 84, y + 12, lab, size=11.5, fill=MUTED))
        p.add(rrect(x + 18, y + 24, RW - 36, 10, r=5, fill=FILL, stroke=None))
        p.add(rrect(x + 18, y + 24, (RW - 36) * frac, 10, r=5, fill=INK if i else FAINT_FILL, stroke=None))
    p.markers([(1, L + 18, 240), (2, L + 69, 590), (3, x + 18, 244), (4, x + 18, 652)])
    return p.footer([
        (1, "Criteria store metric, comparator, value, and timing. AND requires every row; OR requires one."),
        (2, "Actions change income, spending, location, or tax from the completion year. No action fires in a year the milestone is unmet."),
        (3, "Relocation changes jurisdiction and state tax from the completion year and leaves earlier years untouched."),
        (4, "The result line proves the rule: $900,000 at 55 does not complete; completion waits for 2047."),
    ])


def s019():
    p = Page(19, "Projection", "Annual pipeline result. Backend only.", "Projection",
             crumb="Plans / Plan For Retirement / Projection", actions=["Run settings", "Run plan"], frame_h=880)
    p.add(pill(L, 168, "RESULT v12 · Aug 26 2026 14:02")[0])
    p.add(txt(L + 260, 166, "Salary $220,000 · living expenses $8,000/mo · retire 2045", size=11.5, fill=MUTED))
    ix, iy, iw = p.card(L, 200, LW, 376, "Net worth by year")
    p.add(line_chart(L + 18, iy + 10, LW - 36, 280,
                     [{"name": "Net worth", "values": [1.55, 2.0, 2.5, 3.0, 3.4, 3.3, 3.1, 2.9, 2.7], "area": True}],
                     x_labels=["2026", "2036", "2045", "2055", "2065", "2075"], y_max=4.0,
                     milestone_x=[(4, "Retire 2045")]))
    p.add(txt(L + 18, iy + 330, "Rising to 2045, then drawdown. Rerunning replaces this chart from the new result.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 596, LW, 240, "Run")
    p.add(table(L + 18, iy2 + 6, LW - 36,
                [("Run", 140), ("Started", 170), ("Duration", 120), ("Status", 160)],
                [["v12", "14:02:08", "1.8 s", "Complete"],
                 ["v11", "13:41:55", "1.7 s", "Complete"]], row_h=40)[0])
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 200, RW, 300, "2036 snapshot")
    for i, (lab, val) in enumerate([("Net worth", "$3,409,056"), ("Income", "$234,604"), ("Taxes", "$75,102"), ("Spending", "$107,741")]):
        y = iy3 + 8 + i * 44
        p.add(txt(x + 20, y + 12, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 12, val, size=12.5, weight=600, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 26, x + RW - 18, y + 26, stroke=HAIR))
    p.add(warn("Shortfall in 2059: expenses exceed available assets. Warning names the year.", x + 18, 516, RW - 36))
    ix4, iy4, iw4 = p.card(x, 596, RW, 240, "Milestones on chart")
    for i, (lab, val) in enumerate([("Retirement", "2045 · age 55"), ("Financial independence", "2042"), ("Life expectancy", "2075")]):
        y = iy4 + 8 + i * 44
        p.add(circle(x + 26, y + 10, 4, fill=INK, stroke=None))
        p.add(txt(x + 42, y + 14, lab, size=11.5, fill=INK_SOFT))
        p.add(txt(x + RW - 20, y + 14, val, size=11.5, fill=MUTED, anchor="end", family="Menlo, monospace"))
    p.markers([(1, L + 18, 232), (2, L + 18, 636), (3, x + 18, 246), (4, x + 18, 540)])
    return p.footer([
        (1, "One annual pipeline: income → contributions → expenses and debt → RMDs and conversions → surplus or shortfall → flows → drawdown → tax → summary."),
        (2, "Every run is versioned with start time and duration. Selecting an older run shows that result, not a recomputation."),
        (3, "Summary values are the same API response the chart uses. The UI formats, never calculates."),
        (4, "Warnings are data: a shortfall or invalid input names the issue and the year and marks the failure year on the chart."),
    ])


def s020():
    p = Page(20, "Projection · Yearly summary", "Summary, table, and warnings read one result.", "Projection",
             crumb="Plans / Plan For Retirement / Projection / Year 2036", actions=["Table view", "Run plan"], frame_h=880)
    p.add(line_chart(L, 176, LW, 240,
                     [{"name": "Net worth", "values": [1.55, 2.2, 2.9, 3.4, 3.2, 2.9], "area": True}],
                     x_labels=["2026", "2036", "2046", "2056", "2066", "2075"], y_max=3.9,
                     milestone_x=[(4, "2059 shortfall")]))
    p.add(txt(L, 440, "Selected year 2036 · click a year to change the summary", size=11, fill=FAINT))
    for i, (lab, val) in enumerate([("Income", "$234,604"), ("Taxes", "$75,102"), ("Spending", "$107,741"), ("Net worth", "$3,409,056")]):
        p.add(rrect(L + i * 180, 470, 168, 104, r=12, fill=SURFACE, stroke=BORDER))
        p.add(txt(L + i * 180 + 16, 494, lab.upper(), size=10, weight=700, fill=MUTED, ls=0.5))
        p.add(txt(L + i * 180 + 16, 528, val, size=17, weight=600, family="Menlo, monospace"))
        p.add(txt(L + i * 180 + 16, 552, "backend value", size=10, fill=FAINT))
    ix, iy, iw = p.card(L, 596, LW, 240, "Yearly table")
    p.add(table(L + 18, iy + 6, LW - 36,
                [("Year", 110), ("Income", 150), ("Taxes", 150), ("Spending", 150), ("Net worth", 180)],
                [["2035", "$228,940", "$72,110", "$104,220", "$3,102,880"],
                 ["2036", "$234,604", "$75,102", "$107,741", "$3,409,056"],
                 ["2037", "$239,980", "$76,440", "$111,760", "$3,357,320"]], row_h=40, highlight=1)[0])
    x = L + LW + GAP
    ix2, iy2, iw2 = p.card(x, 176, RW, 300, "Warnings")
    p.add(warn("2059: shortfall $18,400. Planned spending exceeds available assets.", x + 18, iy2 + 8, RW - 36))
    p.add(warn("2038: tax balance −$1,240 carried as a refund into 2039 cash flow.", x + 18, iy2 + 66, RW - 36, tone="info"))
    p.add(warn("2061: negative tax-deferred balance blocked; drawdown order adjusted.", x + 18, iy2 + 124, RW - 36))
    p.add(para(x + 18, iy2 + 214, "Warnings name the issue and the year. They never hide a failure.", RW - 36, size=11, fill=FAINT))
    ix3, iy3, iw3 = p.card(x, 500, RW, 336, "Metric detail")
    p.add(txt(x + 18, iy3 + 10, "Taxes · 2036", size=12, weight=600))
    for i, (lab, val) in enumerate([("Federal", "$58,204"), ("State", "$14,301"), ("FICA / Medicare", "$2,597"), ("Total", "$75,102")]):
        y = iy3 + 34 + i * 42
        p.add(txt(x + 20, y + 12, lab, size=11.5, fill=MUTED))
        p.add(txt(x + RW - 20, y + 12, val, size=12, weight=600 if i == 3 else 400, family="Menlo, monospace", anchor="end"))
        p.add(line(x + 18, y + 24, x + RW - 18, y + 24, stroke=HAIR))
    p.markers([(1, L + 18, 260), (2, L + 18, 640), (3, x + 18, 212), (4, x + 18, 540)])
    return p.footer([
        (1, "A year selection drives the summary, the table row highlight, and the metric detail from one API response."),
        (2, "Table rows match chart years exactly: 2036 shows income $234,604, taxes $75,102, spending $107,741, net worth $3,409,056."),
        (3, "Hovering a metric shows the backend value and any preview value side by side. No client-side recomputation."),
        (4, "A prior-year tax balance settles in the next year's cash flow as a refund or a payment, and the warning states which."),
    ])


def s021():
    p = Page(21, "Drawdown order and shortfall", "Order is a plan setting used by the engine.", "Settings",
             crumb="Plans / Plan For Retirement / Settings / Drawdown", actions=["Save order"], frame_h=860)
    ix, iy, iw = p.card(L, 176, LW, 396, "Withdrawal order")
    for i, (name, note, bal) in enumerate([("Cash", "Savings, checking", "$92,000"),
                                           ("Taxable", "Brokerage", "$420,555"),
                                           ("Tax-deferred", "401(k), IRA", "$1,012,000"),
                                           ("Tax-free", "Roth IRA, HSA", "$138,500")]):
        y = iy + 6 + i * 64
        p.add(rrect(L + 18, y, LW - 36, 54, r=8, fill=SURFACE if i else FILL, stroke=BORDER))
        p.add(txt(L + 34, y + 22, "≡", size=14, fill=FAINT))
        p.add(txt(L + 62, y + 22, name, size=12.5, weight=600))
        p.add(txt(L + 62, y + 40, note, size=11, fill=MUTED))
        p.add(txt(L + LW - 40, y + 32, bal, size=12, family="Menlo, monospace", anchor="end"))
        p.add(txt(L + LW - 130, y + 22, f"{i+1}", size=11, fill=FAINT, anchor="end"))
    p.add(warn("Early withdrawals before the allowed age include the penalty in the result.", L + 18, iy + 276, LW - 36, tone="info"))
    p.add(txt(L + 18, iy + 344, "Drag to reorder. The saved order is used by the engine on the next run.", size=11, fill=FAINT))
    ix2, iy2, iw2 = p.card(L, 588, LW, 248, "Preview: $50,000 need", sub="Cash first, then taxable")
    p.add(bars(L + 18, iy2 + 10, LW - 36,
               [("Cash", 18000, "$18,000"), ("Taxable", 32000, "$32,000"), ("Tax-deferred", 0, "$0"), ("Tax-free", 0, "$0")],
               row_h=26, gap=8, max_val=32000))
    x = L + LW + GAP
    ix3, iy3, iw3 = p.card(x, 176, RW, 336, "Balance reconciliation")
    p.add(table(x + 18, iy3 + 6, RW - 36,
                [("Account", 150), ("Open", 110), ("Out", 90), ("Close", 100)],
                [["Cash", "$92,000", "$18,000", "$74,000"],
                 ["Taxable", "$420,555", "$32,000", "$388,555"]], row_h=40)[0])
    p.add(txt(x + 18, iy3 + 168, "Withdrawals sum to the need. Any gap becomes a shortfall.", size=11, fill=FAINT))
    p.add(warn("Need $117,523 at age 59: covered, shortfall $0.", x + 18, iy3 + 200, RW - 36, tone="info"))
    ix4, iy4, iw4 = p.card(x, 536, RW, 300, "Shortfall example")
    p.add(warn("Assets exhausted in 2059. Need exceeds balances by $18,400.", x + 18, iy4 + 8, RW - 36))
    p.add(para(x + 18, iy4 + 76, "The result records a shortfall and a warning. It never shows a negative balance.", RW - 36, size=11.5, fill=MUTED))
    p.add(txt(x + 18, iy4 + 116, "Shortfall", size=11, fill=MUTED))
    p.add(txt(x + 18, iy4 + 142, "$18,400", size=18, weight=600, family="Menlo, monospace"))
    p.add(txt(x + 160, iy4 + 116, "Year", size=11, fill=MUTED))
    p.add(txt(x + 160, iy4 + 142, "2059", size=18, weight=600, family="Menlo, monospace"))
    b, bw = btn(x + 18, iy4 + 190, "Review drawdown order", variant="secondary")
    p.add(b)
    p.markers([(1, L + 18, 236), (2, L + 18, 640), (3, x + 18, 236), (4, x + 18, 600)])
    return p.footer([
        (1, "Default order is cash, taxable, tax-deferred, tax-free. The stored setting drives every run."),
        (2, "For a $50,000 need, cash supplies $18,000 and taxable supplies the remaining $32,000. Ending balances reconcile with the withdrawals."),
        (3, "Penalties for withdrawals before the allowed age are included in the year's tax result, not netted silently."),
        (4, "Insufficient assets produce a shortfall record and a warning with the year. No negative balance is ever displayed."),
    ])
