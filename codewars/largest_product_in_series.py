def greatest_product(n):
    list_n = [int(i) for i in n]
    k = []
    tmp1=1
    for i,j in enumerate(list_n):
        print(i,j)
    for i in range(len(list_n)-4):

        tmp = list_n[i] * list_n[i + 1] * list_n[i + 2] * list_n[i + 3] * list_n[i + 4]
        k.append(tmp)
        '''
        except IndexError:
            print("index error", i-1)
            t1 = i-1
            break

    for k1 in range(t1, len(list_n)):
        print("value", list_n[k1])
        tmp1 = list_n[k1]*tmp1
        print(tmp1)
        
    k.append(tmp1)
    '''
    print(k)
    return max(k)


greatest_product("395831238345393272382")