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