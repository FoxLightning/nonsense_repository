

def pow1(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return (pow(a**2, b//2))
    else:
        return (pow(a, b-1) * a)

def pow0(a, b):
    if b == 0:
        return 1
    else:
        return pow(a, b-1) * a


def test(func):
    a = 10
    b = 3
    c = a ** b
    print("Test 1: {}".format("Ok" if func(a, b) == c else "Fale"))
    a = 7
    b = 5
    c = a ** b
    print("Test 2: {}".format("Ok" if func(a, b) == c else "Fale"))

test(pow1)
test(pow0)

print(pow1(2, 1024))
print(pow0(2, 1024))

