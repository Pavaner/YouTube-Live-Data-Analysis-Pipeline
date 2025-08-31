import pandas as pd

df = pd.read_csv("../data/sample_silver.csv")

agg_df = df.groupby("channelTitle").size().reset_index(name="video_count")

agg_df.to_csv("../data/sample_gold.csv", index=False)
print("✅ Data aggregated and stored in Gold Layer")
