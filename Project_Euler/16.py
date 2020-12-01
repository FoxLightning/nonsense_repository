
def find(a,b):
    s = 0
    for i in str(a ** b):
        s += int(i)
    return s


enter = input().split()
print((find(int(enter[0]), int(enter[1]))))
