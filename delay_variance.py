import pandas as pd

# Load the dataset
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin-1')
df.columns = df.columns.str.strip()

# Calculate the actual delay variance for late shipments
df['Delay_Gap'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
late_shipments = df[df['Late_delivery_risk'] == 1]

print("=== GLOBAL FULFILLMENT DELAY VARIANCE ===")
print(f"Average days late per delayed order: {late_shipments['Delay_Gap'].mean():.2f} days")
print("\nDistribution of late delivery delays (in days):")
print(late_shipments['Delay_Gap'].value_counts().sort_index())