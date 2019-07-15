'''
Problem, given a graph, traverse it using Breath First Search
'''

from graph import Graph


'''
Give a node in the graph, run dfs on the graph from that node
'''


def breath_first_search(value, graph):
    node = Graph.findNodeWithValue(graph.getNodes(), value)
    queue = []
    order_of_visit = []
    queue.append(node)
    node.setVisited(True)
    while len(queue) != 0:
        curr_node = queue.pop(0)
        order_of_visit.append(curr_node)
        neighbors = curr_node.getNeighbors()
        for neighbor in neighbors:
            if not neighbor.getVisited():
                neighbor.setVisited(True)
                queue.append(neighbor)
    return order_of_visit


'''
Application of breath first search
Given a graph and a node, compute shortest path to other node

Return the shortest path and the distance
'''


def shortest_path(valueFrom, valueTo, graph):
    nodeFrom = Graph.findNodeWithValue(graph.getNodes(), valueFrom)
    nodeFrom.setDistance(0)
    nodeTo = Graph.findNodeWithValue(graph.getNodes(), valueTo)
    if nodeTo is None:
        raise Exception("No node found in graph for the destination!")
    queue = []
    order_of_visit = []
    queue.append(nodeFrom)
    nodeFrom.setVisited(True)
    while len(queue) != 0:
        curr_node = queue.pop(0)
        order_of_visit.append(curr_node)
        if curr_node is nodeTo:
            break
        neighbors = curr_node.getNeighbors()
        for neighbor in neighbors:
            if not neighbor.getVisited():
                neighbor.setVisited(True)
                queue.append(neighbor)
                neighbor.setDistance(curr_node.getDistance() + 1)
                neighbor.setPrevious(curr_node)
    if nodeTo not in order_of_visit:
        raise Exception("Can't reach the destination node!")
    shortest_path = []
    target_node = order_of_visit[-1]
    while target_node.getPrevious() is not None:
        shortest_path.insert(0, target_node)
        target_node = target_node.getPrevious()
    shortest_path.insert(0, nodeFrom)
    return shortest_path


'''
Find connected components in graph using breath first search
in O(m + n)
'''


def find_connected_components(graph):
    components = []
    for node in graph.getNodes():
        if not node.getVisited():
            components.append(breath_first_search(node.getValue(), graph))
    return components


if __name__ == '__main__':
    graph = Graph()
    for i in xrange(1, 11):
        graph.addNode(i)
    graph.addUnDirectedEdgeWithName(1, 3, "a")
    graph.addUnDirectedEdgeWithName(1, 5, "b")
    graph.addUnDirectedEdgeWithName(3, 5, "c")
    graph.addUnDirectedEdgeWithName(5, 7, "d")
    graph.addUnDirectedEdgeWithName(5, 9, "e")
    graph.addUnDirectedEdgeWithName(2, 4, "f")
    graph.addUnDirectedEdgeWithName(6, 8, "g")
    graph.addUnDirectedEdgeWithName(6, 10, "h")
    graph.addUnDirectedEdgeWithName(8, 10, "i")
    for component in find_connected_components(graph):
        print "current component: "
        for node in component:
            print node