# Framework · Dimension 1: Infrastructure Scalability Scorecard

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

This scorecard assesses whether a SaaS target's infrastructure can support the acquirer's projected growth without requiring a full platform rewrite. It produces a **scalability rating (1–5)** across 6 sub-dimensions and a plain-language recommendation for the deal team.

---

## Scoring Guide

| Score | Meaning |
|---|---|
| **5** | Best-in-class. No material risk. |
| **4** | Minor gaps. Addressable within 6 months. |
| **3** | Moderate risk. Remediation required, cost quantifiable. |
| **2** | Significant risk. Likely deal condition or valuation adjustment. |
| **1** | Critical. Potential deal blocker. Needs independent validation. |

---

## Assessment: Cross-Border Payments Platform

### Sub-dimension Scores

| Sub-Dimension | Score | RAG | Notes |
|---|---|---|---|
| **Compute & Auto-scaling** | 4 | 🟢 | Kubernetes-based, auto-scaling configured. Minor tuning needed at 4x load. |
| **Database Architecture** | 3 | 🟡 | Postgres monolith. Sharding not implemented. Bottleneck above 3x volume. |
| **Queue & Async Processing** | 3 | 🟡 | RabbitMQ in use. Throughput limits tested at 2.5x current peak. |
| **Payment Rail Dependencies** | 2 | 🔴 | Single PSP handles 68% of volume. Concentration risk. |
| **CDN & Edge Latency** | 4 | 🟢 | Cloudfront deployed. Adequate for NA and SEA corridors. |
| **Disaster Recovery** | 3 | 🟡 | RTO: 4 hours. RPO: 1 hour. Acceptable but not tier-1 for a payments product. |

**Composite Scalability Score: 3.2 / 5.0**  
**RAG Rating: 🟡 AMBER — Scalable to 3x; investment required for 5x**

---

## Key Finding

The platform can **comfortably handle 3x current transaction volume** on its current architecture. Reaching 5x requires two targeted investments:

1. **Database sharding** — estimated $700K–$900K engineering effort over 9–12 months
2. **Queue management upgrade** (Kafka migration or RabbitMQ scaling) — estimated $200K–$400K, 4–6 months

**Total remediation estimate: ~$1.2M**

This was structured as a **$1.5M tech debt escrow** in final deal terms (buffer included for timeline slippage).

---

## Scalability Projection

```
Transaction Volume  │  Architecture Status       │  Investment Required
────────────────────┼────────────────────────────┼──────────────────────
1x  (current)       │  ✅ Stable                  │  $0
2x                  │  ✅ Handles with headroom    │  $0
3x                  │  ⚠️  At limit (DB layer)     │  $0 (short-term)
4x                  │  ❌ DB bottleneck            │  $700K–$900K
5x                  │  ❌ DB + Queue bottleneck    │  ~$1.2M total
```

---

## Evidence Gathered

- [ ] Architecture diagram reviewed (C4 Level 2)
- [ ] Load test results reviewed (last run: 6 months prior to engagement)
- [ ] CTO interview: 2 sessions, 3 hours total
- [ ] Infrastructure cost breakdown reviewed (AWS Cost Explorer export)
- [ ] Kubernetes config reviewed by senior engineer
- [ ] Database schema reviewed for normalization and index coverage

---

## Recommended Deal Conditions

1. **Tech debt escrow of $1.5M** — held in escrow for 18 months post-close, released upon completion of DB sharding milestone
2. **Rail diversification covenant** — target must onboard a second PSP within 12 months of close
3. **Load testing pre-close** — updated load test at 3x volume to validate current-state assumptions

---

## Template Reuse Notes

To apply this scorecard to a different engagement:

1. Replace all scored rows with your assessment
2. Adjust sub-dimensions to match the target's tech stack profile
3. Update the scalability projection table with deal-specific volume assumptions
4. Link to supporting evidence (architecture docs, interview notes, test results)
