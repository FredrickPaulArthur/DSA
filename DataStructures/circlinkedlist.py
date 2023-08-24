class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
class CLL:
	def __init__(self):
		self.head = self.tail = None
		self.length = 0
	
	def isEmpty(self):
		if self.head is None:
			return True
		
	def addFront(self, newNode):
		if self.isEmpty():
			self.head = self.tail = newNode
		else:
			newNode.next = self.head
			self.tail.next = newNode
			self.head = newNode
		self.length +=1
	
	def deleteFront(self):
		if self.isEmpty():
			print("List is Empty")
		else:
			temp = self.head
			self.tail.next = self.head.next
			temp.next = None
			self.head = self.tail.next
			self.length -=1
	
	def addEnd(self, newNode):
		if self.isEmpty():
			self.head = self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.next = self.head
			self.tail = self.tail.next
		self.length +=1
	
	def deleteEnd(self):
		if self.isEmpty():
			print("List is Empty")
		else:
			prevNode = self.tail
			currNode = self.head
			position = 1
			while True:
				if position == self.length:
					prevNode.next = currNode.next
					currNode.next = None
					self.length -=1
					break
				prevNode = prevNode.next
				currNode = currNode.next
				position +=1
				
	
	def deleteNode(self, delNode):
		if self.head is None:
			print("Cannot delete, list is empty")
			return
		
		elif self.head.data == delNode.data:	#Head node
			self.deleteFront()
			return
			
		elif (self.head.data != delNode.data)and(self.tail.data != delNode.data):
			prevNode = self.tail
			currNode = self.head					#Anywhere middle
			while True:								#If this happend "Last Node" will not happen
				if currNode is None:
					break
				if delNode.data == currNode.data:
					prevNode.next = currNode.next
					currNode.next = None
					self.length -=1
					return
				currNode = currNode.next
				prevNode = prevNode.next
		
		elif self.tail.data == delNode.data:			#Last node
			self.deleteEnd()
			return
		
		print("Nothing was deleted")
	
	def deleteAt(self, position):
		if 0 < position <= self.length:
			if self.isEmpty():
				print("List Empty, cannot delete")
			elif position == 1:
				self.deleteFront()
			elif position == self.length:
				self.deleteEnd()
			else:
				currPos = 2
				prevNode = self.head
				currNode = self.head.next
				while currPos <= self.length:
					if position == currPos:
						prevNode.next = currNode.next
						currNode.next = None
						self.length -=1
						break
					prevNode = prevNode.next
					currNode = currNode.next
					currPos +=1
		else:
			print("Invalid position for deleting")
	
	def printList(self):
		if self.isEmpty():
			print("Cannot print, List is empty")
		else:
			currNode = self.head
			pos = 0
			while True:
				if pos < self.length-1:
					print(currNode.data, end=" ")
					currNode = currNode.next
					pos +=1
				
				else:
					print(currNode.data)
					break
	
#Driver's Code
n = int(input())
a = list(map(int,input().split()))
if n == len(a):
	cll = CLL()
	for i in a:
		i = Node(i)
		cll.addFront(i)
	cll.printList()


