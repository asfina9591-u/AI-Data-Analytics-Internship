import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")

# Load the cleaned dataset
df = pd.read_csv("cleaned_telco_churn.csv")

print("Dataset loaded successfully!")
print("Shape of dataset:", df.shape)

# Display first 5 rows
print("\n--- First 5 Rows ---")
print(df.head())

# Display dataset information
print("\n--- Dataset Information ---")
print(df.info())

# Display number of missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Display statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())

# Churn Distribution
print("\n--- Churn Distribution ---")
print(df["Churn Label"].value_counts())

plt.figure(figsize=(6, 4))
sns.countplot(x="Churn Label", data=df)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

# Save instead of show
plt.tight_layout()
plt.savefig("churn_distribution.png")
plt.close()

# Contract Type vs Churn
print("\n--- Contract Type vs Churn ---")
print(pd.crosstab(df["Contract"], df["Churn Label"]))

plt.figure(figsize=(8, 5))
sns.countplot(
    x="Contract",
    hue="Churn Label",
    data=df
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.legend(title="Churn")

plt.tight_layout()
# Save instead of show
plt.savefig("contract_vs_churn.png")
plt.close()

# -----------------------------------------
# Tenure Months vs Churn
# -----------------------------------------

print("\n--- Average Tenure by Churn ---")

print(
    df.groupby("Churn Label")["Tenure Months"].mean()
)

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="Churn Label",
    y="Tenure Months",
    data=df
)

plt.title("Tenure Months vs Customer Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure Months")

plt.tight_layout()

plt.savefig("tenure_vs_churn.png")

plt.close()

print("Tenure vs Churn visualization saved successfully!")

# Average Monthly Charges by Churn

print("\n--- Average Monthly Charges by Churn ---")

avg_monthly_charges = df.groupby("Churn Label")["Monthly Charges"].mean()

print(avg_monthly_charges)


# Visualization

plt.figure(figsize=(6, 4))

sns.barplot(
    x=avg_monthly_charges.index,
    y=avg_monthly_charges.values
)

plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")

plt.tight_layout()

plt.savefig("average_monthly_charges_by_churn.png")

plt.show()

print("Monthly Charges vs Churn visualization saved successfully!")

# Internet Service vs Churn

print("\n--- Internet Service vs Churn ---")

internet_churn = pd.crosstab(
    df["Internet Service"],
    df["Churn Label"]
)

print(internet_churn)


# Visualization

plt.figure(figsize=(8, 5))

sns.countplot(
    x="Internet Service",
    hue="Churn Label",
    data=df
)

plt.title("Customer Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.legend(title="Churn")

plt.tight_layout()

plt.savefig("internet_service_vs_churn.png")

plt.show()

print("Internet Service vs Churn visualization saved successfully!")

# -----------------------------------------
# Payment Method vs Churn
# -----------------------------------------

print("\n--- Payment Method vs Churn ---")

payment_churn = pd.crosstab(
    df["Payment Method"],
    df["Churn Label"]
)

print(payment_churn)


# Visualization

plt.figure(figsize=(10, 5))
sns.countplot(
    x="Payment Method",
    hue="Churn Label",
    data=df
)
plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig("payment_method_vs_churn.png")
plt.close()
print("Payment Method vs Churn visualization saved successfully!")

# -----------------------------------------
# Correlation Analysis
# -----------------------------------------

print("\n--- Correlation Analysis ---")

# Compute correlation matrix for numeric features
corr = df.corr(numeric_only=True)

print(corr)

# Visualization
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

print("Correlation heatmap saved successfully!")
