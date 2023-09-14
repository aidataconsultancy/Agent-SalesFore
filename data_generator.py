'''
This file contains functions to generate dummy sales data for the forecasting project.
'''
import pandas as pd
import random
def generate_sales_data():
    # Generate dummy sales data
    dates = pd.date_range(start='1/1/2022', end='12/31/2022', freq='D')
    sales = [random.randint(100, 1000) for _ in range(len(dates))]
    # Create a DataFrame with the generated data
    sales_data = pd.DataFrame({'Date': dates, 'Sales': sales})
    return sales_data