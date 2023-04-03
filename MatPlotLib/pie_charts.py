import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ['r', 'g', 'b', 'k']

plt.pie(y, labels=mylabels, explode=myexplode)
# plt.legend(title="Fruits")
plt.show()
