# End-to-End Sales Analytics Project

## Workflow
1. **Excel:** Initial data inspection, profit margin & month fields, and Pivot Table check (`sales_excel_clean.xlsx`).
2. **SQL (SQLite):** Loaded data into `sql/sales.db` and ran category & loss-making order queries (`sql/run_sql.py`).
3. **Python:** Calculated `Profit_Margin_Pct` and `Avg_Price_Per_Unit`, exported `data/sales_cleaned.csv`, and generated a category profit chart (`python/analyze.py`).
4. **Power BI:** Built an interactive dashboard with KPI cards and category profit visuals (`dashboard/sales_dashboard.pbix`).

## Key Findings
- **Electronics** leads in both sales and profit.
- **Furniture** shows negative profit (loss-making orders), pointing to pricing or discounting issues.
