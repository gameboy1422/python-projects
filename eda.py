import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
# Fill missing 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)
# Fill missing 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
# Drop 'Cabin' column as it has too many missing values
df.drop('Cabin', axis=1, inplace=True)

# Verify missing values after handling
print("\nMissing Values After Handling:")
print(df.isnull().sum())

# Visualize the distribution of survivors
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.show()

# Visualize the distribution of passengers by gender
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', data=df, palette='Set3')
plt.title('Passenger Gender Distribution')
plt.show()

# Visualize the distribution of passengers by passenger class
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', data=df, palette='Set1')
plt.title('Passenger Class Distribution')
plt.show()

# Visualize the age distribution of passengers
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualize survival rate by gender
plt.figure(figsize=(6, 4))
sns.barplot(x='Sex', y='Survived', data=df, palette='Set2')
plt.title('Survival Rate by Gender')
plt.show()

# Visualize survival rate by passenger class
plt.figure(figsize=(6, 4))
sns.barplot(x='Pclass', y='Survived', data=df, palette='Set1')
plt.title('Survival Rate by Passenger Class')
plt.show()

# Visualize survival rate by age and gender
plt.figure(figsize=(10, 6))
sns.violinplot(x='Sex', y='Age', hue='Survived', data=df, split=True, palette='Set2')
plt.title('Survival Rate by Age and Gender')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()