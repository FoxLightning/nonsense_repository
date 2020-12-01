def colatz(n):
    if not n:
        return n
    s = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            s += 1
        else:
            n = 3*n + 1
            s += 1
    return s

def find(n):
    element = 0
    max = 0
    for i in range(n):
        current = colatz(i)
        if current > max:
            max = current
            element = i

    return element





print(find(int(input())))