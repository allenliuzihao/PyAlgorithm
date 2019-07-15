'''
Problem:
Given a directed weighted graph (no two direction edges) with non-negative weights, find the shortest path from one node to the other
Assuming that the starting node has path to every other node

I gave two solutions to this problem. Both of them use the idea of Dijkstra shortest path algorithm.
The first one is a simple brutal force that check every edge for every iteration. The run time is O(mn)
The second one is an optimization. Basically we use a heap data structure to shorten our time to find the
min score vertex in each iteration. The run time is O(mlogn)
'''

from graph import Graph
from heap import Heap


def dijkstra_no_heap(graph, start_node, destination_node):
    explored = [start_node]
    start_node.setLabel(0)
    for node in graph.getNodes():
        if node is not start_node:
            node.setLabel(float('inf'))
    while len(explored) != len(graph.getNodes()):
        smallest_score = float('inf')
        node_to_explore = None
        previous_node = None
        for node in explored:
            edges = node.getEdges()
            for edge in edges:
                end_node = edge.getEndNodes()[0]
                if not end_node in explored:
                    if smallest_score > edge.getWeight() + node.getLabel():
                        smallest_score = edge.getWeight() + node.getLabel()
                        node_to_explore = end_node
                        previous_node = node
        node_to_explore.setLabel(smallest_score)
        node_to_explore.setPrevious(previous_node)
        explored.append(node_to_explore)
    temp_node = destination_node
    shortest_path = []
    while temp_node is not None:
        shortest_path.insert(0, temp_node)
        temp_node = temp_node.getPrevious()
    return [shortest_path, destination_node.getLabel()]


def dijkstra_with_heap(graph, start_node, destination_node):
    heap = Heap(True)    # min heap
    for node in graph.getNodes():
        if node is not start_node:
            node.setLabel(float('inf'))
            heap.insert(node)
    start_node.setLabel(0)
    start_node.setPrevious(None)
    heap.insert(start_node)
    while not heap.isEmpty():
        curr_node = heap.extract()
        curr_edges = curr_node.getEdges()
        for edge in curr_edges:
            end_node = edge.getEndNodes()[0]
            if heap.contains(end_node):
                heap.remove(end_node)
                if edge.getWeight() + curr_node.getLabel() < end_node.getLabel():
                    end_node.setLabel(edge.getWeight() + curr_node.getLabel())
                    end_node.setPrevious(curr_node)
                heap.insert(end_node)
    temp_node = destination_node
    shortest_path = []
    while temp_node is not None:
        shortest_path.insert(0, temp_node)
        temp_node = temp_node.getPrevious()
    return [shortest_path, destination_node.getLabel()]


if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 7):
        graph.addNode(i)
    graph.addDirectedEdgeWithWeight(1, 2, 1)
    graph.addDirectedEdgeWithWeight(1, 3, 3)
    graph.addDirectedEdgeWithWeight(2, 3, 1)
    graph.addDirectedEdgeWithWeight(3, 4, 1)
    graph.addDirectedEdgeWithWeight(3, 5, 5)
    graph.addDirectedEdgeWithWeight(4, 5, 7)
    graph.addDirectedEdgeWithWeight(2, 4, 4)
    graph.addDirectedEdgeWithWeight(4, 6, 2)
    graph.addDirectedEdgeWithWeight(5, 6, 1)

    node1 = Graph.findNodeWithValue(graph.getNodes(), 1)
    node2 = Graph.findNodeWithValue(graph.getNodes(), 5)
    result = dijkstra_with_heap(graph, node1, node2)
    shortest_path = result[0]
    print "the score of path: ", result[1]
    string = "Here is the path: "
    for node in shortest_path:
        string += str(node.getValue()) + " -> "
    print string[0:-4]