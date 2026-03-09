# 📦 M&A Tech Due Diligence: Cross-Border Payments SaaS

> **Case Study · Product Portfolio · Adeitia Kalyann Boniface**  
> Role: Director of Product (Fractional M&A Advisor) | Engagement: 6 weeks | Deal Size: $22M

---

## Overview

This repository documents a technology due diligence engagement for a **Series B cross-border payments SaaS** platform being evaluated by a PE firm for acquisition. The target operated in SME payment corridors across North America and Southeast Asia, with 140% ARR YoY growth at time of assessment.

> ⚠️ **Anonymization Notice:** All company names, personnel, and commercially sensitive figures have been anonymized per NDA obligations. Deal size, domain, and structural findings are representative of a real engagement.

---

## The Ask

The PE firm needed answers to three questions before proceeding to term sheet:

1. Can the platform scale **5x current transaction volume** without a platform rewrite?
2. Is the **technical moat** (payment rail integrations, proprietary routing logic) defensible enough to justify the valuation premium?
3. Are there any **regulatory or security risks** that should be surfaced as deal conditions?

---

## Engagement Snapshot

| Dimension | Detail |
|---|---|
| **Deal Type** | Acquisition (PE-led) |
| **Deal Size** | $22M |
| **Target** | Series B SaaS, Cross-Border Payments |
| **Geography** | North America + Southeast Asia corridors |
| **Engagement Length** | 6 weeks |
| **My Role** | Lead Product & Technology Advisor |
| **Deliverables** | Red-flag memo (Week 3), Full DD report (Week 6), Deal condition recommendations |

---

## Methodology

This engagement followed my **SaaS M&A Technology Due Diligence Framework** — a 6-dimension assessment model designed to produce consistent, investor-grade outputs across deal sizes and domains.

```
Week 1–2  │  Discovery Sprint
          │  ├── Document ingestion (architecture, roadmap, audits, org charts)
          │  ├── Stakeholder mapping
          │  └── Red-flag hypothesis generation

Week 2–4  │  Deep Dive Workshops
          │  ├── CTO architecture review (3 sessions)
          │  ├── Engineering lead interviews (3 engineers)
          │  ├── SOC2 Type II audit walkthrough
          │  └── Customer reference calls (2 accounts)

Week 4–6  │  Risk Synthesis & Reporting
          │  ├── Risk heatmap generation
          │  ├── Technical debt quantification
          │  ├── Deal condition drafting
          │  └── Investor-ready final report
```

---

## Repository Structure

```
saas-payments-dd/
│
├── README.md                        ← You are here
│
├── framework/
│   ├── 01_scalability_scorecard.md  ← Infrastructure & scalability assessment
│   ├── 02_product_maturity.md       ← Product maturity scoring model
│   ├── 03_technical_debt.md         ← Tech debt quantification template
│   ├── 04_security_compliance.md    ← Security & SOC2 risk register
│   ├── 05_team_dependency_map.md    ← Engineering org & key-person risk
│   └── 06_integration_risk.md       ← Post-close integration risk matrix
│
├── analysis/
│   ├── risk_heatmap.py              ← Generates risk heatmap visualization
│   ├── risk_data.json               ← Structured risk findings (anonymized)
│   └── requirements.txt             ← Python dependencies
│
├── docs/
│   ├── red_flag_memo.md             ← Week 3 red-flag summary (template)
│   └── deal_conditions.md           ← Recommended deal conditions & escrow
│
└── assets/
    └── risk_heatmap_output.png      ← Generated heatmap (pre-run output)
```

---

## Key Findings Summary

### 🟡 Scalability
The platform could support **3x transaction volume** without re-architecture. Reaching 5x required an estimated **$1.2M infrastructure investment** — primarily in database sharding and queue management. This was surfaced as a deal condition (tech debt escrow), not a deal blocker.

### 🔴 Concentration Risk
A **single-PSP dependency** (one payment rail partner accounting for ~68% of processed volume) was identified as the most significant risk. Acquirer was advised to negotiate a rail diversification milestone into post-close integration terms.

### 🟡 Security & Compliance
SOC2 Type II audit was current. **Two open control gaps** were identified — both low severity, both remediated within the 6-week engagement window. GDPR posture was adequate for current operating geographies.

### 🟢 Product Moat
Proprietary FX routing logic and existing PSP relationship network represented a credible technical moat. Customer NPS of **68** across 4 reference accounts. Churn risk assessed as low.

---

## Outcome

| Metric | Result |
|---|---|
| Deal Status | ✅ Closed with modified terms |
| Tech Debt Escrow | $1.5M negotiated into deal terms |
| Pre-close Remediation | 2 SOC2 control gaps resolved |
| Decision Cycle | 12% faster than PE firm baseline |
| Post-close Risk | Rail concentration milestone added to integration plan |

---

## Framework & Templates

The [/framework](./framework/) directory contains the full 6-dimension assessment templates used in this engagement. Each template is designed to be reusable across SaaS M&A deals — parameterized by domain and deal stage.

The [/analysis](./analysis/) directory contains a Python script that takes a `risk_data.json` file (structured per the schema in this repo) and generates an investor-ready risk heatmap. See [Running the Analysis](#running-the-analysis) below.

---

## Running the Analysis

```bash
# Clone the repo
git clone https://github.com/AdeitiaBoniface/saas-payments-dd.git
cd saas-payments-dd

# Install dependencies
pip install -r analysis/requirements.txt

# Generate the risk heatmap
python analysis/risk_heatmap.py

# Output saved to assets/risk_heatmap_output.png
```

---

## About This Portfolio

This case study is part of a product portfolio documenting my work as a **Fractional Head of Product and M&A Technology Advisor**. Each case covers a different Fintech SaaS domain:

| Repo | Domain | Deal Size |
|---|---|---|
| **saas-payments-dd** ← this repo | Cross-Border Payments | $22M |
| saas-banking-infra-dd *(coming soon)* | Core Banking Infrastructure | $18M |
| saas-regtech-dd *(coming soon)* | AML/KYC RegTech | $9M |

---

## Connect

- 🌐 [LinkedIn](https://www.linkedin.com/in/adeitiaboniface/)
- 📍 Chennai, India

> *Open to fractional engagements with PE/VC-backed Fintech SaaS companies. Typical availability: 2–3 days/week.*
