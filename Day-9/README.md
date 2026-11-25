# Day 9: Exploratory Data Analysis (EDA)

## Learning Objectives

- Inspect a cleaned dataset's structure, data types, missing values, and duplicate records.
- Use descriptive statistics to understand numerical weather measurements.
- Analyse temporal trends, distributions, correlations, and potential outliers.
- Communicate evidence-based business insights with clear visualizations.

## Dataset

- Input: `../Day-8/cleaned_weather.csv`
- The cleaned weather dataset contains 96,429 hourly observations from 2005-12-31 to 2016-12-31.
- It includes timestamps, weather summaries, temperature, apparent temperature, humidity, wind, visibility, pressure, and daily summaries.
- The notebook reads this file only; it does not duplicate or modify the dataset.

## Tools and Libraries

Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, and Seaborn.

## Analysis Performed

- Displays the dataset shape, columns, data types, missing-value counts, duplicate count, and descriptive statistics.
- Parses `formatted_date` as timezone-aware UTC and creates month and meteorological season fields for analysis.
- Analyses monthly and seasonal temperature patterns, temperature distribution, temperature-humidity association, and numerical correlations.
- Uses the IQR rule to identify potentially unusual temperature records without treating them automatically as errors.

## Visualizations

1. Monthly average temperature line chart.
2. Temperature distribution histogram.
3. Temperature versus humidity scatter plot using a reproducible 5,000-row sample.
4. Seasonal temperature box plot.
5. Numerical-feature correlation heatmap.

## Key Findings

- The cleaned data has no missing values and no exact duplicate records.
- July is the warmest average month at 22.97 C, while January is the coolest at 0.82 C.
- Summer averages 22.02 C and winter averages 1.52 C.
- Temperature and humidity have a moderate negative Pearson correlation of -0.632.
- The IQR rule flags 44 unusually cold records (0.046%), ranging from -21.82 C to -16.67 C.

## Business Insights

- Plan weather-sensitive staffing, stock, and events around the 22.15 C difference between July and January average temperatures.
- Prepare heating, maintenance, and operational capacity for the 20.51 C difference between average winter and summer temperatures.
- Monitor temperature and humidity together in comfort or operations dashboards, while treating their -0.632 correlation as association rather than causation.
- Evaluate whether both measured and apparent temperature are necessary for compact reporting because their correlation is 0.993.
- Keep targeted extreme-cold safety and contingency procedures for the rare readings below the IQR lower bound.

## Execution Instructions

1. Open a terminal in the `Day-9` folder.
2. Install packages if needed: `python -m pip install pandas numpy matplotlib seaborn notebook`.
3. Start Jupyter: `jupyter notebook`.
4. Open `exploratory_data_analysis.ipynb` and run all cells from top to bottom.
5. Confirm that all five visualizations display and that `../Day-8/cleaned_weather.csv` is available.

## Note

Correlation describes association in this dataset and does not establish causation. Results may not generalize beyond the data's location, period, and collection process.
