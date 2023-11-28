
sample_percentile_98_bmi = np.percentile(sample_data['BMI'], 98)
population_percentile_98_bmi = np.percentile(diabetes_data['BMI'], 98)

# Create a bar chart for comparison
labels = ['Population 98th Percentile BMI', 'Sample 98th Percentile BMI']
values = [population_percentile_98_bmi, sample_percentile_98_bmi]

plt.bar(labels, values, color=['red', 'green'])
plt.ylabel('BMI Values')
plt.title('Comparison of 98th Percentile BMI: Population vs Sample')
plt.show()
