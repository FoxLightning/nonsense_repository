
def triangle_number(n:int):
    return int((1 + n)*n / 2)

def num_of_div(n:int):
    d = {}
    i = 2
    while n != 1:
        if n % i == 0:
            d[i] = 1
        while n % i == 0:
            n //= i
            d[i] += 1
        i += 1
    ans = 1
    for i in d.values():
        ans *= i
    return ans

def triangle_div(n):
    i = 1
    div = 0
    t_num = 1
    while div <= n:
        t_num = triangle_number(i)
        div = num_of_div(t_num)
        i += 1
    return t_num


print(triangle_div(int(input())))






