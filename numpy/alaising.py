from numpy import *

arr1=array([1,2,3,4])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

print("Example above is a copy and has same address so basially both the array point to the same location")