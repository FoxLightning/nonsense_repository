import sys

enter = sys.stdin.read().split("\n")

for i in range(len(enter)):
    enter[i] = enter[i].split()

for i in range(1, len(enter)):
    for j in range(len(enter[i])):
        if j < len(enter[i-1]) and j-1 >= 0:
            enter[i][j] = max(int(enter[i-1][j-1]), int(enter[i-1][j])) + int(enter[i][j])
        elif j >= len(enter[i-1]) and j-1 >=0:
            enter[i][j] = int(enter[i - 1][j - 1]) + int(enter[i][j])
        else: # j < len(enter(i-1) and j-1 < 0:
            enter[i][j] = int(enter[i-1][j]) + int(enter[i][j])

print(max(enter[-1]))



