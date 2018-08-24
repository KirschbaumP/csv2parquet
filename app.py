import pandas as pd
import os

print("CSV-File:")
print(os.environ.get('CSV'))
print("PARQUET-File:")
print(os.environ.get('PARQUET'))

df = pd.read_csv(os.environ.get('CSV'))
df.to_parquet(os.environ.get('PARQUET'))

