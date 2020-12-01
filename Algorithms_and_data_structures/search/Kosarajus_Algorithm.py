class Stack:

    def __init__(self):
        """
        Create new exemplar of Linked List
        """
        self._begin = None

    def __str__(self):
        """
        convert exemplar to str
        :return: array of all values in linkedlist
        """
        m = []
        a = self._begin

        while True:
            m.append(a[0])
            a = a[1]
            if a is None:
                break
        return str(m)

    def push(self, value):
        """
        input value at begin of LList
        :param value: any object
        """
        self._begin = [value, self._begin]

    def pop(self):
        """
        delete first value
        :return: first value
        """
        assert self._begin is not None, "List empty"
        value = self._begin[0]
        self._begin = self._begin[1]
        return value

    def top(self):
        """
        :return: first value
        """
        assert self._begin is not None, "List empty"
        return self._begin[0]

    def is_empty(self):
        """
        :return: True / False
        """
        return self._begin is None

    def clear(self):
        """
        delete all values in stack
        """
        self._begin = None

def invert(G):
    IG = {}
    for i in G:
        if i not in IG:
            IG[i] = set()
        for j in G[i]:
            if j not in IG:
                IG[j] = set()
            IG[j].add(i)
    return IG

def dfs(vertex, G, used):
    used.add(vertex)
    global stack
    stack.push(vertex)

    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)


def dfs2(vertex, G, used):
    used.add(vertex)
    global stack
    stack.push(vertex)

    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)


stack = Stack()
G = {"A":{"B"},
    "B":{"C", "D"},
    "C":{"A"},
    "D":{"E"},
    "E":{"F"},
    "F":{"D"},
    "G":{"F", "H"},
    "H":{"I"},
    "I":{"J"},
    "J":{"G"},
    "K":{"J"}}

used = set()
N = 0 # Порядок графа
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1

used.clear()

while not stack.is_empty():
    tmp = stack.pop()




print(N)