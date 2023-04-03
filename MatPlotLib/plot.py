import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, marker='o', markersize=20, markeredgecolor='#000000', markerfacecolor='#4CAF50', linestyle='solid', color='r', linewidth=10)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title('Title', fontdict=font1, loc='center')
plt.xlabel('X-Axis', fontdict=font2)
plt.ylabel('Y-Axis', fontdict=font2)

plt.show()
