import matplotlib.pyplot as plt
import pandas as pd

# loading the data from the CSV File
df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df.head())

#metrics to display
total_sales = df["Sales"].sum()
total_units = df["Units"].sum()
average_sales = df["Sales"].mean()

print("\n---Summary---")
print(f"Total Sales: {total_sales}")
print(f"Total Units sold: {total_units}")
print(f"Average Monthly Sales: {average_sales:.2f}")    #rounded off the the monthly sales

#Sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_by_product)

#Sales by month
sales_by_month = df.groupby("Month")["Sales"].sum()
print("\nSales by Month:")
print(sales_by_month)

#Sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_by_region)

# chart 1: Sales by product 
plt.figure(figsize = (8, 5))
plt.bar(sales_by_product.index, sales_by_product.values)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#chart 2: Sales by month
plt.figure(figsize = (8, 5))
plt.bar(sales_by_month.index, sales_by_month.values)
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

#chart 3: Sales by region
plt.figure(figsize = (8, 5))
plt.bar(sales_by_region.index, sales_by_region.values)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

