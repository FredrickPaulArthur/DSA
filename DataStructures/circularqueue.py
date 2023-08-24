class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularQueue:
	def __init__(self):
		self.front = self.rear = None
		self.size = 0
	
	def isEmpty(self):
		if self.front == None:
			return True
	
	def Enqueue(self, newVal):
		newNode = Node(newVal)
        if self.isEmpty():
			self.front = self.rear = newNode
		else:
			self.rear.next = newNode
			self.rear = newNode
			self.rear.next = self.front
		self.size +=1
	
	def Dequeue(self):
		if self.isEmpty():
			print("Cannot dequeue, list is empty")
		elif self.size == 1:
			self.front = self.rear = None
			self.size = 0
		else:
			temp = self.front
			self.front = self.front.next
			self.rear.next = self.front
			temp.next = None
			self.size -=1
	
	def printQueue(self):
		if self.isEmpty():
			print("Cannot print, queue is empty")
		else:
			currNode = self.front
			pos = 1
			while True:
				if pos == self.size:
					print(currNode.data)
					break
				else:
					print(currNode.data, end=' ')
				currNode = currNode.next
				pos +=1

#Driver's code
a = [1, 2, 3, 4, 5, 6]
cq = CircularQueue()
for i in a:
	cq.Enqueue(i)

cq.printQueue()