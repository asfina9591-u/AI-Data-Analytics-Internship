# ============================================================
# WEEK 4 - SUPERVISED LEARNING MODEL IMPLEMENTATION
# Telco Customer Churn Prediction
# ============================================================

# -----------------------------
# 1. IMPORT LIBRARIES
# -----------------------------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)


# ============================================================
# 2. CREATE OUTPUT FOLDER
# ============================================================

OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("WEEK 4 - SUPERVISED LEARNING")
print("TELCO CUSTOMER CHURN PREDICTION")
print("=" * 70)


# ============================================================
# 3. LOAD DATASET
# ============================================================

DATA_PATH = "Data/cleaned_telco_churn.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 4. BASIC DATA INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDataset Shape:")
print(df.shape)


# ============================================================
# 5. DEFINE TARGET VARIABLE
# ============================================================

TARGET = "Churn Label"

if TARGET not in df.columns:
    raise ValueError(
        f"Target column '{TARGET}' was not found in the dataset."
    )

print("\nTarget Variable:")
print(TARGET)

print("\nTarget Distribution:")
print(df[TARGET].value_counts())


# ============================================================
# 6. REMOVE UNNECESSARY COLUMNS
# ============================================================

# CustomerID is an identifier and should not be used
# as a predictive feature.

columns_to_drop = []

for column in ["CustomerID", "Churn Value"]:
    if column in df.columns:
        columns_to_drop.append(column)

X = df.drop(columns=[TARGET] + columns_to_drop)
y = df[TARGET]


# ============================================================
# 7. CONVERT TARGET TO BINARY
# ============================================================

if y.dtype == "object":

    y = (
        y.astype(str)
        .str.strip()
        .str.lower()
        .map({
            "yes": 1,
            "no": 0,
            "true": 1,
            "false": 0,
            "1": 1,
            "0": 0
        })
    )

elif set(y.dropna().unique()).issubset({0, 1}):
    y = y.astype(int)

else:
    raise ValueError(
        "Target variable could not be converted to binary values."
    )


# Remove rows where target conversion produced missing values

valid_rows = y.notna()

X = X.loc[valid_rows].copy()
y = y.loc[valid_rows].astype(int)


print("\nTarget after encoding:")
print(y.value_counts())


# ============================================================
# 8. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numeric_features = X.select_dtypes(
    include=["int64", "float64", "int32", "float32"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("\nNumerical Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)


# ============================================================
# 9. PREPROCESSING
# ============================================================

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)


categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "onehot",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )
        )
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)


# ============================================================
# 10. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\n" + "=" * 70)
print("TRAIN-TEST SPLIT")
print("=" * 70)

print("\nTraining Samples:")
print(X_train.shape[0])

print("\nTesting Samples:")
print(X_test.shape[0])


# ============================================================
# 11. RANDOM FOREST MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)


# ============================================================
# 12. CREATE COMPLETE PIPELINE
# ============================================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ============================================================
# 13. TRAIN MODEL
# ============================================================

print("\n" + "=" * 70)
print("TRAINING RANDOM FOREST MODEL")
print("=" * 70)

pipeline.fit(X_train, y_train)

print("\nModel training completed successfully!")


# ============================================================
# 14. MAKE PREDICTIONS
# ============================================================

y_pred = pipeline.predict(X_test)


# ============================================================
# 15. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)


print("\n" + "=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

print(f"\nAccuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")


# ============================================================
# 16. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["No Churn", "Churn"],
        zero_division=0
    )
)


# ============================================================
# 17. SAVE MODEL METRICS
# ============================================================

metrics_df = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1
    ]
})

metrics_path = os.path.join(
    OUTPUT_DIR,
    "model_metrics.csv"
)

metrics_df.to_csv(
    metrics_path,
    index=False
)

print("\nSaved:")
print(metrics_path)


# ============================================================
# 18. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)


plt.figure(figsize=(7, 6))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Churn", "Churn"]
)

disp.plot()

plt.title("Confusion Matrix - Random Forest")

plt.tight_layout()

confusion_path = os.path.join(
    OUTPUT_DIR,
    "confusion_matrix.png"
)

