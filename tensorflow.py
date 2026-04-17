import tensorflow as tf

a = tf.constant([1,2,3])
b = tf.constant([4,5,6])

print("a =",a)
print("b =",b)

c = tf.add(a,b)
d = tf.multiply(a,b)

print("add =",c)
print("mul =",d)

e = tf.reduce_sum(a)
f = tf.reduce_mean(a)

print("sum =",e)
print("mean =",f)

g = tf.reshape(a,[3,1])
print("reshape =",g)

h = tf.cast(a,tf.float32)
print("type =",h)
