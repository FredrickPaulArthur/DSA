class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insertNode(self, newNode):
        if self.isListEmpty():
            self.head = newNode
            self.length +=1
            
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            self.length +=1
    
    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
        self.length +=1
    
    def insertAt(self, newNode, position):
        if position<0 or position >= self.length:  #self.listLength():
            print("Invalid position")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:  #skips the first time
                previousNode.next = newNode
                newNode.next = currentNode
                self.length +=1
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1

    def deleteNode(self, delNode):
        if self.isListEmpty():
            print("List is Empty, cannot delete")
            return
        elif delNode.data == self.head.data:
            self.deleteHead()
            return
        else:
            lastNode = self.head
            previousNode = None
            a = 0
            while True:
                #print(a,delNode.data,lastNode.data)
                if lastNode.data == delNode.data:
                    previousNode.next = lastNode.next
                    lastNode.next = None
                    self.length -=1
                    break
                previousNode = lastNode
                lastNode = lastNode.next
                a +=1
                if a == len(array):
                    print("No element found to delete")
                    break
            
    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead  = self.head
            self.head = self.head.next
            previousHead.next = None
            self.length -=1
        else:
            print("LinkedList is empty. Delete failed")
    
    def deleteAt(self,position):			#Deletes first appearance
        if position < 0 or position >= self.listLength():
            print("InvalidPosition")
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:        #skips the first time
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    self.length -=1
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition +=1
        else:
            print("List is empty")

    def deleteEnd(self):
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
            self.length -=1
        else:
            print("Linked list is empty. Delete failed")
            
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                print(currentNode.data)
                break
            print(currentNode.data, end=' ')
            currentNode = currentNode.next



#Driver's code
''' insertNode	insertHead	insertAt	insertEnd
	deleteHead	deleteAt	deleteEnd	deleteNode
	isListEmpty		printList	listLength '''
n = int(input())
m = input().split()      
linkedList = LinkedList()

for i in range(len(m)):
    node = Node(m[i])
    linkedList.insertNode(node)

linkedList.printList()
print(linkedList.head.data, linkedList.length)
linkedList.insertHead(Node('head'))
linkedList.insertAt(Node('at3'),3)
linkedList.insertNode(Node('end'))
linkedList.printList()
print(linkedList.head.data, linkedList.length)
