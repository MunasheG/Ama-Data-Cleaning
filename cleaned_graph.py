from data_cleaning_project import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Scatter plot
# df.plot.scatter(x='Age_At_Exit', y='Exit_Year')
# plt.xlabel('Age of Cadet')
# plt.title('Age of Cadet Graduation')
# plt.show()

# Line plot
df.groupby('Exit_Year')['Age_At_Exit'].mean().plot()
plt.ylabel('Average Age')
plt.title('Average Age at Exit Over Time')

grouped = df.groupby('Exit_Year')['Age_At_Exit'].mean()
grouped.plot()

# line of best fit
z = np.polyfit(grouped.index, grouped.values, 1)
p = np.poly1d(z)
plt.plot(grouped.index, p(grouped.index), 'r--', label='Best Fit')
plt.legend()
plt.ylabel('Average Age')
plt.title('Average Age at Exit Over Time')
plt.show()