import collections

def main():
    Point = collections.namedtuple("Point", "X Y")
    p1 = Point(10,20)
    p2 = Point(20,30)
    print(p1, p2)
    print(p1.X, p1.Y)

    p1 = p1._replace(X=100)
    print(p1.X)



if __name__ == "__main__":
    main()