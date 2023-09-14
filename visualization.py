'''
This file contains functions to create interactive visualizations of the sales data and forecasting results.
'''
import pandas as pd
import streamlit as st
import plotly.express as px
def create_visualizations(sales_data, forecast_data):
    # Visualize sales data
    st.subheader("Sales Data")
    fig_sales = px.line(sales_data, x='Date', y='Sales')
    st.plotly_chart(fig_sales)
    # Visualize sales forecasting
    st.subheader("Sales Forecasting")
    forecast_dates = pd.date_range(start=sales_data['Date'].max(), periods=len(forecast_data)+1, closed='right')
    forecast_dates = forecast_dates[1:]  # Exclude the last date from sales data
    forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecast_data})
    fig_forecast = px.line(forecast_df, x='Date', y='Forecast')
    st.plotly_chart(fig_forecast)
