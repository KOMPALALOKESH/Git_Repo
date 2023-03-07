# Singly Linked List..
from socket import inet_aton


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Slinkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def insertsll(self,value,location):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == 1:
                self.tail.next = newnode
                self.tail = newnode
            else:
                index = 0
                tempNode  = self.head
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newnode.next = tempNode.next
                tempNode.next = newnode
    def printSll(self):
        tempNode = self.head
        if tempNode is None:
            print("Linked List is empty.")
        else:
            while tempNode:
                print(tempNode.value , end = " ")
                tempNode = tempNode.next
        print(end = "\n")
    def SearchValue(self,Value):
        tempNode = self.head
        if self.head is None:
            return "List not exist."
        else:
            while tempNode is not None:
                if tempNode.value is Value:
                    return tempNode.value
                tempNode = tempNode.next
            return "Value not exist."
    def deleteNode(self,position):
        if self.head == None:
            return "List not exist."
        else:
            if position == 'start':
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    self.head = tempNode.next
                    tempNode.next = None
            elif position == 'end':
                if self.head is self.tail:
                    self.head,self.tail = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next is self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                nextNode = self.head
                tempNode = None
                index = 0
                while index < position - 1:
                    tempNode = nextNode
                    nextNode = nextNode.next
                    index += 1
                tempNode.next = nextNode.next
                nextNode.next = None


Sll = Slinkedlist()
Sll.insertsll(1,1)
Sll.insertsll(2,1)
Sll.insertsll(3,1)
Sll.insertsll(4,1)
Sll.insertsll(5,1)
Sll.printSll()
# print([node.value for node in Sll])
# print(Sll.SearchValue(4))
Sll.deleteNode('start')
Sll.printSll()
Sll.deleteNode(2)
Sll.printSll()
Sll.deleteNode('end')
Sll.printSll()