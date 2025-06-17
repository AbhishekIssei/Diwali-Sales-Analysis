# Diwali Sales Analysis using Python, Pandas, Matplotlib, and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv("Diwali Sales Data.csv", encoding='unicode_escape')

# Display first few rows
print(df.head())

# Shape and info
print("Dataset shape:", df.shape)
print(df.info())

# Drop unnecessary columns safely
columns_to_drop = ['Status', 'unnamed1']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)


# Check for null values
print(df.isnull().sum())

# Drop nulls
df.dropna(inplace=True)

# Convert 'Amount' column to integer (if it's not already)
df['Amount'] = df['Amount'].astype(int)

# Basic summary
print(df.describe())

# --- 📊 Exploratory Data Analysis (EDA) ---

# Gender distribution
ax = sns.countplot(data=df, x='Gender', palette='Set2')
plt.title('Gender Distribution')
plt.show()

# Total Amount by Gender
sales_by_gender = df.groupby('Gender')['Amount'].sum().reset_index()
sns.barplot(data=sales_by_gender, x='Gender', y='Amount', palette='Set1')
plt.title('Total Sales by Gender')
plt.show()

# Age Group vs Total Sales
age_sales = df.groupby('Age Group')['Amount'].sum().reset_index()
sns.barplot(data=age_sales, x='Age Group', y='Amount', palette='coolwarm')
plt.title('Total Sales by Age Group')
plt.show()

# Top 10 States by Sales
state_sales = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
state_sales.plot(kind='bar', color='teal')
plt.title('Top 10 States by Total Sales')
plt.ylabel('Amount')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.show()

# Most sold product categories
category_sales = df.groupby('Product Category')['Amount'].sum().sort_values(ascending=False)
category_sales.plot(kind='bar', color='purple')
plt.title('Product Category-wise Sales')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.show()

# Top 10 Customers by Sales
top_customers = df.groupby('Customer Name')['Amount'].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind='barh', color='orange')
plt.title('Top 10 Customers')
plt.xlabel('Sales Amount')
plt.show()
