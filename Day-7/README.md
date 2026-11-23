# Day 7: Weather Data Analysis - Exploring Temporal Patterns

## Objective

Explore historical weather observations with Pandas, NumPy, Matplotlib, and Seaborn. The notebook introduces dataset inspection, cleaning decisions, time features, trailing rolling averages, and four clear visualizations. No machine-learning model is used.

## Dataset

- Source: [Weather Dataset on Kaggle](https://www.kaggle.com/datasets/muthuj7/weather-dataset)
- Expected file: `weatherHistory.csv`
- The CSV is stored in this `Day-7` folder beside `weather_analysis.ipynb`.

## Technologies

Python, Jupyter Notebook, Pandas, NumPy, Matplotlib, and Seaborn.

## Setup and Execution

1. Download the dataset from the Kaggle link above while signed in to Kaggle if requested.
2. Extract `weatherHistory.csv` into `Day-7/`.
3. Open a PowerShell terminal in `Day-7/` and install dependencies if needed: `python -m pip install pandas numpy matplotlib seaborn notebook`.
4. Start Jupyter with `jupyter notebook`.
5. Open `weather_analysis.ipynb` and run all cells from top to bottom.
6. Confirm that four PNG files appear in `screenshots/` and review the calculated findings in `insights.md`.

## Analysis and Visualizations

The notebook displays the head, tail, shape, `info()`, `describe()`, columns, and data types. It checks missing values and exact duplicates without removing observations simply because weather measurements match.

It parses `Formatted Date` with `utc=True`, sorts timestamps, extracts year and month, calculates temperature and humidity summaries, computes monthly average temperatures, and creates a trailing 30-day rolling temperature average. A trailing window avoids using future readings to describe past conditions. The cleaning check found 517 missing `Precip Type` values and 24 exact duplicate rows. All rows are retained: no values are imputed, and repeated measurements can be valid weather observations.

The generated charts are:

- `screenshots/temperature_trend.png`: recorded temperature and 30-day trailing average.
- `screenshots/monthly_temperature.png`: average temperature by calendar month.
- `screenshots/humidity_distribution.png`: histogram of humidity values.
- `screenshots/correlation_heatmap.png`: correlations among selected numerical weather features.

## Key Findings and Limitations

The executed dataset has 96,453 observations from late 2005 through 2016. Mean temperature is 11.93 C, with values from -21.82 C to 39.91 C, and mean humidity is 0.735. July is the warmest average month (22.97 C), while January is the coolest (0.82 C). Temperature is strongly positively associated with apparent temperature (correlation 0.993) and moderately negatively associated with humidity (correlation -0.632). See `insights.md` for all evidence-based findings.

Correlation measures association, not causation. The dataset's location, collection process, time coverage, missing precipitation-type records, and duplicate records may limit how broadly the findings generalize.

## Demo Script (2-5 Minutes)

"This Day 7 project explores temporal patterns in the Weather History dataset. I use Pandas to load and inspect the CSV, including its columns, data types, summary statistics, missing values, and exact duplicates. I report duplicates but do not delete records only because measurements match, since they may be valid weather observations at different times.

Next, I convert the `Formatted Date` column to a consistent UTC timezone and sort it so every time-based calculation is chronological. I extract year and month, calculate average, minimum, and maximum temperature, and calculate average humidity. I also group the observations by calendar month to compare their average temperatures.

For temporal analysis, I calculate a 30-day trailing rolling average. It smooths short daily variation and makes longer temperature patterns easier to see. Because the window is trailing, it uses only the current and previous observations rather than future readings.

The first chart compares the recorded temperature with the rolling average. The second shows the average temperature by month. The third shows how humidity values are distributed. The last chart is a correlation heatmap for numerical weather features. In the results, July is the warmest average month at 22.97 C and January is the coolest at 0.82 C. I explain correlations as relationships in this dataset, not proof that one variable causes another. Finally, I summarize the exact values in the insights file and note the dataset limitations."
