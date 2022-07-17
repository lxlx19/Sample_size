
sample_size <- function(n_pop, cl, e, p) {
    # Z-score of the sample size
    z <- qnorm(1 - (1 - cl) / 2)
    # Cochran's Formula for sample size
    n_0 <- z^2 * p * (1 - p) / e^2

    n <- n_0 / (1 + (n_0 - 1) / n_pop)
    return(ceiling(n))
}

print(sample_size(127, 0.95, 0.05, 0.5))
