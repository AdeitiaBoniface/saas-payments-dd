# Red-Flag Memo · Week 3 Summary

> **Engagement:** Cross-Border Payments SaaS · $22M PE Acquisition  
> **Issued:** End of Week 3 (mid-engagement)  
> **Audience:** Deal team, Investment Committee  
> **Status:** Preliminary — full report follows Week 6

---

## Purpose

This memo summarizes the highest-priority findings identified in the first three weeks of due diligence. It is designed to give the deal team sufficient information to:

1. Decide whether to proceed to full diligence (or pause/terminate)
2. Surface any issues requiring immediate legal or financial attention
3. Begin preliminary deal condition drafting

---

## Proceed Recommendation

> ✅ **Recommend: Proceed to full diligence with modified term sheet**

No findings at Week 3 constitute a deal-blocker. The target is a fundamentally sound business with identifiable and quantifiable risks. The risk profile is consistent with a company at Series B stage.

---

## Top 5 Red Flags

### 🔴 RED-01 — PSP Concentration Risk (HIGH)
**Dimension:** Infrastructure Scalability / Integration Risk  
**Finding:** A single payment service provider processes approximately 68% of total transaction volume. This represents both operational risk (single point of failure) and commercial risk (pricing leverage held by one vendor).  
**Deal Impact:** High. This is the most significant structural risk identified to date.  
**Recommended Action:** Add rail diversification milestone as a post-close deal condition. Validate PSP contract terms before close (notice periods, assignment clauses, pricing tiers).

---

### 🟡 RED-02 — Scalability Ceiling at 3x (MEDIUM)
**Dimension:** Infrastructure Scalability  
**Finding:** The database layer (Postgres monolith) creates a hard ceiling at approximately 3x current transaction volume. The acquirer's growth assumptions projected 5x within 24 months of close.  
**Deal Impact:** Medium. Does not block the deal but creates a post-close investment obligation.  
**Recommended Action:** Negotiate tech debt escrow to cover DB sharding work ($700K–$900K estimated). Validate assumptions with independent engineering review before close.

---

### 🟡 RED-03 — Key-Person Dependency (MEDIUM)
**Dimension:** Team & Key-Person Risk  
**Finding:** One Principal Backend Engineer is the sole author of 4 critical system components including the FX routing engine and core payment rail integrations. Bus factor of 1. Documentation of this knowledge is minimal.  
**Deal Impact:** Medium. Departure of this individual post-close would materially impact the integration timeline and product roadmap.  
**Recommended Action:** Structure retention package (accelerated vesting + retention bonus). Mandate knowledge transfer program as Day 1 post-close activity.

---

### 🟡 RED-04 — SOC2 Control Gaps (LOW-MEDIUM)
**Dimension:** Security & Compliance  
**Finding:** Two open control gaps identified in the most recent SOC2 Type II audit cycle — access review completion and vendor risk assessments.  
**Deal Impact:** Low-medium. Not material to the deal but must be remediated before close to avoid inherited audit findings.  
**Recommended Action:** Require written evidence of remediation as a pre-close condition. *Update: Both gaps remediated by Week 5 of engagement.*

---

### 🟡 RED-05 — Roadmap Over-commitment (LOW)
**Dimension:** Product Maturity  
**Finding:** The 18-month product roadmap is 20–30% over-committed relative to current engineering capacity. Two roadmap items have no customer pull evidence.  
**Deal Impact:** Low. Execution risk post-close, not a deal risk.  
**Recommended Action:** Flag to acquirer's CPO for roadmap rationalization exercise in Month 1 post-close. Recommend deprioritizing the two unvalidated items.

---

## Items Not Yet Assessed (Week 3)

The following will be covered in the full Week 6 report:

- [ ] Customer reference calls (2 accounts scheduled for Week 4)
- [ ] Full PCI-DSS review
- [ ] FX routing engine architecture deep-dive
- [ ] Engineering capacity modelling for 18-month roadmap
- [ ] Integration risk matrix (full version)
- [ ] Data migration complexity assessment

---

## Next Steps

| Action | Owner | By When |
|---|---|---|
| Draft tech debt escrow language | Deal lawyer + AKB | End of Week 4 |
| PSP contract review | Legal | End of Week 4 |
| Retention package terms | HR / Deal team | End of Week 5 |
| SOC2 remediation evidence | Target company | End of Week 5 |
| Full DD report | AKB | End of Week 6 |
