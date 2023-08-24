class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
class Stack:
	def __init__(self):
		self.head = None
	
	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False
	
	def push(self, newNode):
		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
	
	def pop(self):
		if self.isEmpty():
			print("Queue Empty")
			return None
		else:
			poppedNode = self.head
			self.head = self.head.next
			poppedNode.next = None
			return poppedNode.data
	
	def peek(self):
		if self.isEmpty():
			print("Queue Empty")
			return None
		else:
			return self.head.data
	
	def printStack(self):
		currNode = self.head
		if self.isEmpty():
			print("Queue Empty")
		else:
			while True:
				if currNode.next is None:
					print(currNode.data)
					break
				else:
					print(currNode.data, end=' ')
					currNode = currNode.next
					
#Driver's code
n=int(input())
a = list(map(int,input().split()))
stack = Stack()
for i in a:
	node = Node(i)
	stack.push(node)
stack.printStack()
print(stack.peek())
print(stack.pop())
stack.printStack()