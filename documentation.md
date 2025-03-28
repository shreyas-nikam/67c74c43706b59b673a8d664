id: 67c74c43706b59b673a8d664_documentation
summary: Stress Testing - Algorithmic Approaches to Stress Testing
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Extreme Value Theory (EVT) Stress Tester Codelab

## Introduction to Extreme Value Theory for Financial Stress Testing
Duration: 00:05

Welcome to the QuLab Extreme Value Theory (EVT) Stress Tester codelab!

In today's financial world, understanding and managing extreme risks is more critical than ever. Traditional risk management methods often fall short when it comes to capturing the rare but impactful events that can significantly affect financial stability. This is where **Extreme Value Theory (EVT)** comes into play.

This application is designed to help you grasp the fundamental concepts of EVT and its practical application in financial stress testing. You will learn how EVT can be used to model extreme financial losses and gain hands-on experience with two key EVT methodologies: **Block Maxima (BM)** and **Peak-Over-Threshold (POT)**.

**Why is EVT important?**

*   **Captures Extreme Risks:** EVT is specifically tailored to model the tails of distributions, focusing on extreme events that traditional methods often overlook.
*   **Improves Risk Measurement:** By using EVT, we can obtain more accurate estimates of risk measures like Value at Risk (VaR) and Expected Shortfall (ES) during extreme market conditions.
*   **Enhances Stress Testing:** EVT provides a robust framework for stress testing, allowing financial institutions to better prepare for and mitigate the impact of severe market shocks.

**What you will learn:**

*   **Core Concepts of EVT:** Understand the theoretical foundations of Extreme Value Theory.
*   **Application of EVT in Finance:** Learn how to apply EVT to model extreme financial losses using synthetic data.
*   **Block Maxima (BM) Method:** Explore the Block Maxima approach and its implementation.
*   **Peak-Over-Threshold (POT) Method:** Discover the Peak-Over-Threshold approach and its advantages.
*   **Risk Measures (VaR & ES):** Calculate and interpret Value at Risk and Expected Shortfall using both BM and POT methods.

We will be using a synthetic dataset of daily returns throughout this codelab, allowing you to experiment with different parameters and observe how EVT models behave under various scenarios.

Let's dive in and start exploring the power of Extreme Value Theory!

## 1. Synthetic Data Generation
Duration: 00:03

First, we need to generate synthetic financial data to work with. This application uses a simple model to create daily returns, which will serve as our dataset for EVT analysis.

### 1.1. Data Parameters

On the left sidebar, you will find sliders to adjust the parameters for generating synthetic data.

*   **Number of Data Points:** This slider controls the size of the dataset. You can choose between 100 and 5000 data points. A larger dataset generally provides more robust results, especially for extreme value analysis. Try adjusting this slider to see how it affects the distribution and the subsequent EVT analysis.

*   **Volatility (Annualized):** This slider sets the annualized volatility of the synthetic returns, ranging from 1% to 50%. Volatility represents the degree of variation in returns. Higher volatility means more significant fluctuations and a higher chance of extreme values. Experiment with different volatility levels to observe its impact on extreme value modeling.

<aside class="positive">
: **Tip:** For initial exploration, start with a smaller dataset size (e.g., 1000) and moderate volatility (e.g., 20%). As you become more comfortable, you can increase these values to observe how EVT behaves with more data and higher risk.
</aside>

The application uses these parameters to generate synthetic daily returns based on a normal distribution.  While real-world financial returns may exhibit more complex characteristics, this simplified model is excellent for understanding the core concepts of EVT.

### 1.2. Sample Data and Distribution

Once you've set the data parameters, the application generates the synthetic returns and displays:

*   **Sample Data:** A table showing the first 10 rows of the generated daily returns. This gives you a glimpse of the actual numbers being generated.

*   **Distribution Histogram:** A histogram visualizing the distribution of the synthetic returns. This chart helps you understand the overall shape and spread of the generated data. Observe how the histogram changes as you adjust the volatility slider. Higher volatility should lead to a wider distribution.

