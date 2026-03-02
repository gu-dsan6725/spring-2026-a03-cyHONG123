# temp_0.py
import pandas as pd

# Read daily sales data
sales_data = pd.read_csv('data/structured/daily_sales.csv')

# Filter data for West region
west_region_data = sales_data[sales_data['region'] == 'West']

# Filter data for fitness products
fitness_products = west_region_data[west_region_data['category'] == 'Fitness']

# Group data by product_id and calculate total sales
product_sales = fitness_products.groupby('product_id')['units_sold'].sum().reset_index()

# Merge product sales with product details
product_details = pd.read_csv('data/unstructured/SPRT001_product_page.txt', sep='\t', header=None, names=['product_id', 'product_name', 'rating'])
merged_data = pd.merge(product_sales, product_details, on='product_id')

# Filter data for highly rated products
highly_rated_products = merged_data[merged_data['rating'] > 4]

# Sort data by total sales in descending order
recommended_products = highly_rated_products.sort_values(by='units_sold', ascending=False)

# Save recommended products to a file
recommended_products.to_csv('temp_0.txt', index=False)