'''
Python | super() function with multilevel inheritance
super() function in Python:
Python super function provides us the facility to refer to the parent class explicitly. It is basically useful where we have to call superclass functions. It returns the proxy object that allows us to refer parent class by 'super'.

To understand Python super function we must know about the inheritance. In Python inheritance, the subclasses are inherited from the superclass.

Python Super function provides us the flexibility to do single level or multilevel inheritances and makes our work easier and comfortable. Keep one thing in mind that while referring the superclass from subclass, there is no need of writing the name of superclass explicitly.

Here is one example of how to call the super function in Python3:
'''

# parent class also sometime called the super class 
class Parentclass(): 
	def __init__(self): 
		pass

# derived or subclass 
# initialize the parent or base class within the subclass 
class subclass(Parentclass): 
	def __init__(self):
		# calling super() function to make process easier 
		super() 