```info
**Understanding the Data Generation:**

*   We are simulating daily returns using a normal distribution for simplicity.
*   **Volatility** is the key driver of the data's spread and the likelihood of extreme values. Higher volatility leads to more extreme returns.
*   Keep in mind that this is synthetic data for educational purposes. Real financial data can have different properties like skewness, kurtosis, and autocorrelation.
```

Take a moment to adjust the "Number of Data Points" and "Volatility (Annualized)" sliders and observe how the sample data and the histogram change. This will help you build intuition about the data generation process.

## 2. Extreme Value Theory Methods
Duration: 00:02

Now that we have our synthetic data, we can move on to applying Extreme Value Theory. The application offers two primary EVT methods for you to explore:

*   **Block Maxima (BM)**
*   **Peak-Over-Threshold (POT)**

You can select your preferred method using the radio buttons labeled "Choose EVT Method:" located below the "Synthetic Data Generation" section.

```info
**Choosing an EVT Method:**

*   **Block Maxima (BM):** This method focuses on the *maximum* extreme value within specific blocks of time (e.g., the maximum daily loss each year). It's useful for analyzing annual extremes and is based on the Generalized Extreme Value (GEV) distribution.

*   **Peak-Over-Threshold (POT):** This method considers *all* values that exceed a high threshold. It's more data-efficient than Block Maxima as it utilizes more extreme observations and is based on the Generalized Pareto Distribution (GPD).

Select either "Block Maxima (BM)" or "Peak-Over-Threshold (POT)" to proceed with the corresponding EVT analysis. The subsequent steps will guide you through each method in detail.
```

Choose **Block Maxima (BM)** to start with and let's delve into this method.

## 2.1. Block Maxima (BM) Analysis
Duration: 00:10

If you've selected "Block Maxima (BM)", you're now in the Block Maxima analysis section.

```markdown
**Block Maxima (BM) Approach:**

The Block Maxima (BM) method is based on dividing your dataset into non-overlapping blocks of equal size (e.g., years, months, or weeks). For each block, you identify the maximum value (or minimum return in our case, representing the maximum loss).  The **Fisher-Tippett-Gnedenko theorem** tells us that under certain conditions, the distribution of these block maxima will converge to a **Generalized Extreme Value (GEV) distribution**.

The GEV distribution is defined by three parameters:

*   **Shape parameter (ξ - xi):**  This parameter dictates the tail behavior of the distribution.
    *   ξ = 0:  Gumbel distribution (light tail)
    *   ξ > 0:  Fréchet distribution (heavy tail - common in financial data)
    *   ξ < 0:  Reverse Weibull distribution (bounded tail)
*   **Location parameter (μ - mu):**  This parameter shifts the distribution along the x-axis. It's roughly the average of the block maxima.
*   **Scale parameter (σ - sigma):**  This parameter controls the spread or dispersion of the distribution.

In the following steps, we will apply the Block Maxima method to our synthetic returns data and fit a GEV distribution to the block maxima.
```

### 2.1.1. Fitting GEV Distribution

To perform Block Maxima analysis, you need to decide on a **Block Size (Years)**.  A slider is provided for this purpose, allowing you to choose between 1 and 5 years.

*   **Block Size (Years):** This slider determines the length of each block in years. For example, if you select 1 year, each block will represent one year of daily returns, and we will find the minimum return (maximum loss) within each year.

Adjust the "Block Size (Years)" slider. The application then calculates the block maxima (minimum returns in each block) and fits a Generalized Extreme Value (GEV) distribution to these maxima.

You will see the output:

```
Fitted GEV Distribution Parameters:
Shape (ξ): [value] , Location (μ): [value], Scale (σ): [value]
```

These are the parameters of the fitted GEV distribution.

```info
**GEV Parameters Interpretation:**

*   **Shape (ξ):** [value]. A positive shape parameter (ξ > 0) is typical for financial data and suggests a **heavy-tailed** distribution, meaning extreme events are more likely than in a normal distribution.
*   **Location (μ):** [value]. The location parameter is an indicator of the central tendency of the block maxima, roughly the average of the minimum returns in each block.
*   **Scale (σ):** [value]. The scale parameter reflects the variability or spread of the block maxima. A larger scale parameter indicates a wider spread of extreme values.
```

