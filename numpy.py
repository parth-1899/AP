import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,4,3,2,1])

print("a =",a)
print("b =",b)

print("add =",a+b)
print("sub =",a-b)
print("mul =",a*b)
print("div =",a/b)

print("sum =",np.sum(a))
print("mean =",np.mean(a))
print("max =",np.max(a))
print("min =",np.min(a))

print("sqrt =",np.sqrt(a))
print("square =",np.square(a))

print("sorted =",np.sort(a))
print("unique =",np.unique(a))

c = np.arange(0,10)
print("arange =",c)

d = np.linspace(0,1,5)
print("linspace =",d)

e = np.zeros(5)
print("zeros =",e)

f = np.ones(5)
print("ones =",f)

g = np.reshape(a,(5,1))
print("reshape =",g)

print("shape =",a.shape)
