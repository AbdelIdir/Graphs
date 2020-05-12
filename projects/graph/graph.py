""" 

MINIMUM SPANNING TREE
is the result of a Depth First Traversal



"""


"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Edge error vert not found:")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        ancestor_path = [starting_vertex]

        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                if len(path) > len(ancestor_path):
                    ancestor_path = path
                elif len(path) == len(ancestor_path):
                    if path[-1] < ancestor_path[-1]:
                        ancestor_path = path
                visited.add(node)
                neighbors = self.get_neighbors(node)
                for next_node in neighbors:
                    new_path = list(path)
                    new_path.append(next_node)
                    queue.enqueue(new_path)

        return ancestor_path

    def dft(self, starting_vertex):
        print("\n")
        """
		Print each vertex in depth-first order
		beginning from starting_vertex.
		"""
        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        while stack.size() > 0:

            path = stack.pop()

            if path not in visited:
                print(94, path)
                visited.add(path)
                for next in self.get_neighbors(path):
                    stack.push(next)
        print("\n")

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.add(starting_vertex)
        print(113, starting_vertex)
        for next in self.vertices[starting_vertex]:
            if next not in visited:
                self.dft_recursive(next, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        qq = Queue()
        qq.enqueue([starting_vertex])
        visited = set()

        while qq.size() > 0:
            path = qq.dequeue()
            vert = path[-1]

            if vert not in visited:

                visited.add(vert)
                nextverts = self.get_neighbors(vert)

                for next in nextverts:
                    new_path = list(path)
                    new_path.append(next)

                    if next == destination_vertex:

                        print(152, new_path)
                        return new_path

                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        ss = Stack()
        ss.push([starting_vertex])

        visited = set()

        while ss.size() > 0:

            path = ss.pop()

            if path[-1] not in visited:

                if path[-1] == destination_vertex:
                    return path

                visited.add(path[-1])

                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
	Should print:
		{1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
	'''
    print(graph.vertices)

    '''
	Valid BFT paths:
		1, 2, 3, 4, 5, 6, 7
		1, 2, 3, 4, 5, 7, 6
		1, 2, 3, 4, 6, 7, 5
		1, 2, 3, 4, 6, 5, 7
		1, 2, 3, 4, 7, 6, 5
		1, 2, 3, 4, 7, 5, 6
		1, 2, 4, 3, 5, 6, 7
		1, 2, 4, 3, 5, 7, 6
		1, 2, 4, 3, 6, 7, 5
		1, 2, 4, 3, 6, 5, 7
		1, 2, 4, 3, 7, 6, 5
		1, 2, 4, 3, 7, 5, 6
	'''
    graph.bft(1)

    '''
	Valid DFT paths:
		1, 2, 3, 5, 4, 6, 7
		1, 2, 3, 5, 4, 7, 6
		1, 2, 4, 7, 6, 3, 5
		1, 2, 4, 6, 3, 5, 7
	'''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
	Valid BFS path:
		[1, 2, 4, 6]
	'''
    print(graph.bfs(1, 6))
    print(graph.bfs(4, 5))

    '''
	Valid DFS paths:
		[1, 2, 4, 6]
		[1, 2, 4, 7, 6]
	'''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
