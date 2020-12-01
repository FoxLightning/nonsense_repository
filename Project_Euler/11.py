import sys


m = sys.stdin.read().split("\n")
for i in range(len(m)):
    m[i] = m[i].split(" ")
def find(m):
    max = 0
    # for horizontal
    for row in range(len(m)):
        for col in range(len(m[row])-4):
            current = int(m[row][col]) * int(m[row][col+1]) * int(m[row][col+2]) * int(m[row][col+3])
            max = current if current > max else max
    # for diagonal left
    for row in range(len(m)-4):
        for col in range(len(m[row])-4):
            current = int(m[row][col]) * int(m[row+1][col+1]) * int(m[row+2][col+2]) * int(m[row+3][col+3])
            max = current if current > max else max
    # for diagonal left
    for row in range(len(m) - 4):
        for col in range(len(m[row]) - 4):
            current = int(m[row][col+3]) * int(m[row+1][col+2]) * int(m[row+2][col+1]) * int(m[row+3][col])
            max = current if current > max else max
    # for diagonal left
    for row in range(len(m) - 4):
        for col in range(len(m[row])):
            current = int(m[row][col]) * int(m[row + 1][col]) * int(m[row + 2][col]) * int(m[row+3][col])
            max = current if current > max else max
    return max

print(find(m))

