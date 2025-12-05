#Mini Project Assignment: Weather Data Visualizer#------------------------------------------------------------------------------------------------------

# Course            : Programming for Problem Solving using Python
# Assignment Title  : Data Analysis and Visualization with Real-World Weather Data
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
#____________________________________________________________________________________________________


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------
# Ensure folders exist
# ---------------------------------------------------
os.makedirs("cleaned_data", exist_ok=True)
os.makedirs("plots", exist_ok=True)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
df = pd.read_csv("data/weather.csv")

# ---------------------------------------------------
# Cleaning Data
# ---------------------------------------------------
df["date"] = pd.to_datetime(df["date"])
df = df.dropna()
df = df.sort_values("date")

df.to_csv("cleaned_data/weather_cleaned.csv", index=False)

# ---------------------------------------------------
# Statistical Analysis
# ---------------------------------------------------
daily_mean_temp = df["temperature"].mean()
monthly_rainfall = df.groupby(df["date"].dt.month)["rainfall"].sum()
humidity_temp_corr = df["humidity"].corr(df["temperature"])

monthly_stats = df.groupby(df["date"].dt.month).agg({
    "temperature": ["mean", "min", "max"],
    "rainfall": "sum",
    "humidity": "mean"
})
monthly_stats.to_csv("cleaned_data/monthly_summary.csv")

# ---------------------------------------------------
# Plot 1: Daily Temperature Trend
# ---------------------------------------------------
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["temperature"], marker="o")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trend")
plt.grid(True)
plt.savefig("plots/daily_temperature.png")
plt.close()

# ---------------------------------------------------
# Plot 2: Monthly Rainfall Bar Chart
# ---------------------------------------------------
plt.figure(figsize=(8,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values, color="skyblue")
plt.xlabel("Month")
plt.ylabel("Total Rainfall (mm)")
plt.title("Monthly Rainfall Totals")
plt.savefig("plots/monthly_rainfall.png")
plt.close()

# ---------------------------------------------------
# Plot 3: Humidity vs Temperature Scatter Plot
# ---------------------------------------------------
plt.figure(figsize=(8,5))
plt.scatter(df["temperature"], df["humidity"], color="red")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Humidity vs Temperature")
plt.grid(True)
plt.savefig("plots/humidity_vs_temperature.png")
plt.close()

# ---------------------------------------------------
# Combined Plot Figure
# ---------------------------------------------------
fig, axes = plt.subplots(3, 1, figsize=(9, 15))

# Line chart
axes[0].plot(df["date"], df["temperature"], marker="o")
axes[0].set_title("Daily Temperature Trend")
axes[0].set_ylabel("Temperature (°C)")

# Bar chart
axes[1].bar(monthly_rainfall.index, monthly_rainfall.values)
axes[1].set_title("Monthly Rainfall Totals")
axes[1].set_ylabel("Rainfall (mm)")

# Scatter plot
axes[2].scatter(df["temperature"], df["humidity"], color="green")
axes[2].set_title("Humidity vs Temperature")
axes[2].set_xlabel("Temperature (°C)")
axes[2].set_ylabel("Humidity (%)")

plt.tight_layout()
plt.savefig("plots/combined_plot.png")
plt.close()

# ---------------------------------------------------
# Generate Summary Report
# ---------------------------------------------------
summary = f"""
WEATHER DATA ANALYSIS SUMMARY

1. Daily Mean Temperature: {daily_mean_temp:.2f} °C

2. Monthly Rainfall Totals:
{monthly_rainfall.to_string()}

3. Correlation Between Humidity and Temperature:
{humidity_temp_corr:.3f}

4. Monthly Statistical Summary Saved To:
cleaned_data/monthly_summary.csv

5. Generated Plots:
- daily_temperature.png
- monthly_rainfall.png
- humidity_vs_temperature.png
- combined_plot.png
"""

with open("report.txt", "w") as f:
    f.write(summary)

print("Analysis complete! Check the 'cleaned_data', 'plots', and 'report.txt' files.")
