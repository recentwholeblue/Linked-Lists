#Initialize new nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None #Set head to none

    def insertAtBeginning(self, data):
        #Create node
        node = Node(data)
        node.next = self.head
        #Update head to new node
        self.head = node

    def insertAtEnd(self, data):
        #Create new node
        node = Node(data)
        #Set new node as head
        if self.head is None:
            self.head = node
            return
        #If not empty, go through the list until at end.
        current = self.head
        while current.next:
            current = current.next #Move to next ndoe
        current.next = node

    def deleteAtBeginning(self):
        #If empty list return nothing
        if self.head is None:
            return
        #Change head to link to next node
        self.head = self.head.next

    #Display linked list
    def display(self):
        current = self.head
        #Show each node while going through each node
        while current: 
            print(current.data, end=" -> ")  
            current = current.next
        print("None") #Show the end of list

ll=LinkedList()
x=0
ll.insertAtBeginning(0)
ll.insertAtEnd(2)
ll.display()
ll.deleteAtBeginning()
ll.display()
ll.insertAtBeginning(2)
while x<100:
    ll.insertAtBeginning(x)
    ll.display()
    x=x+1
