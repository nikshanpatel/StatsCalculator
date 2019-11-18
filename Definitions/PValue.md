**P Value:**

P-value. The P-value is the probability of observing a sample statistic as extreme as the test statistic.
Test statistic. The test statistic is a z-score (z) defined by the following equation.
z = (p - P) / σ

where P is the hypothesized value of population proportion in the null hypothesis, p is the sample proportion, and σ is the standard deviation of the sampling distribution.
Standard deviation (σ) of the sampling distribution can be calculated by the following formula:
σ = sqrt[ P * ( 1 - P ) / n ]

where P is the hypothesized value of population proportion in the null hypothesis, and n is the sample size.
If the sample findings are unlikely, given the null hypothesis, the researcher rejects the null hypothesis. Typically, this involves comparing the P-value to the significance level, and rejecting the null hypothesis when the P-value is less than the significance level.

Example:
The CEO of a large electric utility claims that 80 percent of his 1,000,000 customers are very satisfied with the service they receive. To test this claim, the local newspaper surveyed 100 customers, using simple random sampling. Among the sampled customers, 73 percent say they are very satisified. Based on these findings, can we reject the CEO's hypothesis that 80% of the customers are very satisfied? Use a 0.05 level of significance.
Solution: The solution to this problem takes four steps: (1) state the hypotheses, (2) formulate an analysis plan, (3) analyze sample data, and (4) interpret results. We work through those steps below:
	State the hypotheses. The first step is to state the null hypothesis and an alternative hypothesis.
Null hypothesis: P = 0.80

Alternative hypothesis: P ≠ 0.80

Note that these hypotheses constitute a two-tailed test. The null hypothesis will be rejected if the sample proportion is too big or if it is too small.
	Formulate an analysis plan. For this analysis, the significance level is 0.05. The test method, shown in the next section, is a one-sample z-test.
	Analyze sample data. Using sample data, we calculate the standard deviation (σ) and compute the z-score test statistic (z).
σ = sqrt[ P * ( 1 - P ) / n ]

σ = sqrt [(0.8 * 0.2) / 100]

σ = sqrt(0.0016) = 0.04

z = (p - P) / σ = (.73 - .80)/0.04 = -1.75

where P is the hypothesized value of population proportion in the null hypothesis, p is the sample proportion, and n is the sample size.
Since we have a two-tailed test, the P-value is the probability that the z-score is less than -1.75 or greater than 1.75.
We use the Normal Distribution Calculator to find P(z < -1.75) = 0.04, and P(z > 1.75) = 0.04. Thus, the P-value = 0.04 + 0.04 = 0.08.
	Interpret results. Since the P-value (0.08) is greater than the significance level (0.05), we cannot reject the null hypothesis.
Problem 2: One-Tailed Test

Suppose the previous example is stated a little bit differently. Suppose the CEO claims that at least 80 percent of the company's 1,000,000 customers are very satisfied. Again, 100 customers are surveyed using simple random sampling. The result: 73 percent are very satisfied. Based on these results, should we accept or reject the CEO's hypothesis? Assume a significance level of 0.05.
Solution: The solution to this problem takes four steps: (1) state the hypotheses, (2) formulate an analysis plan, (3) analyze sample data, and (4) interpret results. We work through those steps below:
	State the hypotheses. The first step is to state the null hypothesis and an alternative hypothesis.
Null hypothesis: P >= 0.80

Alternative hypothesis: P < 0.80

Note that these hypotheses constitute a one-tailed test. The null hypothesis will be rejected only if the sample proportion is too small.
	Formulate an analysis plan. For this analysis, the significance level is 0.05. The test method, shown in the next section, is a one-sample z-test.
	Analyze sample data. Using sample data, we calculate the standard deviation (σ) and compute the z-score test statistic (z).

σ = sqrt[ P * ( 1 - P ) / n ] = sqrt [(0.8 * 0.2) / 100]

σ = sqrt(0.0016) = 0.04

z = (p - P) / σ = (.73 - .80)/0.04 = -1.75

where P is the hypothesized value of population proportion in the null hypothesis, p is the sample proportion, and n is the sample size.
Since we have a one-tailed test, the P-value is the probability that the z-score is less than -1.75. We use the Normal Distribution Calculator to find P(z < -1.75) = 0.04. Thus, the P-value = 0.04.

	Interpret results. Since the P-value (0.04) is less than the significance level (0.05), we cannot accept the null hypothesis.
