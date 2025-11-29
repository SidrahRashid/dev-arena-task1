import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\developers arena\week3\simple_sales.csv")

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# 1️⃣ Total Sales
total_sales = df["TotalPrice"].sum()

# 2️⃣ Best-Selling Product (by revenue)
product_sales = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)
best_product = product_sales.idxmax()
best_product_revenue = product_sales.max()

# Print results
print("=== SIMPLE SALES REPORT ===")
print(f"Total Sales: ₹{total_sales}")
print(f"Best-Selling Product: {best_product}")
print(f"Revenue from Best Product: ₹{best_product_revenue}")

# 3️⃣ Optional: Show product-wise summary
print("\nProduct-wise Revenue:")
print(product_sales)


# report.py

report = """
Simple Sales Analysis Report

Dataset Overview:
The dataset contains sales records for Pen, Notebook, Bag, and Mug.

Key Findings:
1. Total Sales: ₹695
2. Best-Selling Product: Notebook (₹340)

Product-wise revenue:
- Notebook: ₹340
- Bag: ₹150
- Mug: ₹120
- Pen: ₹85

Conclusion:
Notebook is the top-performing product.
"""

with open("sales_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("sales_report.txt created successfully!")
