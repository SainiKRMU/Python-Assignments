#Capstone Project Assignment: Campus Energy-Use Dashboard
#------------------------------------------------------------------------------------------------------

# Course            : Programming for Problem Solving using Python
# Assignment Title  : End-to-End Energy Consumption Analysis and Visualization
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A
#____________________________________________________________________________________________________



#-------------------Importing-----------------------

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import os

# -------------------- Classes --------------------
class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.readings)

    def generate_report(self):
        values = [r.kwh for r in self.readings]
        return {
            "total": sum(values),
            "mean": np.mean(values),
            "min": np.min(values),
            "max": np.max(values)
        }

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def load_from_dataframe(self, df):
        for _, row in df.iterrows():
            name = row['building']
            if name not in self.buildings:
                self.buildings[name] = Building(name)
            reading = MeterReading(row['timestamp'], row['kwh'])
            self.buildings[name].add_reading(reading)

    def generate_building_summary(self):
        summary = {}
        for name, building in self.buildings.items():
            summary[name] = building.generate_report()
        return summary

# -------------------- Functions --------------------
def ingest_data(folder_path='data'):
    folder = Path(folder_path)
    all_files = list(folder.glob('*.csv'))
    df_list = []

    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines='skip')
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['building'] = file.stem
            df_list.append(df)
        except FileNotFoundError:
            print(f"File {file} not found, skipping.")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if df_list:
        return pd.concat(df_list, ignore_index=True)
    else:
        return pd.DataFrame(columns=['timestamp', 'kwh', 'building'])

def calculate_daily_totals(df):
    return df.groupby(['building', pd.Grouper(key='timestamp', freq='D')])['kwh'].sum().reset_index()

def calculate_weekly_aggregates(df):
    return df.groupby(['building', pd.Grouper(key='timestamp', freq='W')])['kwh'].mean().reset_index()

def plot_dashboard(daily_df, weekly_df, output_path='output/dashboard.png'):
    buildings = daily_df['building'].unique()
    fig, axs = plt.subplots(3, 1, figsize=(12, 15))

    # Line Chart - daily consumption
    for b in buildings:
        subset = daily_df[daily_df['building'] == b]
        axs[0].plot(subset['timestamp'], subset['kwh'], label=b)
    axs[0].set_title('Daily Energy Consumption per Building')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('kWh')
    axs[0].legend()
    
    # Bar Chart - weekly average
    for b in buildings:
        subset = weekly_df[weekly_df['building'] == b]
        axs[1].bar(subset['timestamp'], subset['kwh'], label=b, alpha=0.7)
    axs[1].set_title('Weekly Average Energy Usage per Building')
    axs[1].set_xlabel('Week')
    axs[1].set_ylabel('Average kWh')
    axs[1].legend()

    # Scatter Plot - daily peaks
    for b in buildings:
        subset = daily_df[daily_df['building'] == b]
        axs[2].scatter(subset['timestamp'], subset['kwh'], label=b)
    axs[2].set_title('Daily Peak Energy Usage')
    axs[2].set_xlabel('Date')
    axs[2].set_ylabel('kWh')
    axs[2].legend()

    plt.tight_layout()
    Path('output').mkdir(exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def export_summary(building_summary, df_combined):
    Path('output').mkdir(exist_ok=True)
    # Export cleaned data
    df_combined.to_csv('output/cleaned_energy_data.csv', index=False)
    # Export building summary
    summary_df = pd.DataFrame.from_dict(building_summary, orient='index')
    summary_df.to_csv('output/building_summary.csv')
    # Export textual summary
    total_consumption = df_combined['kwh'].sum()
    highest_building = summary_df['total'].idxmax()
    peak_value = df_combined['kwh'].max()
    with open('output/summary.txt', 'w') as f:
        f.write(f"Total Campus Energy Consumption: {total_consumption:.2f} kWh\n")
        f.write(f"Highest Consuming Building: {highest_building}\n")
        f.write(f"Peak Load Value: {peak_value:.2f} kWh\n")

# -------------------- Main Program --------------------
def main():
    df_combined = ingest_data()
    if df_combined.empty:
        print("No data available.")
        return

    building_manager = BuildingManager()
    building_manager.load_from_dataframe(df_combined)
    building_summary = building_manager.generate_building_summary()

    daily_df = calculate_daily_totals(df_combined)
    weekly_df = calculate_weekly_aggregates(df_combined)

    plot_dashboard(daily_df, weekly_df)
    export_summary(building_summary, df_combined)
    print("All outputs generated in the 'output/' folder.")

if __name__ == '__main__':
    main()
