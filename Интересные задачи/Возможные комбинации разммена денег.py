a = int(input())
b = input().split()
for i in range(len(b)):
    b[i] = int(b[i])

def make_exchange(money, coins):
    coins = [0] + [i for i in coins]
    coins.sort()
    combinations = [[0]*(money+1) for i in range(len(coins))]
    methods = [[0]*(money+1) for i in range(len(coins))]
    for i in range(1, len(coins)):
        for j in range(1, money + 1):
            if j - coins[i] == 0:
                methods[i][j] = j
                combinations[i][j] = combinations[i-1][j] +1
            elif j - (coins[i] + methods[i][j - coins[i]]) == 0:
                methods[i][j] = j
                combinations[i][j] = combinations[i-1][j] + combinations[i][j - coins[i]]
            else:
                methods[i][j] = methods[i-1][j]
                combinations[i][j] = combinations[i-1][j]

    return combinations[-1][-1]

print(make_exchange(a, b))















