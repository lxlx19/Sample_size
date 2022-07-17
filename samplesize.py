from math import ceil
import scipy.stats as stats


class SampleSizeCalculator:
    """_summary_

    Args:
        N (int): population size
        cl (float): confidence level
        e (float): margin of error
    """

    def __init__(self, N, cl, e):
        self.N = N
        self.cl = cl
        self.e = e
        self.p = 0.5 # Target population mean

    def calculate(self):
        """_summary_

        Returns:
            int: sample size
        """
        # calculate the z-score (the difference between the target population and the mean)
        z = stats.norm.ppf(1 - (1 - self.cl) / 2)

        # Cochran's formula for the sample size
        n_0 = z**2 * self.p * (1 - self.p) / self.e**2

        n = n_0 / (1 + (n_0 - 1) / self.N)

        return ceil(n)

    def m_error(self, s):
        """_summary_
            s (int): sample size
        Returns:
            float: margin of error
        """

        # calculate the z-score (the difference between the target population and the mean)
        z = stats.norm.ppf(1 - (1 - self.cl) / 2)

        e = z * 0.5 / (((self.N - 1) * s) / (self.N - s)) ** 0.5

        return round(e, 4)

sample = SampleSizeCalculator(10000, 0.95, 0.05)

print(sample.calculate())
print(sample.m_error(400))
