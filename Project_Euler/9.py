
def is_pifagor_triple(n):
    for x in range(1, n-1):
        for y in range(1, n-1):
            if x + y <= n-2:
                z = n - x - y
                if x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or z**2 + y**2 == x**2:
                    return x*y*z
    return "Not found"
print(is_pifagor_triple(int(input())))

def test(func):
    print("Test 1: {}".format("Ok" if func(12) == 60 else "Fail"))
    print(func(12))
    print()
    print("Test 2: {}".format("Ok" if func(100) == "Not found" else "Fail"))
    print(func(100))
    print()
    print("Test 3: {}".format("Ok" if func(150) == 97500 else "Fail"))
    print(func(150))

test(is_pifagor_triple)