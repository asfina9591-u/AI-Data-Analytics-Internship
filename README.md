# AI Data Analytics Internship

This repository contains my work, assignments, projects, reports, datasets, Python scripts, notebooks, visualizations, and analysis completed during my **AI/Data Analytics Internship**.

The internship focuses on practical applications of:

- Data Acquisition
- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Data Visualization
- Unsupervised Learning
- Clustering
- Supervised Learning
- Classification
- Feature Engineering
- Model Evaluation
- Cross-Validation
- Data-Driven Business Insights

---

# Internship Progress

| Week | Task | Status |
|---|---|---|
| Week 1 | Data Acquisition, Cleaning, and Preprocessing | ✅ Completed |
| Week 2 | Exploratory Data Analysis and Visualization | ✅ Completed |
| Week 3 | Unsupervised Learning and Clustering Analysis | ✅ Completed |
| Week 4 | Supervised Learning Model Implementation | ✅ Completed |
| Week 5 | Pending | ⏳ Pending |
| Week 6 | Pending | ⏳ Pending |

---

# Week 1 – Data Acquisition, Cleaning, and Preprocessing

## Objective

The objective of Week 1 was to acquire a publicly available dataset, understand its structure, identify data quality issues, clean the dataset, handle missing values, and prepare the data for further analysis and machine learning tasks.

The **Telco Customer Churn dataset** was selected for this task.

## Key Tasks

The following activities were performed:

- Loaded the dataset using Pandas
- Examined the dataset structure
- Checked the number of rows and columns
- Inspected data types
- Identified missing values
- Handled missing values
- Checked for duplicate records
- Examined numerical and categorical features
- Performed basic statistical analysis
- Cleaned inconsistent data
- Converted appropriate columns into suitable data types
- Performed preprocessing
- Saved the cleaned dataset
- Saved the preprocessed dataset

## Dataset

The Telco Customer Churn dataset contains information about customers of a telecommunications company.

Important variables include:

```text
Customer information
Gender
Senior Citizen
Partner
Dependents
Tenure
Phone Service
Internet Service
Contract
Payment Method
Monthly Charges
Total Charges
Churn
```

## Dataset Statistics

The cleaned dataset contained:

```text
Rows: 7043
Columns: 28
```

Important numerical statistics included:

```text
Average Tenure: 32.37 months
Average Monthly Charges: 64.30
Average Total Charges: 2279.27
```

## Deliverables

```text
Week1_Data_Cleaning_Preprocessing/
│
├── Week1_Data_Cleaning_Preprocessing.ipynb
├── Week1_Data_Cleaning_Preprocessing_Report.docx
├── customer_churn.csv.ipynb
├── cleaned_telco_churn.csv
├── preprocessed_telco_churn.csv
└── placeholder.txt
```

## Technologies and Libraries

```text
Python
Pandas
NumPy
Jupyter Notebook
Data Cleaning
Data Preprocessing
```

---

# Week 2 – Exploratory Data Analysis and Visualization

## Objective

The objective of Week 2 was to perform **Exploratory Data Analysis (EDA)** on the cleaned Telco Customer Churn dataset.

The purpose was to identify patterns, relationships, trends, and potential factors associated with customer churn.

## Key Tasks

The following analyses were performed:

- Dataset exploration
- Missing-value verification
- Statistical analysis
- Churn distribution analysis
- Contract versus churn analysis
- Tenure versus churn analysis
- Monthly charges versus churn analysis
- Internet service versus churn analysis
- Payment method versus churn analysis
- Correlation analysis
- Data visualization
- Business insight generation

## Analysis Performed

### Churn Distribution

The distribution of customers who churned and customers who remained was analyzed.

This helped understand the overall proportion of churned customers.

### Contract vs Churn

Customer churn was compared across different contract types.

This analysis helped identify whether customers with different contract durations exhibited different churn behavior.

### Tenure vs Churn

Customer tenure was analyzed to understand whether the length of the customer relationship affected churn.

### Monthly Charges vs Churn

Monthly charges were compared between customers who churned and customers who did not.

The analysis produced the following average values:

```text
Average Monthly Charges

Churn = No  → 61.27
Churn = Yes → 74.44
```

This indicated that customers with higher monthly charges showed higher average churn in the analyzed dataset.

### Internet Service vs Churn

Different internet service categories were compared with customer churn.

### Payment Method vs Churn

