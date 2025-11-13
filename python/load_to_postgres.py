import pandas as pd
from sqlalchemy import create_engine, text

# Step 1: Connect to PostgreSQL
engine = create_engine("postgresql+psycopg2://admin:admin@localhost:55432/analytics_lab")

# Step 2: Load CSV
file_upload = pd.read_csv('../data/clean/superstore_sales.csv', encoding='latin1')


# Step 3: Preview
print(file_upload.head())
print(file_upload.info())

# Step 4: Ensure schema exists
with engine.connect() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS dashboard;"))
    conn.commit()

# Step 5: Upload data to PostgreSQL
file_upload.to_sql(
    name='sales_raw',       # ✅ table name
    schema='dashboard',     # ✅ schema created above
    con=engine,
    if_exists='replace',    # overwrite if exists
    index=False
)

print("✅ Data uploaded successfully to dashboard.sales_raw")

# Step 6: Verify upload
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM dashboard.sales_raw;"))
    print("✅ Rows inserted:", result.scalar())
