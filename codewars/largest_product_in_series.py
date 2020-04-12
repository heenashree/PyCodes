def greatest_product(n):
    list_n = [int(i) for i in n]
    k = []
    for i in range(len(list_n)-4):

        tmp = list_n[i] * list_n[i + 1] * list_n[i + 2] * list_n[i + 3] * list_n[i + 4]
        k.append(tmp)


    return max(k)


greatest_product("395831238345393272382")