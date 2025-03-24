import yfinance as yf
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt


df = yf.download("BTC-USD", start="2020-01-01", end="2024-12-31")

df["Date"] = df.index
df["Month"] = df["Date"].dt.month


df["Benefit"] = (df[df["Month"] == 0 ]["Close"] - df[df["Month"] == 0 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 1 ]["Close"] - df[df["Month"] == 1 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 2 ]["Close"] - df[df["Month"] == 2 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 3 ]["Close"] - df[df["Month"] == 3 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 4 ]["Close"] - df[df["Month"] == 4 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 5 ]["Close"] - df[df["Month"] == 5 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 6 ]["Close"] - df[df["Month"] == 6 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 7 ]["Close"] - df[df["Month"] == 7 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 8 ]["Close"] - df[df["Month"] == 8 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 9 ]["Close"] - df[df["Month"] == 9 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 10 ]["Close"] - df[df["Month"] == 10 ]["Open"]).plot()
df["Benefit"] = (df[df["Month"] == 11 ]["Close"] - df[df["Month"] == 11 ]["Open"]).plot()


plt.show()