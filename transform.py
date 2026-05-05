import pandas as pd
import os

# check if file exists
if not os.path.exists("data/raw_data.csv"):
    print("Raw data not found! Run extract.py first.")
    exit()

df = pd.read_csv("data/raw_data.csv")

# select important columns
df = df[['name', 'current_price', 'market_cap']]

# remove null values
df.dropna(inplace=True)

# sort by market cap
df = df.sort_values(by='market_cap', ascending=False)

# save processed data
df.to_csv("data/processed_data.csv", index=False)

print("Data transformed successfully!")