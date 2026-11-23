import sqlite3
import pandas as pd

# 1. CSV data load karo
df = pd.read_csv("data/sales_raw.csv")

# 2. SQLite database banao/connect karo aur table daalo
conn = sqlite3.connect("sql/sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# 3. Query 1: Category wise Total Sales aur Total Profit
query_1 = """
SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;
"""

print("--- Category Performance ---")
print(pd.read_sql_query(query_1, conn))

# 4. Query 2: Kaunse orders loss mein gaye (Profit < 0)
query_2 = """
SELECT
    Order_ID,
    Region,
    Category,
    Sub_Category,
    Sales,
    Profit
FROM sales
WHERE Profit < 0;
"""

print("\n--- Loss Making Orders ---")
print(pd.read_sql_query(query_2, conn))

# 5. Connection band karo
conn.close()