### 2.1.2. Visualizing Block Maxima and GEV Fit

To visually assess how well the GEV distribution fits the block maxima, the application generates a chart: **Block Maxima Histogram and Fitted GEV Distribution**.

This chart displays:

*   **Histogram of Block Maxima:**  Blue bars representing the frequency distribution of the calculated block maxima (minimum returns).
*   **Fitted GEV PDF:** A red line showing the Probability Density Function (PDF) of the GEV distribution fitted to the block maxima.

Examine this chart. Ideally, the red GEV PDF line should closely follow the shape of the blue histogram bars, indicating a good fit.

```caption
Comparison of the histogram of Block Maxima with the Probability Density Function (PDF) of the fitted GEV distribution.
```

### 2.1.3. Risk Measures: VaR and ES (Block Maxima)

Finally, the Block Maxima analysis section calculates and displays two crucial risk measures derived from the fitted GEV distribution: **Value at Risk (VaR)** and **Expected Shortfall (ES)**.

You can adjust the **Confidence Level (%)** for both VaR and ES using sliders:

*   **VaR Confidence Level (%):**  Sets the confidence level for VaR calculation, typically between 90% and 99%.
*   **ES Confidence Level (%):** Sets the confidence level for ES calculation, also typically between 90% and 99%.

Adjust these sliders to your desired confidence levels. The application will then calculate and display the VaR and ES values:

```
Value at Risk (VaR) at [Confidence Level]% confidence level: **[VaR Value]**
Expected Shortfall (ES) at [Confidence Level]% confidence level: **[ES Value]**
```

```info
**Risk Measures Interpretation (Block Maxima):**

*   **Value at Risk (VaR):**  At a [Confidence Level]% confidence level, the VaR [VaR Value] represents the maximum expected loss within a block period (e.g., year, depending on your block size choice) that will not be exceeded with [Confidence Level]% probability. In simpler terms, it's the worst-case loss you can expect over a block period at the given confidence level.

*   **Expected Shortfall (ES):** At a [Confidence Level]% confidence level, the ES [ES Value] (also known as Conditional Value at Risk - CVaR) is the expected loss given that the loss exceeds the VaR. It represents the average loss in the worst (100 - Confidence Level)% of cases. ES provides a more comprehensive measure of tail risk than VaR, as it considers the severity of losses beyond the VaR threshold.
```

Experiment with different confidence levels and observe how VaR and ES change. Higher confidence levels will generally result in larger VaR and ES values, reflecting a more conservative risk assessment.

## 2.2. Peak-Over-Threshold (POT) Analysis
Duration: 00:10

Now, let's explore the **Peak-Over-Threshold (POT)** method. If you haven't already, select "Peak-Over-Threshold (POT)" from the "Choose EVT Method:" radio buttons.

```markdown
**Peak-Over-Threshold (POT) Approach:**

The Peak-Over-Threshold (POT) method focuses on the *exceedances* over a high threshold. Instead of looking at block maxima, POT considers all instances where the data goes beyond a pre-defined threshold. The **Pickands-Balkema-de Haan theorem** states that for a sufficiently high threshold, the distribution of these exceedances can be approximated by a **Generalized Pareto Distribution (GPD)**.

POT is often considered more data-efficient than Block Maxima because it utilizes more extreme observations.

The Generalized Pareto Distribution (GPD) is characterized by three parameters, although in practice, it's often simplified to two (the location parameter is sometimes fixed at the threshold):

*   **Shape parameter (ξ - xi):** Similar to GEV, it governs the tail behavior.
*   **Scale parameter (σ - beta):**  Determines the spread of the exceedances.
*   **Threshold (θ - u):** The level above which values are considered exceedances. In our case, we are looking at returns *below* a threshold, representing losses.

In the following steps, we'll apply the POT method to our synthetic returns data, fit a GPD to the exceedances, and calculate risk measures.
```

### 2.2.1. Fitting GPD Distribution

For POT analysis, the key parameter you need to set is the **Threshold Percentile**.

*   **Threshold Percentile:** This slider allows you to choose the percentile to determine the threshold. For example, if you select 95%, the threshold will be set at the 95th percentile of the *returns* (meaning we are looking at the 5% worst returns as exceedances representing losses). A higher percentile means a more extreme threshold, resulting in fewer exceedances.

