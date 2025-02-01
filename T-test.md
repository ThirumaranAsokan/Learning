# T-test

### 1. One-Sample t-test  
*When to Use*: Compare a sample mean to a known population mean.  
*Formula*:  
\[
t = \frac{\bar{X} - \mu}{s / \sqrt{n}}
\]  
- \(\bar{X}\): Sample mean  
- \(\mu\): Population mean  
- \(s\): Sample standard deviation  
- \(n\): Sample size  

*Example Problem*:  
A factory claims its lightbulbs last 1,200 hours. You test 25 bulbs and find a mean lifespan of 1,150 hours with a standard deviation of 100 hours. Is the factory’s claim valid?  

*Solution*:  
\[
t = \frac{1150 - 1200}{100 / \sqrt{25}} = \frac{-50}{20} = -2.5  
\]  
Degrees of freedom (\(df\)) = \(n - 1 = 24\).  
Critical t-value (α=0.05, two-tailed) ≈ ±2.064.  
*Conclusion*: Reject \(H_0\) (factory’s claim is invalid).  

---

### *2. Independent Samples t-test*  
*When to Use*: Compare two unrelated groups.  
*Formula*:  
\[
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
\]  
*Degrees of Freedom*:  
\[
df = n_1 + n_2 - 2
\]  

*Example Problem*:  
Group A (\(n=30\), \(\bar{X}=85\), \(s=5\)) vs. Group B (\(n=30\), \(\bar{X}=80\), \(s=6\)). Is there a significant difference?  

*Solution*:  
\[
t = \frac{85 - 80}{\sqrt{\frac{5^2}{30} + \frac{6^2}{30}}} = \frac{5}{\sqrt{0.83 + 1.2}} = \frac{5}{1.42} ≈ 3.52  
\]  
\(df = 30 + 30 - 2 = 58\).  
Critical t-value (α=0.05, two-tailed) ≈ ±2.00.  
*Conclusion*: Reject \(H_0\) (groups differ significantly).  

---

### *3. Paired t-test*  
*When to Use*: Compare the same group under two conditions (e.g., pre-test vs. post-test).  
*Formula*:  
\[
t = \frac{\bar{D}}{s_D / \sqrt{n}}
\]  
- \(\bar{D}\): Mean of differences  
- \(s_D\): Standard deviation of differences  

*Example Problem*:  
10 patients’ blood pressure before (\([120, 125, 130, 115, 140]\)) and after (\([110, 120, 125, 110, 135]\)) medication. Did the medication work?  

*Solution*:  
| Patient | Before | After | Difference (\(D\)) |  
|---------|--------|-------|-------------------|  
| 1       | 120    | 110   | 10                |  
| 2       | 125    | 120   | 5                 |  
| 3       | 130    | 125   | 5                 |  
| 4       | 115    | 110   | 5                 |  
| 5       | 140    | 135   | 5                 |  

\[
\bar{D} = \frac{10 + 5 + 5 + 5 + 5}{5} = 6,\quad s_D = 2.24
\]  
\[
t = \frac{6}{2.24 / \sqrt{5}} = \frac{6}{1.0} = 6.0
\]  
\(df = n - 1 = 4\).  
Critical t-value (α=0.05, two-tailed) ≈ ±2.776.  
*Conclusion*: Reject \(H_0\) (medication is effective).  

---

### *Key Assumptions*  
1. *Normality*: Data is normally distributed (use Shapiro-Wilk test).  
2. *Homogeneity of Variance: For independent t-test, use **Levene’s test*.  
3. *Independence*: Observations are not related (except paired tests).  

---

### *Effect Size*  
- *Cohen’s \(d\)*:  
\[
d = \frac{\text{Mean Difference}}{\text{Pooled Standard Deviation}}
\]  
- Interpret:  
  - \(d = 0.2\): Small  
  - \(d = 0.5\): Medium  
  - \(d = 0.8\): Large  

---

### Common Mistakes  
1. Using a t-test for >2 groups (use ANOVA instead).  
2. Ignoring non-normal data (use Mann-Whitney U test).  
3. Confusing paired vs. independent tests.  

---

### *Practice Problems*  
1. *One-Sample*: A sample of 50 students has an average IQ of 105 (population μ=100, σ=15). Test if they’re smarter.  
2. *Independent*: Compare salaries of men (\(\bar{X}=50k, s=10k, n=40\)) vs. women (\(\bar{X}=45k, s=8k, n=40\)).  
3. *Paired*: Test if a training program improves productivity (pre-test: [10, 12, 8], post-test: [15, 14, 12]).  

---

### *Need More?*  
- *Formulas*: [Stat Trek](https://stattrek.com/) or [Khan Academy](https://www.khanacademy.org/math/statistics-probability).  
- *Practice Datasets*: Use free tools like [JASP](https://jasp-stats.org/) or [R](https://www.r-project.org/).
