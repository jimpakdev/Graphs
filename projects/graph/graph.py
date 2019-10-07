"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # BFT Pseudocode
        # Create a queue
        qq = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        qq.enqueue(starting_vertex)
        # While: queue not empty
        while qq.size() > 0:
            # Pop first node out of queue
            vertex = qq.dequeue()
            # If not visited
            if vertex not in visited:
                #Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)
        # Goto top of loop

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        stack.push(starting_vertex)
        # While: queue not empty
        while stack.size() > 0:
            # Pop first node out of queue
            vertex = stack.pop()
            # If not visited
            if vertex not in visited:
                #Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)
        # Goto top of loop

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # initialize visited
        if visited == None:
            visited = set()
        # add first vertex 
        visited.add(starting_vertex)
        print(starting_vertex)
        # check adjacent edges
        for adjacent in self.vertices[starting_vertex]: 
            if adjacent not in visited:
                self.dft_recursive(adjacent, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()
        # add first vertex
        qq.enqueue([starting_vertex])

        while qq.size() > 0:
            # first path from queue
            path = qq.dequeue()
            # last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # if vertex has not been visited
            if node not in visited:
                # add vertex to visited
                visited.add(starting_vertex)
                # get adjacent edges for that vertex
                for adjacent in self.vertices[node]:
                    # construct a new path
                    new_path = list(path)
                    # add the adjacent edges to new path
                    new_path.append(adjacent)
                    # add new path to queue
                    qq.enqueue(new_path)

                
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        # add first vertex
        stack.push([starting_vertex])

        while stack.size() > 0:
            # first path from stack
            path = stack.pop()
            # last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # if vertex has not been visited
            if node not in visited:
                # add vertex to visited
                visited.add(starting_vertex)
                # get adjacent edges for that vertex
                for adjacent in self.vertices[node]:
                    # construct a new path
                    new_path = list(path)
                    # add the adjacent edges to new path
                    new_path.append(adjacent)
                    # add new path to stack
                    stack.push(new_path)
                    # creating branch





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)

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
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('RECURSIVE DFT')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
