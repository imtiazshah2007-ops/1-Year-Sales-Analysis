import pandas as pd

# ============================================
# READ CSV AND CLEAN
# ============================================
df = pd.read_csv("Total Sales_2019.csv")

print(f"Original rows: {len(df)}")
print("\n👀 First 3 rows:")
print(df.head(3))
print("\n👀 Last 3 rows:")
print(df.tail(3))

# ============================================
# FIX 1: Remove rows where "Order Date" is text "Order Date"
# ============================================
df = df[df["Order Date"] != "Order Date"]

print(f"\n✅ After removing bad rows: {len(df)}")

# ============================================
# FIX 2: Remove completely empty rows
# ============================================
df = df.dropna(how='all')

# ============================================
# FIX 3: Convert numeric columns
# ============================================
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors='coerce')
df["Price Each"] = pd.to_numeric(df["Price Each"], errors='coerce')

# ============================================
# FIX 4: Remove rows where conversion failed
# ============================================
df = df.dropna(subset=["Quantity Ordered", "Price Each"])

print(f"✅ After cleaning numeric data: {len(df)}")

# ============================================
# FIX 5: Create Total Sales
# ============================================
df["Total Sales"] = df["Quantity Ordered"] * df["Price Each"]

# ============================================
# FIX 6: Convert Order Date (with error handling)
# ============================================
df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

# Remove rows where date conversion failed
df = df.dropna(subset=["Order Date"])

print(f"✅ Final clean data: {len(df)}")

# ============================================
# FIX 7: Extract Month, Hour, Day
# ============================================
df["Month"] = df["Order Date"].dt.month
df["Hour"] = df["Order Date"].dt.hour
df["Day"] = df["Order Date"].dt.day



# ============================================
# SAVE CLEANED DATA
# ============================================
df.to_csv("Final Total Sales.csv", index=False)
print("\n✅ Cleaned data saved as 'Cleaned_Sales_January_2019.csv'")