Date: June 1, 2026 (Day 1)

Task: Project Environment Setup & Baseline Data Ingestion

Understanding: The goal was to initialize the Jupyter Notebook environment and load the Portuguese Bank Marketing dataset to verify its structure. Standard methods like .info() and .isnull().sum() show that the dataset has 41,188 rows and 21 columns with no structural Python NaN values. The target variable is y (whether the customer subscribed to a term deposit).

Problems Encountered: Initial look at df.isnull().sum() shows 0 missing values across all columns, which makes the dataset seem falsely perfect. However, reading the project brief shows that missing data is hidden as text strings named 'unknown'.

Solution/Code: 

#Importing CSV files
import pandas as pd

# Load the dataset
df = pd.read_csv('bankmarketing.csv')

# Display the first few rows
df.head()

# Check for missing values and data types
print("--- Data Info ---")
df.info()

print("\n--- Missing Values Count ---")
print(df.isnull().sum())


Date: June 2, 2026 (Day 2)

Task: Hidden Placeholder Audit & Local SQL Database Initialization

Understanding: The objective was to expose missing values hidden as text strings ('unknown') within categorical columns and design an optimized local storage layer in MS SQL Server. By breaking the 21 columns into dimensional (dim_customers, dim_economic_indicators) and fact-based (fact_marketing_campaigns) tables, we ensure optimal indexing and faster execution of complex analytical queries during Phase 2.

Problems Encountered: Found massive data gaps masquerading as valid text fields (e.g., default containing 8,597 'unknowns'). Additionally, standard flat-file architectures cause redundant data storage, requiring a relational schema mapping approach before importing data.

Solution/Code: Created the BankMarketingDB database and executed DDL scripts to establish explicit data types, primary keys, and foreign key constraints across our core fact and dimension layers.

# Load data
df = pd.read_csv('../Data/bankmarketing.csv')

print("════════════════════════════════════════════")
print("          HIDDEN 'UNKNOWN' AUDIT            ")
print("════════════════════════════════════════════")

# Find 'unknown' values in categorical columns
cat_cols = df.select_dtypes(include=['object']).columns
unknown_data = {}

for col in cat_cols:
    count = (df[col] == 'unknown').sum()
    pct = (count / len(df)) * 100
    if count > 0:
        unknown_data[col] = [count, round(pct, 2)]

# Display as a clean executive summary table
unknown_df = pd.DataFrame.from_dict(unknown_data, orient='index', columns=['Missing Count', 'Percentage (%)'])
print(unknown_df.sort_values(by='Missing Count', ascending=False))

print("\n════════════════════════════════════════════")
print("          JOB PROFILE DISTRIBUTION          ")
print("════════════════════════════════════════════")
# See who the bank spends most of its time calling
print(df['job'].value_counts())


Data Migration Script:

import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import os

# 1. Load your local dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '../Data/bankmarketing.csv')
df = pd.read_csv(csv_path)

# 2. Configure Database Connection (Windows Authentication)
SERVER = 'LOQ\SQLEXPRESS'  
DATABASE = 'BankMarketingDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

connection_string = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
# Added fast_executemany=True here to speed up inserts dramatically
engine = create_engine(connection_string, fast_executemany=True)

print("🚀 Connection established successfully. Starting data migration...")

try:
    # Use engine.begin() so everything commits together safely
    with engine.begin() as connection:
        print("🧹 Cleaning destination tables safely...")
        
        # Step A: Delete the Fact table first (removes foreign key parents)
        connection.execute(text("TRUNCATE TABLE fact_marketing_campaigns;"))
        
        # Step B: Safe delete for tables targeted by Foreign Keys
        connection.execute(text("DELETE FROM dim_customers;"))
        connection.execute(text("DELETE FROM dim_economic_indicators;"))
        
        # Step C: Reset identity counters
        connection.execute(text("DBCC CHECKIDENT ('dim_customers', RESEED, 0);"))
        connection.execute(text("DBCC CHECKIDENT ('dim_economic_indicators', RESEED, 0);"))

        print("🗑️ Database tables cleared and identity counters reseeded.")

        # -------------------------------------------------------------
        # STEP 3: Populate dim_customers (Notice con=connection)
        # -------------------------------------------------------------
        print("📦 Migrating Customer Demographics...")
        customers_df = df[['age', 'job', 'marital', 'education', 'default', 'housing', 'loan']].copy()
        customers_df.to_sql('dim_customers', con=connection, if_exists='append', index=False, chunksize=5000)

        # -------------------------------------------------------------
        # STEP 4: Populate dim_economic_indicators (Notice con=connection)
        # -------------------------------------------------------------
        print("📈 Migrating Economic Indicators...")
        economic_df = df[['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']].copy()
        economic_df.columns = ['emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed']
        economic_df.to_sql('dim_economic_indicators', con=connection, if_exists='append', index=False, chunksize=5000)

        # -------------------------------------------------------------
        # STEP 5: Populate fact_marketing_campaigns
        # -------------------------------------------------------------
        print("⚙️ Mapping and Migrating Fact Campaign Table...")
        
        # Fetch the IDs using the same active open transaction connection
        customer_ids = pd.read_sql("SELECT customer_id FROM dim_customers ORDER BY customer_id", con=connection)
        economic_ids = pd.read_sql("SELECT economic_id FROM dim_economic_indicators ORDER BY economic_id", con=connection)

        fact_df = pd.DataFrame({
            'customer_id': customer_ids['customer_id'],
            'economic_id': economic_ids['economic_id'],
            'contact_type': df['contact'],
            'month': df['month'],
            'day_of_week': df['day_of_week'],
            'duration': df['duration'],
            'campaign_count': df['campaign'],
            'pdays': df['pdays'],
            'previous_contacts': df['previous'],
            'previous_outcome': df['poutcome'],
            'subscribed': df['y']
        })

        fact_df.to_sql('fact_marketing_campaigns', con=connection, if_exists='append', index=False, chunksize=5000)
        print("✅ Data Migration Complete! All 41,188 records processed successfully.")

except Exception as e:
    print(f"❌ Error encountered during migration: {str(e)}")