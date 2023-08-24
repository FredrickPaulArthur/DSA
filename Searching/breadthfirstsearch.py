#To print BFS traversal from a given source vertex
#BFS(int s) traverses vertices reachable from s
from collections import defaultdict
#Class represents a directed graph using
#adjacency list representation
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    #To print BFS of graph
    def BFS(self,s):
        #Mark all the vertices as not visited
        visited=[False]*(len(self.graph))
        queue=[]
        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s]=True
        while queue:
            #Dequeue a vertex from queue and print it
            s=queue.pop(0)
            print(s,end=' ')
            #Get all adjacent vertices of the dequeued vertex s
            #If adjacent has not been visied, then mark it 
            #visited and enqueue it
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g=Graph()
n=int(input("Enter the size of graph "))
print("Enter u and then v ")
for i in range(n):
    x,y=map(int,input().split())
    g.addEdge(x,y)
ver=int(input("The vertex for starting "))
print("Following is Breadth First Traversal"
                    "(starting from vertex 2)")
g.BFS(ver)