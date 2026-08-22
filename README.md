# AI Data Analytics Internship

This repository contains my work and assignments completed during my AI/Data Analytics Internship.

The internship focuses on practical data analytics, including data acquisition, data cleaning, exploratory data analysis, data visualization, unsupervised learning, clustering, and interpretation of analytical results.

---

# Internship Weekly Work

| Week | Topic | Status |
|---|---|---|
| Week 1 | Data Acquisition, Cleaning and Preprocessing | Completed |
| Week 2 | Exploratory Data Analysis and Visualization | Completed |
| Week 3 | Unsupervised Learning and Clustering Analysis | Completed |

---

# Week 1 – Data Acquisition, Cleaning, and Preprocessing

## Objective

The objective of Week 1 was to acquire a real-world dataset, inspect its structure, identify data quality issues, handle missing values, and prepare the dataset for further analysis.

## Dataset

The Telco Customer Churn dataset was used for this task.

The dataset contains information related to:

- Customer demographics
- Tenure
- Contract details
- Internet services
- Payment methods
- Monthly charges
- Total charges
- Customer churn

## Key Steps

### 1. Data Acquisition

The dataset was loaded into Python using the Pandas library.

### 2. Data Exploration

Initial exploration was performed to understand:

- Number of rows and columns
- Data types
- Missing values
- Duplicate records
- Statistical characteristics of the dataset

### 3. Data Cleaning

The following data cleaning steps were performed:

- Checked for missing values
- Identified and handled incomplete records
- Converted numerical columns to appropriate data types
- Checked for duplicate records
- Inspected the dataset for data quality issues

### 4. Data Preprocessing

The cleaned dataset was prepared for further analysis and machine learning tasks.

Numerical and categorical variables were examined and prepared appropriately for subsequent analytical operations.

## Dataset Statistics

After cleaning and preprocessing:

- Total records: `7,043`
- Total features: `28`
- Average Tenure: approximately `32.37 months`
- Average Monthly Charges: approximately `64.30`
- Average Total Charges: approximately `2279.27`

## Deliverables

The Week 1 deliverables include:

- Jupyter Notebook
- Cleaned dataset
- Preprocessed dataset
- Week 1 report

## Folder

```text
Week1_Data_Cleaning_Preprocessing/
```

---

# Week 2 – Exploratory Data Analysis and Visualization

## Objective

The objective of Week 2 was to perform Exploratory Data Analysis (EDA) on the cleaned Telco Customer Churn dataset and identify important patterns, trends, and relationships within the data.

## Dataset

The cleaned Telco Customer Churn dataset from Week 1 was used for the analysis.

## Key Analysis

The following analyses were performed:

### 1. Customer Churn Distribution

The distribution of customers who churned and customers who remained with the company was analyzed.

This helped understand the overall proportion of churned and retained customers.

### 2. Contract Type vs Churn

Customer churn was analyzed across different contract types.

This analysis helped identify whether customers with different contract durations showed different churn behavior.

### 3. Tenure vs Churn

The relationship between customer tenure and churn was analyzed.

This helped understand whether customers who had stayed with the company for longer periods behaved differently from newer customers.

### 4. Monthly Charges vs Churn

Average monthly charges were compared between customers who churned and customers who remained.

This analysis helped identify whether higher monthly charges were associated with increased churn.

### 5. Internet Service vs Churn

Churn behavior was compared across different internet service types.

### 6. Payment Method vs Churn

Different payment methods were analyzed to identify possible relationships between payment behavior and customer churn.

### 7. Correlation Analysis

A correlation heatmap was created to identify relationships between numerical variables in the dataset.

## Visualizations

The Week 2 analysis included visualizations such as:

- Churn distribution
- Contract type vs churn
- Tenure vs churn
- Monthly charges vs churn
- Internet service vs churn
- Payment method vs churn
- Correlation heatmap

## Key Insights

The exploratory analysis showed that customer churn can be associated with several customer characteristics and service-related factors.

Important factors investigated included:

- Contract type
- Customer tenure
- Monthly charges
- Internet service
- Payment method

