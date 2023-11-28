# Number of bootstrap samples and sample size
num_bootstrap_samples = 500
sample_size = 150

# Function to calculate mean, standard deviation, and percentile for BloodPressure
def calculate_statistics(data):
    mean_bp = np.mean(data['BloodPressure'])
    std_bp = np.std(data['BloodPressure'])
    percentile_95_bp = np.percentile(data['BloodPressure'], 95)
    return mean_bp, std_bp, percentile_95_bp

# Initialize arrays to store bootstrap statistics
bootstrap_means = np.zeros(num_bootstrap_samples)
bootstrap_stds = np.zeros(num_bootstrap_samples)
bootstrap_percentiles = np.zeros(num_bootstrap_samples)

# Perform bootstrap sampling
for i in range(num_bootstrap_samples):
    bootstrap_sample = diabetes_data.sample(n=sample_size, replace=True)
    mean_bp, std_bp, percentile_95_bp = calculate_statistics(bootstrap_sample)
    bootstrap_means[i] = mean_bp
    bootstrap_stds[i] = std_bp
    bootstrap_percentiles[i] = percentile_95_bp

# Calculate population statistics for comparison
population_mean_bp, population_std_bp, population_percentile_95_bp = calculate_statistics(diabetes_data)

# Create charts for comparison
labels = ['Population Mean', 'Bootstrap Sample Mean', 'Population Std', 'Bootstrap Sample Std',
          'Population 95th Percentile', 'Bootstrap Sample 95th Percentile']

values = [population_mean_bp, np.mean(bootstrap_means), population_std_bp, np.mean(bootstrap_stds),
          population_percentile_95_bp, np.mean(bootstrap_percentiles)]

plt.bar(labels, values, color=['green', 'red', 'green', 'red', 'green', 'red'])
plt.ylabel('BloodPressure Values')
plt.title('Comparison of BloodPressure Statistics: Population vs Bootstrap Samples')
plt.xticks(rotation=45)
plt.show()
