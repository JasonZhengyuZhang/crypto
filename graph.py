old_graph = {
    0: [(0, 1), (0, 2), (0, 3)],
    1: [],
    2: [(2, 1)],
    3: [(3, 4), (3, 5)],
    4: [(4, 3), (4, 5)],
    5: [(5, 3), (5, 4), (5, 7)],
    6: [(6, 8)],
    7: [],
    8: [(8, 9)],
    9: []}

def connected_components(neighbors):
    seen = set()
    def component(node):
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            seen.add(node)
            nodes |= neighbors[node] - seen
            yield node
    for node in neighbors:
        if node not in seen:
            yield component(node)
    
new_graph = {node: set(each for edge in edges for each in edge)
             for node, edges in old_graph.items()}
components = []
for component in connected_components(new_graph):
    c = set(component)
    components.append([edge for edges in old_graph.values()
                            for edge in edges
                            if c.intersection(edge)])
print(components)