import pandas as pd
import matplotlib.pyplot as plt

westbound_data_file = 'M4_WB_15Min_Report_1_3678_01_10_2023_01_10_2024.csv'
eastbound_data_file = 'M4_EB_15Min_Report_1_6209_01_10_2023_01_10_2024.csv'

westbound_data = pd.read_csv(westbound_data_file)
eastbound_data = pd.read_csv(eastbound_data_file)

time_interval_mean_wb = westbound_data.drop(columns=["Report Date", "Total"]).mean()
time_interval_mean_eb = eastbound_data.drop(columns=["Report Date", "Total"]).mean()

net_traffic_flow = time_interval_mean_eb.values - time_interval_mean_wb.values
total_flow = net_traffic_flow.sum()

plt.figure(figsize=(12, 6))
plt.plot(time_interval_mean_wb.index, time_interval_mean_wb.values, marker="o", color="blue", label="Leaving London")
plt.plot(time_interval_mean_eb.index, time_interval_mean_eb.values, marker="o", color="orange", label="Entering London")
#plt.plot(net_traffic_flow.index, net_traffic_flow.values, marker="o", color="red", label="Net inflow (+) or outflow (-)")
plt.xticks(rotation=45, fontsize=8)
plt.title("Average Traffic Flow by Time Interval (October 2023 - October 2024)")
plt.xlabel("Time Interval")
plt.ylabel("Average Traffic Flow")
plt.legend(loc="upper right")
plt.grid()
plt.tight_layout()
plt.show()