Different payment methods were analyzed to identify potential relationships with customer churn.

### Correlation Analysis

A correlation analysis was performed on numerical variables and visualized using a correlation heatmap.

## Visualizations

The Week 2 analysis included visualizations such as:

```text
Churn Distribution
Contract vs Churn
Tenure vs Churn
Monthly Charges vs Churn
Internet Service vs Churn
Payment Method vs Churn
Correlation Heatmap
```

## Deliverables

```text
Week2_EDA_and_Visualization/
│
├── Week2_EDA.py
├── Week 2 Task – Exploratory Data Analysis and Visualization.docx
├── cleaned_telco_churn.csv
├── preprocessed_telco_churn.csv
│
├── churn_distribution.png
├── contract_vs_churn.png
├── tenure_vs_churn.png
├── average_monthly_charges_by_churn.png
├── internet_service_vs_churn.png
├── payment_method_vs_churn.png
├── correlation_heatmap.png
└── placeholder.txt
```

## Technologies and Libraries

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Exploratory Data Analysis
Data Visualization
Correlation Analysis
```

---

# Week 3 – Unsupervised Learning and Clustering Analysis

## Objective

The objective of Week 3 was to apply **unsupervised learning techniques** to segment customers into meaningful groups.

A publicly available **Mall Customers dataset** was selected for the clustering task.

The primary technique used was **K-Means Clustering**.

## Dataset

The dataset contains information about mall customers including:

```text
CustomerID
Genre
Age
Annual Income (k$)
Spending Score (1-100)
```

## Selected Features

For clustering, the following numerical features were selected:

```text
Age
Annual Income (k$)
Spending Score (1-100)
```

The final feature matrix contained:

```text
Shape: (200, 3)
```

## Key Tasks

The following steps were performed:

- Loaded the Mall Customers dataset
- Inspected the dataset
- Checked data types
- Selected relevant clustering features
- Prepared numerical features
- Standardized the features
- Applied K-Means clustering
- Tested different values of K
- Used the Elbow Method
- Used Silhouette Analysis
- Selected the appropriate number of clusters
- Assigned customers to clusters
- Created cluster visualizations
- Analyzed cluster characteristics
- Generated business interpretations

## Clustering Method

The **K-Means Clustering algorithm** was selected because it is a commonly used unsupervised learning algorithm for customer segmentation.

The algorithm groups customers based on similarities in their:

```text
Age
Annual Income
Spending Score
```

## Cluster Analysis

The final clustering analysis produced **6 customer clusters**.

The cluster summary was:

```text
Cluster 0
Customers: 45
Average Age: 56.33
Average Income: 54.27
Average Spending: 49.07

Cluster 1
Customers: 39
Average Age: 26.79
Average Income: 57.10
Average Spending: 48.13

Cluster 2
Customers: 33
Average Age: 41.94
Average Income: 88.94
Average Spending: 16.97

Cluster 3
Customers: 39
Average Age: 32.69
Average Income: 86.54
Average Spending: 82.13

Cluster 4
Customers: 23
Average Age: 25.00
Average Income: 25.26
Average Spending: 77.61

Cluster 5
Customers: 21
Average Age: 45.52
Average Income: 26.29
Average Spending: 19.38
```

## Business Interpretation

The clusters represent different customer segments.

For example:

### Cluster 3 – High Income, High Spending

```text
Average Income: 86.54 k$
Average Spending Score: 82.13
```

This segment represents customers with high purchasing potential and high spending behavior.

### Cluster 2 – High Income, Low Spending

```text
Average Income: 88.94 k$
Average Spending Score: 16.97
```

These customers have high income but relatively low spending scores, making them a potential target for personalized promotions.

### Cluster 4 – Low Income, High Spending

```text
Average Income: 25.26 k$
Average Spending Score: 77.61
```

These customers have lower income but relatively high spending scores.

## Visualizations

The clustering analysis included visualizations such as:

```text
Age Distribution
Income Distribution
Spending Score Distribution
Age vs Spending Score
Income vs Spending Score
Cluster Distribution
Cluster Comparison
3D Cluster Visualization
Elbow Curve
Silhouette Score Analysis
```

## Deliverables

```text
Week-3-Unsupervised-Learning-Clustering/
│
├── data/
│   └── Mall_Customers.csv
│
├── notebooks/
│   └── Week3_Clustering_Analysis.ipynb
│
├── outputs/
│   ├── age_distribution.png
│   ├── income_distribution.png
│   ├── spending_score_distribution.png
│   ├── age_vs_spending_clusters.png
│   ├── income_vs_spending_clusters.png
│   ├── cluster_distribution.png
│   ├── cluster_business_comparison.png
│   ├── clusters_3d.png
│   ├── elbow_curve.png
│   ├── silhouette_scores.png
│   ├── customer_clusters.csv
│   ├── cluster_summary.csv
│   └── final_cluster_profile.csv
│
└── Week3_Clustering_Report.docx
```

## Technologies and Libraries

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
K-Means Clustering
Feature Scaling
Elbow Method
Silhouette Analysis
```

