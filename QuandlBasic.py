import pandas as pd
import quandl

quandl.ApiConfig.api_key = "cRh7FgUrx7zsJVcmjtxP" # key for > 50 calls a day to quandl
##df = quandl.get("WGC/GOLD_DAILY_EUR")
df = quandl.get("BUNDESBANK/BBK01_WT5511", authtoken="cRh7FgUrx7zsJVcmjtxP")
print(df.head())

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df['Value'].plot()
plt.legend()
plt.show()
