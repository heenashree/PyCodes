# code

if __name__ == "__main__":
    number_of_inputes = input()
    for i in range(int(number_of_inputes)):
        len_of_array, y = input().split()
        x = [int(i) for i in input().split()]
        r = int(y) % int(len_of_array)
        k = x[int(r):] + x[0:int(r)]
        print(' '.join(str(v) for v in k))
