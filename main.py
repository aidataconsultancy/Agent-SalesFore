'''
This is the main file that runs the Streamlit web application.
'''
import streamlit as st
from data_generator import generate_sales_data
from forecasting import perform_forecasting
from visualization import create_visualizations
def main():
    st.title("Sales Forecasting Project")
    # Generate dummy sales data
    sales_data = generate_sales_data()
    # Perform sales forecasting
    forecast_data = perform_forecasting(sales_data)
    # Create interactive visualizations
    create_visualizations(sales_data, forecast_data)
if __name__ == "__main__":
    main()