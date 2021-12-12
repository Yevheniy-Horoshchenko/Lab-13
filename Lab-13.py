from scipy import integrate
from numpy import *
y = 0.4632 + 0.4574 + 0.4518 + 0.4463 + 0.4411 + 0.4360 + 0.4311 + 0.4264 + 0.4218 + 0.4174
b = 1.4
a = 0.8
n = 10
h = (b-a)/n
kv = y * h
def f(x):
    return 1/sqrt(2*x + 3)
v,err = integrate.quad(f,0.8,1.4)
print('The rectangle method=',kv)
print('Check for the rectangle method=',v)