# part_d_visualizations.py
# Visualization for Retail Sales Data using Matplotlib

import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend to enable GUI plot windows

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert SaleDate to datetime
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# Create TotalAmount column
df['TotalAmount'] = df['Quantity'] * df['Price']

# Extract month for grouping
df['Month'] = df['SaleDate'].dt.to_period('M').astype(str)

# Create output folder for plots if it doesn't exist
os.makedirs("plots", exist_ok=True)

# -------------------------------
# 1. Bar Chart – Total Revenue per Product
# -------------------------------
revenue_per_product = df.groupby('Product')['TotalAmount'].sum().reset_index()

plt.figure(figsize=(8, 6))
plt.bar(revenue_per_product['Product'], revenue_per_product['TotalAmount'], color='skyblue')
plt.title('Total Revenue per Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.savefig("plots/bar_revenue_per_product.png")
plt.show()  # Show plot window

# -------------------------------
# 2. Line Chart – Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()
monthly_sales = monthly_sales.sort_values('Month')

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Month'], monthly_sales['TotalAmount'], marker='o', linestyle='-', color='green')
plt.title('Monthly Sales Trend (2024)')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/line_monthly_sales_trend.png")
plt.show()  # Show plot window

# -------------------------------
# 3. Pie Chart – Product Revenue Contribution
# -------------------------------
plt.figure(figsize=(8, 8))
plt.pie(
    revenue_per_product['TotalAmount'],
    labels=revenue_per_product['Product'],
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Product Revenue Contribution')
plt.tight_layout()
plt.savefig("plots/pie_product_contribution.png")
plt.show()  # Show plot window

# -------------------------------
# 4. Scatter Plot – Quantity vs TotalAmount
# -------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(df['Quantity'], df['TotalAmount'], alpha=0.7, color='purple')
plt.title('Quantity vs Total Amount')
plt.xlabel('Quantity')
plt.ylabel('Total Amount')
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/scatter_quantity_vs_totalamount.png")
plt.show()  # Show plot window
