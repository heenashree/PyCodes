# code

if __name__ == "__main__":
    number_of_inputes = input()
    for i in range(int(number_of_inputes)):
        len_of_array, y = input().split()
        x = [int(i) for i in input().split()]

        # result = [4,6,1,10,20,2], [6,1,10,20,2,4]

        k = x[int(y):] + x[0:int(y)]
        print(' '.join(str(v) for v in k))
