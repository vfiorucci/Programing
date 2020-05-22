import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'QX5GBOT5PPMIOHI8'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min',outputsize='full')


close_data = data['4. close']
percent_change = close_data.pct_change()

# print(percent_change)

last_change = percent_change[-1]
i = 1
while i == 1:
    data, meta_data = ts.get_intraday(symbol='TSLA', interval='1min',outputsize='full')
    data.to_excel('output.xlsx')
    if abs(last_change) > 0.004:
        print('Tesala Alert Up: {:.2f}'.format(last_change*100))
    if abs(last_change) < -.004:
        print('Tesala Alert Down: {:.2f}'.format(last_change*100))
    time.sleep(60)