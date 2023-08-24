#Basic Dequeue Structure

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Dequeue:
	def __init__(self, maxsize):
		self.front = self.rear = None
		self.maxsize = maxsize
		self.size = 0
	
	def isEmpty(self):
		return self.front==None

	def Qsize(self):
		return self.size
	
	def addFront(self, newNode):
		self.size += 1
		if self.size <= self.maxsize:
			if self.rear == self.front == None:
				self.rear = newNode
				self.front = newNode
			else:
				newNode.next = self.front
				self.front = newNode
				
				'''temp = self.front
				newNode = self.front
				newNode.next = temp'''
		else:
			print("Dequeue Overflow")
			self.size -=1
		
	def addRear(self,newNode):
		self.size += 1
		if self.size <= self.maxsize:
			if self.rear == self.front == None:
				self.rear = newNode
				self.front = newNode
			else:
				self.rear.next = newNode
				self.rear = newNode
		else:
			print("Dequeue Overflow")
			self.size -= 1
	
	def delFront(self):
		if self.front == self.rear == None:
			print("Dequeue Uderflow")
			self.size = 0
		else:
			temp = self.front
			self.front = self.front.next
			temp.next = None
			self.size -= 1
		
		'''if self.front is None:
			self.rear = None
			self.size =0'''
	
	def delRear(self):
		pass
	
	def printQueue(self):
		if self.front == self.rear == None:
			print("Dequeue Empty")
		else:
			currNode = self.front
			while True:
				if currNode.next is None:
					print(currNode.data)
					#print(self.size)
					return
				else:
					print(currNode.data, end=' ')
					currNode = currNode.next
	
#Driver's Code
maxsize = int(input())
a = list(map(int,input().split()))
queue = Dequeue(maxsize)
for i in a:
	node = Node(i)
	queue.addRear(node)

queue.printQueue()










