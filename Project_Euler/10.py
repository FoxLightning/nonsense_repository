def prime_sum(n):
    not_prime = set()
    sum = 0
    for i in range(2, n):
        if i not in not_prime:
            sum += i
            k = 2
            while i * k < n:
                not_prime.add(i * k)
                k += 1
    return sum

print(prime_sum(int(input())))
