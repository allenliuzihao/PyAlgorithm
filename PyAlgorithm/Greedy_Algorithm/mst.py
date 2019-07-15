'''
Input: undirected graph G=(V, E), find the minimum spanning tree in the graph

Assumption:
    Graph is connected (could easily check using DFS or BFS)
    Input graph the edge costs are distinct (But Prims and Kruskal are able to handle ties)
'''

import sys
from graph import Graph
from heap import Heap

sys.path.append("../Data_Structure")

from union_find import Union_Find

def find_distinct_endnode(nodes, other_node):
    candidate = None
    for node in nodes:
        if node is not other_node:
            candidate = node
    return candidate


def prim_no_heap(graph):
    mst = []
    start_node = graph.getNodes()[0]
    explored = [start_node]
    start_node.setLabel(0)
    for node in graph.getNodes():
        if node is not start_node:
            node.setLabel(float('inf'))
    while len(explored) != len(graph.getNodes()):
        smallest_score = float('inf')
        node_to_explore = None
        edge_explored = None
        for node in explored:
            for edge in node.getEdges():
                end_node = find_distinct_endnode(edge.getEndNodes(), node)
                if end_node not in explored:
                    if smallest_score > edge.getWeight():
                        smallest_score = edge.getWeight()
                        node_to_explore = end_node
                        edge_explored = edge
        node_to_explore.setLabel(smallest_score)
        mst.append(edge_explored)
        explored.append(node_to_explore)
    return mst


def prim_with_heap(graph):
    mst = []
    heap = Heap(True)
    start_node = graph.getNodes()[0]
    for node in graph.getNodes():
        if node is not start_node:
            node.setLabel(float('inf'))
            heap.insert(node)
    start_node.setLabel(0)
    heap.insert(start_node)
    while not heap.isEmpty():
        curr_node = heap.extract()
        curr_edges = curr_node.getEdges()
        for edge in curr_edges:
            end_node = find_distinct_endnode(edge.getEndNodes(), curr_node)
            if heap.contains(end_node):
                heap.remove(end_node)
                if edge.getWeight() < end_node.getLabel():
                    end_node.setLabel(edge.getWeight() + curr_node.getLabel())
                    end_node.setTargetEdge(edge)
                heap.insert(end_node)
    for node in graph.getNodes():
        if node is not start_node:
            mst.append(node.getTargetEdge())
    return mst


def has_cycle(graph, start_node, end_node):
    queue = []
    cycle = False
    queue.append(start_node)
    start_node.setVisited(True)
    while len(queue) != 0:
        curr_node = queue.pop(0)
        if curr_node is end_node:
            cycle = True
        curr_edges = curr_node.getEdges()
        for edge in curr_edges:
            if edge.isSelected():
                neighbor = find_distinct_endnode(edge.getEndNodes(), curr_node)
                if not neighbor.getVisited():
                    neighbor.setVisited(True)
                    queue.append(neighbor)
    return cycle


def kruskal(graph):
    mst = []
    edges = graph.getEdges()
    sorted_edges = sorted(edges, key=lambda edge: edge.getWeight())
    for edge in sorted_edges:
        start_node = edge.getEndNodes()[0]
        end_node = edge.getEndNodes()[1]
        if not has_cycle(graph, start_node, end_node):
            edge.setSelected(True)
            mst.append(edge)
        graph.clearVisited()
    return mst


def kruskal_with_union_find(graph):
    mst = []
    edges = graph.getEdges()
    sorted_edges = sorted(edges, key=lambda edge: edge.getWeight())
    union_find = Union_Find(graph)
    for edge in sorted_edges:
        start_node = edge.getEndNodes()[0]
        end_node = edge.getEndNodes()[1]
        if union_find.find(start_node) is not union_find.find(end_node):
            mst.append(edge)
            start_node_leader = start_node.getLeader()
            end_node_leader = end_node.getLeader()
            union_find.union(start_node_leader.getComponent(), end_node_leader.getComponent())
    return mst

if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 10):
        graph.addNode(i)
    graph.addUnDirectedEdgeWithWeightName(1, 2, 1, 'a')
    graph.addUnDirectedEdgeWithWeightName(2, 3, 6, 'c')
    graph.addUnDirectedEdgeWithWeightName(1, 4, 4, 'b')
    graph.addUnDirectedEdgeWithWeightName(2, 5, 2, 'e')
    graph.addUnDirectedEdgeWithWeightName(3, 6, 1, 'd')
    graph.addUnDirectedEdgeWithWeightName(4, 5, 3, 'g')
    graph.addUnDirectedEdgeWithWeightName(5, 6, 1, 'f')
    graph.addUnDirectedEdgeWithWeightName(5, 7, 1, 'l')
    graph.addUnDirectedEdgeWithWeightName(5, 8, 4, 'j')
    graph.addUnDirectedEdgeWithWeightName(6, 8, 1, 'h')
    graph.addUnDirectedEdgeWithWeightName(5, 6, 1, 'f')
    graph.addUnDirectedEdgeWithWeightName(8, 9, 3, 'i')
    graph.addUnDirectedEdgeWithWeightName(5, 9, 7, 'k')
    result = kruskal_with_union_find(graph)
    string = "Here is the MST: "
    for edge in result:
        string += str(edge.getName()) + " + "
    print string[0:-2]
