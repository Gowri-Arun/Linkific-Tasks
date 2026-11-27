# Day 11: Classification Using Logistic Regression and Decision Tree

## Learning Objectives

- Load a built-in classification dataset with scikit-learn.
- Prepare reproducible training and testing data.
- Train and compare Logistic Regression and Decision Tree classifiers.
- Evaluate classification results with accuracy, precision, recall, F1-score, and confusion matrices.

## Dataset

This task uses scikit-learn's built-in Breast Cancer Wisconsin dataset. It has 569 samples, 30 numeric features calculated from breast mass images, and a binary target. Target `0` means malignant and target `1` means benign.

## Logistic Regression vs Decision Tree

Logistic Regression is a linear classifier that estimates the probability of each class. It benefits from feature scaling because its optimization and coefficients are affected by feature ranges. A Decision Tree splits data into rule-based branches and does not require feature scaling. The tree depth is limited to 4 to keep the model simpler.

## Train-Test Split and Preprocessing

The data is split into 80% training data and 20% testing data using `random_state=42` and `stratify=y`. Both models use this exact same split. `StandardScaler` is fitted only on the training features and then used to transform both feature sets, which prevents information from the test set leaking into training. Scaling gives every feature a comparable range for Logistic Regression. The Decision Tree uses the unscaled features.

## Accuracy Comparison

| Model | Accuracy |
| --- | --- |
| Logistic Regression | 98.25% |
| Decision Tree | 93.86% |

Logistic Regression had the higher accuracy for this split. The generated `accuracy_comparison.csv` contains the exact computed values.

## Additional Evaluation Metrics

The notebook reports precision, recall, and F1-score for positive class `1`, which is benign. It also displays confusion matrices. Precision measures how often predicted benign cases are actually benign, recall measures how many actual benign cases are found, and F1-score balances precision and recall.

| Model | Precision | Recall | F1-score |
| --- | --- | --- | --- |
| Logistic Regression | 98.61% | 98.61% | 98.61% |
| Decision Tree | 95.77% | 94.44% | 95.10% |

## Cross-Validation Results

Five-fold stratified cross-validation uses `shuffle=True` and `random_state=42`. Logistic Regression is evaluated in a pipeline that fits `StandardScaler` separately within each training fold, preventing preprocessing leakage.

| Model | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean | Standard Deviation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Logistic Regression | 97.37% | 94.74% | 96.49% | 99.12% | 99.12% | 97.37% | 1.66% |
| Decision Tree | 95.61% | 86.84% | 92.11% | 92.98% | 93.81% | 92.27% | 2.95% |

## Observations

1. Logistic Regression achieved 98.25% testing accuracy, compared with 93.86% for the Decision Tree.
2. Logistic Regression made 2 false predictions, while the Decision Tree made 7.
3. Logistic Regression had a 0.66 percentage-point train-test accuracy gap (98.90% training, 98.25% testing).
4. Across five folds, Logistic Regression averaged 97.37% with a 1.66% standard deviation, while the Decision Tree averaged 92.27% with a 2.95% standard deviation.
5. The Decision Tree had a 4.82 percentage-point train-test accuracy gap (98.68% training, 93.86% testing), and neither the holdout nor cross-validation results make either model universally better.

## Limitations and Conclusion

The train-test measurements describe one stratified split and may change with another split. Cross-validation provides more evidence across five partitions, but it is still limited to this dataset and model configuration. Accuracy alone does not show the types or consequences of false predictions, so the additional metrics and confusion matrices are important. Neither model is universally better; the appropriate model depends on the data, validation results, and application requirements.

## Run Instructions

1. Open `classification.ipynb` in Jupyter Notebook or JupyterLab.
2. Run all cells from top to bottom.
3. Review the printed metrics and tables.
4. The notebook writes `accuracy_comparison.csv` in the Day-11 folder.