plt.savefig(
    confusion_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSaved:")
print(confusion_path)


# ============================================================
# 19. CROSS-VALIDATION
# ============================================================

print("\n" + "=" * 70)
print("CROSS-VALIDATION")
print("=" * 70)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

cv_scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

print("\nCross-Validation Scores:")

for i, score in enumerate(cv_scores, start=1):
    print(f"Fold {i}: {score:.4f}")


mean_cv_accuracy = cv_scores.mean()

print(
    f"\nMean Cross-Validation Accuracy: "
    f"{mean_cv_accuracy:.4f}"
)


# ============================================================
# 20. SAVE CROSS-VALIDATION RESULTS
# ============================================================

cv_df = pd.DataFrame({
    "Fold": [
        "Fold 1",
        "Fold 2",
        "Fold 3",
        "Fold 4",
        "Fold 5"
    ],
    "Accuracy": cv_scores
})

cv_df.loc[len(cv_df)] = [
    "Mean",
    mean_cv_accuracy
]

cv_path = os.path.join(
    OUTPUT_DIR,
    "cross_validation_results.csv"
)

cv_df.to_csv(
    cv_path,
    index=False
)

print("\nSaved:")
print(cv_path)


# ============================================================
# 21. FEATURE IMPORTANCE
# ============================================================

print("\n" + "=" * 70)
print("FEATURE IMPORTANCE")
print("=" * 70)


# Get trained Random Forest model

trained_model = pipeline.named_steps["model"]

# Get preprocessing step

trained_preprocessor = pipeline.named_steps[
    "preprocessor"
]


# Get transformed feature names

feature_names = (
    trained_preprocessor
    .get_feature_names_out()
)


# Get feature importance values

importance_values = (
    trained_model.feature_importances_
)


importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance_values
})


importance_df = (
    importance_df
    .sort_values(
        by="Importance",
        ascending=False
    )
    .reset_index(drop=True)
)


print("\nTop 10 Important Features:")

print(
    importance_df
    .head(10)
    .to_string(index=False)
)


# ============================================================
# 22. SAVE FEATURE IMPORTANCE CSV
# ============================================================

feature_importance_csv = os.path.join(
    OUTPUT_DIR,
    "feature_importance.csv"
)

importance_df.to_csv(
    feature_importance_csv,
    index=False
)

print("\nSaved:")
print(feature_importance_csv)


# ============================================================
# 23. FEATURE IMPORTANCE VISUALIZATION
# ============================================================

top_features = importance_df.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"][::-1],
    top_features["Importance"][::-1]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title(
    "Top 10 Feature Importances - Random Forest"
)

plt.tight_layout()

feature_plot_path = os.path.join(
    OUTPUT_DIR,
    "feature_importance.png"
)

plt.savefig(
    feature_plot_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nSaved:")
print(feature_plot_path)


# ============================================================
# 24. SAVE PREDICTIONS
# ============================================================

prediction_df = X_test.copy()

prediction_df["Actual_Churn"] = y_test.values

prediction_df["Predicted_Churn"] = y_pred

prediction_path = os.path.join(
    OUTPUT_DIR,
    "model_predictions.csv"
)

prediction_df.to_csv(
    prediction_path,
    index=False
)

print("\nSaved:")
print(prediction_path)


# ============================================================
# 25. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("WEEK 4 ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)

print("\nTraining Samples:")
print(X_train.shape[0])

print("\nTesting Samples:")
print(X_test.shape[0])

print("\nModel: Random Forest Classifier")

print(f"\nAccuracy: {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall: {recall:.4f}")

print(f"F1 Score: {f1:.4f}")

print(
    f"\nMean Cross-Validation Accuracy: "
    f"{mean_cv_accuracy:.4f}"
)

print("\nOutput Files Created:")

print("1. confusion_matrix.png")
print("2. feature_importance.png")
print("3. feature_importance.csv")
print("4. model_metrics.csv")
print("5. cross_validation_results.csv")
print("6. model_predictions.csv")

print("\nAll files are saved inside:")
print("Week4_Supervised_Learning/outputs/")

print("\n" + "=" * 70)