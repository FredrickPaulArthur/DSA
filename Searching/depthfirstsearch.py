#To print DFS traversal from a given graph
from collections import defaultdict
#This class represents a directed graph using
#adjacency list representation
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def DFSUtil(self,v,visited):
        #Mark the current node as visited and
        #print it
        visited[v]=True
        print(v,end=' ')
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)
    
    def DFS(self,v):
        #Mark all the vertices as not visited
        visited=[False]*(max(self.graph)+1)
        #Call the recursive helper function to
        #print DFS traversal
        self.DFSUtil(v,visited)

g=Graph()
n=int(input("Enter the size of graph "))
print("Enter u then v in same line at a time")
for i in range(n):
    x,y=map(int,input().split())
    g.addEdge(x,y)
ver=int(input("Vertex from which traversal shoul start from "))
g.DFS(ver)