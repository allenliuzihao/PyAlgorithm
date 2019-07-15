'''
File contains Union-Find data structure specifically for graph
'''

class Union_Find():
    def __init__(self, graph):
        nodes = graph.getNodes()
        for node in nodes:
            node.setLeader(node)

    def find(self, node):
        return node.getLeader()

    def union(self, nodes1, nodes2):
        # choose the smaller node component to merge first
        smaller_component = nodes1 if len(nodes1) < len(nodes2) else nodes2
        larger_component  = nodes1 if len(nodes1) >= len(nodes2) else nodes2
        leader = larger_component[0].getLeader()
        leader_component = leader.getComponent()
        leader_component += smaller_component[0].getLeader().getComponent()
        for node in smaller_component:
            node.setLeader(leader)