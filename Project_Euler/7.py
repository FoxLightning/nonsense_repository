def prime_number(n):
    if n < 3:
        return n + 1
    c_num = 3
    count = 2
    while count != n:
        c_num += 2
        t = 3
        while t * t <= c_num and c_num % t != 0:
            t += 2
        if t * t > c_num:
            count += 1
    return c_num


print(prime_number(int(input())))


def test(f):
    print("Test:1 {}".format("Pass" if PrimeNumber(5) == 11 else "Fail"))
    print("Test:2 {}".format("Pass" if PrimeNumber(20) == 71 else "Fail"))
    print("Test:3 {}".format("Pass" if PrimeNumber(40) == 173 else "Fail"))
    print("Test:4 {}".format("Pass" if PrimeNumber(200) == 1223 else "Fail"))

test(prime_number)