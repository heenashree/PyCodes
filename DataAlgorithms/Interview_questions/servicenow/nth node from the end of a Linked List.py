#create a list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    #Function to get the nth node from last of a linked list

    def nthfromlast(self, n):
        temp = self.head
        length =0
        while temp is not None:
            temp=temp.next
            length = length +1
            