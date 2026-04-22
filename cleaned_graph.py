from data_cleaning_project import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Scatter plot
df.plot.scatter(x='Age_At_Exit', y='Exit_Year')
plt.xlabel('Age of Cadet')
plt.title('Age of Cadet Graduation')
plt.show()

