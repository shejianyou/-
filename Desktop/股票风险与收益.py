# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:38:53 2019

@author: 23909
"""
import datetime
import pandas as pd
import pandas_datareader.data as web
start = datetime.datetime(1980, 1, 1)
end = datetime.date.today()
df = web.DataReader('AAPL', 'yahoo', start, end)
print(df.head(1000000))
df.to_csv(r'E:\stock\apple.csv',index=True)

StockPrices = pd.read_csv(r'E:\stock\apple.csv',parse_dates=['Date'], index_col='Date')

