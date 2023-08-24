class Vertex:
    def __init__(self, val):
        self.val = val
        self.next = None



class Edge:
    def __init__(self, val, weight=1):
        #Vertex.__init__(self, val)
        self.val = val
        self.weight = weight
        self.next = None


# Maintain a separate list for edges 
class Graph(Edge):
    def __init__(self):
        self.graph = list()
        # I didnt use two lists for vertex=[] and edges=[] 
        # Instead I used a list of LinkedLists

    
    def addVertex(self, key):
        for v in self.graph:
            if v.val == key:
                return
        self.graph.append(Vertex(key))
    
    
    def addEdge(self, src, dest):
        # Making src and dest as Vertices
        self.addVertex(src)
        self.addVertex(dest)
        
        # Updating the Edges 
        src = Edge(src)
        dest = Edge(dest)
        for vertex in self.graph:
            
            if vertex.val == src.val:   # src already exists in Graph
                currNode = vertex
                while currNode.next is not None:
                    currNode = currNode.next
                currNode.next = dest
                
            # Remove elif for Directed graph
            elif vertex.val == dest.val:
                currNode = vertex
                while currNode.next is not None:
                    currNode = currNode.next
                currNode.next = src                    
                
    
    def printgraph(self):   # Adjacency List
        for ver in self.graph:
            currNode = ver.next
            while currNode is not None:
                print(ver.val, '->', currNode.val)
                currNode = currNode.next
            
   
# Graph is an Adjacency list, which is a list(Array) of Linked lists

g = Graph()         #Array
g.addVertex('a')
g.addEdge('a','b')
g.addEdge('a','c')    
g.addEdge('a','d')    
g.addEdge('b','d')    
g.addEdge('c','b')    

g.printgraph()

for v in g.graph:
    print(v.val)
    currVer = v.next
    while currVer is not None:
        print(currVer.val, currVer.weight)
        currVer = currVer.next







'''    
class Vertex:
    def __init__(self, val):
        self.val = val
        self.next = None


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def addVertex(self, val):
        for vertex in self.vertices:
            if vertex.val == val:
                print('Vertex already exists.')
                return
        self.vertices.append(Vertex(val))

    def addEdge(self, src, dest, weight):
        src_vertex = None
        dest_vertex = None
        for vertex in self.vertices:
            if vertex.val == src:
                src_vertex = vertex
            elif vertex.val == dest:
                dest_vertex = vertex

        if src_vertex is None:
            src_vertex = Vertex(src)
            self.vertices.append(src_vertex)

        if dest_vertex is None:
            dest_vertex = Vertex(dest)
            self.vertices.append(dest_vertex)
        # The above code only assigns values for "src_vertex" and "dest_vertex" considering various scenarios
        
        edge = Edge(src_vertex, dest_vertex, weight)
        self.edges.append(edge)

    def printGraph(self):
        for vertex in self.vertices:
            print("Vertex:", vertex.val)
            print("Edges:")
            for edge in self.edges:
                if edge.src == vertex:
                    print(edge.src.val, "->", edge.dest.val, "(Weight:", edge.weight, ")")
                elif edge.dest == vertex:
                    print(edge.dest.val, "->", edge.src.val, "(Weight:", edge.weight, ")")
            print()


g = Graph()
g.addVertex('a')
g.addEdge('a', 'b', 10)
g.addEdge('a', 'c', 20)
g.addEdge('a', 'd', 30)
g.addEdge('b', 'd', 40)
g.addEdge('c', 'b', 50)

g.printGraph()
'''