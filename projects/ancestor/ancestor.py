

from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    # initializing graph
    graph = Graph()

    for pair in ancestors:
        #setting the start with parent
        parent = pair[0]
        child = pair[1]
        # add node vertex,starting with parent
        graph.add_vertex(parent)

        graph.add_vertex(child)

        #add another vertex, attach child
        #connect the edges to child and parent vertices
        graph.add_edge(child, parent)

    path_result = graph.bft(starting_node)

#returning earliest ancestor
    if len(path_result) == 1:
        return - 1

    else:
        return path_result[-1]