Customers with shorter tenure and certain contract or service combinations showed higher churn tendencies.

The analysis demonstrates how Exploratory Data Analysis can be used to identify patterns that may support customer retention and business decision-making.

## Deliverables

The Week 2 deliverables include:

- Python EDA script
- Visualizations
- Processed dataset
- Week 2 report

## Folder

```text
Week2_EDA_and_Visualization/
```

---

# Week 3 – Unsupervised Learning and Clustering Analysis

## Objective

The objective of Week 3 was to apply unsupervised machine learning techniques to segment customers into meaningful groups based on their demographic and behavioral characteristics.

K-Means clustering was used to identify customer segments and analyze the characteristics of each segment.

## Dataset

The Mall Customers dataset was selected for the clustering analysis.

The dataset contains the following attributes:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

## Features Used for Clustering

The following numerical features were selected:

- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`

The `CustomerID` column was excluded because it is only an identifier and does not provide meaningful information for clustering.

The `Genre` column was also not included in the K-Means feature set because the main clustering analysis focused on numerical demographic and behavioral characteristics.

## Data Preprocessing

The selected numerical features were standardized before applying the clustering algorithm.

`StandardScaler` from Scikit-learn was used to standardize the features.

This was important because the selected features have different numerical ranges.

Standardization ensures that one feature does not dominate the clustering process simply because it has a larger numerical scale.

## Clustering Algorithm

### K-Means Clustering

K-Means was selected as the primary clustering algorithm.

K-Means is an unsupervised machine learning algorithm that groups similar observations into clusters.

The algorithm works by:

1. Selecting a specified number of clusters.
2. Initializing cluster centroids.
3. Assigning each data point to the nearest centroid.
4. Updating the centroids.
5. Repeating the process until the clusters stabilize.

## Selecting the Number of Clusters

Two methods were used to determine a suitable number of clusters:

### Elbow Method

The Elbow Method was used to calculate the inertia for different values of `K`.

The analysis tested:

```text
K = 2 to 8
```

Inertia represents the within-cluster sum of squared distances between data points and their assigned cluster centroids.

The elbow curve was visualized to help identify an appropriate number of clusters.

### Silhouette Score

Silhouette scores were calculated for the tested values of `K`.

The silhouette score measures how well each data point fits within its assigned cluster compared with other clusters.

A higher silhouette score generally indicates better-defined and better-separated clusters.

## Final Number of Clusters

Based on the combined evaluation using the Elbow Method and Silhouette Analysis, the final K-Means model used:

```text
Number of Clusters = 6
```

The final silhouette score was approximately:

```text
0.4284
```

This indicates a moderate level of cluster separation and provides a useful segmentation of the customer population.

---

# Final Cluster Profiles

The final clustering analysis produced six customer segments.

| Cluster | Customers | Average Age | Average Income (k$) | Average Spending |
|---:|---:|---:|---:|---:|
| 0 | 45 | 56.33 | 54.27 | 49.07 |
| 1 | 39 | 26.79 | 57.10 | 48.13 |
| 2 | 33 | 41.94 | 88.94 | 16.97 |
| 3 | 39 | 32.69 | 86.54 | 82.13 |
| 4 | 23 | 25.00 | 25.26 | 77.61 |
| 5 | 21 | 45.52 | 26.29 | 19.38 |

---

# Cluster Interpretation

## Cluster 0 – Older Moderate Customers

Cluster 0 contains `45` customers.

Average characteristics:

- Average age: `56.33`
- Average income: `54.27 k$`
- Average spending score: `49.07`

These customers represent a relatively older customer segment with moderate income and average spending behavior.

This group may respond to stable, personalized offers and loyalty-based marketing strategies.

---

## Cluster 1 – Young Moderate Customers

Cluster 1 contains `39` customers.

Average characteristics:

- Average age: `26.79`
- Average income: `57.10 k$`
- Average spending score: `48.13`

These customers are relatively young and have moderate income and spending behavior.

Marketing strategies for this group could focus on engagement, personalized recommendations, and products relevant to younger customers.

---

## Cluster 2 – High-Income Low-Spending Customers

Cluster 2 contains `33` customers.

Average characteristics:

- Average age: `41.94`
- Average income: `88.94 k$`
- Average spending score: `16.97`

This segment has relatively high income but a low spending score.

This group represents a potential business opportunity because customers have purchasing capacity but are currently not spending heavily.

Personalized offers, targeted promotions, loyalty benefits, and improved customer engagement could potentially increase their spending.

---

## Cluster 3 – High-Income High-Spending Customers

Cluster 3 contains `39` customers.

Average characteristics:

- Average age: `32.69`
- Average income: `86.54 k$`
- Average spending score: `82.13`

This segment has both high income and high spending behavior.

These customers can be considered a valuable customer segment.

Potential strategies include:

- Premium loyalty programs
- Exclusive offers
- Personalized recommendations
- Early access to new products
- VIP customer benefits

---

## Cluster 4 – Young High-Spending Customers

Cluster 4 contains `23` customers.

Average characteristics:

- Average age: `25.00`
- Average income: `25.26 k$`
- Average spending score: `77.61`

These customers have relatively low income but a high spending score.

This segment may respond well to:

- Discounts
- Affordable products
- Promotional campaigns
- Trend-oriented marketing
- Limited-time offers

---

## Cluster 5 – Low-Income Low-Spending Customers

Cluster 5 contains `21` customers.

Average characteristics:

- Average age: `45.52`
- Average income: `26.29 k$`
- Average spending score: `19.38`

This segment has relatively low income and low spending activity.

Businesses could use value-oriented products, discounts, and targeted promotional campaigns to improve engagement with this group.

---

# Business Implications

The clustering analysis can support customer segmentation and targeted marketing strategies.

Different customer groups can be approached using different strategies instead of applying the same marketing strategy to every customer.

### High-Income High-Spending Customers

Customers in Cluster 3 could receive:

- Premium loyalty programs
- VIP benefits
- Exclusive products
- Personalized recommendations
- Early access offers

### High-Income Low-Spending Customers

Customers in Cluster 2 could receive:

- Personalized promotions
- Product recommendations
- Special discounts
- Loyalty incentives
- Targeted engagement campaigns

The goal would be to convert their high purchasing capacity into higher spending.

### Young High-Spending Customers

Customers in Cluster 4 could be targeted using:

- Discounts
- Social media campaigns
- Trend-based products
- Affordable premium products
- Limited-time offers

### Low-Income Low-Spending Customers

Customers in Cluster 5 could receive:

- Value-based offers
- Affordable product recommendations
- Discounts
- Budget-friendly packages

### Older Moderate Customers

Cluster 0 could be approached using:

- Loyalty programs
- Personalized offers
- Customer retention campaigns
- Products suited to their preferences

### Young Moderate Customers

Cluster 1 could be targeted using:

- Personalized recommendations
- Engagement campaigns
- Membership programs
- Youth-oriented products and promotions

---

# Visualizations

The Week 3 project contains multiple visualizations to understand the customer clusters.

The main visualizations include:

- Age distribution
- Income distribution
- Spending score distribution
- Elbow curve
- Silhouette score analysis
- Cluster distribution
- Age vs Spending Score cluster visualization
- Income vs Spending Score cluster visualization
- 3D cluster visualization
- Gender cluster distribution
- Cluster business comparison

These visualizations help communicate the differences between customer segments.

---

# Week 3 Deliverables

The Week 3 project contains:

- Jupyter Notebook
- Mall Customers dataset
- Clustered customer dataset
- Cluster summary
- Cluster profile
- Elbow curve
- Silhouette score visualization
- Cluster visualizations
- Business comparison visualization
- Week 3 report

## Folder

```text
Week-3-Unsupervised-Learning-Clustering/
```

---

# Technologies Used

The following tools and libraries were used throughout the internship:

- `Python`
- `Pandas`
- `NumPy`
- `Matplotlib`
- `Seaborn`
- `Scikit-learn`
- `Jupyter Notebook`
- `VS Code`
- `Git`
- `GitHub`
- `python-docx`

---

# Machine Learning and Data Analytics Techniques

The internship work demonstrates practical experience with:

- Data acquisition
- Data cleaning
- Data preprocessing
- Missing value handling
- Data type conversion
- Exploratory Data Analysis
- Statistical analysis
- Data visualization
- Feature selection
- Feature scaling
- Unsupervised learning
- K-Means clustering
- Elbow Method
- Silhouette Analysis
- Customer segmentation
- Cluster interpretation
- Business-oriented data analysis

---

# Repository Structure

The repository is organized by internship week.

```text
AI-Data-Analytics-Internship/
│
├── README.md
│
├── Week1_Data_Cleaning_Preprocessing/
│   │
│   ├── Week1_Data_Cleaning_Preprocessing.ipynb
│   ├── Week1_Data_Cleaning_Preprocessing_Report.docx
│   ├── cleaned_telco_churn.csv
│   ├── customer_churn.csv.ipynb
│   └── preprocessed_telco_churn.csv
│
├── Week2_EDA_and_Visualization/
│   │
│   ├── Week2_EDA.py
│   ├── Week 2 Task — Exploratory Data Analysis and Visualization.docx
│   ├── cleaned_telco_churn.csv
│   ├── preprocessed_telco_churn.csv
│   ├── contract_vs_churn.png
│   ├── tenure_vs_churn.png
│   ├── average_monthly_charges_by_churn.png
│   ├── internet_service_vs_churn.png
│   ├── payment_method_vs_churn.png
│   ├── correlation_heatmap.png
│   └── other EDA visualizations
│
└── Week-3-Unsupervised-Learning-Clustering/
    │
    ├── data/
    │   └── Mall_Customers.csv
    │
    ├── notebooks/
    │   └── Week3_Clustering_Analysis.ipynb
    │
    ├── outputs/
    │   ├── age_distribution.png
    │   ├── age_vs_spending_clusters.png
    │   ├── cluster_business_comparison.png
    │   ├── cluster_distribution.png
    │   ├── cluster_summary.csv
    │   ├── clusters_3d.png
    │   ├── customer_clusters.csv
    │   ├── elbow_curve.png
    │   ├── final_cluster_profile.csv
    │   ├── genre_cluster_distribution.png
    │   ├── income_distribution.png
    │   ├── income_vs_spending_clusters.png
    │   ├── silhouette_scores.png
    │   └── spending_score_distribution.png
    │
    ├── report/
    │
    ├── src/
    │
    └── README.md
