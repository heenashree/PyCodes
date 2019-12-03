# Python doesnt have overloading concept, insteady you can use *args
#  For overiding, check below example

class A:

    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B Show")
        super().__init__()


a1 = B()
a1.show()