---

# Week 4 – Supervised Learning Model Implementation

## Objective

The objective of Week 4 was to design and implement a **supervised machine learning model** using Python and Scikit-learn.

A **classification problem** was selected using the Telco Customer Churn dataset.

The goal was to predict whether a customer is likely to churn.

## Problem Definition

The machine learning problem was defined as a binary classification problem.

The target variable was:

```text
Churn Label
```

The target classes were:

```text
0 → No Churn
1 → Churn
```

The model learns patterns from customer information and predicts whether a customer is likely to churn.

## Dataset

The Telco Customer Churn dataset was used for the supervised learning task.

The dataset contains customer-related features such as:

```text
Gender
Age
Senior Citizen
Partner
Dependents
Tenure Months
Phone Service
Internet Service
Contract
Payment Method
Monthly Charges
Total Charges
CLTV
```

## Data Preparation

The following preprocessing steps were performed:

- Loaded the cleaned dataset
- Identified the target variable
- Removed unnecessary identifier columns
- Converted the target into binary values
- Identified numerical features
- Identified categorical features
- Handled missing values
- Applied numerical preprocessing
- Applied categorical preprocessing
- Encoded categorical variables
- Scaled numerical features
- Prepared the final machine learning pipeline

## Feature Engineering and Preprocessing

Numerical features were processed using:

```text
Median Imputation
Standard Scaling
```

Categorical features were processed using:

```text
Most Frequent Imputation
One-Hot Encoding
```

The preprocessing was implemented using Scikit-learn's:

```text
ColumnTransformer
Pipeline
SimpleImputer
StandardScaler
OneHotEncoder
```

## Train-Test Split

The dataset was divided into training and testing sets.

The model was trained using the training dataset and evaluated using the unseen testing dataset.

The split used:

```text
Training Data: 80%
Testing Data: 20%
```

Stratified splitting was used to preserve the class distribution.

## Machine Learning Model

A **Random Forest Classifier** was selected as the supervised learning algorithm.

Random Forest was selected because it:

- Handles nonlinear relationships
- Works with multiple feature types
- Can capture complex patterns
- Provides feature importance
- Is relatively robust to noise
- Performs well for classification tasks

The model was configured using:

```text
Number of Estimators: 200
Random State: 42
Class Weight: Balanced
```

## Model Training

The Random Forest model was trained using the prepared training data.

The complete workflow was implemented using a Scikit-learn Pipeline combining:

```text
Data Preprocessing
        ↓
Feature Transformation
        ↓
Random Forest Classifier
        ↓
Prediction
        ↓
Evaluation
```

## Model Evaluation

The model was evaluated using the following metrics:

```text
Accuracy
Precision
Recall
F1 Score
```

A confusion matrix was also generated to analyze correct and incorrect predictions.

## Cross-Validation

To evaluate the stability of the model, **5-fold Stratified Cross-Validation** was performed.

The cross-validation process evaluated the model across multiple subsets of the dataset.

The following results were saved:

```text
Fold 1 Accuracy
Fold 2 Accuracy
Fold 3 Accuracy
Fold 4 Accuracy
Fold 5 Accuracy
Mean Cross-Validation Accuracy
```

## Feature Importance

Random Forest feature importance was analyzed to identify the features that contributed most to the model's predictions.

Important features included:

```text
Tenure Months
Total Charges
Monthly Charges
Contract
CLTV
```

Feature importance was visualized using a bar chart.

## Output Files

The following outputs were generated:

```text
confusion_matrix.png
cross_validation_results.csv
cross_validation_scores.csv
feature_importance.csv
feature_importance.png
model_metrics.csv
model_predictions.csv
```

