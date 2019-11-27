class test():
    def __init__(self):
        self.name = 'Heena'
        self.lname = 'Shree'
        self.age = 29
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    cls = test()
    print(cls.name)
    print(repr(cls.name))
    print(str(cls.name))
    print(repr(cls))
    print(str(cls))