```

---

# Overall Internship Progress

## Week 1

Completed data acquisition, cleaning, and preprocessing of the Telco Customer Churn dataset.

## Week 2

Completed Exploratory Data Analysis and visualization of the customer churn dataset.

## Week 3

Completed unsupervised learning and customer segmentation using K-Means clustering on the Mall Customers dataset.

---

# Conclusion

Across the first three weeks of the internship, the project progressed from raw data preparation to exploratory analysis and finally to machine learning-based customer segmentation.

Week 1 established a clean and reliable dataset through data acquisition, cleaning, and preprocessing.

Week 2 explored the cleaned data through statistical analysis and visualization to identify important patterns and relationships.

Week 3 extended the analysis into unsupervised machine learning by applying K-Means clustering to segment customers based on age, annual income, and spending behavior.

The final clustering analysis identified six customer segments with different demographic and spending characteristics.

The analysis demonstrates how unsupervised learning can be used to transform customer data into meaningful segments that can support targeted marketing strategies and business decision-making.

Together, these three weeks demonstrate practical experience in Python-based data analytics, data preprocessing, visualization, exploratory analysis, and machine learning.

---

# Author

**Asfina Magi**

B.Tech Computer Science Engineering – AI/ML

Alliance University

---

# Project Status

```text
Week 1  - Completed
Week 2  - Completed
Week 3  - Completed
```

The repository will be updated with additional internship tasks as they are completed.
