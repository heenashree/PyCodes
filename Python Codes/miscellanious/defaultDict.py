#collections has defaultdict, namedTuple, OrderedDict

# defualtdict is used when you have to give a default key to the dictionary. You can use lambda to start dictionary with a number
'''
x = defaultDict(int)
or
x = defaultDict(lambda:100)
'''

# Demonstrate the usage of defaultdict objects
from collections import defaultdict

def main():

    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    '''
    fruitsCounter ={}
    for fruit in fruits:
        if fruit in fruitsCounter.keys():
            fruitsCounter[fruit] += 1
        else:
            fruitsCounter[fruit] = 1
    '''
    # to reduce above code we use defaultDict. So now if the key doenst exist,
    #defultDict will create one for you.
    fruitsCounter = defaultdict(int)
    for fruit in fruits:
        fruitsCounter[fruit]+=1
    # fruitCounter = defultDict(lambda:100) key will start at 100
    for (k, v) in fruitsCounter.items():
        print(k + ": " + str(v))
if __name__ == "__main__":
    main()
