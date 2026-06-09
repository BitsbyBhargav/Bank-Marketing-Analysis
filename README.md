# Bank Customer Subscription Analytics
### End-to-End Data Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/MS%20SQL%20Server-CC2927?style=flat&logo=microsoftsqlserver&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat)

---

## Business Problem

A Portuguese bank conducted direct marketing campaigns via telephone
to promote term deposit subscriptions. Despite contacting **41,188
customers**, only **11.3% subscribed** — meaning **88.7% of campaign
effort produced zero return**.

This project performs a comprehensive data analysis to identify
*who* subscribes, *why* they subscribe, and *how* the bank can
optimize future campaigns for significantly higher conversion rates.

---

## Project Objectives

| # | Objective |
|---|---|
| 1 | Identify customer profiles most likely to subscribe |
| 2 | Discover which campaign strategies drive conversions |
| 3 | Understand how economic conditions influence decisions |
| 4 | Segment customers by behavior and subscription likelihood |
| 5 | Build a scalable multi-tool analytics pipeline |
| 6 | Deliver actionable business recommendations |

---

## Dataset

| Attribute | Detail |
|---|---|
| **Source** | UCI Machine Learning Repository |
| **Domain** | Portuguese Bank — Direct Marketing Campaign |
| **Records** | 41,188 customer interactions |
| **Features** | 20 input variables + 1 target variable |
| **Target** | `y` — Did customer subscribe? (`yes` / `no`) |
| **Class Balance** | 88.7% No \| 11.3% Yes (1:7 imbalance) |
| **Missing Values** | None (hidden unknowns in 6 categorical columns) |

### Feature Categories

**Customer Demographics**
`age` · `job` · `marital` · `education` · `default` · `housing` · `loan`

**Campaign Contact Details**
`contact` · `month` · `day_of_week` · `duration` · `campaign` · `pdays` · `previous` · `poutcome`

**Macroeconomic Indicators**
`emp.var.rate` · `cons.price.idx` · `cons.conf.idx` · `euribor3m` · `nr.employed`

---

## Tech Stack

| Layer | Tool |
|---|---|
| Data Processing | Python 3.x · Pandas · NumPy |
| Visualization | Matplotlib · Seaborn |
| Statistical Modeling | Scikit-learn (Logistic Regression) |
| Database Layer | Microsoft SQL Server |
| Cloud Storage | AWS S3 |
| Cloud Query | AWS Athena |
| Business Intelligence | Power BI Desktop |
| Version Control | Git · GitHub |
| Documentation | Markdown · Notion |
| IDE | Jupyter Notebook |

---

## Project Architecture

```
Raw Dataset (CSV)
        │
        ▼
┌───────────────────┐
│   Python Layer    │  Pandas · NumPy · Matplotlib · Seaborn
│   - Data cleaning │  Scikit-learn (Logistic Regression)
│   - EDA           │
│   - Modeling      │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  MS SQL Server    │  Window Functions · CTEs
│  - Schema design  │  Advanced aggregations
│  - SQL analysis   │  Customer profiling queries
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   AWS Cloud       │  S3 (storage) · Athena (query)
│   - Data lake     │  Cloud-native pipeline
│   - Cloud queries │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   Power BI        │  Interactive dashboard
│   - Dashboard     │  Executive-level visuals
│   - Business KPIs │  Campaign insights
└───────────────────┘
```

---

## Repository Structure

```
bank-marketing-analysis/
│
├── data/
│   └── data.csv                          # Raw dataset
│
├── notebooks/
│   ├── Bank_Marketing_Inspection.ipynb   # Milestone 1 — Basic EDA
│   └── Advance_Bank_Term_Deposit.ipynb   # Milestone 2 — Deep analysis
│                                           + modeling
│
├── sql/
│   ├── schema.sql                        # Table creation script
│   ├── eda_queries.sql                   # Exploratory queries
│   ├── customer_profiling.sql            # Segmentation queries
│   └── campaign_analysis.sql            # Campaign performance
│
├── dashboard/
│   └── bank_marketing.pbix              # Power BI dashboard file
│
├── docs/
│   ├── DATA_DICTIONARY.md               # All 21 columns explained
│   ├── PROJECT_LOGBOOK.md               # 30-day session log
│   └── INSIGHTS.md                      # Key business findings
│
├── assets/
│   ├── age_distribution.png
│   ├── job_distribution.png
│   ├── economic_indicators.png
│   ├── contact_method.png
│   ├── contact_frequency.png
│   ├── correlation_matrix.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── architecture_diagram.png
│
├── .gitignore
└── README.md
```

