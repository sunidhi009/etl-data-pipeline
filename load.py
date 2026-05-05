import pandas as pd
import os

# check file exists
if not os.path.exists("data/processed_data.csv"):
    print("Processed data not found! Run transform.py first.")
    exit()

df = pd.read_csv("data/processed_data.csv")

print("\nTop 5 Records:\n")
print(df.head())

print("\nTotal Records:", len(df))
print("Columns:", df.columns.tolist())