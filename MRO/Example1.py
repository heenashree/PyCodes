class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


class C(A, B):
    pass


#obj = C()
#obj.process()

# Output   class C(A, B):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B

#to solve this, just inherit from A, no need to inherit from B as well.Your GameObject is inheriting from Player and Enemy. Because Enemy already inherits from Player Python now cannot determine what class to look methods up on first; either Player, or on Enemy, which would override things defined in Player.

#You don't need to name all base classes of Enemy here; just inherit from that one class:

#class GameObject(Enemy):
#    pass
#Enemy already includes Player, you don't need to include it again.

class D(A):
    pass


obj = D()
obj.process()