Adjust the "Threshold Percentile" slider. The application calculates the threshold value based on the chosen percentile and identifies the exceedances (returns below the threshold, representing losses).

You will see the output:

```
Threshold Value (at [Percentile]th percentile): **[Threshold Value]**
Number of Exceedances: **[Number of Exceedances]**
```

The "Threshold Value" is the actual return value corresponding to the selected percentile. "Number of Exceedances" indicates how many data points fall below this threshold.

```warning
**Insufficient Exceedances:** If you choose a very high threshold percentile, you might end up with very few exceedances. If the number of exceedances is too low (less than around 10), the GPD fitting might not be reliable. In such cases, consider lowering the threshold percentile or increasing the data size.
```

If you have sufficient exceedances, the application proceeds to fit a Generalized Pareto Distribution (GPD) to these exceedances.

You will see the output:

```
Fitted GPD Distribution Parameters:
Shape (ξ): [value] , Location (μ): [value], Scale (σ): [value]
```

These are the parameters of the fitted GPD distribution.

```info
**GPD Parameters Interpretation:**

*   **Shape (ξ):** [value]. Similar to the GEV shape parameter, a positive shape parameter (ξ > 0) suggests a heavy tail for the exceedance distribution.
*   **Scale (σ):** [value]. The scale parameter indicates the spread of the exceedances above the threshold.
*   **Location (μ):** [value]. In this implementation, the location parameter is ideally close to zero as we are fitting the GPD to the *excesses* above the threshold (after shifting the data so the threshold is effectively at zero).
```

### 2.2.2. Visualizing Exceedances and GPD Fit

To visualize the GPD fit, the application generates the chart: **Exceedances Histogram and Fitted GPD Distribution**.

This chart shows:

*   **Histogram of Exceedances:** Blue bars representing the frequency distribution of the exceedances (returns below the threshold).
*   **Fitted GPD PDF:** A red line showing the Probability Density Function (PDF) of the GPD distribution fitted to the exceedances.

Examine the chart to see how well the red GPD PDF line matches the shape of the blue histogram of exceedances. A good fit is indicated by the GPD PDF closely following the histogram.

```caption
Histogram of exceedances over the threshold and the Probability Density Function (PDF) of the fitted GPD distribution.
```

### 2.2.3. Risk Measures: VaR and ES (POT)

Finally, the POT analysis section calculates and displays Value at Risk (VaR) and Expected Shortfall (ES) based on the fitted GPD.

You can again adjust the **Confidence Level (%)** for VaR and ES using sliders:

*   **VaR Confidence Level (%) :** Sets the confidence level for VaR calculation using the POT method.
*   **ES Confidence Level (%) :** Sets the confidence level for ES calculation using the POT method.

Adjust these sliders. The application calculates and displays the VaR and ES values:

```
Value at Risk (VaR) at [Confidence Level]% confidence level: **[VaR Value]**
Expected Shortfall (ES) at [Confidence Level]% confidence level: **[ES Value]**
```

```info
**Risk Measures Interpretation (POT):**

*   **Value at Risk (VaR):** At a [Confidence Level]% confidence level, the VaR [VaR Value] represents the return level that is expected to be exceeded with a probability of (100 - Confidence Level)%. In risk terms, it's the loss level that will not be exceeded at the given confidence level.

*   **Expected Shortfall (ES):** At a [Confidence Level]% confidence level, the ES [ES Value] is the expected loss, given that the loss exceeds the VaR threshold calculated using the POT method. It's the average loss in the tail beyond the VaR.
```

Experiment with different confidence levels and observe how VaR and ES change under the POT method. Compare these values with those obtained from the Block Maxima method.

This concludes the codelab for the QuLab Extreme Value Theory (EVT) Stress Tester. You have now explored both Block Maxima and Peak-Over-Threshold methods for modeling extreme risks and calculating key risk measures. By adjusting the data parameters and method-specific parameters, you can further investigate how EVT behaves under different scenarios and deepen your understanding of extreme value theory in financial risk management.

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. To access the full legal documentation, please visit this link. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
