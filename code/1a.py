import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
diabetes_data = pd.read_csv('diabetes.csv')
np.random.seed(35)

sample_data = diabetes_data.sample(n=25)
sample_mean_glucose = sample_data['Glucose'].mean()
sample_highest_glucose = sample_data['Glucose'].max()
population_mean_glucose = diabetes_data['Glucose'].mean()
population_highest_glucose = diabetes_data['Glucose'].max()

# Create a bar chart for comparison
labels = ['Population Mean', 'Population Highest', 'Sample Mean', 'Sample Highest']
values = [population_mean_glucose, population_highest_glucose, sample_mean_glucose, sample_highest_glucose]

plt.bar(labels, values, color=['green', 'green', 'red', 'red'])
plt.ylabel('Glucose Values')
plt.title('Comparison of Glucose Statistics: Population vs Sample')
plt.show()
