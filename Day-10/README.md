# Day 10: Linear Regression for Temperature Prediction

## Objective

Predict `temperature_c` from weather measurements, compare the original linear regression baseline with a mean dummy benchmark, and assess whether seasonal month features improve the result.

## Dataset

The notebook reads `../Day-8/cleaned_weather.csv`, which contains 96,429 cleaned hourly weather observations. The baseline model uses these numerical features:

- `humidity`
- `wind_speed_km_h`
- `wind_bearing_degrees`
- `visibility_km`
- `pressure_millibars`

`apparent_temperature_c` is not used because it is derived from temperature and would leak information about the target.

The enhanced model also extracts the month from `formatted_date` and represents it as cyclical sine and cosine features. This represents the annual cycle without treating December and January as far apart.

## Model and Split

The notebook uses scikit-learn's `LinearRegression` and `DummyRegressor(strategy='mean')`. It removes any remaining missing or infinite values from the selected modeling columns, then creates one `train_test_split` with `test_size=0.2` and `random_state=42`. All three models use the same training and test rows.

This is a same-observation prediction exercise rather than future forecasting. The randomized split does not demonstrate future forecasting capability. `StandardScaler` is fitted only on the training data for the standardized coefficient comparison.

## Analysis Included

- Correlation heatmap for the numerical weather features and temperature.
- Raw and standardized baseline regression coefficients.
- Dummy mean, baseline linear regression, and seasonal linear regression comparison.
- MAE reduction from the seasonal features.
- Baseline actual-versus-predicted plot and seasonal-model residual plot.

## Run the Notebook

1. Open a terminal in the `Day-10` folder.
2. Install dependencies if needed: `python -m pip install pandas numpy matplotlib scikit-learn notebook`.
3. Start Jupyter with `jupyter notebook`.
4. Open `linear_regression.ipynb` and run all cells from top to bottom.
5. The notebook creates `prediction_results.csv` in `Day-10`.

## Results

Using the same reproducible test split, the models produced:

- Dummy mean model: MAE 7.9540 C, RMSE 9.5759 C, R2 -0.0000
- Baseline Linear Regression: MAE 5.7063 C, RMSE 7.1163 C, R2 0.4477
- Seasonal Linear Regression: MAE 3.3341 C, RMSE 4.2414 C, R2 0.8038

The seasonal month features reduce MAE by 41.57% versus the baseline. The CSV includes actual temperatures plus dummy, baseline, and seasonal predictions and errors for every test observation.
