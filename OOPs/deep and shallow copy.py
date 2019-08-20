'''
Deep Copy
Deep copy is a process in which the copying process occurs recursively.
It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original.
In case of deep copy, a copy of object is copied in other object.
It means that any changes made to a copy of object do not reflect in the original object. In python, this is implemented using “deepcopy()” function.
'''
import copy
list1 = [1,2,3,4]
list2 = copy.deepcopy(list1)
list1.append(80)
list2.append(8) #this will not affect list1
print(list1, list2)

'''
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. 
The copying process does not recurse and therefore won’t create copies of the child objects themselves. 
In case of shallow copy, a reference of object is copied in other object. 
It means that any changes made to a copy of object do reflect in the original object. In python, this is implemented using “copy()” function.'''

list3 = [4,6,8]
list4 = copy.copy(list3)
list4.append(5)
list3.append(111)
print(list3, list4)