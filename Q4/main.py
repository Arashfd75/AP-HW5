import random
import math

def isInCircle(x,y):
    return (x*x + y*y) <= 0.25


PI = 3.1415
def find():
    count_inside = 0
    for count in range(0, 90000):
        x = random.random()-0.5
        y = random.random()-0.5
        if (isInCircle(x,y)): count_inside += 1
        count += 1
        pi = 4.0 * count_inside / count
        if(abs(pi - PI)/PI < 0.01):
            print(pi)
            return pi 

print(find())

sumPI = 0
n = input("please Enter a number")
print(n)
for i in range(int(n)):
    sumPI += find()

print("average of PI is = ", sumPI / int(n))