# Data Dictionary — Bank Marketing Dataset

| Column | Type | Description | Business Relevance |
|---|---|---|---|
| age | int | Customer age | Older = more financially stable |
| job | categorical | Occupation | Behavior varies by job type |
| duration | int | Call duration (sec) | Strong predictor — leakage risk |
| pdays | int | Days since last contact | 999 = never contacted before |
| euribor3m | float | 3-month Euribor rate | Macro indicator — deposit appeal |
| y | binary | Subscribed? yes/no | **Target variable** |