---

## Analysis Scope

### Phase 1 — Exploratory Data Analysis
- Data quality inspection + hidden null detection
- Univariate analysis — every column profiled
- Bivariate analysis — each feature vs target
- Customer demographic segmentation
- Campaign behavior and contact pattern analysis
- Macroeconomic indicator impact analysis

### Phase 2 — SQL Analysis Layer
- MS SQL Server schema design and data ingestion
- Subscription rate queries by demographic segment
- Window function analysis — rankings and percentiles
- CTE-based customer journey analysis
- Campaign performance and ROI simulation queries
- Ideal customer profile extraction

### Phase 3 — Predictive Modeling
- Feature engineering and encoding
- Logistic Regression with class imbalance handling
- Model evaluation — classification report, confusion matrix
- Feature importance analysis
- Business interpretation of model outputs

### Phase 4 — Cloud Integration
- Dataset storage on AWS S3
- SQL querying via AWS Athena
- Cloud pipeline documentation

### Phase 5 — Business Intelligence
- Power BI interactive dashboard
- Executive summary report
- Campaign optimization recommendations

---

## Key Business Questions Answered

```
Q1. Who is the ideal customer profile for term deposit campaigns?
Q2. Which months and contact methods produce highest conversion?
Q3. How do economic conditions influence subscription likelihood?
Q4. Does previous campaign history predict future behavior?
Q5. How many contacts optimizes conversion before diminishing returns?
Q6. Which customer segments should the next campaign prioritize?
```

---

## Key Findings (Preview)

> Full findings in [`docs/INSIGHTS.md`](docs/INSIGHTS.md)

- **Class imbalance:** 1:7 ratio (yes:no) — naive model useless
- **Contact method:** Cellular significantly outperforms telephone
- **Optimal contacts:** 1–2 contacts per customer maximizes conversion
- **Economic timing:** Low Euribor rate periods correlate with higher subscription
- **Top segments:** Retired and student job categories show highest conversion rates
- **Data leakage:** `duration` column excluded from production model — unknown pre-call

---

## Project Deliverables

- [x] Raw dataset loaded and inspected
- [x] Basic EDA notebook (Milestone 1)
- [x] Advanced EDA + modeling notebook (Milestone 2)
- [x] GitHub repository structured
- [ ] SQL analysis layer (MS SQL Server)
- [ ] AWS S3 + Athena cloud integration
- [ ] Power BI dashboard
- [ ] Data dictionary complete
- [ ] Executive insights report
- [ ] 30-day project logbook
- [ ] LinkedIn project post

---

## Project Logbook

> Detailed session logs in [`docs/PROJECT_LOGBOOK.md`](docs/PROJECT_LOGBOOK.md)

| Session | Date | Focus | Status |
|---|---|---|---|
| 001 | TBD | Dataset inspection + basic EDA | ✅ Done |
| 002 | TBD | Advanced EDA + modeling | ✅ Done |
| 003 | TBD | SQL schema + data ingestion | 🔄 Upcoming |
| 004 | TBD | SQL analysis queries | 🔄 Upcoming |
| 005 | TBD | AWS S3 + Athena setup | 🔄 Upcoming |
| 006 | TBD | Power BI dashboard | 🔄 Upcoming |
| ... | ... | ... | ... |

---

## Author

**Bhargav Sonawane**
Computer Science Student · Big Data & Cloud Engineering
Primary: Data Analytics · Secondary: Cloud Engineering

[![GitHub](https://img.shields.io/badge/GitHub-BitsbyBhargav-181717?style=flat&logo=github)](https://github.com/BitsbyBhargav)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/yourprofile)

---

## License

This project is licensed under the MIT License.
Dataset source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing)

---

*Built as part of a 30-day advanced analytics portfolio project — June 2026*