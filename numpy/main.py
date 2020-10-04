# https://docs.scipy.org/doc/
import numpy as np

# a = np.array([1,2,3.3])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# print(a.size)
# print(a.itemsize)
# print(a.nbytes)

# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a[1, 2])

# a = np.zeros((2,2,2))
# a = np.random.rand(4,2)




# a = np.ones((5,5))
# b = np.zeros((3,3))
# b[1,1] = 9
#
# a[1:4,1:4] = b

# a = np.array([1,2,3,4])
# print(a.mean())

a = np.genfromtxt('data.txt',delimiter=',').astype('int32')
print(a)