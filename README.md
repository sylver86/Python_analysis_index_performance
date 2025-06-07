# Stock Market Index Analysis: S&P 500 vs. EURO STOXX 50

## 1. Project Overview

This project provides a comprehensive analysis of the historical performance of two major stock market indices over the last decade: the **S&P 500** (representing the US market) and the **EURO STOXX 50** (representing the European market).

The primary goal is to extract actionable insights from historical data using Python's data science stack. This repository is structured as a professional data analysis project, emphasizing clean code, modularity, reproducibility, and clear visualization of results. The core logic is encapsulated in a Python module, while the analysis narrative and visualizations are presented in a Jupyter Notebook.

## 2. Key Analyses & Visualizations

The analysis covers several key areas to understand the behavior of these indices:
-   **Historical Price and Volume Trends**: Visualization of closing prices and trading volumes over time to identify long-term trends.
-   **Returns Distribution**: A histogram of daily returns to understand volatility and risk profile.
-   **Periodic Performance**: Calculation of aggregated monthly and annual returns to assess performance over different time horizons.
-   **Weekday Effect**: Analysis of average returns for each day of the week.
-   **Volatility Analysis**: Identification of the top 5 best and worst trading days to pinpoint periods of extreme market movement.

## 3. Technologies Used
-   Python 3
-   Pandas
-   NumPy
-   Matplotlib & Seaborn
-   JupyterLab


## 4. Setup and Usage
To run this analysis on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the analysis:**
    Launch Jupyter Lab and open the `main_analysis.ipynb` notebook located in the `notebooks/` folder.
    ```bash
    jupyter lab
    ```

## 5. Data Source
The datasets for S&P 500 and EURO STOXX 50 were originally sourced from the "Complete-Financial-Data" collection and made available via Google Drive. For reproducibility, the raw CSV files are included in the `data/` directory of this repository.

## 6. License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
