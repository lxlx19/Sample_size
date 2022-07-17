import scipy.stats as stats

population_size = 127
confidence_level = 0.95
margin_of_error = 0.05
target_population = 0.5

# calculate the z-score (the difference between the target population and the mean)
z = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Cochran's formula for the sample size
n_0 = z**2 * target_population * (1 - target_population) / margin_of_error**2

sample = n_0 / (1 + (n_0 - 1) / population_size)

print(round(sample))
