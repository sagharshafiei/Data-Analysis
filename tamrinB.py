import yfinance as yf
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt


df = yf.download("BTC-USD", start="2020-01-01", end="2024-12-31")

df["Date"] = df.index
df["Weekday"] = df["Date"].dt.weekday

print(df[df["Weekday"] == 0]["Open"].mean())
print(df[df["Weekday"] == 1 ]["Open"].mean())
print(df[df["Weekday"] == 2 ]["Open"].mean())
print(df[df["Weekday"] == 3 ]["Open"].mean())
print(df[df["Weekday"] == 4 ]["Open"].mean())
print(df[df["Weekday"] == 5 ]["Open"].mean())
print(df[df["Weekday"] == 6 ]["Open"].mean())
