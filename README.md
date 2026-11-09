# Disease Prediction from Medical Data

## Project Overview
This project uses Machine Learning to predict the presence of heart disease based on medical data.

The main goal is to train and evaluate different classification models and identify the best-performing model.

## Dataset
- **Source:** UCI Machine Learning Repository
- **Dataset:** Heart Disease
- **Samples:** 303
- **Features:** 13
- **Target:** 
  - `0` – No heart disease
  - `1` – Heart disease

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

## Project Workflow
1. Data Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Train-Test Split
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Feature Importance Analysis
9. ROC Curve and AUC
10. Model Saving and Testing

## Machine Learning Models
Three classification algorithms were trained:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

## Model Evaluation Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 86.89% | 81.25% | 92.86% | 86.67% |
| Random Forest | 88.52% | 81.82% | 96.43% | 88.52% |
| SVM | 85.25% | 80.65% | 89.29% | 84.75% |

Random Forest achieved the best results on the current test split.

## Saved Models
The trained model and scaler are saved in the `models/` directory:

- `heart_disease_model.pkl`
- `scaler.pkl`

## How to Run

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the data download script:

```bash
python src/download_data.py
```

4. Open the notebook:

```text
notebooks/01_eda.ipynb
```

## Disclaimer
This project is for educational purposes only. It is not intended for clinical use or medical diagnosis.
