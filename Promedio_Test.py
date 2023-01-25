import numpy as np
import matplotlib.pyplot as plt

CSVData = open('Test.csv')
Array = np.loadtxt(CSVData, delimiter=",")

Data = []
Promedio = 0
i = 0
for x in Array:
    i = i + 1
    Promedio = Promedio + x 
    Data.append(x)

print(Data)
print("Promedio = " + str(Promedio/i) )
