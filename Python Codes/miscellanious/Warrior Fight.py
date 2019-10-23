class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        return True if self.health > 0 else False


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7


def fight(a, b):
    while a.is_alive and b.is_alive:
        b.health -= a.attack
        a.health -= b.attack
        if b.health <= 0:
            b.is_alive = False
            return True
        elif a.health <= 0:
            a.is_alive = False
            return False
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
