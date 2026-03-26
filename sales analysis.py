import pandas as pd

# Read CSV file

df = pd.read_csv("Final Total Sales.csv")

# Conversion of Data types for Mathematical operation

df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors='coerce')
df["Price Each"] = pd.to_numeric(df["Price Each"], errors='coerce')

# Creating new column of total sales

df["Total Sales"]=df["Quantity Ordered"]*df["Price Each"]

#----------------------------------------------------
#              Convert to datetime
#-----------------------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract Month
df["Month"] = df["Order Date"].dt.month

# Extract Hour
df["Hour"] = df["Order Date"].dt.hour

# Extract Day
df["Day"] = df["Order Date"].dt.day

#-----------------------------------------------
#           City Extract Process
#-----------------------------------------------

df["City"] = df["Purchase Address"].apply(lambda x: x.split(",")[1])

#--------------------------------------
#            Graph Plot Process
#--------------------------------------
import matplotlib.pyplot as plt

monthly_sales = df.groupby("Month")["Total Sales"].sum()

# Plot line
plt.plot(monthly_sales.index, 
         monthly_sales.values, 
         marker='o',           # Circle markers
         linewidth=3,        # Line thickness
         markersize=7,        # Marker size
         color='blue',         # Line color
         markerfacecolor='green', # Marker fill color
         markeredgecolor='darkblue', # Marker edge color
         markeredgewidth=2.5)

# ============================================
# STEP 4: CUSTOMIZE THE GRAPH
# ============================================
# Month names for x-axis
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Set x-axis labels
plt.xticks(monthly_sales.index, 
           [month_names[i-1] for i in monthly_sales.index],
           fontsize=11)

# Add labels and title
plt.xlabel('Month', fontsize=14, fontweight='bold')
plt.ylabel('Total Sales ($)', fontsize=14, fontweight='bold')
plt.title('Monthly Sales Trend 2019', fontsize=16, fontweight='bold', pad=20)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Add value labels on each point
for i, (month, sales) in enumerate(monthly_sales.items()):
    plt.text(month, sales + 50000, f'${sales/1000000:.1f}M', 
             ha='center', 
             fontsize=9,
             fontweight='bold')

# Format y-axis to show currency
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M'))

# Tight layout
plt.tight_layout()

# ============================================
# STEP 5: SAVE AND DISPLAY
# ============================================
plt.savefig('monthly_sales_trend.png', dpi=300, bbox_inches='tight')
print("\n✅ Graph saved as 'monthly_sales_trend.png'")

plt.show()

print("\n🎉 SUCCESS! Graph created!")

#=======================================
#          Total Sales
#==========================================================
product_sales = df.groupby("Product")["Quantity Ordered"].sum()
product_sales.sort_values(ascending=False).plot(kind="bar", figsize=(10,5))
plt.title("Best Selling Products")
plt.ylabel("Quantity Sold")
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000000:.1f}M' if x >= 1000000 else f'{x/1000:.0f}K' if x >= 1000 else f'{x:.0f}'))
plt.tight_layout()
plt.savefig('Best Selling product.png', dpi=300, bbox_inches='tight')
plt.show()

#=============================================================
#                 Revenue by Product
#=======================================================================
revenue_by_product = df.groupby("Product")["Total Sales"].sum()

revenue_by_product.sort_values(ascending=False).plot(kind="bar", color="green")
plt.title("Revenue by Product")
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M' if x >= 1000000 else f'${x/1000:.0f}K' if x >= 1000 else f'${x:.0f}'))
plt.tight_layout()
plt.savefig('Revenue by product.png', dpi=300, bbox_inches='tight')
plt.show()

#================================================================
#                 Sales by City
#================================================================
city_sales = df.groupby("City")["Total Sales"].sum()

city_sales.sort_values(ascending=False).plot(kind="bar", color="orange")
plt.title("Sales by City")
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M' if x >= 1000000 else f'${x/1000:.0f}K' if x >= 1000 else f'${x:.0f}'))
plt.tight_layout()
plt.savefig('Sales by City.png', dpi=300, bbox_inches='tight')
plt.show()

#================================================================
#             Best Time to Advertise (Hour Analysis)
#================================================================
hour_sales = df.groupby("Hour")["Order ID"].count()

hour_sales.plot(kind="line")
plt.title("Orders by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000000:.1f}M' if x >= 1000000 else f'{x/1000:.0f}K' if x >= 1000 else f'{x:.0f}'))
plt.tight_layout()
plt.savefig('Best Time to Advertise (Hour Analysis).png', dpi=300, bbox_inches='tight')
plt.show()

#================================================================
#             Daily Trend Analysis
#================================================================
daily_sales = df.groupby("Day")["Total Sales"].sum()

daily_sales.plot()
plt.title("Daily Sales Trend")
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M' if x >= 1000000 else f'${x/1000:.0f}K' if x >= 1000 else f'${x:.0f}'))
plt.tight_layout()
plt.savefig('Daily Trend Analysis.png', dpi=300, bbox_inches='tight')
plt.show()

#================================================================
#             Top 5 Highest Revenue Orders
#================================================================
top_orders = df.sort_values("Total Sales", ascending=False).head()
print(top_orders)

#================================================================
#             Average Order Value
#================================================================
average_order = df["Total Sales"].mean()
print("Average Order Value:", average_order)