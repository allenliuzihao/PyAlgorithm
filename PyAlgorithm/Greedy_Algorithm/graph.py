'''
Graph representation for graph problems. Node value is assumed to be unique
'''


class Edge():
    def __init__(self):
        self.endnodes = []
        self.weight = 0
        self.name = ""
        self.reverse = False
        self.visited = False

    def setSelected(self, visited):
        self.visited = visited

    def isSelected(self):
        return self.visited

    def setReversed(self, reverse):
        self.reverse = reverse

    def getReversed(self):
        return self.reverse

    def setWeight(self, weight):
        self.weight = weight

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getEndNodes(self):
        return self.endnodes

    def addEndNode(self, node):
        self.endnodes.append(node)

    def removeEndNode(self, node):
        self.endnodes.remove(node)

    def __str__(self):
        string = "The name of the edge: " + self.name + " The weight for the edge: " + str(self.weight) + " \nHere are list of nodes the edge points to: \n"
        for node in self.endnodes:
            string += str(node) + " "
        return string


class Node():
    def __init__(self, value):
        self.edges = []
        self.value = value
        self.visited = False
        self.distance = 0
        self.previous = None
        self.label = 0
        self.leader = None
        self.edge = None
        self.components = [self]

    def setLeader(self, node):
        self.leader = node

    def getLeader(self):
        return self.leader

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getComponent(self):
        return self.components
 
    def getEdges(self):
        return self.edges

    def addEdge(self, edge):
        self.edges.append(edge)

    def getNeighbors(self):
        nodes = []
        for edge in self.edges:
            for node in edge.getEndNodes():
                if node.getValue() != self.value:
                    nodes.append(node)
        return nodes

    def setVisited(self, visited):
        self.visited = visited

    def getVisited(self):
        return self.visited

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance

    def setLabel(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def getPrevious(self):
        return self.previous

    def setPrevious(self, node):
        self.previous = node

    def setTargetEdge(self, edge):
        self.edge = edge

    def getTargetEdge(self):
        return self.edge

    def __str__(self):
        string = "Value for this node: " + str(self.value) + " Label of node: " + str(self.label)
        return string

    def __lt__(self, other):
        return self.label < other.label

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.label == other.label

    def __ne__(self, other):
        return not self.__eq__(other)


class Graph():

    @staticmethod
    def findNodeWithValue(nodes, value):
        for node in nodes:
            if node.getValue() == value:
                return node
        return None

    def __init__(self):
        self.nodes = []
        self.edges = []

    def reverseEdges(self):
        for node in self.nodes:
            edges = node.getEdges()
            edges_to_change = []
            for edge in edges:
                if not edge.getReversed() and len(edge.getEndNodes()) == 1:
                    edges_to_change.append(edge)
            for edge in edges_to_change:
                new_node = edge.getEndNodes().pop()
                edge.getEndNodes().append(node)
                node.getEdges().remove(edge)
                new_node.getEdges().append(edge)
                edge.setReversed(True)

    def addNode(self, value):
        new_node = Node(value)
        self.nodes.append(new_node)

    def removeNode(self, node):
        self.nodes.remove(node)

    def addDirectedEdge(self, value1, value2):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        edge.addEndNode(node2)
        node1.addEdge(edge)
        self.edges.append(edge)

    def addUnDirectedEdge(self, value1, value2):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        self.edges.append(edge)
        edge.addEndNode(node2)
        edge.addEndNode(node1)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def addUnDirectedEdgeWithName(self, value1, value2, name):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        edge.setName(name)
        self.edges.append(edge)
        edge.addEndNode(node2)
        edge.addEndNode(node1)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def addUnDirectedEdgeWithWeightName(self, value1, value2, weight, name):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        edge.setName(name)
        edge.setWeight(weight)
        self.edges.append(edge)
        edge.addEndNode(node2)
        edge.addEndNode(node1)
        node1.addEdge(edge)
        node2.addEdge(edge)

    def addDirectedEdgeWithName(self, value1, value2, name):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        edge.setName(name)
        edge.addEndNode(node2)
        node1.addEdge(edge)
        self.edges.append(edge)

    def addDirectedEdgeWithWeight(self, value1, value2, weight):
        node1 = Graph.findNodeWithValue(self.nodes, value1)
        node2 = Graph.findNodeWithValue(self.nodes, value2)
        if node1 is None or node2 is None:
            raise Exception("The value of node is not present in graph!")
        edge = Edge()
        edge.setWeight(weight)
        edge.addEndNode(node2)
        node1.addEdge(edge)
        self.edges.append(edge)

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        return self.edges

    def clearVisited(self):
        for node in self.nodes:
            if node.getVisited():
                node.setVisited(False)

    def clearReversed(self):
        for edge in self.edges:
            if edge.getReversed():
                edge.setReversed(False)

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += "I am node: " + str(node) + "\n"
            neighbor = node.getEdges()
            if len(neighbor) != 0:
                string += "I got edges! Here is my edges: \n"
            for edge in neighbor:
                string += str(edge) + "\n"
        return string

if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 9):
        graph.addNode(i)
    graph.addDirectedEdgeWithName(1, 2, "a")
    graph.addDirectedEdgeWithName(1, 6, "c")
    graph.addDirectedEdgeWithName(1, 5, "b")
    graph.addDirectedEdgeWithName(2, 3, "d")
    graph.addDirectedEdgeWithName(6, 3, "e")
    graph.addDirectedEdgeWithName(6, 7, "f")
    graph.addDirectedEdgeWithName(3, 4, "g")
    graph.addDirectedEdgeWithName(7, 4, "h")
    graph.addDirectedEdgeWithName(4, 8, "i")
    print "*************************** old graph *****************************"
    print graph
    graph.reverseEdges()
    print "**************************** new graph *****************************"
    print graph