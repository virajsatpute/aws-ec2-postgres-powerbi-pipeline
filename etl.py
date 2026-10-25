import re
import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv("/home/ubuntu/superstore.csv", encoding="latin-1")

# Transform
df.columns = [re.sub(r"[^0-9a-zA-Z]+", "_", c).strip("_").lower() for c in df.columns]
df = df.dropna(how="all").drop_duplicates()
for c in df.columns:
    if "date" in c:
        df[c] = pd.to_datetime(df[c], errors="coerce", dayfirst=True, format="mixed")
        print(c, "-> unparsed dates:", df[c].isna().sum())

# Load
engine = create_engine("postgresql+psycopg2://etl:YOUR_PASSWORD@localhost/sales")
df.to_sql("orders", engine, if_exists="replace", index=False)
print("Loaded rows:", len(df))
print("Columns:", list(df.columns))