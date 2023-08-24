#Basic Queue structure

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Queue:
	def __init__(self, maxsize):
		self.front = self.rear = None	#!!
		self.maxsize = maxsize
		self.size = 0 

	'''def Qsize(self):
		return self.size
		if self.isEmpty() is None:
			return 0
		else:
			currNode = self.front
			size = 0
			while True:
				if currNode is None:
					return size
				else:
					currNode = currNode.next
					size += 1'''
	
	def isEmpty(self):
		return self.front==None		#!!
	
	def Enqueue(self, newNode):
		#temp = Node(newNode)
		#size = self.Qsize()
		self.size +=1
		if self.size <= self.maxsize:
			if self.rear is None:    #Empty Queue
				self.front = newNode
				self.rear = newNode
				#print(self.size)
				return
			else:
				self.rear.next = newNode
				self.rear = newNode
				#print(self.size)
		else:
			print("Tried Enqueue",newNode.data,",Queue Overflow")
		
	def Dequeue(self):
		if self.isEmpty():
			print("Tried Dequeue, Queue Underflow")
			return
		else:
			temp = self.front
			self.front = temp.next
			self.size -= 1
			return temp.data
		
		'''if self.front is None:
			self.rear = None
			self.size = 0'''
	
	def printQueue(self):
		if self.isEmpty():
			print("Queue is Empty")
		else:
			currNode = self.front
			while True:
				if currNode.next is None:
					print(currNode.data)
					return
				else:
					print(currNode.data, end=' ')
					currNode = currNode.next

#Driver's code      should add if maxsize == len(a):
maxsize = int(input())
a = list(map(int,input().split()))
queue = Queue(maxsize)
for i in a:
	node = Node(i)
	queue.Enqueue(node)

queue.printQueue()
queue.Dequeue()
b=queue.isEmpty()
queue.printQueue()
#queue.Enqueue(Node(69))
print(b)
queue.printQueue()
print(queue.size)