## Deliverables

```text
Week4_Supervised_Learning/
│
├── Data/
│   └── cleaned_telco_churn.csv
│
├── outputs/
│   ├── confusion_matrix.png
│   ├── cross_validation_results.csv
│   ├── cross_validation_scores.csv
│   ├── feature_importance.csv
│   ├── feature_importance.png
│   ├── model_metrics.csv
│   └── model_predictions.csv
│
├── Week4_Supervised_Learning.py
└── Week4_Supervised_Learning_Report.docx
```

## Technologies and Libraries

```text
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Random Forest
Classification
Feature Engineering
Train-Test Split
Cross-Validation
Confusion Matrix
Feature Importance
Model Evaluation
```

---

# Week 5 – Pending

## Status

```text
⏳ Pending
```

The Week 5 assignment will be added to this repository after completion.

The following sections will be updated once the task is completed:

```text
Objective
Dataset
Data Preparation
Methodology
Implementation
Analysis
Results
Evaluation
Visualizations
Business / Research Insights
Deliverables
Technologies Used
```

---

# Week 6 – Pending

## Status

```text
⏳ Pending
```

The Week 6 assignment will be added to this repository after completion.

The following sections will be updated once the task is completed:

```text
Objective
Dataset
Data Preparation
Methodology
Implementation
Analysis
Results
Evaluation
Visualizations
Business / Research Insights
Deliverables
Technologies Used
```

---

# Technologies Used

The following technologies and Python libraries are being used throughout the internship:

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook
Visual Studio Code
Git
GitHub
```

---

# Repository Structure

The repository is organized according to the internship weeks:

```text
AI-Data-Analytics-Internship/
│
├── Week1_Data_Cleaning_Preprocessing/
│   ├── Dataset
│   ├── Notebook
│   ├── Cleaned Data
│   ├── Preprocessed Data
│   └── Report
│
├── Week2_EDA_and_Visualization/
│   ├── Python Script
│   ├── Dataset
│   ├── Visualizations
│   └── Report
│
├── Week-3-Unsupervised-Learning-Clustering/
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   └── Report
│
├── Week4_Supervised_Learning/
│   ├── Data/
│   ├── outputs/
│   ├── Python Script
│   └── Report
│
├── Week5/
│
├── Week6/
│
└── README.md
```

---

# Overall Internship Progress

```text
Week 1  ████████████████████ 100% ✅
Week 2  ████████████████████ 100% ✅
Week 3  ████████████████████ 100% ✅
Week 4  ████████████████████ 100% ✅
Week 5  ░░░░░░░░░░░░░░░░░░░░   0% ⏳
Week 6  ░░░░░░░░░░░░░░░░░░░░   0% ⏳
```

## Current Progress

```text
4 / 6 Weeks Completed

Overall Progress: 66.7%
```

---

# Learning Outcomes

Through the completed assignments, I have gained practical experience in:

```text
Data Acquisition
Data Cleaning
Data Preprocessing
Exploratory Data Analysis
Data Visualization
Statistical Analysis
Unsupervised Learning
K-Means Clustering
Customer Segmentation
Elbow Method
Silhouette Analysis
Supervised Learning
Classification
Random Forest
Feature Engineering
Train-Test Split
Cross-Validation
Confusion Matrix
Feature Importance
Model Evaluation
Business Insights
```

---

# Conclusion

This repository documents my practical learning journey during the AI/Data Analytics Internship.

The completed assignments demonstrate the application of data analytics and machine learning techniques to real-world datasets.

The internship work has progressed from basic data preparation and exploratory analysis to advanced machine learning techniques such as clustering and supervised classification.

The completed weeks currently include:

```text
Week 1 → Data Cleaning and Preprocessing
Week 2 → Exploratory Data Analysis and Visualization
Week 3 → Unsupervised Learning and Clustering
Week 4 → Supervised Learning Model Implementation
```

Week 5 and Week 6 will be added as the internship progresses.

---

# Author

## Asfina Magi

**B.Tech Computer Science Engineering – AI/ML**

**Alliance University**

GitHub: `asfina9591-u`

---

# Repository Status

```text
Week 1 → ✅ Completed
Week 2 → ✅ Completed
Week 3 → ✅ Completed
Week 4 → ✅ Completed
Week 5 → ⏳ Pending
Week 6 → ⏳ Pending
```

**Last Updated: August 2026**
