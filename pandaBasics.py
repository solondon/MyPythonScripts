import pandas as pd
import datetime
import pandas.io.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("XOM", "yahoo", start, end) #pulls data for Exxon from the Yahoo Finance API, storing the data to our df variable

#print(df.head())

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df['High'].plot()
plt.legend()
plt.show()
