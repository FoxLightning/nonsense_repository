inp = input().split()

m = [[0 for i in range(int(inp[0])+1)] for j in range(int(inp[1])+1)]

for i in range(len(m)):
        m[i][0] = 1
for i in range(len(m[0])):
        m[0][i] = 1

for row in range(1, len(m)):
    for col in range(1, len(m[0])):
        m[row][col] = m[row-1][col] + m[row][col-1]

print(m[-1][-1])
