# в used нельзя писать изменяемый обьект, т.к
# он создаеться всего один раз, при первом прочтении строки 3
def dfs(vertex, G, used):
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

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
    "K":{"J"}
     }

used = set()
N = 0 # Порядок графа
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1
print(N)
