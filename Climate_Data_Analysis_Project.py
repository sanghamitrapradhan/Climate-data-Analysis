# Climate Analysis Project
# Data sourced from web
# Import libraries for Extraction and analysis
#import requests
#from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
 
# This is to read the CSV file into a DataFrame
df = pd.read_csv('Global_Tempeartures.csv')

# This is to display basic information about the dataset
print(df.info())
print(df.head())

# datatype conversion
df['Date'] = pd.to_datetime(df['Date'])

# Date range of interest from 2000 to 2015
df = df[(df['Date'] >= '2000-01-01') & (df['Date'] <= '2015-12-31')]

# Handle missing values (approximation)
df.fillna(df.mean(), inplace=True)

#Compute annual averages
df_yearly = df.resample('Y', on='Date').mean()

# Create a line plot for Yearly Average Land Temperature
plt.figure(figsize=(12, 6))
plt.plot(df_yearly.index, df_yearly['LandAverageTemperature'], '-', label='Yearly Average Temperature', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Yearly Average Land Temperature (2000-2015)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# data quality checks
correlation = df['LandAverageTemperature'].corr(df['LandMaxTemperature'])
print(f"Correlation between Land Average Temperature and Land Max Temperature: {correlation: .2f}")

