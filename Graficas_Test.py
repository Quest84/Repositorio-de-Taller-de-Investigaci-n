import numpy as np
import matplotlib.pyplot as plt

CSVData = open('Test.csv')
Array = np.loadtxt(CSVData, delimiter=",")

N = []
Data = []
i = 0
for x in Array:
    i = i + 1 
    N.append(i)
    Data.append(x)

print(N)
print(Data)

fig, ax = plt.subplots()
ax.plot(N, Data)

ax.set(xlabel='time (n)', ylabel='Medida (px)',
       title='Grafica')
ax.grid()
plt.xticks( N )

fig.savefig("test.png")
plt.show()
