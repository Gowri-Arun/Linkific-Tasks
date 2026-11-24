# Day 8: Data Preprocessing and Data Cleaning

## Dataset

This project reuses the Weather History dataset from `Day-7/weatherHistory.csv`. It contains historical weather observations, including date, temperature, humidity, wind, visibility, pressure, and weather descriptions.

## Preprocessing Steps

- Inspects the dataset's first rows, shape, columns, data types, and missing values.
- Removes only exact duplicate records.
- Renames columns to lowercase snake_case.
- Converts the date column with safe error handling and converts weather measurements to numeric values.
- Fills missing `precip_type` values with the mode.
- Checks numerical columns individually and would fill missing values with the median only when needed.
- Leaves complete text columns and any invalid dates unchanged rather than creating values that were not present in the dataset.
- Saves the cleaned data as `cleaned_weather.csv` without an index.

## Run the Notebook

1. Install the required packages if needed: `python -m pip install pandas numpy notebook`.
2. Open a terminal in the `Day-8` folder and run `jupyter notebook`.
3. Open `data_cleaning.ipynb` and run all cells from top to bottom.
4. Confirm that `cleaned_weather.csv` is created in `Day-8`.
