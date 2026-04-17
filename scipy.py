import numpy as np
from scipy import constants
from scipy import integrate
from scipy import optimize
from scipy import linalg
from scipy import fft
from scipy import ndimage

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
print("det =",linalg.det(m))
print("inv =",linalg.inv(m))

x = np.array([1,2,3,4])
print("fft =",fft.fft(x))

img = np.array([[1,2,3],[4,5,6],[7,8,9]])
blur = ndimage.gaussian_filter(img,1)

print("image =",img)
print("blur =",blur)
