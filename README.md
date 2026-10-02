# Oncology Cancer Opportunity & Drug Portfolio Analytics

## Project Objective

This project builds a data-driven framework to screen cancer indications and oncology drugs for **clinical-development opportunity**.

The analysis combines:

- Cancer epidemiology and disease burden
- Clinical-trial activity
- Active and completed trials
- Sponsor breadth and competitive landscape
- Cross-cancer drug presence
- Robustness and sensitivity analysis
- Therapeutic annotation where sufficiently defensible

The final outputs are designed for **business, strategy, portfolio-screening, and Power BI visualization**.

> **Important:** The final drug ranking is a clinical-development opportunity screen. It is not a guaranteed financial-return forecast, valuation model, or investment recommendation.

---

## Final Analytical Scope

The final Tier-1 analysis covers:

- **21** cancer indications screened
- **4** Tier-1 cancer indications retained:
  1. Lung
  2. Pancreatic
  3. Colorectal
  4. Liver
- **325** Tier-1 drugs
- **602** unique Tier-1 drug–cancer pairs
- No duplicate Tier-1 drug–cancer pairs in the final landscape

---

## Authoritative Step-56 Drug Ranking

The preserved **Step-56 ranking** is used as the authoritative final drug ranking.

### Top 5 drugs by Step-56 opportunity score

1. Carboplatin
2. Gemcitabine
3. Cisplatin
4. Oxaliplatin
5. Pemetrexed

### Step-56 scoring framework

| Component | Weight |
|---|---:|
| Cancer breadth | 40% |
| Active trials | 30% |
| Trial activity | 20% |
| Sponsor breadth | 10% |

The score is intended to identify drugs with stronger signals across the selected clinical-development dimensions.

---

## Key Findings

### Cancer Opportunities

The final Tier-1 cancer screen retained:

- Lung
- Pancreatic
- Colorectal
- Liver

### Cross-Cancer Drug Landscape

The top five drugs by the authoritative Step-56 opportunity score were:

- Carboplatin
- Gemcitabine
- Cisplatin
- Oxaliplatin
- Pemetrexed

### Interpretation

These rankings identify drugs with substantial presence across the selected Tier-1 cancer indications and clinical-development activity.

They should be interpreted as **portfolio-screening signals**, rather than evidence of commercial profitability, future sales, or investment returns.

---

## Power BI Dashboard

The planned Power BI dashboard contains five analytical pages.

### Page 1 — Executive Overview

- Tier-1 cancer count
- Tier-1 drug count
- Top 5 drugs by opportunity score
- Total trials for selected drugs
- Cancer opportunity ranking

### Page 2 — Cancer Landscape

- Cancer opportunity ranking
- Incidence vs. deaths
- Trial volume by cancer
- Late-stage / Phase 3 activity
- Sponsor count and competition density

### Page 3 — Drug Landscape

- Top 20 authoritative drug ranking
- Total trials
- Active trials
- Sponsor breadth
- Cancer breadth
- Opportunity score

### Page 4 — Drug × Cancer

- Cancer slicer
- Top drugs for the selected cancer
- Indication-specific trial activity
- Active vs. completed trials
- Sponsor breadth

### Page 5 — Robustness

- Scenario ranks
- Mean rank
- Best and worst rank
- Rank range
- Top-5 / Top-10 scenario counts

---

## Repository Structure

```text
oncology-cancer-opportunity/
│
├── README.md
│
├── data/
│   ├── 01_epidemiology_final.csv
│   ├── 01_FINAL_CANCER_OPPORTUNITY_DECISION.csv
│   ├── 02_FINAL_TOP_DRUGS_BY_CANCER.csv
│   ├── 03_cancer_competitive_landscape.csv
│   ├── 04_drug_cancer_trial_metrics.csv
│   ├── 06_drug_therapeutic_dashboard.csv
│   ├── 07_AUTHORITATIVE_STEP56_TOP20.csv
│   ├── 07_robustness_ranking.csv
│   ├── 08_AUTHORITATIVE_STEP56_TOP5.csv
│   ├── 09_robust_top10.csv
│   ├── DASHBOARD_CROSS_CANCER_TOP15.csv
│   ├── DASHBOARD_DISEASE_MASTER.csv
│   └── DASHBOARD_DRUG_SHORTLIST.csv
│
└── docs/
    └── POWER_BI_DASHBOARD_PLAN.md
