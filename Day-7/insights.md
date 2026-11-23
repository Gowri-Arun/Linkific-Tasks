# Analysis Insights

- The dataset contains 96,453 hourly weather observations from 2005-12-31 23:00 UTC through 2016-12-31 22:00 UTC.
- The mean recorded temperature is 11.93 C. Temperatures range from -21.82 C to 39.91 C.
- Average humidity is 0.735 on the dataset's 0-to-1 scale. Humidity ranges from 0.00 to 1.00.
- July is the warmest calendar month by average temperature at 22.97 C, followed by August at 22.34 C.
- January is the coolest calendar month by average temperature at 0.82 C; December is the next coolest at 1.63 C.
- Temperature and apparent temperature have a very strong positive correlation of 0.993, so they move closely together in these observations.
- Temperature and humidity have a moderate negative correlation of -0.632, while temperature and visibility have a moderate positive correlation of 0.393. These correlations describe associations only and do not establish causes.
- `Precip Type` is the only column with missing values (517). The dataset also has 24 exact duplicate rows; all records were retained because repeated weather measurements can be valid observations.
