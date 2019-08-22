class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def Endinsert(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode =self.head
            while True:
                if lastnode.next is None:  # last node
                    break
                lastnode = lastnode.next  # we go to next node which is ben
            lastnode.next = newnode

    def Homeinsert(self,newnode):
        tempnode = self.head
        self.head = newnode
        newnode.next = tempnode

    def InBetweenInsert(self, node, position):
        currentNode = self.head
        currentPosition  = 0
        while True:
            if currentPosition == position:
                previousNode.next=node
                node.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition+=1

    def deletenode(self):
        currentnode = self.head
        while currentnode.next is not None:
            previousNode = currentnode
            currentnode = currentnode.next
        previousNode.next=None


    def printlist(self):
        currenetnode = self.head
        while currenetnode:
            print(currenetnode.data)
            currenetnode = currenetnode.next

    def DeleteFrom(self, position):
        #traverse the list
        currentnode = self.head
        currentposition = 0
        while currentnode:
            if currentposition == position:
                previousnode.next = currentnode.next
                currentnode.next=None
                break
            previousnode=currentnode
            currentnode=currentnode.next
            currentposition+=1



firstnode = Node("J")
linkedlist = Linkedlist()
linkedlist.Endinsert(firstnode)

secondnode = Node("J12")
linkedlist.Endinsert(secondnode)

thirdnode = Node("J22")
linkedlist.Endinsert(thirdnode)



homenode = Node("Heena")
linkedlist.Homeinsert(homenode)

betweennode = Node("I am in between")
linkedlist.InBetweenInsert(betweennode, 2)
print("before")
linkedlist.printlist()

print("after")
linkedlist.DeleteFrom(1)
linkedlist.printlist()