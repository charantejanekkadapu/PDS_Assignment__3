import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
diabetes_data = pd.read_csv('diabetes.csv')
# Set a seed for reproducibility
np.random.seed(35)

# Take a random sample of 25 observations
sample_data = diabetes_data.sample(n=25)

# Calculate mean and highest Glucose values for the sample
sample_mean_glucose = sample_data['Glucose'].mean()
sample_highest_glucose = sample_data['Glucose'].max()

# Calculate mean and highest Glucose values for the population
population_mean_glucose = diabetes_data['Glucose'].mean()
population_highest_glucose = diabetes_data['Glucose'].max()

# Create a bar chart for comparison
labels = ['Population Mean', 'Population Highest', 'Sample Mean', 'Sample Highest']
values = [population_mean_glucose, population_highest_glucose, sample_mean_glucose, sample_highest_glucose]

plt.bar(labels, values, color=['green', 'green', 'red', 'red'])
plt.ylabel('Glucose Values')
plt.title('Comparison of Glucose Statistics: Population vs Sample')
plt.show()