import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
from scipy.optimize import minimize

st.set_page_config(page_title="QuCreate Streamlit Lab - EVT Stress Tester", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Extreme Value Theory (EVT) Stress Tester")
st.divider()

# Introduction and Explanation
st.markdown("""
    ## Introduction to Extreme Value Theory (EVT) for Stress Testing

    This application demonstrates the use of **Extreme Value Theory (EVT)** for financial stress testing. 
    EVT is crucial for modeling and quantifying extreme risks, which are often underestimated by traditional statistical methods. 
    This tool helps you explore two primary approaches within EVT: **Block Maxima** and **Peak-Over-Threshold (POT)**.

    **Learning Objectives:**
    - Understand the core concepts of Extreme Value Theory.
    - Learn how EVT can be applied to model extreme financial losses.
    - Explore and compare the Block Maxima and Peak-Over-Threshold methods.
    - Visualize and interpret risk measures like Value at Risk (VaR) and Expected Shortfall (ES) derived from EVT.

    **Dataset:**
    We use a synthetic dataset of daily returns to simulate financial market data. You can adjust the parameters of this synthetic data to observe how EVT behaves under different scenarios.

    Let's get started by generating some synthetic data!
""")

st.header("1. Synthetic Data Generation", divider='blue')

# Data Generation Parameters
st.subheader("1.1. Data Parameters")
data_size = st.slider("Number of Data Points", min_value=100, max_value=5000, value=1000, step=100,
                       help="Adjust the size of the synthetic dataset.")
volatility = st.slider("Volatility (Annualized)", min_value=0.01, max_value=0.50, value=0.20, step=0.01, format="%.2f",
                        help="Set the volatility of the synthetic returns. Higher volatility means more fluctuation and potentially larger extreme values.")

# Generate Synthetic Data
@st.cache_data
def generate_synthetic_returns(size, vol):
    """Generates synthetic daily returns using a normal distribution."""
    daily_vol = vol / np.sqrt(252)  # Assuming 252 trading days in a year
    returns = np.random.normal(0, daily_vol, size)
    return returns

synthetic_returns = generate_synthetic_returns(data_size, volatility)
df_returns = pd.DataFrame({'Returns': synthetic_returns})

st.info("""
    **Understanding the Data Generation:**
    - We are generating synthetic daily returns using a normal distribution.
    - **Volatility** is a key parameter controlling the spread of returns. Higher volatility leads to a wider range of returns, including more extreme values.
    - The data is generated using a simplified model and is for educational purposes. Real-world financial returns may exhibit different characteristics.
""")

# Display Data Sample and Histogram
st.subheader("1.2. Sample Data and Distribution")
col1, col2 = st.columns(2)
with col1:
    st.dataframe(df_returns.head(10), height=200, use_container_width=True)
    st.caption("Sample of generated synthetic daily returns.")

with col2:
    fig_hist = px.histogram(df_returns, x="Returns", nbins=50, title="Distribution of Synthetic Returns",
                             labels={'Returns': 'Daily Returns'})
    st.plotly_chart(fig_hist, use_container_width=True)
    st.caption("Histogram showing the distribution of the generated returns.")

st.header("2. Extreme Value Theory Methods", divider='blue')
evt_method = st.radio("Choose EVT Method:",
                          ['Block Maxima (BM)', 'Peak-Over-Threshold (POT)'],
                          help="Select the method you want to use for Extreme Value Theory analysis.")

st.info("""
    **Choosing an EVT Method:**
    - **Block Maxima (BM):** Focuses on the maximum loss (or minimum return) within non-overlapping blocks of time (e.g., years). It is useful for estimating the distribution of annual extreme losses.
    - **Peak-Over-Threshold (POT):** Considers all losses that exceed a certain high threshold. It is more data-efficient than Block Maxima as it uses more extreme observations.

    Select a method to proceed with the EVT analysis.
""")

if evt_method == 'Block Maxima (BM)':
    st.subheader("2.1. Block Maxima (BM) Analysis")
    st.markdown("""
        **Block Maxima (BM) Approach:**

        The Block Maxima method involves dividing the data into blocks of equal size (e.g., yearly blocks) and identifying the maximum value (or minimum return in case of losses) in each block. 
        According to the **Fisher-Tippett-Gnedenko theorem**, the distribution of these block maxima, under certain conditions, converges to a **Generalized Extreme Value (GEV)** distribution.

        The GEV distribution is characterized by three parameters:
        - **Shape parameter (ξ or xi):**  Determines the tail behavior of the distribution.
            - ξ = 0:  Gumbel distribution (light tail)
            - ξ > 0:  Fréchet distribution (heavy tail)
            - ξ < 0:  Reverse Weibull distribution (bounded tail)
        - **Location parameter (μ or mu):**  Shifts the distribution along the x-axis.
        - **Scale parameter (σ or sigma):**  Determines the spread of the distribution.

        We will now apply the Block Maxima method to our synthetic returns data.
    """)

    block_size_years = st.slider("Block Size (Years)", min_value=1, max_value=5, value=1, step=1,
                                 help="Choose the size of blocks in years for Block Maxima. For example, block size of 1 year means each block is one year long.")

    # Assuming daily data, roughly 252 trading days per year
    block_size = block_size_years * 252
    if block_size > len(synthetic_returns):
        block_size = len(synthetic_returns) # Adjust block size if data is less than chosen block size

    num_blocks = len(synthetic_returns) // block_size
    if num_blocks == 0:
        st.error("Data size is too small for the selected block size. Please increase data size or decrease block size.")
    else:
        block_maxima = []
        for i in range(num_blocks):
            start_index = i * block_size
            end_index = (i + 1) * block_size
            block_returns = synthetic_returns[start_index:end_index]
            block_min_return = np.min(block_returns) # Considering minimum return as maximum loss
            block_maxima.append(block_min_return)

        st.subheader("2.1.1. Fitting GEV Distribution")
        st.write("Calculating Block Maxima and fitting Generalized Extreme Value (GEV) distribution...")

        # Fit GEV distribution to block maxima
        params_gev = stats.genextreme.fit(block_maxima)
        shape_gev, loc_gev, scale_gev = params_gev

        st.write(f"Fitted GEV Distribution Parameters:")
        st.write(f"Shape (ξ): {shape_gev:.4f}, Location (μ): {loc_gev:.4f}, Scale (σ): {scale_gev:.4f}")
        st.info(f"""
            **GEV Parameters Interpretation:**
            - **Shape (ξ):** {shape_gev:.4f}.  A positive shape parameter suggests a heavy-tailed distribution, common in financial data.
            - **Location (μ):** {loc_gev:.4f}. The location parameter is roughly the average of the block maxima.
            - **Scale (σ):** {scale_gev:.4f}. The scale parameter indicates the dispersion or spread of the block maxima.
        """)

        # Visualization of Block Maxima and Fitted GEV
        st.subheader("2.1.2. Visualizing Block Maxima and GEV Fit")
        fig_gev_fit = go.Figure()

        # Histogram of Block Maxima
        hist_data = np.histogram(block_maxima, bins=10, density=True) # Reduced bins for smaller block maxima sample
        fig_gev_fit.add_trace(go.Bar(x=hist_data[1][:-1], y=hist_data[0], name='Histogram of Block Maxima', opacity=0.6))

        # GEV PDF Curve
        x_gev = np.linspace(min(block_maxima), max(block_maxima), 100)
        pdf_gev = stats.genextreme.pdf(x_gev, shape_gev, loc_gev, scale_gev)
        fig_gev_fit.add_trace(go.Scatter(x=x_gev, y=pdf_gev, mode='lines', name='Fitted GEV PDF', line=dict(color='red')))

        fig_gev_fit.update_layout(title='Block Maxima Histogram and Fitted GEV Distribution',
                                  xaxis_title='Block Maxima (Minimum Returns)',
                                  yaxis_title='Density')
        st.plotly_chart(fig_gev_fit, use_container_width=True)
        st.caption("Comparison of the histogram of Block Maxima with the Probability Density Function (PDF) of the fitted GEV distribution.")

        # VaR and ES Calculation for BM
        st.subheader("2.1.3. Risk Measures: VaR and ES (Block Maxima)")
        confidence_level_var_bm = st.slider("VaR Confidence Level (%)", min_value=90, max_value=99, value=95, step=1,
                                        help="Confidence level for Value at Risk (VaR) calculation.")
        confidence_level_es_bm = st.slider("ES Confidence Level (%)", min_value=90, max_value=99, value=95, step=1,
                                       help="Confidence level for Expected Shortfall (ES) calculation.")
        alpha_var_bm = (100 - confidence_level_var_bm) / 100.0
        alpha_es_bm = (100 - confidence_level_es_bm) / 100.0

        var_bm = stats.genextreme.ppf(alpha_var_bm, shape_gev, loc_gev, scale_gev)
        es_bm = stats.genextreme.expect(lambda x: x, args=(shape_gev,), loc=loc_gev, scale=scale_gev, lb=var_bm) / alpha_es_bm if shape_gev != 0 else (var_bm + scale_gev) / alpha_es_bm

        st.write(f"Value at Risk (VaR) at {confidence_level_var_bm}% confidence level: **{var_bm:.4f}**")
        st.write(f"Expected Shortfall (ES) at {confidence_level_es_bm}% confidence level: **{es_bm:.4f}**")
        st.info(f"""
            **Risk Measures Interpretation (Block Maxima):**
            - **Value at Risk (VaR):** At a {confidence_level_var_bm}% confidence level, the maximum expected loss over a block period (e.g., year) is {var_bm:.4f}.
            - **Expected Shortfall (ES):**  If losses exceed the VaR, the expected loss (average loss in the worst {100-confidence_level_es_bm}%) is {es_bm:.4f}.
        """)


elif evt_method == 'Peak-Over-Threshold (POT)':
    st.subheader("2.2. Peak-Over-Threshold (POT) Analysis")
    st.markdown("""
        **Peak-Over-Threshold (POT) Approach:**

        The Peak-Over-Threshold (POT) method focuses on excesses over a high threshold.  For a sufficiently high threshold, the distribution of these excesses can be approximated by a **Generalized Pareto Distribution (GPD)**. 
        This approach is more efficient in using extreme values compared to Block Maxima, as it considers all exceedances, not just the block maxima.

        The GPD is defined by three parameters, though often simplified to two in practice (location is sometimes considered threshold itself and fixed):
        - **Shape parameter (ξ or xi):**  Similar to GEV, it controls the tail behavior.
        - **Scale parameter (σ or beta):**  Determines the spread of the excesses.
        - **Threshold (θ or u):**  The level above which excesses are considered.

        We will now apply the Peak-Over-Threshold method to our synthetic returns data.
    """)

    threshold_percentile = st.slider("Threshold Percentile", min_value=90, max_value=99, value=95, step=1,
                                     help="Percentile to determine the threshold for POT. Higher percentile means a more extreme threshold.")

    threshold_value = np.percentile(synthetic_returns, threshold_percentile)
    exceedances = synthetic_returns[synthetic_returns <= threshold_value] # Losses are negative returns, so we look at returns less than or equal to the threshold

    st.write(f"Threshold Value (at {threshold_percentile}th percentile): **{threshold_value:.4f}**")
    st.write(f"Number of Exceedances: **{len(exceedances)}**")

    if len(exceedances) < 10: # Need enough exceedances to fit GPD
        st.warning("Insufficient exceedances for reliable GPD fitting. Consider lowering the threshold or increasing data size.")
    else:
        st.subheader("2.2.1. Fitting GPD Distribution")
        st.write("Fitting Generalized Pareto Distribution (GPD) to exceedances...")

        # Fit GPD to exceedances
        params_gpd = stats.genpareto.fit(exceedances, floc=threshold_value) # Fixed threshold as location
        shape_gpd, loc_gpd, scale_gpd = params_gpd # loc_gpd might be very close to threshold due to floc=threshold_value

        st.write(f"Fitted GPD Distribution Parameters:")
        st.write(f"Shape (ξ): {shape_gpd:.4f}, Location (μ): {loc_gpd:.4f}, Scale (σ): {scale_gpd:.4f}") # Location here is relative to the threshold.
        st.info(f"""
            **GPD Parameters Interpretation:**
            - **Shape (ξ):** {shape_gpd:.4f}.  Similar to GEV, a positive shape suggests a heavy tail.
            - **Scale (σ):** {scale_gpd:.4f}.  Indicates the spread of the exceedances above the threshold.
            - **Location (μ):** {loc_gpd:.4f}. Ideally should be close to the threshold value set.
        """)

        # Visualization of Exceedances and Fitted GPD
        st.subheader("2.2.2. Visualizing Exceedances and GPD Fit")
        fig_gpd_fit = go.Figure()

        # Histogram of Exceedances
        hist_data_gpd = np.histogram(exceedances, bins=20, density=True)
        fig_gpd_fit.add_trace(go.Bar(x=hist_data_gpd[1][:-1], y=hist_data_gpd[0], name='Histogram of Exceedances', opacity=0.6))

        # GPD PDF Curve
        x_gpd = np.linspace(min(exceedances), max(exceedances), 100)
        pdf_gpd = stats.genpareto.pdf(x_gpd, shape_gpd, loc_gpd, scale_gpd)
        fig_gpd_fit.add_trace(go.Scatter(x=x_gpd, y=pdf_gpd, mode='lines', name='Fitted GPD PDF', line=dict(color='red')))

        fig_gpd_fit.update_layout(title='Exceedances Histogram and Fitted GPD Distribution',
                                  xaxis_title='Exceedances (Returns below Threshold)',
                                  yaxis_title='Density')
        st.plotly_chart(fig_gpd_fit, use_container_width=True)
        st.caption("Histogram of exceedances over the threshold and the Probability Density Function (PDF) of the fitted GPD distribution.")

        # VaR and ES Calculation for POT
        st.subheader("2.2.3. Risk Measures: VaR and ES (POT)")
        confidence_level_var_pot = st.slider("VaR Confidence Level (%) ", min_value=90, max_value=99, value=95, step=1, key="var_pot_slider",
                                            help="Confidence level for Value at Risk (VaR) calculation using POT.")
        confidence_level_es_pot = st.slider("ES Confidence Level (%) ", min_value=90, max_value=99, value=95, step=1, key="es_pot_slider",
                                           help="Confidence level for Expected Shortfall (ES) calculation using POT.")
        alpha_var_pot = (100 - confidence_level_var_pot) / 100.0
        alpha_es_pot = (100 - confidence_level_es_pot) / 100.0

        # VaR calculation for POT is threshold + GPD quantile
        var_pot = threshold_value + stats.genpareto.ppf(alpha_var_pot, shape_gpd, loc=loc_gpd, scale=scale_gpd)
        # ES calculation for POT (formula adjusted for location parameter if needed, assuming location is close to 0 for excesses above threshold)
        es_pot = (var_pot + scale_gpd - shape_gpd * loc_gpd) / (1 - shape_gpd) if shape_gpd != 1 else var_pot + scale_gpd # Simplified ES calculation for GPD

        st.write(f"Value at Risk (VaR) at {confidence_level_var_pot}% confidence level: **{var_pot:.4f}**")
        st.write(f"Expected Shortfall (ES) at {confidence_level_es_pot}% confidence level: **{es_pot:.4f}**")
        st.info(f"""
            **Risk Measures Interpretation (POT):**
            - **Value at Risk (VaR):** At a {confidence_level_var_pot}% confidence level, the expected loss will not exceed {var_pot:.4f}.
            - **Expected Shortfall (ES):**  When losses exceed the VaR, the expected loss (average loss in the tail) is {es_pot:.4f}.
        """)


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
