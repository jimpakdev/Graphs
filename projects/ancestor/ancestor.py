
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
    # longest path has our earliest ancestor
    # if input node has no parents, return -1
def earliest_ancestor(ancestors, starting_node):
    # storing input list of pairs as key - value pairs in dictionary
    my_dict = dict(ancestors)
    stack = Stack()
    visited = set()
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
    
            # get key from dict
            # check dict to see if key is a child in another pair
            # if the key is a child in another pair 
            # repeat loop
            # else return ancestor parent key


# def get_neighbors(word):
#     neighbors = []
#     string_word = list(word)
#     for i in range(len(string_word)):
#         for letter in list("abcdefghijklmopqrstuvwxyz"):
#             temp_word = list(string_word)
#             temp_word[i] = letter
#             w = ''.join(temp_word)
#             if w != word and w in word_set:
#                 neighbors.append(w)

#     return neighbors

# def find_word_ladder(beginWord, endWord):

#     qq = Queue()
#     visited = set()
#     qq.enqueue([beginWord])

#     while qq.size() > 0:
#         path = qq.dequeue()
#         vertex = path[-1] # vertex is our word ``
#         if vertex not in visited:
#             if vertex == endWord:
#                 return path
#             visited.add(vertex)
#             for new_vert in get_neighbors(vertex):
#                 new_path = list(path)
#                 new_path.append(new_vert)
#                 qq.enqueue



