# Oncology Cancer Opportunity & Drug Portfolio Analytics

## Clinical Development Opportunity Screening Using Cancer Burden, Clinical Trials and Drug Portfolio Data

🔗 **Live Interactive Dashboard:**  
https://oncology-cancer-opportunity-drug-portfolio-analytics-ykw9bldgq.streamlit.app/

---

## 📌 Project Overview

Oncology drug development involves significant uncertainty around disease burden, clinical-development activity, competitive intensity and the breadth of existing drug portfolios.

This project develops a **data-driven clinical-development opportunity screening framework** for oncology.

The analysis integrates:

- Cancer epidemiology
- Clinical-trial activity
- Active and completed clinical trials
- Drug–cancer relationships
- Sponsor breadth
- Cross-cancer drug presence
- Therapeutic classification
- Scenario-based opportunity analysis
- Robustness analysis across different analytical assumptions

The final results are presented through an interactive **Streamlit dashboard** that allows users to explore cancer indications, oncology drugs and drug–cancer relationships.

> **Important:** This project is designed as an opportunity-screening and portfolio-analytics framework. It is not intended to provide financial investment advice or a definitive recommendation to invest in a particular drug or cancer indication.

---

# 🎯 Business Problem

Pharmaceutical companies evaluating oncology portfolios need to consider multiple dimensions simultaneously.

Looking only at disease prevalence or only at clinical-trial activity can provide an incomplete picture.

The project therefore asks:

### Cancer-level questions

- Which cancer indications show substantial disease burden?
- How much clinical-development activity exists around each indication?
- How active is the current development landscape?
- How broad is the sponsor presence?
- Do opportunity rankings remain stable under different analytical scenarios?

### Drug-level questions

- Which drugs are being studied across multiple cancer indications?
- Which drugs have broad clinical-development activity?
- Which drugs have substantial active-trial presence?
- How many sponsors are associated with each drug?
- Which therapeutic areas and classes dominate the development landscape?

### Portfolio-level question

> Can epidemiology and clinical-development data be combined into a structured framework for screening oncology development opportunities?

---

# 🧬 Analytical Framework

The project follows a multi-stage analytical pipeline:

```text
Public Data Sources
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning & Standardization
        │
        ▼
Drug / Cancer Name Harmonization
        │
        ▼
Clinical Trial Aggregation
        │
        ├───────────────┐
        ▼               ▼
Cancer-Level       Drug-Level
Analysis           Analysis
        │               │
        ▼               ▼
Opportunity       Drug Opportunity
Scenarios         Analysis
        │               │
        └───────┬───────┘
                ▼
       Robustness Analysis
                │
                ▼
       Dashboard & Visualization
