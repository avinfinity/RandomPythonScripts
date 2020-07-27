import numpy as np
dir(np.array)

arr1 = np.array([1,2,3,4,5], ndmin=1)
arr2 = np.array([1,2,3,4,5], ndmin=2)
arr3 = np.array([1,2,3,4,5], ndmin=3)

print(arr1)
print(arr2)
print(arr3)

c_arra = np.array([1,2,3,4,5], dtype=np.int32)
print(c_arra)

DataType = np.dtype(np.int32)
print(DataType)
print(np.dtype('i4'))


DataType = np.dtype([('Age',np.int8)])
arr = np.array([(10,),(20,),(30,)],dtype=DataType)
print(arr)
print(arr['Age'])

student = np.dtype([('Name','S40'),('Age', 'i1'), ('Marks','f4')])
arr = np.array([('Sam',16,50.01),('Harry',10,12.89)],dtype=student,ndmin = 2)
print(arr)

arr = np.array([[1,2,3,],[4,5,6]])
print(arr.shape)
print(arr)

arr.shape=(3,2)
print(arr.shape)
print(arr)

arr = np.arange(24)
print(arr)
print(arr.ndim)

arr1 = arr.reshape(2,4,3)
print(arr1)
print(arr1.ndim)

arr = np.array([1,2,3,4,5], dtype=np.float32)
print(arr.itemsize)

print(arr.flags)