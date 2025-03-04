import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuCreate Streamlit Lab - Maximum Loss Scenario Explorer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Maximum Loss Scenario Explorer")
st.divider()

# Introduction and Explanation
st.header("Welcome to the Maximum Loss Scenario Explorer!")
st.write(
    "This interactive application allows you to explore maximum loss scenarios for a synthetic portfolio by adjusting constraints on risk factor changes."
    " By manipulating these constraints, you can visualize their impact on potential portfolio losses and the likelihood of such scenarios."
)

st.subheader("Learning Objectives:")
st.markdown(
    """
    - **Understand Maximum Loss Scenarios:** Learn how different risk factor movements can lead to portfolio losses.
    - **Interactive Data Visualization:** Explore portfolio loss through interactive charts and understand the influence of constraints.
    - **Data Exploration:** Gain insights into how constraints on risk factors affect the distribution of potential losses.
    - **User-Friendly Application:** Interact with an intuitive application to analyze risk scenarios in real-time.
    """
)
st.divider()

# --- Synthetic Data Generation ---
st.subheader("Synthetic Portfolio and Risk Factors")
st.write("To make this lab self-sufficient, we are using synthetic data. Let's define our synthetic portfolio and risk factors:")

# Define Risk Factors (simplified to 2 for clarity)
risk_factors = ["Interest Rate", "Equity Index"]
st.write(f"**Risk Factors:** {', '.join(risk_factors)}")

# Define Synthetic Portfolio (simplified - values are arbitrary for demonstration)
portfolio_assets = ["Asset A", "Asset B", "Asset C"]
portfolio_weights = np.array([0.4, 0.3, 0.3])  # Example weights
st.write(f"**Portfolio Assets:** {', '.join(portfolio_assets)}")
st.write(f"**Portfolio Weights:** {portfolio_weights}")

# Function to generate synthetic risk factor changes and portfolio loss
def generate_scenarios(num_scenarios, interest_rate_change_range, equity_index_change_range):
    """Generates synthetic scenarios for risk factor changes and portfolio loss."""
    np.random.seed(42) # for reproducibility

    interest_rate_changes = np.random.uniform(interest_rate_change_range[0], interest_rate_change_range[1], num_scenarios)
    equity_index_changes = np.random.uniform(equity_index_change_range[0], equity_index_change_range[1], num_scenarios)

    portfolio_losses = np.zeros(num_scenarios)
    for i in range(num_scenarios):
        # Simplified loss calculation - assuming linear sensitivity for demonstration
        portfolio_loss = (
            portfolio_weights[0] * interest_rate_changes[i] * 100 +  # Asset A sensitive to Interest Rate
            portfolio_weights[1] * equity_index_changes[i] * 100 +     # Asset B sensitive to Equity Index
            portfolio_weights[2] * (0.5 * interest_rate_changes[i] + 0.5 * equity_index_changes[i]) * 100 # Asset C sensitive to both
        )
        portfolio_losses[i] = portfolio_loss

    df = pd.DataFrame({
        "Interest Rate Change (%)": interest_rate_changes,
        "Equity Index Change (%)": equity_index_changes,
        "Portfolio Loss (%)": portfolio_losses
    })
    return df

st.divider()

