# make node class
#creating singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #initializing next to null

class LinkedList:
    def __init__(self):
        self.head = None

    #This will print the contents of the linked list
    #starting from head

    def printlist(self):
        temp = self.head
        print(self.head)

        while(temp):
            print (temp.data)
            temp= temp.next


if __name__ == "__main__":
    #start with empty list
    llist= LinkedList()
    print (llist)

    llist.head=Node(1)
    second = Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third
    llist.printlist()


