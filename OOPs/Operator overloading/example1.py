# operator overloading. We have basic operations done behind the scene but what if we want to add objects. In that case we perfomr operator overloading
# Lets take a simple example below
a = 2
b = 3
print(a+b)
# or the above is of type int and int is a class which has methods called __add__
print(int.__add__(a,b))
#output
#5
#5
# the output for both is same. here __add__ , __sub__ are all magic methods


#https://www.youtube.com/watch?v=9wd50TKv_OQ

#
# a = '5'
# b = '6'
#
# print(a + b)
#
# print(str.__add__(a,b))

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return  s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format( self.m1,self.m2)


s1 = Student(58,69)
s2 = Student(69,65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a.__str__())

print(s2)