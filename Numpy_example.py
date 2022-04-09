import numpy as np
import sys
import time

#creation of numpy
array1 = np.array([10,20,30])
print(array1)
# creation of 1D array
array2 = np.array([5, -7.4, 'a', 7.2])
print(array2)
# creation of 2D array
array2 =  np.array([[2.4,3], [4.91,7],[0,-1]])
print(array2)
#check number of dimensions
array2 =  np.array([[2.4,3], [4.91,7],[0,-1]])
print(array2.ndim)
#numpy vs list

s=range(1000)
print("Size of Python List:")
print(sys.getsizeof(75)*len(s))

d=np.arange(1000)
print("Size of NumPy:")
print(d.size*d.itemsize)
#Numpy is faster than list

Size=1000000
L1 = range(Size)
L2 = range(Size)

A1 = np.arange(Size)
A2 = np.arange(Size)

start = time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print("Time for execute Python List")
print((time.time()-start)*1000)

start=time.time()
result=A1+A2
print("Time for execute NumPy")
print((time.time()-start)*1000)
#Access array elements
arr = np.array([1, 2, 3, 4])

print(arr[0])
#Access 2D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[1, 1])
#Access 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

#slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

#slicing 2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4
#Array shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)
#array reshaping 1D-2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)
#reshape 1D-3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
#Arithmetic operations
array1 = np.array([(10,20,30),(10,11,12)])
print(array1)
array2 =  np.array([(24,31,22), (41,17,8)])
print("Addition:",array1+array2)
print("Subtraction:",array1-array2)
print("Multiplication:",array1*array2)
print("Division:",array1/array2)
#Transpose
array1 = np.array([(10,20,30),(10,11,12)])
print('Before transposing:')
print(array1)
print('After transposing:')
print(array1.transpose())

#sorting
array1 = np.array([(30,10,20),(110,101,102)])
print('Before sorting:')
print(array1)
print('After sorting:')
print(np.sort(array1))
#concatenating
array1 = np.array([(30,10,20),(110,101,102)])
array2 =  np.array([(24,31,22), (41,17,8)])
print('After concatenating:')
print(np.concatenate((array1,array2),axis=1))

