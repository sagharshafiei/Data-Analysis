from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import arabic_reshaper
from bidi.algorithm import get_display

# اطلاعات 10 شهر مهم ایران
cities = [
    {"name": "تهران", "lat": 35.6892, "lon": 51.3890, "pop": 8693706},
    {"name": "مشهد", "lat": 36.2605, "lon": 59.6168, "pop": 3001184},
    {"name": "اصفهان", "lat": 32.6539, "lon": 51.6660, "pop": 1961260},
    {"name": "کرج", "lat": 35.8400, "lon": 50.9391, "pop": 1592492},
    {"name": "شیراز", "lat": 29.5926, "lon": 52.5836, "pop": 1565572},
    {"name": "تبریز", "lat": 38.0962, "lon": 46.2738, "pop": 1558693},
    {"name": "قم", "lat": 34.6416, "lon": 50.8746, "pop": 1201158},
    {"name": "اهواز", "lat": 31.3183, "lon": 48.6706, "pop": 1184788},
    {"name": "کرمانشاه", "lat": 34.3277, "lon": 47.0778, "pop": 952285},
    {"name": "ارومیه", "lat": 37.5522, "lon": 45.0761, "pop": 736224}
]

# تنظیم فونت برای نمایش فارسی در matplotlib
plt.rcParams["font.family"] = "B Nazanin"  # یا یک فونت فارسی دیگر

fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

m = Basemap(
    llcrnrlon=44, llcrnrlat=25,
    urcrnrlon=63, urcrnrlat=39.5,
    resolution='l', projection='merc',
    lat_0=32, lon_0=53
)

x, y, pop_sizes = [], [], []
for city in cities:
    xi, yi = m(city["lon"], city["lat"])
    x.append(xi)
    y.append(yi)
    pop_sizes.append(city["pop"] / 10000)

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray')
m.scatter(x, y, s=pop_sizes, color='red', alpha=0.7, edgecolor='black')

# افزودن نام شهرها با اصلاح راست‌به‌چپ
for city, xi, yi in zip(cities, x, y):
    text = get_display(arabic_reshaper.reshape(city["name"]))
    ax.text(xi + 10000, yi + 10000, text, fontsize=10, va='center', ha='center')

# اصلاح عنوان با فونت فارسی
title = get_display(arabic_reshaper.reshape("۱۰ شهر پرجمعیت ایران (اندازه نقطه متناسب با جمعیت)"))
plt.title(title, fontsize=14, pad=20)

m.drawparallels(np.arange(25, 40, 5), labels=[1,0,0,0])
m.drawmeridians(np.arange(45, 65, 5), labels=[0,0,0,1])

plt.show()