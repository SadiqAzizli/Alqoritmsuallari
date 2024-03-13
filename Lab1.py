#26
import math

eps=0.01
x=float(input("x = "))
d=0
k=1
y=1
while abs(y)>eps:
    y=(math.sin(x*k))/math.factorial(k+1)
    k+=1
    d+=y
print(d)
