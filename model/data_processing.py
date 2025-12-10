#model/: Contains code for data cleaning and processing.
import numpy as np

def load_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)
    return data

def clean_data(data):
    valid_mask = (data['Invoice_ID'] != '') & (data['Branch'] != '') & (data['Unit_price'] > 0)
    clean_data = data[valid_mask]
    return clean_data
 
def total_sales(data):
    return np.sum(data['Total'])

def sales_by_product_line(data):
    product_lines = np.unique(data['Product_line'])   # unique product categories
    sales = []
    for p in product_lines:
        mask = (data['Product_line'] == p)      # select rows by product line
        sales.append(np.sum(data['Total'][mask]))   # sum sales for product line
    return product_lines, sales

def sales_by_city(data):
    city_names = np.unique(data['City'])
    sales = []
    for c in city_names:
        mask = (data['City'] == c)
        sales.append(np.sum(data['Total'][mask]))
    return city_names, sales

def sales_by_branch(data):
    branches = np.unique(data['Branch'])
    sales = []
    for b in branches:
        mask = (data['Branch'] == b)
        sales.append(np.sum(data['Total'][mask]))
    return branches, sales

def sales_over_time(data):
    dates = data['Date']
    month_years = []
    for d in dates:
        parts = d.split('/')
        if len(parts) == 3:
            month = parts[0].zfill(2)
            year = parts[2]
            month_year = f"{year}-{month}"
            month_years.append(month_year)
    unique_months = sorted(list(set(month_years)))
    sales = []
    for m in unique_months:
        mask = np.array([x == m for x in month_years])
        sales.append(np.sum(data['Total'][mask]))
    return unique_months, sales
