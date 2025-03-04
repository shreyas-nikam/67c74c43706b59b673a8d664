# QuLab: Extreme Value Theory (EVT) Stress Tester

## Description

This Streamlit application, **QuLab: Extreme Value Theory (EVT) Stress Tester**, is designed to demonstrate and explore the application of Extreme Value Theory in financial stress testing. It provides an interactive platform to understand how EVT can be used to model and quantify extreme financial risks, which are often underestimated by traditional statistical methods.

The application focuses on two primary methods within EVT:

- **Block Maxima (BM):** Analyzes the maximum (or minimum in the case of losses) values within specified blocks of time to fit a Generalized Extreme Value (GEV) distribution.
- **Peak-Over-Threshold (POT):** Examines values that exceed a certain threshold to fit a Generalized Pareto Distribution (GPD).

**Key Features:**

- **Synthetic Data Generation:** Generate synthetic financial returns with adjustable volatility to simulate different market conditions.
- **Interactive Parameter Tuning:** Easily adjust parameters for data generation, Block Maxima (block size), and Peak-Over-Threshold (threshold percentile).
- **GEV and GPD Fitting:** Fit the GEV distribution to Block Maxima and the GPD distribution to Peak-Over-Threshold exceedances.
- **Visualization:** Visualize the distribution of synthetic returns, Block Maxima, and exceedances, along with the fitted GEV and GPD probability density functions.
- **Risk Measure Calculation:** Calculate and interpret Value at Risk (VaR) and Expected Shortfall (ES) using both Block Maxima and Peak-Over-Threshold methods.
- **Educational Tool:** Provides clear explanations and interpretations of EVT concepts, parameters, and risk measures.

This application is intended for educational purposes to help users understand the principles of Extreme Value Theory and its application in financial risk management.

## Installation

To run this Streamlit application, you need to have Python installed on your system. It is recommended to use Python 3.8 or later. Follow these steps to install and set up the application:

1. **Clone the repository (if applicable):**
   If you have access to a repository containing this application, clone it to your local machine using Git:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Create a virtual environment (recommended):**
   It's good practice to create a virtual environment to isolate project dependencies.
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

3. **Install required packages:**
   Install the necessary Python libraries using pip. The application requires Streamlit, NumPy, Pandas, SciPy, and Plotly.
   ```bash
   pip install streamlit numpy pandas scipy plotly
   ```
   Alternatively, you can install all dependencies from a `requirements.txt` file if provided:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: A `requirements.txt` file is not provided in the specification, so you may need to create one if you plan to share this application or ensure consistent dependency versions.)*

## Usage

1. **Run the Streamlit application:**
   Navigate to the directory containing the Streamlit application file (e.g., `app.py`) in your terminal and run the following command:
   ```bash
   streamlit run app.py
   ```

2. **Access the application in your browser:**
   Streamlit will automatically open the application in your default web browser. If it doesn't, you can manually access it by navigating to the URL displayed in the terminal (usually `http://localhost:8501`).

3. **Using the EVT Stress Tester:**

   The application is structured in a step-by-step manner:

   **Step 1: Synthetic Data Generation**
   - **1.1. Data Parameters:**
     - **Number of Data Points:** Use the slider to adjust the size of the synthetic dataset. More data points generally lead to more robust results.
     - **Volatility (Annualized):**  Use the slider to set the annualized volatility of the synthetic returns. Higher volatility will result in more extreme values in the generated data.
   - **1.2. Sample Data and Distribution:**
     - View a sample of the generated synthetic daily returns in the dataframe.
     - Observe the distribution of the generated returns in the histogram.

   **Step 2: Extreme Value Theory Methods**
   - **Choose EVT Method:** Select either "Block Maxima (BM)" or "Peak-Over-Threshold (POT)" using the radio buttons to proceed with the chosen EVT method.

   **If you choose 'Block Maxima (BM)':**
   - **2.1. Block Maxima (BM) Analysis:**
     - **Block Size (Years):**  Use the slider to define the block size in years. The data will be divided into blocks of this duration, and the minimum return (maximum loss) within each block will be used for analysis.
     - **2.1.1. Fitting GEV Distribution:** The application will fit a Generalized Extreme Value (GEV) distribution to the calculated Block Maxima and display the fitted parameters (Shape, Location, Scale). Interpretations of these parameters are provided.
     - **2.1.2. Visualizing Block Maxima and GEV Fit:** A histogram of the Block Maxima and the Probability Density Function (PDF) of the fitted GEV distribution are displayed for visual comparison.
     - **2.1.3. Risk Measures: VaR and ES (Block Maxima):**
       - **VaR Confidence Level (%)**: Use the slider to set the confidence level for Value at Risk (VaR) calculation.
       - **ES Confidence Level (%)**: Use the slider to set the confidence level for Expected Shortfall (ES) calculation.
       - The calculated VaR and ES values are displayed, along with their interpretations in the context of Block Maxima analysis.

   **If you choose 'Peak-Over-Threshold (POT)':**
   - **2.2. Peak-Over-Threshold (POT) Analysis:**
     - **Threshold Percentile:** Use the slider to set the percentile for determining the threshold. Returns below this percentile will be considered exceedances.
     - The threshold value and the number of exceedances are displayed.
     - **2.2.1. Fitting GPD Distribution:** The application will fit a Generalized Pareto Distribution (GPD) to the exceedances and display the fitted parameters (Shape, Location, Scale). Interpretations of these parameters are provided.
     - **2.2.2. Visualizing Exceedances and GPD Fit:** A histogram of the exceedances and the PDF of the fitted GPD distribution are displayed.
     - **2.2.3. Risk Measures: VaR and ES (POT):**
       - **VaR Confidence Level (%)**: Use the slider to set the confidence level for VaR calculation using the POT method.
       - **ES Confidence Level (%)**: Use the slider to set the confidence level for ES calculation using the POT method.
       - The calculated VaR and ES values are displayed, along with their interpretations in the context of Peak-Over-Threshold analysis.

4. **Experiment and Learn:**
   Adjust the parameters, explore different EVT methods, and observe how the results change. This interactive tool allows you to gain a practical understanding of EVT and its application in stress testing.

## Credits

Developed by QuantUniversity © 2025. All Rights Reserved.

For educational use. For full legal documentation, please visit [link to legal documentation - *replace with actual link if available*]. Any reproduction of this demonstration requires prior written consent from QuantUniversity.

## License

This application is for educational use and is provided as is.  While no specific license is explicitly stated in the provided specification, for open-source best practices, we can assume a permissive license such as the MIT License.

**MIT License**

*[Replace the following with the full text of the MIT License or the actual license if different]*

Copyright (c) 2025 QuantUniversity

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**Note:** Please replace the bracketed placeholders (e.g., `[repository-url]`, `[repository-directory]`, `[link to legal documentation - replace with actual link if available]`, and the MIT License text if a different license applies) with the correct information for your project. If a specific license is intended other than MIT, ensure to replace the license section accordingly and include the full license text.
