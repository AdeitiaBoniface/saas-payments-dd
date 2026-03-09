# Framework · Dimension 3: Technical Debt Quantification

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

Translates qualitative engineering observations into a **dollar-denominated technical debt estimate** that can be used in deal structuring. The output is designed to be understood by non-technical stakeholders (investors, CFOs, deal lawyers) and used to negotiate escrow arrangements, price adjustments, or post-close milestones.

---

## Debt Classification Model

Technical debt is categorized into three types:

| Type | Definition | Deal Relevance |
|---|---|---|
| **Critical** | Blocks scalability, creates security exposure, or introduces regulatory risk | Deal condition or valuation adjustment |
| **Significant** | Slows delivery velocity, increases operational cost, or creates key-person dependency | Factor into post-close integration budget |
| **Routine** | Normal accumulation; manageable within standard engineering operations | Note only; no deal impact |

---

## Debt Register: Cross-Border Payments Platform

### Critical Debt Items

| ID | Component | Description | Estimated Remediation | Timeline |
|---|---|---|---|---|
| TD-01 | Database Layer | Postgres monolith; no sharding strategy. Blocks growth beyond 3x volume. | $700K–$900K | 9–12 months |
| TD-02 | Payment Rail | Single-PSP dependency (68% volume concentration). Operational and commercial risk. | $150K–$250K (integration + testing) | 6–9 months |

**Critical Debt Subtotal: $850K–$1.15M**

---

### Significant Debt Items

| ID | Component | Description | Estimated Remediation | Timeline |
|---|---|---|---|---|
| TD-03 | Queue Management | RabbitMQ at throughput ceiling. Kafka migration needed for 4x+ scale. | $200K–$400K | 4–6 months |
| TD-04 | Test Coverage | Integration test coverage at 41% (target: ≥75%). Slows release velocity. | $80K–$120K (2 engineers, 3 months) | 3–4 months |
| TD-05 | Observability | Logging and alerting is partial. No distributed tracing. Operational blind spots. | $40K–$80K | 2–3 months |
| TD-06 | Documentation | Internal API docs incomplete for 4 of 12 integrations. Onboarding friction. | $20K–$40K | 1–2 months |

**Significant Debt Subtotal: $340K–$640K**

---

### Routine Debt Items

| ID | Component | Description |
|---|---|---|
| TD-07 | Frontend | React components on v16; migration to v18 would improve performance. Non-urgent. |
| TD-08 | Dependency Management | 12 npm packages >2 major versions behind. No security exposure confirmed. |
| TD-09 | CI/CD Pipeline | Build times average 18 min. Optimization possible but not blocking. |

**Routine Debt: No deal impact. Document for integration planning.**

---

## Total Debt Summary

```
Critical Debt      │  $850K  –  $1,150K
Significant Debt   │  $340K  –  $640K
─────────────────────────────────────────
Total Range        │  $1,190K – $1,790K
Midpoint Estimate  │  ~$1,490K
```

---

## Deal Structuring Recommendation

Based on the total debt estimate, a **$1.5M tech debt escrow** was recommended with the following terms:

```
Escrow Amount:   $1,500,000
Hold Period:     18 months post-close
Release Trigger: Completion of TD-01 (DB sharding) and TD-02 (rail diversification)
Milestone 1:     3x load test passed at Month 9  →  $750K released
Milestone 2:     Second PSP live and processing ≥20% volume at Month 15  →  $750K released
Forfeiture:      Remaining balance reverts to acquirer if milestones missed
```

---

## Methodology Notes

Debt estimates are based on:
- Senior engineer effort rates ($150–$200/hr blended, fully-loaded)
- Scope estimates validated in CTO interviews
- Comparable remediation efforts across 3 previous similar engagements
- A 25% contingency buffer applied to all estimates

> These are **order-of-magnitude estimates** for deal structuring purposes — not engineering quotes. Post-close, a detailed technical scoping exercise should be conducted before committing to timelines.
