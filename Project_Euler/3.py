def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def find(n):
    max = n
    i = 2
    while n >= i:
        if isPrime(n):
            return max if max > n else n
        if n % i == 0:
            n = n // i
            if isPrime(i):
                max = i
        i += 1
    return max



print(find(int(input())))

