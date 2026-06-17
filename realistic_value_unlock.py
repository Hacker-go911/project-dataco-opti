import pandas as pd

# Load the dataset
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin-1')
df.columns = df.columns.str.strip()

print("====================================================")
print("     BCG X ENGINE: PHASED MARGIN TURNAROUND          ")
print("====================================================\n")

# --- 1. CORE COMMERCIAL RECOVERY (From previous step) ---
core_categories = ['Cardio Equipment', 'Camping & Hiking', 'Water Sports']
comm_df = df[df['Category Name'].isin(core_categories)]

total_core_sales = comm_df['Sales'].sum()
total_core_discount = comm_df['Order Item Discount'].sum()
total_core_profit = comm_df['Benefit per order'].sum()

target_discount_rate = 0.07 #Shift discount rate from ~10.1% to a highly disciplined 7%
reclaimed_discount = total_core_discount - (total_core_sales * target_discount_rate)
#Adjust for a 5% conservative volume drop-off due to lower discounting (Elasticity)
volume_risk_loss = total_core_profit * 0.05
net_commercial_value = reclaimed_discount - volume_risk_loss


# --- 2. PRAGMATIC LOGISTICS RECOVERY (Based on actual Delay Gap) ---
df['Delay_Gap'] = df['Days for shipping (real)'] - df['Days for shipment (scheduled)']

# Counts based on your terminal run
late_1_day = len(df[df['Delay_Gap'] == 1])
late_multi_day = len(df[df['Delay_Gap'] > 1])

# Assume a conservative $10 cost penalty per on-paper failure
penalty_cost = 10.00

# Phase 1: Wipe out 100% of 1-day delays by recalibrating checkout expectations
phase_1_savings = late_1_day * penalty_cost

# Phase 2: Reduce multi-day delays by a realistic 25% via tightening carrier SLAs
phase_2_savings = (late_multi_day * 0.25) * penalty_cost

total_logistics_value = phase_1_savings + phase_2_savings

print(f"--- LOGISTICS RE-ALIGNMENT ROADMAP ---")
print(f"Phase 1 Savings (Eliminating {late_1_day:,} 1-day on-paper failures):  ${phase_1_savings:,.2f}")
print(f"Phase 2 Savings (25% reduction in multi-day operational delays): ${phase_2_savings:,.2f}")
print(f"Total Pragmatic Logistics Capital Reclaimed:                    ${total_logistics_value:,.2f}\n")


# --- 3. THE REALISTIC C-SUITE SCORECARD ---
total_strategic_value = net_commercial_value + total_logistics_value
company_baseline_profit = df['Benefit per order'].sum()
optimized_profit = company_baseline_profit + total_strategic_value
margin_expansion_bps = (total_strategic_value / df['Sales'].sum()) * 10000

print(f"====================================================")
print(f"             FINAL EXECUTIVE SCORECARD              ")
print(f"====================================================")
print(f"Realistic Annualized Capital Unlocked:  ${total_strategic_value:,.2f}")
print(f"Baseline Corporate Net Profit:          ${company_baseline_profit:,.2f}")
print(f"Target Corporate Net Profit:            ${optimized_profit:,.2f}")
print(f"Feasible Bottom-Line Margin Expansion:  +{margin_expansion_bps:.1f} bps")
print("====================================================")