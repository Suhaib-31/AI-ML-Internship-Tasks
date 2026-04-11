# ==============================
# TASK 1: IRIS DATASET ANALYSIS
# ==============================

# 📌 Libraries import
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD DATASET
# ==============================

df = sns.load_dataset('iris')

# Dataset save (optional)
df.to_csv("iris_dataset.csv", index=False)

print("Dataset Loaded Successfully ✅\n")

# ==============================
# 2. BASIC INFORMATION
# ==============================

print("🔹 Shape of dataset:")
print(df.shape)

print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Info:")
print(df.info())

print("\n🔹 Statistical Summary:")
print(df.describe())

# ==============================
# 3. MISSING VALUES CHECK
# ==============================

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# ==============================
# 4. DATA VISUALIZATION
# ==============================

# Scatter Plot
plt.figure(figsize=(7,5))
sns.scatterplot(
    x='sepal_length',
    y='petal_length',
    hue='species',
    data=df
)
plt.title("Sepal Length vs Petal Length")
plt.show()

# Histogram
df.hist(figsize=(10,6))
plt.suptitle("Feature Distributions")
plt.show()

# Box Plot (Outliers check)
plt.figure(figsize=(8,5))
sns.boxplot(data=df)
plt.title("Box Plot - Outliers Check")
plt.show()

# Pair Plot (Best visualization)
sns.pairplot(df, hue='species')
plt.show()