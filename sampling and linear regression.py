# write a code to read an excel file and plot a scatter plot with a regression line
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Read the excel file
df = pd.read_excel('Other Macroeconomic Timeseries Data.xlsx', sheet_name='Daily')

# Display the first few rows of the dataframe
print(df.head())

# Display the columns of the dataframe
print(df.columns)

# Select the columns for the scatter plot as 'NSE S&P CNX NIFTY' & 'BSE BANKEX'
x = df['NSE S&P CNX NIFTY']
y = df['BSE BANKEX']

# Drop NaN values and string values from the columns
x = x.dropna()
y = y.dropna()
x = x[x.apply(lambda x: isinstance(x, (int, float)))]
y = y[y.apply(lambda y: isinstance(y, (int, float)))]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5)
plt.title('Scatter Plot of NSE S&P CNX NIFTY vs BSE BANKEX')
plt.xlabel('NSE S&P CNX NIFTY')
plt.ylabel('BSE BANKEX')
plt.grid(True)
plt.show()
