import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


die_choice = list(range(1,366))
times = 10000

die_list = np.random.choice(die_choice, times)
frequencies = [ sum(die_list==x)/times for x in range(1, 366)]
print(die_list)
plt.xlim(1, 366)
plt.ylim(0, 1)
plt.xlabel("die")
plt.ylabel("probability")
plt.plot(die_choice, frequencies)
#plt.plot(人數,機率)
plt.show()