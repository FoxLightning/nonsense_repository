
a = int(input())
def f(x):
    m = [i*i for i in range(1, x+1)]
    m1 = [i for i in range(1, x+1)]
    sm = 0
    sm1 = 0
    for i in m:
        sm += i
    for i in m1:
        sm1 += i
    return sm1**2 - sm


print(f(a))
