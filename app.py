import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuCreate Streamlit Lab - Maximum Loss Scenario Explorer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Maximum Loss Scenario Explorer")
st.divider()

st.write("""
    ## Understanding Maximum Loss Scenarios in a Synthetic Portfolio

    This interactive application helps you explore **Maximum Loss Scenarios** in a synthetic portfolio. 
    By adjusting constraints on various risk factors, you can visualize how these factors impact potential portfolio losses.

    **Learning Outcomes:**
    - Gain a clear understanding of maximum loss scenarios and the influence of risk factors.
    - Explore interactive visualizations to interpret data and draw meaningful insights.
    - Understand data preprocessing and scenario exploration for risk assessment.
    - Experience an intuitive user interface for real-time data interaction and visualization.

    Let's dive in and explore!
    """)

st.subheader("Synthetic Portfolio and Risk Factors")
st.write("""
    We begin with a **synthetic portfolio** that is sensitive to three key risk factors: 
    **Interest Rates**, **Equity Indices**, and **Credit Spreads**. 
    This simplified model allows us to clearly demonstrate the principles of maximum loss scenario exploration.

    Below, you can adjust the potential changes in each risk factor to simulate different market conditions. 
    Observe how these changes affect the portfolio loss in real-time through interactive visualizations.
    """)

# --- Data Generation ---
np.random.seed(0)  # for reproducibility

# Define risk factors and their initial sensitivities (example)
risk_factors = ['Interest Rate Change (%)', 'Equity Index Change (%)', 'Credit Spread Change (bps)']
factor_sensitivities = np.array([0.5, 0.8, 0.3])  # Example sensitivities - portfolio response to 1 unit change in factor

# --- Input Sliders for Risk Factor Constraints ---
st.subheader("Define Risk Factor Constraints")
st.write("""
    Use the sliders below to define the range of changes for each risk factor you want to explore. 
    These constraints help us simulate plausible scenarios and understand their potential impact on the portfolio.
    """)

risk_factor_changes = {}
for factor in risk_factors:
    min_val = -5.0 if 'Rate' in factor or 'Index' in factor else -50  # Adjust ranges as needed
    max_val = 5.0 if 'Rate' in factor or 'Index' in factor else 50
    step_val = 0.1 if 'Rate' in factor or 'Index' in factor else 1
    default_min = -1.0 if 'Rate' in factor or 'Index' in factor else -10
    default_max = 1.0 if 'Rate' in factor or 'Index' in factor else 10

    col1, col2 = st.columns(2)
    with col1:
        min_change = st.slider(f"Min {factor}", min_value=min_val, max_value=max_val, value=default_min, step=step_val)
    with col2:
        max_change = st.slider(f"Max {factor}", min_value=min_val, max_value=max_val, value=default_max, step=step_val)
    risk_factor_changes[factor] = (min_change, max_change)


# --- Scenario Generation and Portfolio Loss Calculation ---
st.subheader("Simulating Scenarios and Calculating Portfolio Loss")
st.write("""
    Based on the constraints you've set, we now simulate various scenarios by randomly sampling changes in each risk factor within the defined ranges. 
    For each scenario, we calculate the portfolio loss using a simplified linear model:

    **Portfolio Loss = Σ (Factor Sensitivity<sub>i</sub> * Risk Factor Change<sub>i</sub>)**

    Where:
    - **Factor Sensitivity<sub>i</sub>** represents how sensitive the portfolio is to a 1 unit change in risk factor i.
    - **Risk Factor Change<sub>i</sub>** is the simulated change in risk factor i for a given scenario.

    This model provides a straightforward way to estimate portfolio loss under different market conditions.
    """)

num_scenarios = 500 # Number of scenarios to simulate - adjust for performance if needed
scenarios_data = []

for _ in range(num_scenarios):
    scenario_changes = []
    for i, factor in enumerate(risk_factors):
        min_change, max_change = risk_factor_changes[factor]
        change = np.random.uniform(min_change, max_change)
        scenario_changes.append(change)

    portfolio_loss = -np.sum(factor_sensitivities * np.array(scenario_changes)) # Negative sign to represent loss
    probability = np.exp(-np.sum(np.abs(scenario_changes)) / 5) # Simplified probability - larger changes less probable

    scenarios_data.append(scenario_changes + [portfolio_loss, probability])

scenarios_df = pd.DataFrame(scenarios_data, columns=risk_factors + ['Portfolio Loss', 'Scenario Probability'])


# --- Interactive Scatter Plot Visualization ---
st.subheader("Interactive Scenario Visualization: Portfolio Loss vs. Risk Factor Changes")
st.write("""
    This **Scatter Plot** visualizes the simulated scenarios. Each point represents a scenario with specific risk factor changes and the resulting portfolio loss.

    - **X-axis:**  Displays the change in the selected Risk Factor.
    - **Y-axis:**  Shows the corresponding **Portfolio Loss** for each scenario.
    - **Color:**  Represents the **Scenario Probability**. Scenarios with higher probability are colored more intensely.

    **Interaction:**
    - Hover over points to see detailed information about each scenario, including the changes in all risk factors, portfolio loss, and scenario probability.
    - Use the dropdown below to select which Risk Factor's change you want to visualize on the X-axis.

    By exploring this plot, you can identify potential maximum loss scenarios and understand how different risk factor changes contribute to portfolio vulnerability.
    """)

selected_risk_factor_x = st.selectbox("Select Risk Factor for X-axis", risk_factors, index=0)

fig_scatter = px.scatter(scenarios_df,
                          x=selected_risk_factor_x,
                          y='Portfolio Loss',
                          color='Scenario Probability',
                          size_max=15,
                          opacity=0.7,
                          hover_data=risk_factors + ['Portfolio Loss', 'Scenario Probability'],
                          title=f'Portfolio Loss Scenarios vs. {selected_risk_factor_x}',
                          labels={'Portfolio Loss': 'Portfolio Loss', selected_risk_factor_x: selected_risk_factor_x, 'Scenario Probability': 'Probability'})

st.plotly_chart(fig_scatter, use_container_width=True)


# --- Additional Information and Explanations ---
st.divider()
st.subheader("Key Insights and Further Exploration")
st.write("""
    - **Maximum Loss Identification:** Examine the scatter plot to identify scenarios with the highest portfolio losses (points at the top of the plot).
    - **Risk Factor Impact:** Observe how changes in different risk factors correlate with portfolio loss. Are certain risk factors more influential than others?
    - **Probability Consideration:** Notice how scenario probability is distributed. Are high-loss scenarios also high-probability scenarios, or are they less likely 'tail events'?
    - **Constraint Adjustment:** Experiment by adjusting the risk factor constraints using the sliders. How do changes in constraints affect the range of portfolio losses and the distribution of scenarios?

    **Further Steps:**
    - **More Realistic Models:** For a more accurate analysis, consider using more sophisticated portfolio models and risk factor relationships.
    - **Historical Data Integration:** Incorporate historical data to calibrate risk factor distributions and scenario probabilities for a more data-driven approach.
    - **Advanced Risk Measures:** Explore other risk measures beyond maximum loss, such as Value at Risk (VaR) and Expected Shortfall (ES), to gain a broader understanding of portfolio risk.

    This application provides a foundational understanding of maximum loss scenario exploration. By interacting with the tool and considering these further steps, you can deepen your knowledge of risk management practices.
    """)


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
