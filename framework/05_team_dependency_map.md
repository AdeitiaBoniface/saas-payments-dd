# Framework · Dimension 5: Engineering Team & Key-Person Dependency Map

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

Identifies whether the target's technical capability is concentrated in a small number of individuals whose departure would materially harm the product or business. Produces a **key-person risk score** and structured retention recommendations for the acquirer.

---

## Team Overview

| Function | Headcount | Notes |
|---|---|---|
| Engineering (total) | 15 | Includes 2 contractors |
| Backend | 7 | Core platform team |
| Frontend | 3 | Web app + merchant portal |
| DevOps / Platform | 2 | AWS infra + CI/CD |
| QA | 2 | Manual + some automation |
| Data / Analytics | 1 | BI tooling only |

---

## Org Structure (Anonymized)

```
CTO  ──────────────────────────────────────────────────────────
  │
  ├── Principal Engineer (BE)   ← ⚠️ High key-person risk
  │     ├── Senior BE Engineer 1
  │     ├── Senior BE Engineer 2
  │     ├── BE Engineer 3
  │     └── BE Engineer 4
  │
  ├── Lead Frontend Engineer
  │     ├── FE Engineer 1
  │     └── FE Engineer 2
  │
  ├── Platform Lead
  │     └── DevOps Engineer
  │
  └── QA Lead
        └── QA Engineer
```

---

## Key-Person Risk Assessment

### High Risk: Principal Backend Engineer

| Factor | Assessment |
|---|---|
| **Domain coverage** | Sole author of FX routing logic, payment rail integrations, and core transaction processing engine |
| **Bus factor** | Estimated bus factor of 1 on 4 critical system components |
| **Documentation** | Institutional knowledge is poorly documented. Architecture decisions live in Slack and his head. |
| **Tenure** | 3.5 years. Present since seed stage. |
| **Equity position** | ~40% vested at time of assessment. Cliff on remainder: 18 months post-close. |
| **Retention risk** | Medium-high. Expressed interest in independent projects in reference conversations. |

**Key-Person Risk Score: 🔴 HIGH**  
*This is the single most significant people risk in the deal.*

---

### Medium Risk: CTO

| Factor | Assessment |
|---|---|
| **Domain coverage** | Architecture vision, external relationships (PSP partners), and board-level technical communication |
| **Replaceability** | Replaceable, but PSP relationship network is valuable and relationship-dependent |
| **Retention risk** | Low. Financially motivated to close. Likely to stay through earnout period. |

**Key-Person Risk Score: 🟡 MEDIUM**

---

### Low Risk: Remaining Team

The remainder of the engineering team is assessed as **standard execution risk** — collectively important but individually replaceable within 60–90 days for most roles.

---

## Team Capability Gaps

| Gap | Impact | Recommendation |
|---|---|---|
| No dedicated data engineer | Analytics and reporting are blocked | Hire within 6 months of close |
| QA automation coverage low (41%) | Release velocity constrained | Invest in SDET hire or tooling |
| No security engineer | All security work is outsourced | Bring in-house or retain specialist MSSP |

---

## Retention Recommendations

### For Principal Backend Engineer
1. **Accelerated vesting** on unvested equity as part of close package
2. **Retention bonus** — recommended $150K–$200K, split across months 6 and 18 post-close
3. **Title and scope upgrade** — offer VP Engineering or Head of Platform role if CTO exits
4. **Documentation sprint** — mandate 60-day knowledge transfer program post-close with milestone payment

### For CTO
1. Standard earnout structure (already in deal terms)
2. Clear remit post-close to avoid role ambiguity with acquirer's existing leadership

---

## Knowledge Transfer Plan

Post-close, a structured knowledge transfer program is recommended:

```
Days 1–30   │  Shadow sessions on all critical system components
             │  Recorded architecture walkthroughs (Loom or equivalent)
             │  Confluence/Notion architecture docs created

Days 30–60  │  Pair programming on FX routing and rail integration modules
             │  Runbook creation for all production incident scenarios

Days 60–90  │  Handoff validation: second engineer independently resolves 
             │  3 simulated incidents without Principal Engineer assistance
```
