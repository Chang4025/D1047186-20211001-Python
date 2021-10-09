import matplotlib.pyplot as plt
from math import factorial  #導入階層
B = []
for i in range (1,50):
    f =(1-((factorial(365)/((365**i)*(factorial(365-i))))))  #參考維基公式
    B.append(f)
times = [j for j in range (1,50)]

plt.xlim(1, 49)
plt.ylim(0, 1)
plt.xlabel("人數")
plt.ylabel("機率")
plt.plot(times, B)  #plt.plot(人數,機率)
plt.show()