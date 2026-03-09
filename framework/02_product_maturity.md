# Framework · Dimension 2: Product Maturity & Roadmap Credibility

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

Assesses whether the product is genuinely mature — not just feature-complete — and whether the roadmap is credible, customer-anchored, and executable given the current team. A strong product score can justify valuation premiums; a weak one signals post-close execution risk.

---

## Maturity Model

Product maturity is assessed across **5 stages**:

```
Stage 1 │ MVP / Pre-PMF       — Core functionality, limited real-world validation
Stage 2 │ Early Traction      — PMF signals, early paying customers, manual processes
Stage 3 │ Scaling             — Repeatable GTM, product-led growth emerging, automation
Stage 4 │ Optimising          — Multi-segment, data-driven, strong retention, self-serve
Stage 5 │ Category Leader     — Market-defining, platform thinking, ecosystem plays
```

**Assessment: This target is at Stage 3 (Scaling) — approaching Stage 4 in core payment flows.**

---

## Product Maturity Scorecard

| Dimension | Score (1–5) | RAG | Notes |
|---|---|---|---|
| **Core Product Stability** | 4 | 🟢 | Core payment flows are stable. P1 incident rate <1/month. |
| **Feature Coverage vs. Market** | 3 | 🟡 | Competitive on SME corridor payments; weak on enterprise FX hedging. |
| **API & Integration Ecosystem** | 4 | 🟢 | REST API well-documented. Webhooks available. 12 active integrations. |
| **Self-Serve & Onboarding** | 3 | 🟡 | Onboarding is partially manual. CS-assisted for >$50K/mo customers. |
| **Product Analytics Maturity** | 3 | 🟡 | Mixpanel in use. No feature-level retention cohorts. Data is available but underused. |
| **Roadmap–Customer Alignment** | 4 | 🟢 | Top 3 roadmap items confirmed by ≥2 customer interviews each. |
| **Pricing Model Maturity** | 3 | 🟡 | Volume-based pricing. No usage-based or seat expansion motion yet. |

**Composite Product Maturity Score: 3.4 / 5.0**  
**RAG Rating: 🟢 GREEN — Mature enough to scale; targeted gaps are post-close opportunities, not risks**

---

## Roadmap Credibility Assessment

The 18-month roadmap was reviewed against three criteria:

### 1. Customer Pull Evidence
Each roadmap item was assessed for evidence of customer demand.

| Roadmap Item | Customer Evidence | Status |
|---|---|---|
| Multi-currency wallet | 4 customer requests, 2 signed LOIs | ✅ Well-evidenced |
| Real-time FX rate API | 3 customer requests, 1 enterprise pilot | ✅ Well-evidenced |
| Compliance dashboard (SME) | Internal hypothesis only | ⚠️ Weak evidence |
| White-label payment links | 2 partner requests | ✅ Adequate |
| Enterprise FX hedging | 1 customer mention, no follow-up | ⚠️ Weak evidence |

**Finding:** 2 of 5 roadmap items lacked sufficient customer validation. Recommend deprioritizing or gating behind discovery sprints.

### 2. Engineering Capacity Check
Roadmap was sized against available engineering bandwidth (15 FTEs at time of assessment). Assessment: the 18-month roadmap was **20–30% over-committed** given current headcount. Completion of all items would require 2 additional senior engineers.

### 3. Dependency Risk
One roadmap item (Real-time FX Rate API) is dependent on a third-party data provider contract renewal due in Month 4. Risk: medium. Acquirer advised to include contract assignment clause in deal terms.

---

## Evidence Gathered

- [ ] Product roadmap reviewed (Notion, exported)
- [ ] 2 customer reference interviews (40 min each)
- [ ] Product demo walkthrough (2 sessions)
- [ ] Review of feature release cadence (GitHub release history, 12 months)
- [ ] Mixpanel dashboard access (read-only, 2 weeks)
- [ ] Pricing model and packaging review

---

## Post-Close Opportunity Notes

The product maturity gaps identified are **genuine value creation opportunities** for the acquirer, not liabilities:

- Introducing usage-based pricing could expand NRR by an estimated 15–25%
- Building self-serve onboarding removes the CS dependency and unlocks SMB growth
- Product analytics maturity is an easy win — one dedicated analyst could operationalize cohort reporting within 60 days
