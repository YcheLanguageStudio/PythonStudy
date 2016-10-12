import numpy as np

x, y = np.loadtxt('stock.txt', unpack=True)
print '-'.join(map(str, np.polyfit(x, y, 1)))
