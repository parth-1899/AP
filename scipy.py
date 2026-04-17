import numpy as np
from scipy import constants
from scipy import integrate
from scipy import optimize
from scipy import linalg
from scipy import fft

a = constants.pi
print("pi =",a)

def f(x):
    return x*x

i = integrate.quad(f,0,2)
print("integration =",i)

def g(x):
    return x*x - 4

r = optimize.root(g,0)
print("root =",r.x)

m = np.array([[1,2],[3,4]])
inv = linalg.inv(m)
det = linalg.det(m)

print("inverse =",inv)
print("det =",det)

x = np.array([1,2,3,4])
y = fft.fft(x)

print("fft =",y)
