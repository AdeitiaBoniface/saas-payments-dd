# Deal Conditions & Escrow Recommendations

> **Engagement:** Cross-Border Payments SaaS · $22M PE Acquisition  
> **Issued:** Week 6 (Final Report)  
> **Audience:** Deal team, Investment Committee, Legal

---

## Summary

Four deal conditions are recommended based on the findings of this due diligence engagement. All conditions have been reviewed with the deal team and the target's legal representative.

| ID | Condition | Type | Status |
|---|---|---|---|
| DC-01 | Tech debt escrow ($1.5M) | Escrow | ✅ Agreed — included in SPA |
| DC-02 | SOC2 control gap remediation evidence | Pre-close | ✅ Satisfied (Week 5) |
| DC-03 | PSP contract assignment consent | Pre-close | ✅ Agreed — consent obtained |
| DC-04 | Rail diversification milestone | Post-close | ✅ Agreed — included in SPA |

---

## DC-01: Technical Debt Escrow

**Amount:** $1,500,000  
**Type:** Post-close escrow, milestone-released  
**Hold Period:** 18 months from close

### Rationale
The due diligence engagement identified approximately $1.19M–$1.79M in critical and significant technical debt. The $1.5M escrow amount represents the midpoint estimate with a buffer for timeline slippage.

### Release Schedule

**Milestone 1 — $750,000**  
*Released when:* Updated load test demonstrates the platform handles 3x current peak transaction volume without service degradation.  
*Target Date:* Month 9 post-close  
*Verification:* Independent load test report provided to acquirer

**Milestone 2 — $750,000**  
*Released when:* A second PSP is live and processing a minimum of 20% of total transaction volume for 30 consecutive days.  
*Target Date:* Month 15 post-close  
*Verification:* Transaction volume report from platform analytics

**Forfeiture Clause:**  
If either milestone is not met within the defined window, the escrow balance attributable to that milestone reverts to the acquirer with no obligation to release.

---

## DC-02: SOC2 Control Gap Remediation

**Type:** Pre-close condition  
**Status:** ✅ Satisfied

### Required Evidence (provided by Week 5)
1. Completed Q3 access review documentation, signed by CISO equivalent
2. Removal confirmation for stale admin account (SR-01)
3. Completed vendor risk assessments for 2 previously unassessed sub-processors (SR-02)

All three items received and reviewed. No further action required.

---

## DC-03: PSP Contract Assignment

**Type:** Pre-close condition  
**Status:** ✅ Satisfied

### Background
The target's primary PSP contract (covering ~68% of transaction volume) required explicit consent from the PSP for assignment to the acquiring entity. Assignment without consent would have constituted a breach of the agreement.

### Resolution
PSP consent letter obtained. Contract assignment language included in the purchase agreement. Acquirer introduced to PSP relationship manager prior to close.

---

## DC-04: Rail Diversification Milestone

**Type:** Post-close obligation (included in SPA representations & warranties)  
**Timeline:** Second PSP live within 12 months of close; at 20% volume within 15 months

### Rationale
The single-PSP dependency (DC-03) addresses the legal assignment risk but does not resolve the operational and commercial concentration risk. This condition requires the target's team (under acquirer direction) to actively diversify payment rail coverage post-close.

### Consequence of Non-Compliance
Non-compliance does not trigger escrow forfeiture (escrow is separate via DC-01) but constitutes a breach of post-close covenants. Acquirer's recourse is via standard SPA indemnity provisions.

---

## Additional Recommendations (Not Conditions)

The following were recommended to the acquirer as integration priorities but were not structured as formal deal conditions:

1. **Retention package for Principal Backend Engineer** — $150K–$200K retention bonus structure recommended. Deal team to handle bilaterally.
2. **Knowledge transfer program** — 90-day post-close program. No legal structure required; operational decision.
3. **Secrets Manager migration** — $40K–$80K effort. Add to post-close sprint backlog, Month 1.
4. **Roadmap rationalization** — CPO-level engagement in Month 1 post-close. No legal structure required.
