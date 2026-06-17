import pandas as pd

# Load the big file
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin-1')
df.columns = df.columns.str.strip()

# 1. Isolate only the columns that affect profit
core_columns = [
    'Market', 'Category Name', 'Shipping Mode', 
    'Sales', 'Order Item Discount', 'Benefit per order', 'Late_delivery_risk'
]
df_clean = df[core_columns].copy()

# 2. Look at the high-level profit leak reality
total_sales = df_clean['Sales'].sum()
total_discount = df_clean['Order Item Discount'].sum()
total_profit = df_clean['Benefit per order'].sum()

print("=== DATACO ENTERPRISE PROFIT HEALTH CHECK ===")
print(f"Gross Revenue generated:        ${total_sales:,.2f}")
print(f"Total Revenue Given Away (Discounts): ${(total_discount):,.2f} ({ (total_discount/total_sales)*100:.1f}% of revenue)")
print(f"Net Profit Retained:            ${total_profit:,.2f}")
print(f"Overall Corporate Margin:       { (total_profit/total_sales)*100:.2f}%\n")

# 3. Quick check: How much does a late delivery hurt profit?
print("=== PERFORMANCE IMPACT OF LATE DELIVERIES ===")
late_vs_ontime = df_clean.groupby('Late_delivery_risk')['Benefit per order'].mean().reset_index()
print(late_vs_ontime.to_string(index=False))