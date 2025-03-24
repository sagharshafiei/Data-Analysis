import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("BTC-USD", start="2025-01-01", end="2025-01-25")

X = df.Close.values

plt.plot(X, label="Close")

this_min = np.min(X)
print(f"min is : {this_min}")
this_max = np.max(X)
print(f"max is : {this_max}")

y1 = this_min
y2 = this_max
x1 = 8
x2 = 20

slope = (y2-y1) / (x2-x1)
print(f"slope is :{slope}")


distance = np.sqrt(np.power((x2-x1),2) + np.power((y2-y1),2))
print(f"distance is: {distance}")


plt.plot([8,20], [this_min, this_max])

plt.show()