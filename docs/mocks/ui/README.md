# UI captures from the Yearproof prototype

These screenshots replace the earlier wireframes for issues that already had a mock, and cover
issues that needed a screen but had none.

Source: `ux/` in the local product workspace (`index.html`, `screens.js`, `styles.css`, `site/`).
Captured at 1440 px wide, full page, with Playwright. Sample data only.

| File | Prototype route |
| --- | --- |
| `issue-190-admin-overview.png` | `#/admin?view=overview` |
| `issue-190-admin-audit.png` | `#/admin?view=audit` |
| `issue-191-admin-users.png` | `#/admin?view=users` |
| `issue-191-admin-user-detail.png` | `#/admin?view=users` → account dialog |
| `issue-192-admin-revenue.png` | `#/admin?view=revenue` |
| `issue-193-admin-product.png` | `#/admin?view=product` |
| `issue-194-admin-billing.png` | `#/admin?view=billing` |
| `issue-194-admin-ledger.png` | `#/admin?view=ledger` |
| `issue-195-admin-promos.png` | `#/admin?view=promos` |
| `issue-196-admin-pricing.png` | `#/admin?view=pricing` |
| `issue-196-admin-entitlements.png` | `#/admin?view=entitlements` |
| `issue-197-admin-content.png` | `#/admin?view=content` |
| `issue-197-admin-messages.png` | `#/admin?view=messages` |
| `issue-198-admin-inbox.png` | `#/admin?view=inbox` |
| `issue-198-admin-health.png` | `#/admin?view=health` |
| `issue-199-admin-feedback.png` | `#/admin?view=feedback` |
| `issue-200-admin-costs.png` | `#/admin?view=costs` |
| `issue-186-taxes.png` | `#/taxes` |
| `issue-186-confidence.png` | `#/confidence` |
| `issue-186-compare.png` | `#/compare` |
| `issue-185-strategy.png` | `#/strategy` |
| `issue-185-optimizer.png` | `#/optimizer` |
| `issue-185-estate.png` | `#/estate` |
| `issue-184-relocation-preview.png` | `#/relocation-preview` |
| `issue-184-relocation.png` | `#/relocation` |
| `issue-183-settings.png` | `#/settings` |
| `issue-180-drawdown.png` | `#/drawdown` |
| `issue-177-today.png` | `#/today` |
| `issue-173-allocation.png` | `#/allocation` |
| `issue-172-plans.png` | `#/plans` |
| `issue-172-branches.png` | `#/branches` |
| `issue-174-currency-per-amount.png` | `#/currency` |
| `issue-168-flex-spending.png` | `#/flex` |
| `issue-149-rule-alert.png` | `mockups/emails.html` → rule change |
| `issue-148-review-reminder.png` | `mockups/emails.html` → review due |
| `issue-147-notification-preferences.png` | `#/notifications` |
| `issue-146-review-screen.png` | `#/review` |
| `issue-144-rule-impact.png` | `#/rule-impact` |
| `issue-143-run-diff.png` | `#/run-diff` |
| `issue-142-drift.png` | `#/review` |
| `issue-141-actuals.png` | `#/review` |
| `issue-127-pricing.png` | `site/pricing.html` |
| `issue-126-csv-import.png` | `#/import` |
| `issue-125-explain-panel.png` | `#/year` → derivation drawer |
| `issue-123-rule-provenance.png` | `#/taxes` → rule sets dialog |
| `issue-122-plan-billing.png` | `#/billing` |
| `issue-119-google-signin.png` | `#/signin` |
| `issue-118-email-verification.png` | `#/verify` |
| `issue-118-password-forgot.png` | `#/forgot` |
| `issue-118-password-reset.png` | `#/reset` |
| `issue-062-safe-to-share.png` | `#/settings` → share dialog |
| `issue-061-mortality.png` | `#/longevity` |
| `issue-060-private-equity.png` | `#/private-equity` |
| `issue-059-stock-options.png` | `#/options` |
| `issue-058-variable-rate-loans.png` | `#/loans` |
| `issue-057-property-events.png` | `#/property-events` |
| `issue-056-expense-itemizer.png` | `#/itemizer` |
| `issue-055-snapshots.png` | `#/snapshots` |
| `issue-054-history-undo.png` | `#/history` |

Regenerate from the prototype folder with Playwright at 1440 px. Admin routes use
`#/admin?view=<section>`; dialogs and drawers are captured after the trigger is clicked.

## Issue-specific user mockups

These captures come from the standalone HTML mockups in `docs/mocks/user/` in `product-research`.
Each has a 1440 px desktop capture and a 390 px mobile capture.

