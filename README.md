# QuCreate Streamlit Lab - Maximum Loss Scenario Explorer

## Description

The **Maximum Loss Scenario Explorer** is an interactive Streamlit application designed to help users understand and visualize potential portfolio losses under different risk factor scenarios. By allowing users to define constraints on the changes in risk factors like interest rates and equity indices, the application generates synthetic scenarios and displays the resulting portfolio losses through interactive charts.

This tool is particularly useful for:

- **Risk Management Education:**  Learning how different risk factor movements can impact a portfolio's value.
- **Scenario Analysis:** Exploring "what-if" scenarios by adjusting constraints on risk factor changes.
- **Visualizing Risk:**  Understanding the distribution of potential portfolio losses and identifying maximum loss scenarios through intuitive visualizations.

The application uses synthetic data for demonstration purposes, making it a self-contained learning tool. It is designed to be user-friendly and requires no prior knowledge of complex financial modeling to operate effectively.

## Installation

To run the Maximum Loss Scenario Explorer, you need to have Python installed on your system along with `pip` package manager. Follow these steps to install the application and its dependencies:

1.  **Clone the repository (if applicable) or save the Python script:**
    If you have access to a repository containing the script, clone it to your local machine. Otherwise, save the provided Python code as a `.py` file (e.g., `maximum_loss_explorer.py`).

2.  **Navigate to the project directory:**
    Open your terminal or command prompt and navigate to the directory where you saved the Python script.

3.  **Install required Python packages:**
    Run the following command to install the necessary Python libraries using `pip`:

    ```bash
    pip install streamlit pandas numpy plotly-express
    ```

    This command will install:
    - `streamlit`:  For creating the interactive web application.
    - `pandas`: For data manipulation and analysis.
    - `numpy`: For numerical operations.
    - `plotly-express`: For creating interactive plots and visualizations.

## Usage

Once you have installed the required packages, you can run the Maximum Loss Scenario Explorer application by following these steps:

1.  **Run the Streamlit application:**
    In your terminal, within the project directory, execute the following command:

    ```bash
    streamlit run maximum_loss_explorer.py
    ```
    *(Replace `maximum_loss_explorer.py` with the actual name of your Python script if you saved it with a different name.)*

2.  **Access the application in your browser:**
    Streamlit will automatically launch the application in your default web browser. If it doesn't open automatically, you will see a local URL in your terminal (usually `http://localhost:8501`). Open this URL in your browser to access the application.

3.  **Interact with the application:**
    Once the application is running in your browser, you can interact with it as follows:

    - **Explore the Introduction:**  Read the introduction and learning objectives to understand the purpose and functionality of the application.

    - **Define Constraints:**
        - Use the sliders in the sidebar to set the minimum and maximum percentage changes for **Interest Rates** and **Equity Indices**. These sliders allow you to define the range of risk factor movements for the scenario generation.
        - Adjust the **"Number of Scenarios to Generate"** input field to specify how many synthetic scenarios you want to create and analyze.

    - **Visualize Scenarios:**
        - **Scatter Plot:** Examine the scatter plot to understand the relationship between changes in Interest Rates and Portfolio Loss, with Equity Index changes represented by color. Hover over data points for detailed scenario information.
        - **Histogram:** Analyze the histogram to see the distribution of portfolio losses across all generated scenarios. This shows the frequency of different loss magnitudes.
        - **Line Chart:**  Explore the line chart to see the average portfolio loss in relation to different ranges of Equity Index changes. This helps understand the combined impact of both risk factors on average losses.

    - **Observe Dynamic Updates:** As you adjust the sliders and the number of scenarios, the visualizations will dynamically update to reflect the new constraints and data.

4.  **Explore Different Scenarios:** Experiment with different constraint ranges for interest rates and equity indices to observe how they affect the potential maximum loss scenarios and the distribution of portfolio losses.

## Credits

This application is developed by **QuantUniversity** as part of the QuCreate Streamlit Lab series.

- **QuantUniversity:** [https://www.quantuniversity.com](https://www.quantuniversity.com)

We acknowledge and appreciate the open-source community for providing the libraries that made this application possible, especially:

- **Streamlit:** For the easy-to-use framework to build and share data applications.
- **Pandas:** For powerful data manipulation and analysis capabilities.
- **NumPy:** For efficient numerical computations.
- **Plotly Express:** For creating interactive and visually appealing charts.

## License

**© 2025 QuantUniversity. All Rights Reserved.**

This demonstration is provided for educational purposes only.  Any reproduction, redistribution, or commercial use of this application without prior written consent from QuantUniversity is strictly prohibited. For inquiries regarding licensing or permissions, please contact QuantUniversity through their website.

For full legal documentation and terms of use, please visit [link to legal documentation, if applicable, otherwise remove this line].

This application is intended for educational use and demonstration purposes only.
