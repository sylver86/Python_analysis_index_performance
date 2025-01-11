# Analysis of the Performance of S&P 500 and EURO STOXX 50 Indices

📊 **Project Objective:**

Welcome to the analysis of **S&P 500** and **EURO STOXX 50** indices. This project aims to provide actionable insights by analyzing 10 years of historical data, highlighting trends, and supporting strategic investment decisions.

💼 **Project Description:**

This project is developed for **Global Investment Insights**, a financial consulting firm specializing in detailed analysis of stock market performance. The focus is on two fundamental indices:

- **S&P 500**: Representing the U.S. stock market.
- **EURO STOXX 50**: Representing the European stock market.

The objective is to study the performance of these indices over the last 10 years to derive valuable insights that can assist investors in making strategic decisions. By analyzing daily and monthly returns, identifying days of high volatility, and calculating average daily trading volumes, this project provides a comprehensive overview of the historical trends of two major global indices.

The analysis offers investors a clear and detailed view of:
- Historical trends and performance.
- Daily and monthly returns to guide investment strategies.
- High-volatility days to help mitigate risks.
- Average trading volumes to gauge investor interest and market activity.

---

## Key Features

📈 **Percentage Returns:**
  - Calculates monthly and annual percentage returns to evaluate performance over time.

📅 **Weekday Analysis:**
  - Determines average daily returns for each weekday, uncovering patterns or anomalies in market behavior.

⚡ **Volatility Insights:**
  - Identifies days with the highest and lowest daily returns, highlighting market volatility.

💰 **Volume Analysis:**
  - Analyzes the average daily trading volume to gauge investor activity and interest in both indices.

---

## Project Highlights

🔍 **Data Engineering:**
  - Processed and cleaned large datasets, ensuring data integrity and usability.

📚 **Data Analysis:**
  - Extracted meaningful metrics like percentage returns and average volumes.

🧠 **Problem Solving:**
  - Applied analytical methodologies to address business-relevant questions.

⚙️ **Technologies Used:**
  - **Python**, **Pandas**, **NumPy**

---

## Dataset

The datasets used can be downloaded. They include:

- **Date**: Observation date.
- **Open**: Opening price.
- **High**: Daily high price.
- **Low**: Daily low price.
- **Close**: Closing price.
- **Volume**: Number of trades executed during the day.

---

## Methodology

🔄 **Step-by-Step Process:**

1. **Data Loading and Exploration:**
   - Used **Pandas** to import datasets for both indices.
   - Explored their structure, including checking for missing values and understanding the data distribution.

2. **Data Cleaning:**
   - Employed **Pandas** to handle missing values using forward filling.
   - Ensured the dataset was ready for analysis by validating data types and removing inconsistencies.

3. **Percentage Return Calculation:**
   - Calculated daily, monthly, and annual percentage returns using **Pandas** and the formula:
     ```
     Return = ((Current Close - Previous Close) / Previous Close) * 100
     ```

4. **Weekday Return Analysis:**
   - Grouped data by weekdays using **Pandas**' `groupby` method.
   - Calculated average daily returns to identify patterns associated with specific days of the week.

5. **Volatility Detection:**
   - Identified the days with the highest and lowest daily returns using **Pandas** to sort and filter data.
   - Highlighted periods of extreme volatility for each index.

6. **Volume Analysis:**
   - Used **Pandas** to compute average daily trading volumes.
   - Analyzed investor interest and identified periods of high market activity.

7. **Insights Generation:**
   - Interpreted results using **Pandas** and statistical calculations.
   - Provided actionable insights for strategic investment decisions by investors.

---

## Explore More

🔗 **GitHub Repository:**
Dive into the codebase (file .ipynb).

---

**Author:**
- Name: [Eugenio Pasqua]
- Email: [eugenix86@gmail.com]
- LinkedIn: [LinkedIn Profile]([https://www.linkedin.com](https://www.linkedin.com/in/genxdata58296/))
