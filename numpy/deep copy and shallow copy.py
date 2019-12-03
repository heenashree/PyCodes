from numpy import *

arr1=array([1,2,3,4])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

print("Example above is a copy and has same address so basically both the array point to the same location")

arr1[1] = 4
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
print("above example changes both the array")

arr2 = arr1.view()
print(id(arr1))
print(id(arr2))
print("with view the id of both the array is different. That means we now have 2 different arrays")
arr1[2] = 11
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
print("but even so, if we change arr1, arr2 is also changing. THIS IS SHALLOW COPY")

arr2 = arr1.copy()
arr1[2] = 111
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
print("The above is an example of DEEP COPY")




