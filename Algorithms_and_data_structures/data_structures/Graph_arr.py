M, N = [ int(x) for x in input().split()]
V = [None]*N
index = {}
A = [[0]*N for i in range(N)]

for i in range(N):
    v1, v2 =  input(). split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
    v1_i = index[v1]
    v2_i = index[v2]
    # если граф не простой то += 1
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1
