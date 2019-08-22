#create the linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head= None

    def insert(self, newdata):
        new_node = newdata
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        print(self.head)

        while (temp):
            print(temp.data)
            temp = temp.next

    def inserthead(self, newnode):
        temhead = self.head
        self.head=newnode
        self.head.next=temhead







firstnode = Node("John")
linkedlist = LinkedList()

linkedlist.insert(firstnode)
secondNode = Node("ben")
linkedlist.insert(secondNode)


headnode = Node("basketttt")
linkedlist.inserthead(headnode)
linkedlist.printlist()

