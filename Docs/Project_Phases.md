# Project Roadmap: Bank Customer Subscription Analytics
**Analyst:** Bhargav Sonawane  
**Timeline:** June 2026 (30 Days)  
**Target:** Production-Grade Portfolio Piece & 2-Credit College Submission  

---

## 🏁 Phase 1 — Deep Exploratory Data Analysis (EDA)
- [ ] **Data Quality Inspection:** Check schema, shapes, missing values, and data distributions.
- [ ] **Hidden Null Detection:** Locate and isolate string `'unknown'` values masquerading as clean data.
- [ ] **Univariate Analysis:** Generate structural distributions for all 21 demographic, campaign, and economic variables.
- [ ] **Bivariate Analysis:** Plot every feature directly against the target variable `y` (Subscription Rate).
- [ ] **Customer Segmentation:** Analyze behavior, campaign contact frequencies, and conversion drop-offs.
- [ ] **Economic Impact Analysis:** Evaluate how macro indicators (`euribor3m`, `nr.employed`) correlate with customer choices.

## 🗄️ Phase 2 — SQL Server Analysis Layer
- [ ] **Schema Design & Load:** Configure local MS SQL Server environment, define correct data types, and import raw data.
- [ ] **Demographic Benchmarking:** Query conversion rates sliced by job profile, education level, and marital status.
- [ ] **Window Function Analytics:** Calculate cumulative subscription totals, rankings, and behavioral percentiles.
- [ ] **CTE Customer Journey Tracking:** Map multi-stage conversion behavior using Common Table Expressions.
- [ ] **Campaign Performance Metrics:** Write optimized queries to isolate high-performing contact windows.
- [ ] **Ideal Customer Profile (ICP) Extraction:** Isolate statistical thresholds that yield maximum conversion.

## 🧠 Phase 3 — Advanced Python Analysis
- [ ] **Feature Engineering:** Create behavioral markers (e.g., binning `age`, segmenting contact `duration`, processing `pdays`).
- [ ] **Statistical Significance Testing:** Implement Chi-Square and t-tests to prove features aren't correlating by random chance.
- [ ] **Advanced Visualizations:** Generate matrix plots, violin plots, and multi-dimensional segment breakdowns.
- [ ] **Correlation Deep Dive:** Compute correlation matrices for both linear and non-linear categorical dependencies.

## ☁️ Phase 4 — AWS Cloud Integration
- [ ] **S3 Data Ingestion:** Create and configure secure AWS S3 buckets to host raw and processed datasets.
- [ ] **AWS Athena Configuration:** Define external table schemas mapped directly to data sitting in S3.
- [ ] **Cloud-Based Querying:** Run cloud SQL analysis via Athena to validate remote storage functionality.
- [ ] **Pipeline Documentation:** Diagram and document the local-to-cloud data ingestion flow.

## 📊 Phase 5 — Business Intelligence & Power BI
- [ ] **Data Modeling:** Connect Power BI Desktop to local SQL Server / Cloud outputs and establish clean relations.
- [ ] **DAX Calculations:** Write explicit measures for subscription rates, relative variations, and running totals.
- [ ] **Dashboard Development:** Build an interactive 4-5 page report:
  - Executive Overview Dashboard
  - Demographic & Customer Profiles
  - Behavioral Campaign Optimization Layer
  - Macroeconomic Matrix
- [ ] **Executive Recommendations:** Translate data visuals into corporate strategy recommendations.

## 🚀 Phase 6 — Documentation, Deliverables & Delivery
- [ ] **GitHub Repository Setup:** Organize repository folders systematically (`/notebooks`, `/sql`, `/bi`, `/docs`).
- [ ] **Executive README.md:** Author a comprehensive, business-facing summary detailing findings and pipeline architecture.
- [ ] **Data Dictionary:** Document detailed meta-definitions for all 21 columns.
- [ ] **30-Day Project Logbook:** Assemble daily/weekly session progress notes for academic validation.
- [ ] **LinkedIn Capstone Post:** Craft a data-driven project showcase post highlighting outcomes and tools used.
- [ ] **College Credit Presentation:** Format a technical slide deck optimized for your 2-credit academic evaluation jury.