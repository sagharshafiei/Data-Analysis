import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt
from persiantools.jdatetime import JalaliDate

def week_day(btc_date):
    return JalaliDate(btc_date).isoweekday()

df = yf.download("BTC-USD", start="2020-01-01", end="2024-12-31")
df["Date"] = df.index

df["WeekDay"] = df["Date"].apply(week_day)

day_filter = (df["WeekDay"] == 6) | (df["WeekDay"] == 2)
filtered_df = df[day_filter]

filtered_df["Close_5"] = filtered_df["Close"].shift(-1)
filtered_df.dropna(inplace=True)

new_df = filtered_df[["Open", "Close_5"]]


amount = 1000
amount_list = []

for i in range(len(new_df)):
    amount_list.append(amount- 1000)
    btc_amount = amount /  new_df["Open"].iloc[i]
    amount = btc_amount * new_df["Close_5"].iloc[i]
    print(amount)



plt.plot(amount_list)
plt.show()


