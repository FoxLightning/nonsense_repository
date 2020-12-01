import sys, re
m = sys.stdin.read().split("\n")
s=0
for i in m:
    s += int(i)
print((str(s))[0:10])
