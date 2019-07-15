'''
Problem:
Input: an undirected graph G = (V, E), paralle edges allowed

Goal:
Compute the cut with the fewest number of crossing edges
'''

from graph import Graph
import random
import copy


'''
I will skip the detailed analysis for the randomized contraction algorithm. But the basic
idea is that while the number of nodes in graph is less than 2, we randomly select a edge
and contact two nodes connected by that single edge. In the end, we are left with 2 nodes
connected with many parallel edges (or maybe not). That cut has 1 / n ^2 to be the minimum
cut (theory proofs is online).

To lower the probability for failure, we running many trials and take the minimum cut of those
trails
'''


def random_contraction_one_trial(graph):
    nodes = graph.getNodes()
    while len(nodes) > 2:
        # get the nodes and edges in graph
        nodes = graph.getNodes()
        edges = graph.getEdges()
        # get the index for contracted edges
        edge_index = random.randint(0, len(edges) - 1)
        contract_edge = edges[edge_index]
        # get two nodes about to be merged together
        nodes_to_merge = contract_edge.getEndNodes()
        # take the first node as default node to be merged to
        resulting_node = nodes_to_merge[0]
        # remove the edges from graph and two nodes
        edges.remove(contract_edge)
        resulting_node.getEdges().remove(contract_edge)
        nodes_to_merge[1].getEdges().remove(contract_edge)
        # before we remove the unused node, we make all of its edges point to
        # the merged node
        # Note there are two cases here:
        # case 1:
        #     The node to be merged doesn't has edges already connected to the
        #     node to be merged to
        #     In this case, we just modify all the endpoints of edges of the node
        #     to be merged. We add all these edges to the node to be merged to
        # case 2:
        #     The node to be merged has edges already conneected to the node to be
        #     merged to
        #     In this case, we don't add the edges since it will introduce repeated
        #     edges to the graph
        for edge in nodes_to_merge[1].getEdges():
            edge.removeEndNode(nodes_to_merge[1])
            edge.addEndNode(resulting_node)
            if edge not in resulting_node.getEdges():
                resulting_node.addEdge(edge)
        graph.removeNode(nodes_to_merge[1])
        #remove the self loop
        resulting_edges = resulting_node.getEdges()
        edge_to_remove = []
        for i in xrange(0, len(resulting_edges)):
            edge = resulting_edges[i]
            endNodes = edge.getEndNodes()
            if endNodes[0] is endNodes[1]:
                # first remove from the node then the entire graph
                edge_to_remove.append(edge)
        for edge in edge_to_remove:
            resulting_node.getEdges().remove(edge)
            #if edge in edges:
               # print "edge in edges of graph: ", edge
            edges.remove(edge)
    return graph.getEdges()


def random_contraction(trial_size, graph):
    graph_curr = copy.deepcopy(graph)
    minimum_cut = random_contraction_one_trial(graph_curr)
    for i in xrange(0, trial_size - 1):
        graph_curr = copy.deepcopy(graph)
        curr_cut = random_contraction_one_trial(graph_curr)
        if len(curr_cut) < len(minimum_cut):
            minimum_cut = curr_cut
    return minimum_cut

if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 9):
        graph.addNode(i)
    graph.addUnDirectedEdgeWithName(1, 2, "a")
    graph.addUnDirectedEdgeWithName(1, 5, "b")
    graph.addUnDirectedEdgeWithName(1, 6, "c")
    graph.addUnDirectedEdgeWithName(2, 5, "d")
    graph.addUnDirectedEdgeWithName(2, 6, "e")
    graph.addUnDirectedEdgeWithName(2, 3, "f")
    graph.addUnDirectedEdgeWithName(3, 4, "g")
    graph.addUnDirectedEdgeWithName(3, 7, "h")
    graph.addUnDirectedEdgeWithName(3, 8, "i")
    graph.addUnDirectedEdgeWithName(4, 8, "j")
    graph.addUnDirectedEdgeWithName(4, 7, "k")
    graph.addUnDirectedEdgeWithName(5, 6, "l")
    graph.addUnDirectedEdgeWithName(6, 7, "m")
    graph.addUnDirectedEdgeWithName(7, 8, "n")
    for edge in random_contraction(64, graph):
        print edge
    print "**************"
    for edge in random_contraction_one_trial(graph):
        print edge