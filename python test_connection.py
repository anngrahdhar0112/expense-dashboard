import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

HOST = "localhost"
PORT = "55432"
DB = "analytics_lab"
USER = "admin"
PASSWORD = "admin"

# 1) psycopg2 raw connection (OK)
conn = psycopg2.connect(
    host=HOST, port=PORT, database=DB, user=USER, password=PASSWORD
)
print("✅ psycopg2 connection successful!")

# Prefer using SQLAlchemy for pandas
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

# 2) pandas via SQLAlchemy (no warning)
df = pd.read_sql_query("SELECT current_database(), version();", engine)
print(df)

# 3) SQLAlchemy 2.x query (use text() or exec_driver_sql)
with engine.connect() as con:
    # Either of these is fine:
    # result = con.execute(text("SELECT NOW()"))
    result = con.exec_driver_sql("SELECT NOW()")
    rows = result.fetchall()
    print("✅ SQLAlchemy connection successful!", rows)

conn.close()
