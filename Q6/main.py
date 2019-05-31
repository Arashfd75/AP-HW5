import sys
import math
from pyGausssolver import pyGausssolver
from time import time as epochTime
import subprocess
import matplotlib.pyplot as plt

def aFunction(x):
    xN = 0.5 * x + 0.5
    return ((xN**3) / (xN + 1)) * math.cos(xN**2)
pf = aFunction
a = 0
b = 1
n = sys.argv[1]
#n=2
start = epochTime()
aSolver = pyGausssolver(pf,a,b,int(n))
aSolver.exec()
print(aSolver.getResult())
print(f"took {(epochTime() - start) * 1000:.4f} ms\n")
start = epochTime()
subprocess.call(['./main', f'{n}'])
print(f"took {(epochTime() - start) * 1000:.4f} ms\n")

pythonTime = []
cTime = []
inputList = range(1, int(n) + 1)
for i in inputList:
    start = epochTime()
    aSolver = pyGausssolver(pf, 0, 1, i)
    aSolver.exec()
    pythonTime.append((epochTime() - start) * 1000)
    print(f"\n Result of Python code (n = {i}) : {aSolver.getResult():.20f}")
    start = epochTime()
    subprocess.call(['./main', f'{i}'])
    cTime.append((epochTime() - start) * 1000)


print("\n\nDegree \t Python \t C++")
for i in inputList:
    print(f"{i} \t {pythonTime[i - 1]:.5f}ms \t {cTime[i - 1]:.5f}ms")

f = plt.figure()
plt.plot(inputList, pythonTime, label="Python")
plt.plot(inputList, cTime, label="C++")
plt.xlabel('Degree')
plt.ylabel('Time in ms')
plt.legend()
plt.show()
f.savefig("result.pdf")