# --- Input Forms for Constraints ---
st.subheader("Define Constraints on Risk Factor Changes")
st.write("Adjust the sliders below to set the range of possible changes for each risk factor. This allows you to explore different stress scenarios.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Interest Rate Change Constraint (%)**")
    interest_rate_min_change = st.slider("Minimum Change (%)", min_value=-10.0, max_value=0.0, value=-2.0, step=0.5)
    interest_rate_max_change = st.slider("Maximum Change (%)", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
    interest_rate_change_range = (interest_rate_min_change, interest_rate_max_change)

with col2:
    st.markdown("**Equity Index Change Constraint (%)**")
    equity_index_min_change = st.slider("Minimum Change (%)", min_value=-20.0, max_value=0.0, value=-5.0, step=1.0)
    equity_index_max_change = st.slider("Maximum Change (%)", min_value=0.0, max_value=20.0, value=5.0, step=1.0)
    equity_index_change_range = (equity_index_min_change, equity_index_max_change)

num_scenarios = st.number_input("Number of Scenarios to Generate", min_value=100, max_value=10000, value=1000, step=100)

st.divider()

# --- Generate and Visualize Scenarios ---
st.subheader("Visualizing Maximum Loss Scenarios")
st.write("Based on your defined constraints and the number of scenarios, we are generating and visualizing potential portfolio losses.")

scenario_df = generate_scenarios(num_scenarios, interest_rate_change_range, equity_index_change_range)

# --- Scatter Plot: Portfolio Loss vs. Risk Factor Changes ---
st.markdown("### Scatter Plot: Portfolio Loss vs. Risk Factor Changes")
st.write("This scatter plot visualizes the relationship between changes in risk factors and the resulting portfolio loss. Each point represents a scenario.")

scatter_fig = px.scatter(scenario_df, x="Interest Rate Change (%)", y="Portfolio Loss (%)",
                         color="Equity Index Change (%)",
                         hover_data=["Equity Index Change (%)", "Portfolio Loss (%)"],
                         title="Portfolio Loss Scenarios",
                         labels={"Equity Index Change (%)": "Equity Index Change (%) (Color)"}
                         )
st.plotly_chart(scatter_fig, use_container_width=True)
st.caption("In this scatter plot, the x-axis represents the percentage change in Interest Rates, and the y-axis shows the percentage Portfolio Loss. "
             "The color of each point is determined by the Equity Index Change percentage. Hover over the points to see detailed values for each scenario.")

# --- Histogram: Distribution of Portfolio Losses ---
st.markdown("### Histogram: Distribution of Portfolio Losses")
st.write("This histogram shows the distribution of portfolio losses across all generated scenarios. It helps to understand the frequency and range of potential losses.")

hist_fig = px.histogram(scenario_df, x="Portfolio Loss (%)", nbins=30, title="Distribution of Portfolio Losses",
                        labels={"Portfolio Loss (%)": "Portfolio Loss (%)"})
st.plotly_chart(hist_fig, use_container_width=True)
st.caption("The histogram displays the frequency of different portfolio loss percentages. The shape of the distribution gives an idea about the likelihood of different loss magnitudes under the defined constraints.")

# --- Line Chart: Portfolio Loss vs. Interest Rate Change (Average per Equity Index Range) ---
st.markdown("### Line Chart: Average Portfolio Loss vs. Interest Rate Change")
st.write("This line chart shows how the average portfolio loss changes with Interest Rate changes, categorized by ranges of Equity Index changes. This visualization helps to understand the combined effect of both risk factors.")

# Group data for line chart
equity_bins = pd.cut(scenario_df["Equity Index Change (%)"], bins=5) # Categorize Equity Index Changes
grouped_df = scenario_df.groupby(equity_bins)["Portfolio Loss (%)"].mean().reset_index()
grouped_df.columns = ["Equity Index Change Range", "Average Portfolio Loss (%)"]


line_fig = px.line(grouped_df, x="Equity Index Change Range", y="Average Portfolio Loss (%)",
                   title="Average Portfolio Loss vs. Equity Index Change Range",
                   labels={"Equity Index Change Range": "Equity Index Change Range", "Average Portfolio Loss (%)": "Average Portfolio Loss (%)"})
st.plotly_chart(line_fig, use_container_width=True)
st.caption("This line chart illustrates the trend of average portfolio loss as the Equity Index Change Range varies. It helps to visualize how changes in one risk factor (Equity Index in this case, binned into ranges) influence the average loss across different levels of another risk factor (implicitly across all Interest Rate changes within constraints).")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
