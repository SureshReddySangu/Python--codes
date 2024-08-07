import math as m
import numpy as np
import matplotlib.pyplot as plt
s1=[]
s2 = []

def f(maxtime): 
    for qtime in range(maxtime):
        ez = m.exp(-((qtime-30)*(qtime-30))/100)
        print(ez)  
        s1.append(ez)
        s2.append(qtime)
    return s1

c =f(200)
print(s2)
plt.figure(figsize=(10, 6)) 
plt.plot(s2,s1)
plt.show()