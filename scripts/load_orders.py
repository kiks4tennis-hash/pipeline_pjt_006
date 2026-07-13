from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

# ==============================
# Config
# ==============================

CSV_PATH = Path("data/orders.csv")

DB_USER = "airflow"
DB_PASSWORD = "airflow"
DB_HOST = "postgres"
DB_PORT = "5432"
DB_NAME = "airflow"

TABLE_NAME = "raw_orders"

# ==============================
# Load CSV
# ==============================

df = pd.read_csv(CSV_PATH)

# ==============================
# Connect PostgreSQL
# ==============================

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==============================
# Write Table
# ==============================

df.to_sql(
    TABLE_NAME,
    engine,
    if_exists="replace",
    index=False,
)

print(f"{len(df)} rows loaded into {TABLE_NAME}")