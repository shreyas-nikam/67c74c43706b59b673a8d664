import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuCreate Streamlit Lab - Maximum Loss Scenario Explorer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Maximum Loss Scenario Explorer")
st.divider()

# Explanation of the App
st.markdown("""
    ## Maximum Loss Scenario Explorer

    Welcome to the Maximum Loss Scenario Explorer! This interactive application helps you understand potential maximum losses in a synthetic portfolio by exploring different risk factor change scenarios.

    **Learning Outcomes:**
    - Understand how changes in risk factors impact portfolio loss.
    - Visualize maximum loss scenarios under different constraints.
    - Explore the concept of joint probabilities in risk factor changes.

    **How to Use:**
    1.  **Define Risk Factor Constraints:** Use the sliders to set the maximum allowed change for each risk factor.
    2.  **Explore Scenarios:** Observe the scatter plot visualizing portfolio loss against risk factor changes.
    3.  **Analyze Probabilities:** Notice how scenario probabilities influence the visualization and interpretation of risk.

    Let's dive in and explore!
    """)

st.divider()

# --- Data Generation ---
st.subheader("Synthetic Portfolio and Risk Factors")
st.write("To make this lab self-sufficient, we are using synthetic data. This data simulates a portfolio sensitive to two risk factors.")

# Define risk factors and portfolio (simplified)
risk_factors = ['Interest Rate', 'Equity Index']
initial_portfolio_value = 1000000  # Initial portfolio value

# Function to generate synthetic scenarios
def generate_scenarios(num_scenarios, max_rate_change, max_equity_change):
    np.random.seed(42) # for reproducibility
    rate_changes = np.random.uniform(-max_rate_change, max_rate_change, num_scenarios)
    equity_changes = np.random.uniform(-max_equity_change, max_equity_change, num_scenarios)

    # Simplified portfolio loss function (linear for demonstration)
    portfolio_losses = initial_portfolio_value * (0.5 * rate_changes + 0.5 * equity_changes + 0.01 * np.random.randn(num_scenarios)) # Added noise

    # Synthetic probabilities (inverse relationship with magnitude of change for demonstration)
    probabilities = np.exp(-0.5 * (rate_changes**2 + equity_changes**2))
    probabilities = probabilities / np.sum(probabilities) # Normalize to sum to 1

    scenarios_df = pd.DataFrame({
        risk_factors[0]: rate_changes,
        risk_factors[1]: equity_changes,
        'Portfolio Loss': portfolio_losses,
        'Probability': probabilities
    })
    return scenarios_df

# --- Input Forms for Constraints ---
st.subheader("Define Risk Factor Constraints")
st.write("Adjust the sliders below to set the maximum allowed change for each risk factor. This simulates applying constraints to your stress test scenarios.")

col1, col2 = st.columns(2)

with col1:
    max_rate_change_input = st.slider(f"Maximum Change in {risk_factors[0]} (%)", min_value=0.0, max_value=0.1, value=0.05, step=0.01, format="%.2f")
    st.caption(f"Set the maximum percentage change allowed for {risk_factors[0]}.")

with col2:
    max_equity_change_input = st.slider(f"Maximum Change in {risk_factors[1]} (%)", min_value=0.0, max_value=0.1, value=0.08, step=0.01, format="%.2f")
    st.caption(f"Set the maximum percentage change allowed for {risk_factors[1]}.")

num_scenarios = 500 # Number of scenarios to generate

# Generate scenarios based on user inputs
scenarios_data = generate_scenarios(num_scenarios, max_rate_change_input, max_equity_change_input)

# --- Interactive Visualizations ---
st.subheader("Interactive Scenario Visualization")
st.write("The scatter plot below visualizes different scenarios of risk factor changes and their corresponding portfolio losses. Points are color-coded by probability.")

