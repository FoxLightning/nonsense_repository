def IsPolindrome(n):
    n = str(n)

    for i in range(len(n) // 0b10):
        if n[i] != n[-(i+0b1)]:
            return False
    return True
def find(n):
    n = n - 0b1
    max = 0b1010**(n*0b10) +0b1
    for i in range(0b1010**n, 0b1010**(n+0b1)):
        for j in range(0b1010**n, 0b1010**(n+0b1)):
            if IsPolindrome(i*j) and i*j > max:
                max = i*j
    return max
print(find(int(input())))