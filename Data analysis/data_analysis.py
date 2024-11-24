import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

file_path = 'data.csv'
data = pd.read_csv(file_path)

print("Data Preview:")
print(data.head())

mean_values = data.mean()
median_values = data.median()
mode_values = data.mode().iloc[0]

print("\nMean Values:")
print(mean_values)
print("\nMedian Values:")
print(median_values)
print("\nMode Values:")
print(mode_values)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
mean_values.plot(kind='bar', title='Mean Values')
plt.xlabel('Columns')
plt.ylabel('Mean')

plt.subplot(1, 3, 2)
median_values.plot(kind='bar', title='Median Values', color='orange')
plt.xlabel('Columns')
plt.ylabel('Median')

plt.subplot(1, 3, 3)
mode_values.plot(kind='bar', title='Mode Values', color='green')
plt.xlabel('Columns')
plt.ylabel('Mode')

plt.tight_layout()
plt.show()