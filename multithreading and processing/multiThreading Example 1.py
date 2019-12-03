# https://www.youtube.com/watch?v=GqHLztqy0PU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=67
#https://www.youtube.com/watch?v=PJ4t2U15ACo
import threading
import time
'''
def calc_square(arr1):
    for n in arr1:
        print('square', n*n)

def calc_cube(arr2):
    for n in arr2:
        print('cube', n*n*n)

arr1 = [2,3,4,5]
arr2=[1,3,5,7]

calc_square(arr1)
calc_cube(arr2)
print("the above example run line by line, first calc_square is called and then calc_cube is called")
'''
def calc_square(arr):

    for n in arr:
        time.sleep(1)
        print('square', n*n)

def calc_cube(arr):
    for n in arr:
        time.sleep(1)
        print('cube', n*n*n)

arr1 = [2,3,4,5]
arr2=[1,3,5,7]

t1 = threading.Thread(target=calc_square, args=(arr1,)) #this is first thread
t2 = threading.Thread(target=calc_cube, args=(arr2,)) # this is second thread
t1.start()
t2.start()
t1.join()
t2.join()
print("Without time.sleep() you will not be able to see that there are 2 threads t1 and t2 working simultaneoulsy. also there is a main thread which will"
      "take care of the other prints for example this print itself. To make sure that this print runs after all threads has been run, you use join t1.join and t2.join")