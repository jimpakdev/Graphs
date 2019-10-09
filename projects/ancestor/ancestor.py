
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

# Brian using queue - BFS? 
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


    # use DFS
    # ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # start from input node
    # create the possible paths upwards the tree
    # longest path has the earliest ancestor
    # if input node has no parents, return -1

def earliest_ancestor(ancestors, starting_node):
    # storing input list of pairs as key - value pairs in dictionary
    # my_dict = dict(ancestors)
    graph = Graph()
    stack = Stack()
    visited = set()
    
    # build a graph 
    for pair in ancestors: 
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # this builds in reverse 
        graph.add_edge(pair[1], pair[0])

    stack.push([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while stack.size() > 0:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            visited.add(starting_node)

            # 1st part of this check here is for lowest numeric value answer - if there are two ancestors tied 
            # 2nd part of this check: looking for a path longer than the current path
            if (len(path) >= max_path_length and node < earliest_ancestor) or (len(path) > max_path_length):
                earliest_ancestor = node
                max_path_length = len(path)
                
            for adjacent in graph.vertices[node]:
                new_path = list(path)
                new_path.append(adjacent)
                stack.push(new_path)

    return earliest_ancestor


# Brian's BFS way

# def earliest_ancestor(ancestors, starting_node):
#     # storing input list of pairs as key - value pairs in dictionary
#     # my_dict = dict(ancestors)
#     graph = Graph()
#     # stack = Stack()
#     # visited = set()
    
#     # build a graph 
#     for pair in ancestors: 
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # this builds in reverse 
#         graph.add_edge(pair[1], pair[0])

#     q = Queue()
#     q.enqueue([starting_node])
#     # stack.push([starting_node])

#     max_path_length = 1
#     earliest_ancestor = -1

#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]

#         # 'do the thing' 
#         if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
#             earliest_ancestor = v
#             max_path_length = len(path)

#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
    
#     return earliest_ancestor






