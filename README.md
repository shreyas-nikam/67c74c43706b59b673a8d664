# QuLab: Maximum Loss Scenario Explorer

## Description

The Maximum Loss Scenario Explorer is an interactive Streamlit application designed to help users understand potential maximum losses within a synthetic portfolio. By exploring different risk factor change scenarios and setting constraints, users can visualize and analyze potential portfolio losses under various market conditions.

This application is a valuable tool for:

- **Understanding Risk Factor Impact:**  Visualizing how changes in interest rates and equity indices affect portfolio value.
- **Exploring Maximum Loss Scenarios:** Identifying potential extreme loss scenarios under defined constraints.
- **Visualizing Probabilities:**  Understanding the likelihood of different loss scenarios through probability-based visualizations.

**Key Features:**

- **Interactive Risk Factor Constraints:** Use sliders to define the maximum allowed change for interest rates and equity indices.
- **Scenario Visualization:** Explore scatter plots showing portfolio loss against risk factor changes, color-coded by scenario probability.
- **Loss Distribution Analysis:** View a histogram of portfolio losses to understand the distribution of potential outcomes.
- **Educational Focus:**  Learn about maximum loss concepts, risk factors, constraints, and joint probabilities in a practical, visual manner.

This application uses synthetic data for demonstration purposes, simulating a portfolio sensitive to interest rate and equity index risk factors.

## Installation

To run this Streamlit application, you need to have Python installed on your system. It is recommended to use Python 3.8 or later.

1. **Clone the repository (if applicable):**
   If you have access to a repository containing this application, clone it to your local machine.

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install required Python packages:**
   Navigate to the application directory in your terminal and install the necessary Python libraries using pip:

   ```bash
   pip install streamlit pandas numpy plotly
   ```

   This command will install:
   - `streamlit`:  For creating the web application.
   - `pandas`: For data manipulation and analysis.
   - `numpy`: For numerical operations.
   - `plotly`: For interactive visualizations.

## Usage

1. **Run the Streamlit application:**
   In your terminal, within the application directory, run the following command:

   ```bash
   streamlit run your_script_name.py
   ```
   Replace `your_script_name.py` with the actual name of your Python script (if it's not named as in the example, you can find it in the provided code). If you have saved the provided code as `app.py`, you would run:

   ```bash
   streamlit run app.py
   ```

2. **Access the application in your browser:**
   Streamlit will automatically open the application in your default web browser. If it doesn't open automatically, you will see a URL in your terminal (usually `http://localhost:8501`). Open this URL in your browser.

3. **Interact with the application:**

   - **Define Risk Factor Constraints:**
     - On the left sidebar, you will find sliders to adjust the "Maximum Change in Interest Rate (%)" and "Maximum Change in Equity Index (%)".
     - Use these sliders to set the maximum percentage change you want to consider for each risk factor.
     - The application will dynamically regenerate scenarios based on these constraints.

   - **Explore Scenarios:**
     - **Portfolio Loss vs. Interest Rate Change & Portfolio Loss vs. Equity Index Change:**  Observe the two scatter plots. These plots visualize the generated scenarios.
       - The X-axis represents the change in the respective risk factor.
       - The Y-axis represents the Portfolio Loss in dollars.
       - The color and size of each point indicate the "Probability" of that scenario. Brighter and larger points represent higher probability scenarios.
       - Hover over the points to see detailed information about each scenario, including the changes in both risk factors, Portfolio Loss, and Probability.

     - **Distribution of Portfolio Losses:** Examine the histogram below the scatter plots. This histogram shows the distribution of portfolio losses across all generated scenarios, giving you an overview of the frequency of different loss magnitudes.

   - **Understand Maximum Loss:**
     - Read the "Understanding Maximum Loss" section to learn more about the concepts behind the application and how to interpret the visualizations.


By adjusting the risk factor constraints and observing the changes in the visualizations, you can explore different maximum loss scenarios and gain a deeper understanding of portfolio risk.

## Credits

This application is developed by **QuantUniversity**.

- **Logo:** The QuantUniversity logo is displayed in the sidebar and is sourced from: [https://www.quantuniversity.com/assets/img/logo5.jpg](https://www.quantuniversity.com/assets/img/logo5.jpg)
- **Copyright:** © 2025 QuantUniversity. All Rights Reserved.

## License

This application is provided for educational use and illustration purposes only. All rights are reserved by QuantUniversity.

**License Restrictions:**

- Reproduction of this demonstration requires prior written consent from QuantUniversity.
- For full legal documentation and licensing information, please contact QuantUniversity.

**Disclaimer:**

This demonstration is solely for educational purposes. It is not intended for production use or financial advice. Please consult with a qualified professional for financial decisions.