| File | Screen |
| --- | --- |
| `issue-297-sabbatical-months.png` | Income → Career break, month range, desktop |
| `issue-297-sabbatical-months-mobile.png` | Income → Career break, month range, mobile |
| `issue-298-new-child.png` | Spending → New child costs, desktop |
| `issue-298-new-child-mobile.png` | Spending → New child costs, mobile |
| `issue-299-job-loss.png` | Income → Job loss, desktop |
| `issue-299-job-loss-mobile.png` | Income → Job loss, mobile |
| `issue-300-buy-car.png` | Assets → New car, desktop |
| `issue-300-buy-car-mobile.png` | Assets → New car, mobile |
| `issue-301-buy-home-rent-old.png` | Assets → Home move, desktop |
| `issue-301-buy-home-rent-old-mobile.png` | Assets → Home move, mobile |
| `issue-302-buy-rental.png` | Assets → Rental purchase, desktop |
| `issue-302-buy-rental-mobile.png` | Assets → Rental purchase, mobile |
| `issue-303-sell-home-rent.png` | Assets → Home exit, desktop |
| `issue-303-sell-home-rent-mobile.png` | Assets → Home exit, mobile |
| `issue-304-new-job-package.png` | Income → Job change, full package, desktop |
| `issue-304-new-job-package-mobile.png` | Income → Job change, full package, mobile |
| `issue-305-buy-home-sell-old.png` | Assets → Home replacement, desktop |
| `issue-305-buy-home-sell-old-mobile.png` | Assets → Home replacement, mobile |
| `issue-306-one-time-gift.png` | Spending → One-time gift, desktop |
| `issue-306-one-time-gift-mobile.png` | Spending → One-time gift, mobile |
| `issue-307-family-support.png` | Spending → Family support, desktop |
| `issue-307-family-support-mobile.png` | Spending → Family support, mobile |
| `issue-308-tuition.png` | Spending → Tuition, desktop |
| `issue-308-tuition-mobile.png` | Spending → Tuition, mobile |
| `issue-309-child-accounts-tax.png` | Finances → Child accounts, tax engine, desktop |
| `issue-309-child-accounts-tax-mobile.png` | Finances → Child accounts, tax engine, mobile |
| `issue-310-promotion-raise.png` | Income · Promotion, desktop |
| `issue-310-promotion-raise-mobile.png` | Income · Promotion, mobile |
| `issue-311-equity-refresh.png` | Income · Equity, desktop |
| `issue-311-equity-refresh-mobile.png` | Income · Equity, mobile |
| `issue-312-phased-retirement.png` | Income · Phased retirement, desktop |
| `issue-312-phased-retirement-mobile.png` | Income · Phased retirement, mobile |
| `issue-313-side-income.png` | Income · Side income, desktop |
| `issue-313-side-income-mobile.png` | Income · Side income, mobile |
| `issue-314-parental-leave.png` | Income · Leave, desktop |
| `issue-314-parental-leave-mobile.png` | Income · Leave, mobile |
| `issue-315-commission-income.png` | Income · Commission, desktop |
| `issue-315-commission-income-mobile.png` | Income · Commission, mobile |
| `issue-316-refinance-heloc.png` | Debt · Refinance, desktop |
| `issue-316-refinance-heloc-mobile.png` | Debt · Refinance, mobile |
| `issue-317-renovation.png` | Assets · Renovation, desktop |
| `issue-317-renovation-mobile.png` | Assets · Renovation, mobile |
| `issue-318-first-home.png` | Assets · First home, desktop |
| `issue-318-first-home-mobile.png` | Assets · First home, mobile |
| `issue-319-downsizing.png` | Assets · Downsizing, desktop |
| `issue-319-downsizing-mobile.png` | Assets · Downsizing, mobile |
| `issue-320-rental-exit.png` | Assets · Rental exit, desktop |
| `issue-320-rental-exit-mobile.png` | Assets · Rental exit, mobile |
| `issue-321-k12-tuition.png` | Spending · K-12 tuition, desktop |
| `issue-321-k12-tuition-mobile.png` | Spending · K-12 tuition, mobile |
| `issue-322-college-costs.png` | Spending · College costs, desktop |
| `issue-322-college-costs-mobile.png` | Spending · College costs, mobile |
| `issue-323-adoption-fertility.png` | Spending · Adoption, desktop |
| `issue-323-adoption-fertility-mobile.png` | Spending · Adoption, mobile |
| `issue-324-parent-care.png` | Spending · Parent care, desktop |
| `issue-324-parent-care-mobile.png` | Spending · Parent care, mobile |
| `issue-325-able-trust.png` | Finances · ABLE / trust, desktop |
| `issue-325-able-trust-mobile.png` | Finances · ABLE / trust, mobile |
| `issue-326-charitable-giving.png` | Spending · Charitable, desktop |
| `issue-326-charitable-giving-mobile.png` | Spending · Charitable, mobile |
| `issue-327-annual-gifting.png` | Spending · Gifting plan, desktop |
| `issue-327-annual-gifting-mobile.png` | Spending · Gifting plan, mobile |
| `issue-328-inheritance.png` | Income · Inheritance, desktop |
| `issue-328-inheritance-mobile.png` | Income · Inheritance, mobile |
| `issue-329-estate-transfer.png` | Estate · Transfer, desktop |
| `issue-329-estate-transfer-mobile.png` | Estate · Transfer, mobile |
| `issue-330-insurance.png` | Risk · Insurance, desktop |
| `issue-330-insurance-mobile.png` | Risk · Insurance, mobile |
| `issue-331-student-loan.png` | Debt · Student loans, desktop |
| `issue-331-student-loan-mobile.png` | Debt · Student loans, mobile |
| `issue-332-auto-refinance.png` | Debt · Auto refinance, desktop |
| `issue-332-auto-refinance-mobile.png` | Debt · Auto refinance, mobile |
| `issue-333-credit-card-payoff.png` | Debt · Credit cards, desktop |
| `issue-333-credit-card-payoff-mobile.png` | Debt · Credit cards, mobile |
| `issue-334-marriage-divorce.png` | Life event · Marriage / divorce, desktop |
| `issue-334-marriage-divorce-mobile.png` | Life event · Marriage / divorce, mobile |
| `issue-335-death-spouse.png` | Life event · Survivor, desktop |
| `issue-335-death-spouse-mobile.png` | Life event · Survivor, mobile |
| `issue-336-relocation.png` | Life event · Relocation, desktop |
| `issue-336-relocation-mobile.png` | Life event · Relocation, mobile |
| `issue-337-windfall.png` | Income · Windfall, desktop |
| `issue-337-windfall-mobile.png` | Income · Windfall, mobile |
