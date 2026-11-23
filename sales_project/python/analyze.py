import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. SQLite database se pura data wapas load karo
conn = sqlite3.connect("sql/sales.db")
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

# 2. Naye columns banao: Profit Margin % aur Revenue per Quantity
df["Profit_Margin_Pct"] = (df["Profit"] / df["Sales"]) * 100
df["Avg_Price_Per_Unit"] = df["Sales"] / df["Quantity"]

print("--- Data with New Columns ---")
print(df[["Order_ID", "Category", "Sales", "Profit", "Profit_Margin_Pct"]])

# 3. Region-wise Sales aur Profit dekho
region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()
print("\n--- Region Wise Summary ---")
print(region_summary)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
output_path = BASE_DIR / "data" / "sales_cleaned.csv"

df.to_csv(output_path, index=False)
print("Saved at:", output_path)
# 5. Category-wise Profit ka simple Bar Chart banao
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(7, 4))
category_profit.plot(kind="bar")
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("python/category_profit.png")
plt.show()