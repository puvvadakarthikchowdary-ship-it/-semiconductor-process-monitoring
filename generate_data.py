import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

# 200 readings, ప్రతి 1 minute కి ఒకటి
n = 200
timestamps = [datetime.now() + timedelta(minutes=i) for i in range(n)]

# Normal operating values (example: PECVD/Furnace process)
temperature = np.random.normal(loc=350, scale=5, size=n)   # target ~350°C
pressure = np.random.normal(loc=2.0, scale=0.1, size=n)    # target ~2.0 Torr
gas_flow = np.random.normal(loc=50, scale=2, size=n)       # target ~50 sccm

# కొన్ని anomalies (equipment fault) inject చేయడం
temperature[50:55] += 25   # sudden spike
pressure[120:125] -= 0.8   # sudden drop
gas_flow[170:175] += 15    # flow surge

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_C": temperature,
    "pressure_Torr": pressure,
    "gas_flow_sccm": gas_flow
})

df.to_csv("process_data.csv", index=False)
print("Data generated successfully!")
print(df.head())