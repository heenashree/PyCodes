rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)
print(id1, id2)
'''
On the memory issue, in Python when you "delete" you are basically removing a reference to an object. 
When an object is not referenced by any variable nor other object or becomes unreachable, 
it becomes garbage and can be removed from memory. 
Python has a garbage collector that from time to time it does this job of 
checking which objects are garbage and releases the memory allocated for them. 
If the object you are deleting from the dictionary is referenced by other variable 
then it is still reachable, thus it is not garbage so it won't be deleted. 
I leave you here some links if you are interested in reading about garbage collection in general 
and python's garbage collection in particular.

http://en.wikipedia.org/wiki/Garbage_collection_(computer_science)
http://www.digi.com/wiki/developer/index.php/Python_Garbage_Collection
http://www.doughellmann.com/PyMOTW/gc/
http://docs.python.org/library/gc.html
'''
