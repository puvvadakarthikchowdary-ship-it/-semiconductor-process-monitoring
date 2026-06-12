import pandas as pd

df = pd.read_csv("process_data.csv")

# Process control limits (acceptable range)
limits = {
    "temperature_C": (340, 360),
    "pressure_Torr": (1.7, 2.3),
    "gas_flow_sccm": (45, 55)
}

alerts = []

for col, (low, high) in limits.items():
    out_of_range = df[(df[col] < low) | (df[col] > high)]
    for idx, row in out_of_range.iterrows():
        alerts.append({
            "timestamp": row["timestamp"],
            "parameter": col,
            "value": round(row[col], 2),
            "status": "ANOMALY"
        })

alerts_df = pd.DataFrame(alerts)
alerts_df.to_csv("alerts_log.csv", index=False)

print(f"Total readings checked: {len(df)}")
print(f"Anomalies detected: {len(alerts_df)}")
print(alerts_df)