# QuLab: Maximum Loss Scenario Explorer

## Description

This Streamlit application, **QuLab: Maximum Loss Scenario Explorer**, is designed to help users understand and visualize maximum loss scenarios in a synthetic portfolio. By interactively adjusting constraints on key risk factors such as Interest Rates, Equity Indices, and Credit Spreads, users can explore how these factors influence potential portfolio losses.

**Key Features:**

*   **Interactive Risk Factor Adjustment:** Use sliders to define the range of changes for Interest Rates, Equity Indices, and Credit Spreads.
*   **Scenario Simulation:** Generate multiple scenarios based on the defined risk factor constraints.
*   **Portfolio Loss Calculation:** Calculate portfolio loss for each scenario using a simplified linear model based on factor sensitivities.
*   **Interactive Scatter Plot Visualization:** Visualize scenarios as a scatter plot, showing Portfolio Loss against a selected Risk Factor, with scenario probability indicated by color.
*   **Scenario Exploration:** Hover over data points in the scatter plot to view detailed information about each scenario, including risk factor changes, portfolio loss, and scenario probability.

**Learning Outcomes:**

*   Understand maximum loss scenarios and the impact of risk factors on portfolio performance.
*   Interpret interactive visualizations to gain insights from simulated data.
*   Learn about data preprocessing and scenario exploration techniques for risk assessment.
*   Experience a user-friendly interface for real-time data interaction and visualization.

This application is intended for educational purposes to demonstrate the principles of maximum loss scenario exploration in a simplified setting.

## Installation

To run this Streamlit application, you need to have Python installed on your system. It is recommended to use Python 3.8 or higher.

1.  **Clone the repository (if applicable):**

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

    If you have downloaded the script directly, navigate to the directory containing the script in your terminal.

2.  **Install required Python packages:**

    Ensure you have `pip` installed. Then, install the necessary libraries using pip:

    ```bash
    pip install streamlit pandas numpy plotly
    ```

    This command will install:
    *   `streamlit`:  For creating the web application.
    *   `pandas`: For data manipulation and analysis.
    *   `numpy`: For numerical computations.
    *   `plotly`: For interactive plotting.

## Usage

1.  **Run the Streamlit application:**

    Navigate to the directory containing the Python script (`your_script_name.py`) in your terminal and run the following command:

    ```bash
    streamlit run your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python script file.

2.  **Access the application in your browser:**

    Streamlit will automatically open the application in your default web browser. If it doesn't, you can access it by navigating to the URL displayed in your terminal (usually `http://localhost:8501`).

3.  **Interact with the application:**

    *   **Sidebar:** The sidebar on the left displays the application title and the QuantUniversity logo.
    *   **Risk Factor Constraints:** Use the sliders in the "Define Risk Factor Constraints" section to set the minimum and maximum changes for each risk factor:
        *   **Interest Rate Change (%)**
        *   **Equity Index Change (%)**
        *   **Credit Spread Change (bps)**
        Adjust the sliders to define the range of market scenarios you want to explore.
    *   **Scatter Plot Visualization:** The "Interactive Scenario Visualization" section displays a scatter plot:
        *   **X-axis:** Select a Risk Factor from the dropdown menu to plot on the X-axis.
        *   **Y-axis:**  The Y-axis always represents "Portfolio Loss".
        *   **Color:** The color of each point represents the "Scenario Probability", with more intense colors indicating higher probability.
        *   **Hover:** Hover over data points to see a tooltip with detailed information about the scenario, including changes in all risk factors, portfolio loss, and scenario probability.
    *   **Explore Scenarios:** Analyze the scatter plot to identify potential maximum loss scenarios and understand how different risk factor changes impact the portfolio.
    *   **Key Insights and Further Exploration:** Read the "Key Insights and Further Exploration" section for guidance on interpreting the results and suggestions for further analysis.

## Credits

This application is developed by **QuantUniversity**.

*   **QuantUniversity:** [https://www.quantuniversity.com/](https://www.quantuniversity.com/)

## License

© 2025 QuantUniversity. All Rights Reserved.

This demonstration is for educational use and illustration purposes only. For full legal documentation, please visit the provided link (if applicable, link to legal documentation should be inserted here). Reproduction of this demonstration requires prior written consent from QuantUniversity.
