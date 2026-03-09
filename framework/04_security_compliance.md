# Framework · Dimension 4: Security & Compliance Risk Register

> Part of the SaaS M&A Technology Due Diligence Framework  
> Engagement: Cross-Border Payments SaaS · $22M Deal

---

## Purpose

Maps all security and compliance risks identified during the engagement to severity ratings, deal relevance, and recommended mitigations. Designed to be read by both technical and non-technical stakeholders.

---

## Compliance Scope

This target operates in the following regulatory environments:

| Jurisdiction | Applicable Framework | Status |
|---|---|---|
| United States | SOC 2 Type II, PCI-DSS Level 2 | ✅ Certified (current) |
| Southeast Asia (Singapore, Malaysia) | MAS TRM Guidelines | ⚠️ Partial alignment |
| EU customers (minor) | GDPR | ✅ DPA in place |

---

## Risk Register

### 🔴 Critical Risks

None identified. No deal-blocking security findings.

---

### 🟡 Significant Risks

| ID | Risk | Area | Detail | Recommendation |
|---|---|---|---|---|
| SR-01 | SOC2 Control Gap: Access Review | Identity & Access | Quarterly access reviews not completed in last cycle (Q3). Evidence of one stale admin account. | Remediate pre-close. Requires documented completion of Q3 review and stale account removal. ✅ *Remediated during engagement.* |
| SR-02 | SOC2 Control Gap: Vendor Risk | Third-party Risk | Vendor risk assessment not completed for 2 sub-processors. Policy exists; execution lagged. | Remediate pre-close. Assessments completed for both vendors by Week 5. ✅ *Remediated during engagement.* |
| SR-03 | MAS TRM Gap: Penetration Testing | Security Testing | Annual pen test not completed for Singapore-adjacent infrastructure. MAS requires annual testing. | Complete pen test before Singapore market entry. Non-urgent for current deal scope. |
| SR-04 | Secrets Management | Infrastructure | AWS secrets stored in environment variables in 2 legacy microservices (not Secrets Manager). | Migrate to AWS Secrets Manager. Low effort (~2 weeks). Add to post-close sprint backlog. |

---

### 🟢 Low Risks (Noted, No Deal Impact)

| ID | Risk | Area | Notes |
|---|---|---|---|
| SR-05 | Dependency Vulnerabilities | Application Security | 3 low-severity CVEs in open-source dependencies. No active exploits. Patch within 30 days. |
| SR-06 | Logging Retention | Compliance | Logs retained 90 days; SOC2 requires 1 year. Object storage logging enabled but not enforced for all services. |
| SR-07 | MFA Enforcement | Identity & Access | MFA enforced for all production access except 1 legacy CI/CD service account. Low risk; remediation trivial. |

---

## SOC2 Type II Assessment Summary

| Trust Service Criteria | Status | Notes |
|---|---|---|
| Security (CC) | ✅ Pass | 2 minor gaps remediated during engagement |
| Availability (A) | ✅ Pass | 99.7% uptime over audit period |
| Confidentiality (C) | ✅ Pass | Data classification policy in place |
| Processing Integrity (PI) | ⚠️ Partial | Transaction reconciliation gap noted for edge-case currency pairs |
| Privacy (P) | ✅ Pass | DPA in place; data minimization practices followed |

---

## PCI-DSS Status

- Level 2 compliance current (SAQ D, completed by QSA)
- Cardholder data environment (CDE) is appropriately scoped and segmented
- Tokenization implemented for all stored payment data
- No findings from last QSA assessment

---

## GDPR Posture

- Data Processing Agreement (DPA) in place with all EU customers
- Data Subject Request (DSR) process documented and tested
- No active GDPR enforcement actions or complaints
- Data residency: all EU customer data processed and stored in eu-west-1

---

## Recommended Deal Language

```
Condition 1: Seller to provide written evidence of SOC2 control gap remediation 
             (SR-01 and SR-02) prior to close. ✅ Satisfied.

Condition 2: Seller warrants no material security incidents or regulatory notices 
             in the 24 months prior to close, except as disclosed.

Condition 3: Post-close obligation — Secrets Manager migration (SR-04) to be 
             completed within 90 days of close. Monitored via integration plan.
```
