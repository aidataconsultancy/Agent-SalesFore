'''
This file contains functions to perform the sales forecasting using the generated data.
'''
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
def perform_forecasting(sales_data):
    # Perform sales forecasting using ARIMA model
    model = ARIMA(sales_data['Sales'], order=(1, 1, 1))
    model_fit = model.fit()
    forecast_data = model_fit.predict(start=len(sales_data), end=len(sales_data)+30)
    return forecast_data