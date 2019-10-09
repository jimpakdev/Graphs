
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Cannot create edge based on given vertices!")

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

    # use DFS
    # ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # start from input node
    # create the possible paths upwards the tree
    # longest path has the earliest ancestor
    # if input node has no parents, return -1
def earliest_ancestor(self, ancestors, starting_node):
    # storing input list of pairs as key - value pairs in dictionary
    my_dict = dict(ancestors)
    graph = Graph()
    stack = Stack()
    visited = set()
    
    # build a graph 
    for pair in ancestors: 
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[0], pair[1])

    print(graph.vertices)

    stack.push([starting_node])

    while stack.size() > 0:
        # first path from stack
        path = stack.pop()
        # last node from the path
        node = path[-1]
        # if vertex has not been visited
        if node not in visited:
            # add vertex to visited
            visited.add(starting_node)
            # get adjacent edges for that vertex
            for adjacent in self.vertices[node]:
                # construct a new path
                new_path = list(path)
                # add the adjacent edges to new path
                new_path.append(adjacent)
                # add new path to stack
                stack.push(new_path)
        
            # get key from dict
            # check dict to see if key is a child in another pair
            # if the key is a child in another pair 
            # repeat loop
            # else return ancestor parent key

            # directed movement?





