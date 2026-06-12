import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("process_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

limits = {
    "temperature_C": (340, 360),
    "pressure_Torr": (1.7, 2.3),
    "gas_flow_sccm": (45, 55)
}

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

for ax, (col, (low, high)) in zip(axes, limits.items()):
    ax.plot(df["timestamp"], df[col], label=col, color="blue")
    ax.axhline(low, color="red", linestyle="--", label="Lower Limit")
    ax.axhline(high, color="red", linestyle="--", label="Upper Limit")
    
    anomalies = df[(df[col] < low) | (df[col] > high)]
    ax.scatter(anomalies["timestamp"], anomalies[col], color="red", zorder=5, label="Anomaly")
    
    ax.set_title(col)
    ax.legend(loc="upper right", fontsize=8)
    ax.set_ylabel(col)

plt.xlabel("Time")
plt.tight_layout()
plt.savefig("process_dashboard.png", dpi=150)
plt.show()

print("Dashboard saved as process_dashboard.png")