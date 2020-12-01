
def b(string):
    answer = [0] * len(string)
    i = 2
    k = 1
    j = 0
    while i < len(string):
        if string[j] == string[i] == string[k]:
            answer[i] = j+1
            j += 1
            i += 1
            k += 1
        elif j > 0:
            j -= 1
        elif j == 0:
            i += 1
    return answer

print(*b(input()))
