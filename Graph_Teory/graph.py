class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,neighbor,weight=0):
        self.connectedTo[neighbor] = weight
    def __str__(self):
        return str(self.id) + " connected to: " + str([data.id for data in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,neighbor):
        return self.connectedTo[neighbor]
class Graph:
    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertlist[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n is self.vertlist:
            return self.vertlist[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertlist
    def addEdge(self,fromVert,toVert,weight=0):
        if fromVert not in self.vertlist:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertlist:
            nv = self.addVertex(toVert)
        self.vertlist[fromVert].addNeighbor(self.vertlist[toVert],weight)
    def getVertices(self):
        return self.vertlist.keys()
    def __iter__(self):
        return iter(self.vertlist.values())
    

graph = Graph()

for sayi in range(1,10):
    graph.addVertex(sayi)
graph.addEdge(1,2,0)
graph.addEdge(1,4,0)
#print(graph.vertlist)

for v in graph:
    print(v)
    print(v.getConnections)