import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from model import data_processing as dp
from view import visualization as vz

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'supermarket_sales.csv')
st.set_page_config(page_title="Supermarket Sales Dashboard",layout="wide")

def main():
    st.title("Supermarket Sales Analysis") 
    st.markdown("""
    This dashboard shows diverse and beautiful visualizations of supermarket sales data.
    Select a visualization from the dropdown below to explore insights.
    """)

    # Dropdown for visualization selection below title 
    options = [
        "Sales by Product Line (Bar Chart)", 
        "Sales by City (Pie Chart)", 
        "Sales Over Time (Line Chart)",
        "Quantity vs Gross Income (Scatter Plot)",
    ]
    choice = st.selectbox("Choose Visualization", options)

    data = dp.load_data(DATA_FILE)
    clean_data = dp.clean_data(data)

    total = dp.total_sales(clean_data)
    st.subheader(f"Total Sales: ${total:,.2f}")

    if choice == "Sales by Product Line (Bar Chart)":
        lines, sales = dp.sales_by_product_line(clean_data)
        plt = vz.plot_bar(lines, sales, "Sales by Product Line", "Product Line", "Sales ($)")
        st.pyplot(plt)

    elif choice == "Sales by City (Pie Chart)":
        cities, sales = dp.sales_by_city(clean_data)
        plt = vz.plot_pie(cities, sales, "Sales Distribution by City")
        st.pyplot(plt)

    elif choice == "Sales Over Time (Line Chart)":
        months, sales = dp.sales_over_time(clean_data)
        plt = vz.plot_line(months, sales, "Sales Over Time", "Month-Year", "Sales ($)")
        st.pyplot(plt)

    elif choice == "Quantity vs Gross Income (Scatter Plot)":
        quantity = clean_data['Quantity']
        gross_income = clean_data['gross_income']
        plt = vz.plot_scatter(quantity, gross_income, "Quantity vs Gross Income", "Quantity", "Gross Income")
        st.pyplot(plt)

if __name__ == '__main__':
    main()
