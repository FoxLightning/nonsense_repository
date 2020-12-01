# Наименьшее общее кратное (НОК)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Наибольший общий делитель (НОД)
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b % a != 0:
        a %= b
        if a < b:
            a, b = b, a
    return a

n = int(input())
nok = lcm(1, 2)
for i in range(3, n + 1):
    nok = lcm(nok, i)
if n == 1:
    nok = 1
print(nok)