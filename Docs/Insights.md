# Key Business Insights

## Insight 1 — Severe Class Imbalance
88.7% no / 11.3% yes. 1:7 ratio.
Naive model predicting "no" always = 88.7% accuracy
but zero business value. Must address in modeling phase.

## Insight 2 — Economic Indicators Cluster
emp.var.rate and euribor3m: 0.97 correlation.
cons.price.idx and euribor3m: 0.78 correlation.
Multicollinearity risk. Feature selection needed.

## Insight 3 — pdays anomaly
75% of pdays = 999 (never contacted before).
Median = 999. Needs special handling — not a
true numerical variable. Binary encode: contacted/not.

## Insight 4 — Duration leakage risk
Duration = seconds of last call. Strong predictor
but unknown BEFORE the call happens. Cannot be used
in a real production model. Drop for modeling.