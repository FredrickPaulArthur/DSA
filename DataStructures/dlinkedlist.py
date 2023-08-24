class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DLL:
	def __init__(self):
		self.head = None
		self.last = None
		self.length = 0
	
	def decrement(self):
		self.length -= 1
	
	def isListEmpty(self):
		pass
	
	def addFront(self, newNode):
		if self.head is None:
			self.head = newNode
			self.head.next = None
			self.head.prev = None
			self.last = self.head
		else:
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode
		self.length += 1
	
	def deleteFront(self):
		temp = self.head.next 
		temp.prev = None
		self.head.next = None
		self.head = temp
		self.decrement()
		return
			
	def addEnd(self, newNode):
		if self.head is None:
			self.head = newNode
			self.head.next = None
			self.head.prev = None
			self.last = self.head
		else:
			newNode.prev = self.last
			self.last.next = newNode
			self.last = newNode
		self.length +=1
	
	def deleteEnd(self):
		temp = self.last.prev
		temp.next = None
		self.last.prev = None
		self.last = temp
		self.decrement()
		return
	
	def deleteNode(self, delNode):
		if self.head is None:
			print("Cannot delete, list is empty")
			return
		
		elif self.head.data == delNode.data:	#Head node
			self.deleteFront()
			return
			
		elif (self.head.data != delNode.data)and(self.last.data != delNode.data):
			currNode = self.head					#Anywhere middle
			while True:								#If this happend "Last Node" will not happen
				if currNode is None:
					break
				if delNode.data == currNode.data:
					prevNode = currNode.prev
					prevNode.next = currNode.next
					prevNode.next.prev = prevNode
					currNode.next = currNode.prev = None
					self.decrement()
					return
				currNode = currNode.next
		
		elif self.last.data == delNode.data:			#Last node
			self.deleteEnd()
			return
		
		print("Nothing was deleted")
	
	def deleteAt(self, position):
		if self.head is None or not(0 < position <= self.length):
			print("Cannot delete, list is empty or wrong position")
			return
		
		elif position == 1:
			self.deleteFront()
			return
		
		elif position == self.length:
			self.deleteEnd()
			return
		
		else:
			currNode = self.head
			currPos = 1
			while True:
				if currPos ==self.length:
					break
				if currPos == position:
					prevNode = currNode.prev
					prevNode.next = currNode.next
					prevNode.next.prev = prevNode
					currNode.next = currNode.prev = None
					self.decrement()
					return
				currNode = currNode.next
				currPos +=1
	
	def printList(self):
		if self.head is None:
			print("List is Empty")
		else:
			currNode = self.head
			while True:
				if currNode.next is None:
					print(currNode.data)
					break
				else:
					print(currNode.data, end=' ')
					currNode = currNode.next
	
	def printReverse(self):
		if self.head is None:
			print('List is Empty')
		else:
			currNode = self.last
			while True:
				if currNode.prev is None:
					print(currNode.data)
					break
				else:
					print(currNode.data, end=' ')
					currNode = currNode.prev
	
#Driver's code
n = int(input())
a = list(map(int,input().split()))
dll = DLL()
for i in a:
	i = Node(i)
	dll.addEnd(i)

dll.deleteAt(1)
dll.printList()
dll.printReverse()
print(dll.length)



