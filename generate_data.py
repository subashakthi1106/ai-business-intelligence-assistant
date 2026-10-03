# ============================================================
# AI BUSINESS INTELLIGENCE PROJECT
# SYNTHETIC DATA GENERATION
# ============================================================

# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np


# 2. SET RANDOM SEED
np.random.seed(42)


# ============================================================
# 3. BASIC SETTINGS
# ============================================================

NUMBER_OF_CUSTOMERS = 2000
NUMBER_OF_PRODUCTS = 200
NUMBER_OF_SALES = 20000


# ============================================================
# 4. CREATE CUSTOMER DATA
# ============================================================

customer_ids = [
    f"C{i:04d}" for i in range(1, NUMBER_OF_CUSTOMERS + 1)
]

first_names = [
    "Arun", "Priya", "Rahul", "Ananya", "Karthik",
    "Divya", "Vikram", "Sneha", "Aditya", "Meena",
    "Rohit", "Kavya", "Sanjay", "Nisha", "Arjun",
    "Pooja", "Vivek", "Swetha", "Ajay", "Keerthi"
]

last_names = [
    "Kumar", "Sharma", "Patel", "Reddy", "Iyer",
    "Nair", "Singh", "Rao", "Das", "Menon",
    "Gupta", "Verma", "Pillai", "Joshi", "Bose"
]

customer_names = [
    np.random.choice(first_names) + " " + np.random.choice(last_names)
    for _ in range(NUMBER_OF_CUSTOMERS)
]

regions = [
    "Chennai",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Delhi"
]

customer_regions = np.random.choice(
    regions,
    size=NUMBER_OF_CUSTOMERS,
    p=[0.25, 0.22, 0.20, 0.18, 0.15]
)

signup_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2025-07-01", "2025-12-31"),
        size=NUMBER_OF_CUSTOMERS
    )
)


# ============================================================
# 5. CREATE PRODUCT DATA
# ============================================================

product_ids = [
    f"P{i:04d}" for i in range(1, NUMBER_OF_PRODUCTS + 1)
]

categories = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Beauty & Personal Care",
    "Sports & Fitness"
]

product_types = [
    "Phone",
    "Laptop",
    "Headphones",
    "Shoes",
    "Shirt",
    "Watch",
    "Backpack",
    "Mixer",
    "Chair",
    "Bottle",
    "Skincare Set",
    "Fitness Band",
    "Yoga Mat",
    "Smart TV",
    "Keyboard"
]

product_names = [
    f"{np.random.choice(product_types)} Model {i}"
    for i in range(1, NUMBER_OF_PRODUCTS + 1)
]

product_categories = np.random.choice(
    categories,
    size=NUMBER_OF_PRODUCTS
)

product_prices = np.random.randint(
    500,
    50000,
    size=NUMBER_OF_PRODUCTS
)


# ============================================================
# 6. CREATE SALES DATA
# ============================================================

order_ids = [
    f"O{i:05d}" for i in range(1, NUMBER_OF_SALES + 1)
]

sale_customer_ids = np.random.choice(
    customer_ids,
    size=NUMBER_OF_SALES
)

sale_product_ids = np.random.choice(
    product_ids,
    size=NUMBER_OF_SALES
)

order_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2026-01-01", "2026-06-30"),
        size=NUMBER_OF_SALES
    )
)

quantities = np.random.randint(
    1,
    6,
    size=NUMBER_OF_SALES
)


# ============================================================
# 7. CONNECT CUSTOMER INFORMATION TO SALES
# ============================================================

customer_lookup = pd.DataFrame({
    "customer_id": customer_ids,
    "customer_name": customer_names,
    "region": customer_regions,
    "signup_date": signup_dates
})

sales_customers = customer_lookup.set_index(
    "customer_id"
).loc[sale_customer_ids].reset_index()


# ============================================================
# 8. CONNECT PRODUCT INFORMATION TO SALES
# ============================================================

product_lookup = pd.DataFrame({
    "product_id": product_ids,
    "product_name": product_names,
    "category": product_categories,
    "price": product_prices
})

sales_products = product_lookup.set_index(
    "product_id"
).loc[sale_product_ids].reset_index()


# ============================================================
# 9. CALCULATE REVENUE
# ============================================================

revenues = (
    quantities * sales_products["price"].to_numpy()
)


# ============================================================
# 10. CREATE ONE COMPLETE DATASET
# ============================================================

business_dataset = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": sale_customer_ids,
    "customer_name": sales_customers["customer_name"].to_numpy(),
    "region": sales_customers["region"].to_numpy(),
    "signup_date": sales_customers["signup_date"].to_numpy(),
    "product_id": sale_product_ids,
    "product_name": sales_products["product_name"].to_numpy(),
    "category": sales_products["category"].to_numpy(),
    "price": sales_products["price"].to_numpy(),
    "order_date": order_dates,
    "quantity": quantities,
    "revenue": revenues
})


# ============================================================
# 11. SORT DATA BY ORDER DATE
# ============================================================

business_dataset = business_dataset.sort_values(
    "order_date"
).reset_index(drop=True)


# ============================================================
# 12. CHECK THE DATASET
# ============================================================

print("\n================ DATASET PREVIEW ================\n")

print(business_dataset.head())


print("\n================ DATASET SIZE ================\n")

print("Rows:", business_dataset.shape[0])
print("Columns:", business_dataset.shape[1])


print("\n================ MISSING VALUES ================\n")

print(business_dataset.isnull().sum())


print("\n================ DUPLICATE ROWS ================\n")

print(
    "Duplicate rows:",
    business_dataset.duplicated().sum()
)


# ============================================================
# 13. SAVE THE COMPLETE DATASET
# ============================================================

business_dataset.to_csv(
    "business_dataset.csv",
    index=False
)


# ============================================================
# 14. FINAL MESSAGE
# ============================================================

print("\n==============================================")
print("SYNTHETIC DATASET CREATED SUCCESSFULLY!")
print("==============================================")

print("File created: business_dataset.csv")
print("Total rows:", len(business_dataset))
print("Total columns:", len(business_dataset.columns))

print("==============================================")