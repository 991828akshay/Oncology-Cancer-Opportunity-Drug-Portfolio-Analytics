# Power BI Dashboard Build Plan

## Recommended model

Use these as the main tables:

1. `DASHBOARD_DISEASE_MASTER.csv`
2. `DASHBOARD_DRUG_SHORTLIST.csv`
3. `DASHBOARD_CROSS_CANCER_TOP15.csv`
4. `07_AUTHORITATIVE_STEP56_TOP20.csv`
5. `07_robustness_ranking.csv`
6. `01_epidemiology_final.csv`
7. `03_cancer_competitive_landscape.csv`
8. `06_drug_therapeutic_dashboard.csv`

Do not load every intermediate `DF_*.csv` file.

## Page 1 — Executive Overview

Cards:
- 4 Tier-1 cancers
- 325 Tier-1 drugs
- 602 unique drug-cancer pairs

Charts:
- Cancer ranking: `DASHBOARD_DISEASE_MASTER`
- Top 5 drugs: `08_AUTHORITATIVE_STEP56_TOP5`
- Trial activity by top drug
- Sponsor breadth by top drug

## Page 2 — Cancer Landscape

Use `01_epidemiology_final` and `03_cancer_competitive_landscape`.

Recommended visuals:
- Bar: incidence by cancer
- Bar: deaths by cancer
- Bar: total trials by cancer
- Scatter: trial volume vs competition density
- Table: phase 3 fraction, late-stage fraction, sponsors

Slicer:
- cancer_indication

## Page 3 — Drug Opportunity

Use `07_AUTHORITATIVE_STEP56_TOP20`.

Recommended visuals:
- Bar: drug_opportunity_score by canonical_drug
- Column: active_target_trials
- Column: total_target_trials
- Scatter: active trials vs total sponsors
- Table: rank, score, trials, active trials, sponsors, therapeutic class

## Page 4 — Drug × Cancer

Use `DASHBOARD_DRUG_SHORTLIST`.

Recommended visuals:
- Matrix: cancer_indication × canonical_drug
- Bar: indication_trials
- Bar: active_not_recruiting_trials
- Bar: unique_sponsors

Slicer:
- cancer_indication

## Page 5 — Robustness

Use `07_robustness_ranking` or `09_robust_top10`.

Recommended visuals:
- Mean rank by cancer
- Rank range by cancer
- Top-5 count
- Top-10 count
- Scenario comparison table

## Important interpretation rule

Do not label the Top 5 drugs as "most profitable" or "best investments".

Use:
- "highest clinical-development opportunity score"
- "highest-ranked within the project's selected Tier-1 cancer screen"
- "portfolio-screening candidates"

The current dataset does not contain reliable comparable market-size/revenue information, so commercial ROI cannot be concluded from these results alone.
