'''
Implementation and applications for depth first search
'''

from graph import Graph

# for finding the strongest connected components in a graph
finishing_time = 0    # for recording the current finishing time
leader = None    # for recording the current leader of the SCC

'''
Given a node in the graph, find its depth first search searching path
'''


def depth_first_search(value, graph):
    node = Graph.findNodeWithValue(graph.getNodes(), value)
    stack = []
    order_of_visit = []
    stack.append(node)
    node.setVisited(True)
    while len(stack) != 0:
        curr_node = stack.pop()
        order_of_visit.append(curr_node)
        neighbors = curr_node.getNeighbors()
        for neighbor in neighbors:
            if not neighbor.getVisited():
                neighbor.setVisited(True)
                stack.append(neighbor)
    return order_of_visit


'''
Small modification of depth first search to label the topological order of each node
'''


def dfs_topological_sort(node, graph, label):
    node.setVisited(True)
    neighbors = node.getNeighbors()
    curr_label = label
    for neighbor in neighbors:
        if not neighbor.getVisited():
            curr_label = dfs_topological_sort(neighbor, graph, curr_label)
    node.setLabel(curr_label)
    curr_label -= 1
    return curr_label


'''
Topological sort using DFS
'''


def topological_sort(graph):
    nodes = graph.getNodes()
    label = len(nodes)
    for node in nodes:
        if not node.getVisited():
            label = dfs_topological_sort(node, graph, label)
    topological_order = []
    for i in xrange(1, len(nodes) + 1):
        for node in nodes:
            if node.getLabel() == i:
                topological_order.append(node)
    return topological_order

'''
Helper for DFS on the reverse graph for the SCC problem
'''


def depth_first_search_SCC_reverse(graph, node, order_of_visit):
    global finishing_time
    node.setVisited(True)
    neighbors = node.getNeighbors()
    for neighbor in neighbors:
        if not neighbor.getVisited():
            depth_first_search_SCC_reverse(graph, neighbor, order_of_visit)
    finishing_time += 1
    node.setLabel(finishing_time)
    order_of_visit.insert(0, node)

'''
Helper for finding the leaders in the graph using DFS
'''


def depth_first_search_SCC_leader(graph, node, SCC):
    global leader
    node.setVisited(True)
    neighbors = node.getNeighbors()
    for neighbor in neighbors:
        neighbor.setLeader(leader)
        if not neighbor.getVisited():
            SCC.append(neighbor)
            depth_first_search_SCC_leader(graph, neighbor, SCC)

'''
Find the strongest connected components in DAG (every node in SCC can be reached from other node)

Idea:
1. Run the DFS on the reversed graph. Keep track of the finish time (from the order of visit) of each node
2. Run the DFS on the original graph in the order of decreasing finish time of each node.

Analysis:
Key property in DAG: acyclic. No cycle in the graph
Assume the SCC: C1, C2, C3
We know that the C1, C2 and C3 doesn't have cycle between them. Because for example if C1 has edge to C2, C2 has
edge to C1, then C1 C2 should have form a bigger SCC, which contracdict our previous assumption that C1 and C2 are
SCC

Also, reversing the edges in DAG doesn't change the SCC.

Then we need to prove that if C1 has edge to C2 in original graph. Then the max finishing time of C1 and C2 is in C2
This is true because in the reversed graph, C2 has an edge that points to C1. If we compute the finishing time in C1 first
, then by the point DFS finish in C1, C2 must have higher finishing time since it comes after C1. If we compute the finishing
time in C2 first, based on the property of DFS, the max finishing time must be in C2. So we have the lemma that if in original
graph C1 point to C2, then the max finish time must be in C2.

Then, given the example below, C0 -> C1 -> C2, in the second run of DFS, we will first explore C2 since it has the max finishing
time, then C1, then C0. This order of exploration will make sure that each run of DFS will find the SCC

Since we just run 2 times DFS, the overall run time is still O(m + n)
'''


def find_SCC(graph):
    global leader
    graph.reverseEdges()
    SCCs = []    # store the final result in list
    order_of_visit = []
    for node in graph.getNodes():
        if not node.getVisited():
            depth_first_search_SCC_reverse(graph, node, order_of_visit)
    graph.clearVisited()
    graph.clearReversed()
    graph.reverseEdges()
    for node in order_of_visit:
        leader = node
        if not node.getVisited():
            SCC = [leader]
            depth_first_search_SCC_leader(graph, node, SCC)
            SCCs.append(SCC)
    return SCCs

if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 12):
        graph.addNode(i)
    #graph.addDirectedEdge(1, 7)
    #graph.addDirectedEdge(4, 1)
    #graph.addDirectedEdge(7, 4)
    #graph.addDirectedEdge(7, 9)
    #graph.addDirectedEdge(3, 9)
    #graph.addDirectedEdge(6, 3)
    #graph.addDirectedEdge(9, 6)
    #graph.addDirectedEdge(6, 8)
    #graph.addDirectedEdge(8, 2)
    #graph.addDirectedEdge(2, 5)
    #graph.addDirectedEdge(5, 8)

    graph.addDirectedEdge(1, 2)
    graph.addDirectedEdge(2, 3)
    graph.addDirectedEdge(3, 1)
    graph.addDirectedEdge(2, 4)
    graph.addDirectedEdge(4, 5)
    graph.addDirectedEdge(4, 6)
    graph.addDirectedEdge(6, 5)
    graph.addDirectedEdge(5, 7)
    graph.addDirectedEdge(7, 6)
    graph.addDirectedEdge(3, 9)
    graph.addDirectedEdge(3, 11)
    graph.addDirectedEdge(11, 9)
    graph.addDirectedEdge(10, 11)
    graph.addDirectedEdge(9, 10)
    graph.addDirectedEdge(9, 6)
    graph.addDirectedEdge(9, 8)
    graph.addDirectedEdge(8, 10)
    graph.addDirectedEdge(8, 7)
    for SCC in find_SCC(graph):
        print "******************************* component ********************************"
        for node in SCC:
            print node
        print "******************************* end component *****************************\n"
