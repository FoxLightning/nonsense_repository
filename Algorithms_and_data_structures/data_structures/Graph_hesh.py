M, N = [ int(x) for x in input().split()]
G = {}
for i in range(N):
    v1, v2 = input().split()
    for v,n in (v1,v2), (v2,v1):
        if v not in G:
            G[v] = {n}
        else:
            G[v].add(n)