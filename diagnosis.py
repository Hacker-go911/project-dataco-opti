import pandas as pd
import numpy as np
# (Assuming the main transaction file matches the schema provided in your data dictionary)
df = pd.read_csv('DataCoSupplyChainDataset.csv')

print("=== PILLAR 1: REGIONAL LOGISTICS DIAGNOSTIC ===")
# Aggregate logistics performance by market region
market_diagnostic = df.groupby('Market').agg(
    Total_Orders=('Sales', 'count'),
    Late_Deliveries=('Late_delivery_risk', 'sum'),
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Benefit per order', 'sum')
).reset_index()

# Calculate key business metrics
market_diagnostic['Late_Delivery_Rate (%)'] = (market_diagnostic['Late_Deliveries'] / market_diagnostic['Total_Orders']) * 100
market_diagnostic['Net_Profit_Margin (%)'] = (market_diagnostic['Total_Profit'] / market_diagnostic['Total_Sales']) * 100

print(market_diagnostic.sort_values(by='Late_Delivery_Rate (%)', ascending=False).to_string(index=False))


print("\n=== PILLAR 2: COMMERCIAL PRICING & SEGMENT DIAGNOSTIC ===")
# Aggregate commercial performance by product category
category_diagnostic = df.groupby('Category Name').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Discounts_Given=('Order Item Discount', 'sum'),
    Total_Profit=('Benefit per order', 'sum')
).reset_index()

# Calculate margin erosion metrics
category_diagnostic['Avg_Discount_Rate (%)'] = (category_diagnostic['Total_Discounts_Given'] / category_diagnostic['Total_Sales']) * 100
category_diagnostic['Net_Profit_Margin (%)'] = (category_diagnostic['Total_Profit'] / category_diagnostic['Total_Sales']) * 100

print(category_diagnostic.sort_values(by='Net_Profit_Margin (%)', ascending=True).to_string(index=False))