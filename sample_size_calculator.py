import scipy.stats as stats

population_size = 127
confidence_level = 0.90
margin_of_error = 0.05
target_population = 0.5

z = stats.norm.ppf(1 - (1 - confidence_level) / 2)

n_0 = z**2 * target_population * (1 - target_population) / margin_of_error**2

sample = n_0 / (1 + (n_0 - 1) / population_size)

print(round(sample))