# Scatter Plot: Portfolio Loss vs. Risk Factor 1 Change, color by Probability
st.markdown("### Portfolio Loss vs. Interest Rate Change")
scatter_fig_rate = px.scatter(scenarios_data, x=risk_factors[0], y='Portfolio Loss',
                               color='Probability', size='Probability',
                               hover_data=[risk_factors[1], 'Portfolio Loss', 'Probability'],
                               title=f'Portfolio Loss Scenarios under Constraints',
                               labels={'Portfolio Loss': 'Portfolio Loss ($)',
                                       risk_factors[0]: f'{risk_factors[0]} Change',
                                       'Probability': 'Scenario Probability'},
                                color_continuous_scale=px.colors.sequential.Viridis) # Using Viridis for better color perception
scatter_fig_rate.update_layout(xaxis_title=f'{risk_factors[0]} Change (%)', yaxis_title='Portfolio Loss ($)')
st.plotly_chart(scatter_fig_rate, use_container_width=True)
st.caption("This scatter plot displays how changes in the Interest Rate risk factor relate to portfolio loss. "
             "The color and size of each point represent the probability of that specific scenario. "
             "Higher probability scenarios are shown in brighter colors and larger sizes.")


# Scatter Plot: Portfolio Loss vs. Risk Factor 2 Change, color by Probability
st.markdown("### Portfolio Loss vs. Equity Index Change")
scatter_fig_equity = px.scatter(scenarios_data, x=risk_factors[1], y='Portfolio Loss',
                               color='Probability', size='Probability',
                               hover_data=[risk_factors[0], 'Portfolio Loss', 'Probability'],
                               title=f'Portfolio Loss Scenarios under Constraints',
                               labels={'Portfolio Loss': 'Portfolio Loss ($)',
                                       risk_factors[1]: f'{risk_factors[1]} Change',
                                       'Probability': 'Scenario Probability'},
                                color_continuous_scale=px.colors.sequential.Plasma) # Using Plasma for visual distinction
scatter_fig_equity.update_layout(xaxis_title=f'{risk_factors[1]} Change (%)', yaxis_title='Portfolio Loss ($)')
st.plotly_chart(scatter_fig_equity, use_container_width=True)
st.caption("Similarly, this scatter plot shows the relationship between changes in the Equity Index risk factor and portfolio loss. "
             "Again, color and size indicate scenario probability, helping to identify more likely loss scenarios.")


# Bar Chart: Distribution of Portfolio Losses
st.markdown("### Distribution of Portfolio Losses")
hist_fig_loss = px.histogram(scenarios_data, x='Portfolio Loss', nbins=30,
                             title='Distribution of Portfolio Losses Across Scenarios',
                             labels={'Portfolio Loss': 'Portfolio Loss ($)'})
hist_fig_loss.update_layout(xaxis_title='Portfolio Loss ($)', yaxis_title='Frequency')
st.plotly_chart(hist_fig_loss, use_container_width=True)
st.caption("This histogram shows the distribution of portfolio losses across all generated scenarios. "
             "It helps visualize the range of potential losses and their frequency, giving an overview of the risk profile under the defined constraints.")


# --- Explanation of Maximum Loss Concept ---
st.divider()
st.subheader("Understanding Maximum Loss")
st.write("""
    **Maximum Loss** in this context refers to the scenario where the portfolio experiences the greatest possible loss, given a set of constraints on risk factor changes.
    By exploring different constraints, we can understand:
    -   The potential magnitude of losses under various stress conditions.
    -   The likelihood of these extreme loss scenarios occurring (indicated by probability).
    -   Which risk factors are most influential in driving maximum losses.

    **Key Concepts:**
    -   **Risk Factors:** These are variables that can impact the value of your portfolio (e.g., interest rates, equity indices, commodity prices).
    -   **Constraints:** Limits or boundaries set on how much risk factors can change. These are crucial for making stress tests realistic and plausible.
    -   **Joint Probabilities:** The likelihood of different risk factor changes occurring together. Considering these probabilities helps in assessing the realism of stress scenarios.

    In this application, you are interactively exploring these concepts by adjusting constraints and observing the resulting portfolio loss scenarios.
    """)


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
