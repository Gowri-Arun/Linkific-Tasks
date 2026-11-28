# Day 12: Model Evaluation

## Setup

This evaluation repeats Day 11 exactly: the scikit-learn Breast Cancer Wisconsin dataset, an 80/20 stratified split with `random_state=42`, scaled Logistic Regression (`max_iter=1000`, `random_state=42`), and an unscaled Decision Tree (`max_depth=4`, `random_state=42`).

The dataset encodes malignant as `0` and benign as `1`. This report defines malignant as the positive class for cancer-risk analysis.

## Results

| Model | Accuracy | Malignant precision | Malignant recall | Malignant F1 | FP | FN |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Logistic Regression | 98.25% | 97.62% | 97.62% | 97.62% | 1 | 1 |
| Decision Tree | 93.86% | 90.70% | 92.86% | 91.76% | 4 | 3 |

The complete class-specific values and counts are in `performance_report.csv`.

## Confusion Matrix Terms

- TP: an actual malignant case predicted malignant.
- TN: an actual benign case predicted benign.
- FP: an actual benign case predicted malignant, creating a false alarm.
- FN: an actual malignant case predicted benign, missing a cancer case.

The notebook displays labelled heatmaps with actual classes on rows and predicted classes on columns.

## Interpretation

Logistic Regression has fewer false positives (1 vs. 4) and false negatives (1 vs. 3) than the Decision Tree on this test split. Malignant recall is particularly important because a false negative can delay attention to a malignant case. Raising recall can create more false positives and reduce precision, so a cancer-risk decision should consider both missed cases and false alarms.

## Run

Open `model_evaluation.ipynb` and run all cells. It recreates `performance_report.csv` from the computed test results.
