import math
a=float(input())
b=float(input())
c=float(input())
delta=(b**2)-(4*a*c)
delta=math.sqrt(delta)
x1=(-b+delta)/(2*a)
x2=(-b-delta)/(2*a)
print(x1)
print(x2)
