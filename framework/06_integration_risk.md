# Framework · Dimension 6: Post-Close Integration Risk Matrix

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

Maps integration risks across 6 dimensions for the 0–18 month post-close window. Gives the acquirer's integration team a prioritized action plan and flags decisions that must be made on Day 1 vs. those that can wait.

---

## Integration Risk Matrix

| Dimension | Risk Level | Priority | Owner | Timeline |
|---|---|---|---|---|
| Technology Stack Alignment | 🟡 Medium | High | CTO + Engineering Lead | Month 1–6 |
| Data Migration & Pipelines | 🔴 High | Critical | Platform Lead | Month 1–3 |
| Payment Rail Ownership Transfer | 🔴 High | Critical | CTO + Legal | Day 1 |
| Team Integration & Culture | 🟡 Medium | High | HR + CTO | Month 1–12 |
| Customer Communication | 🟢 Low | Medium | CPO + CS | Month 1–2 |
| Compliance & Audit Continuity | 🟡 Medium | High | Compliance + Legal | Day 1 |

---

## Dimension Deep-Dives

### 🔴 Payment Rail Ownership Transfer (Critical · Day 1)

**Risk:** PSP contracts are in the target company's legal name. Contract assignment to acquirer entity is not automatic. If PSPs don't consent to assignment, payment processing could be interrupted.

**Mitigation:**
- Obtain PSP consent letters as pre-close condition
- Ensure acquirer legal entity is listed as permitted assignee in purchase agreement
- Day 1 playbook must include PSP relationship calls with acquirer intro

---

### 🔴 Data Migration & Pipelines (Critical · Month 1–3)

**Risk:** Transaction data, customer KYC records, and FX rate history are stored across 3 systems (Postgres, S3, and a legacy MySQL instance). Migration to acquirer data infrastructure without data loss or audit trail breaks is high-risk.

**Mitigation:**
- Commission data migration design document within 30 days of close
- Run parallel systems for minimum 60 days during migration
- Engage specialist data migration firm (budget: $80K–$150K)
- Ensure GDPR data transfer obligations are satisfied if moving across jurisdictions

---

### 🟡 Technology Stack Alignment (Medium · Month 1–6)

**Risk:** Target uses AWS; acquirer uses a hybrid AWS/GCP environment. Infra management tooling (Terraform modules, CI/CD) will need alignment. Not blocking but creates operational overhead.

**Mitigation:**
- Maintain target on existing AWS infrastructure for 12 months minimum
- Align on shared observability tooling (Datadog or equivalent) in Month 1
- No forced stack migration in first 12 months — product velocity takes priority

---

### 🟡 Team Integration & Culture (Medium · Month 1–12)

**Risk:** 15-person startup team joining a larger organization. Risk of attrition from culture mismatch, loss of autonomy, or compensation compression.

**Mitigation:**
- Retention packages for top 5 engineers (see Dimension 5)
- Preserve team autonomy for 6 months: own sprint ceremonies, own backlog
- Founder/CTO quarterly communication to team through Month 12
- Salary benchmarking exercise in Month 1 to close any gaps

---

### 🟢 Customer Communication (Low · Month 1–2)

**Risk:** Customers may react negatively to ownership change, particularly if acquirer is a competitor or unknown entity.

**Mitigation:**
- Joint communication plan agreed pre-close (no announcement until Day 1)
- CPO sends personal email to all customers on Day 1
- Key account calls within 48 hours of announcement
- No product or pricing changes communicated for 90 days

---

### 🟡 Compliance & Audit Continuity (Medium · Day 1)

**Risk:** SOC2 and PCI-DSS certifications are issued to the target entity. Post-acquisition, the scope of certification may change. Re-certification timeline: 6–9 months.

**Mitigation:**
- Notify QSA and auditors of acquisition on Day 1
- Determine whether existing certs are maintained under new entity or need re-scoping
- Ensure no gap in compliance coverage communicated to customers

---

## Integration Workstream Plan

```
Day 1           │  ✅ PSP consent confirmed & contracts assigned
                │  ✅ Compliance & audit continuity call with QSA
                │  ✅ Customer communication sent

Month 1         │  Data migration design document completed
                │  Salary benchmarking completed
                │  Shared observability tooling agreed

Month 1–3       │  Data migration executed (parallel systems running)
                │  Knowledge transfer program (see Dimension 5)

Month 3–6       │  Tech stack alignment roadmap agreed
                │  Second PSP onboarded (rail diversification — deal condition)

Month 6–12      │  DB sharding project initiated (tech debt escrow Milestone 1)
                │  Team integration review: retention health check

Month 12–18     │  DB sharding complete → escrow Milestone 1 released ($750K)
                │  Second PSP at 20% volume → escrow Milestone 2 released ($750K)
```
