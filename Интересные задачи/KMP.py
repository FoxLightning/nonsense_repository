s = "asdasdasd"
word = "ab"


def prefix(s):
    '''
    создает массив с префиксами
    '''
    pi = [0] * len(s)
    i = 1
    j = 0

    while i < len(s):
        if s[j] != s[i]:
            if j == 0:
                pi[i] = 0
                i += 1
            else: # j != 0
                j = pi[j-1]
        else:  # s[j] == s[i]
            pi[i] = j + 1
            j += 1
            i += 1
    return pi

def KMP(string, word):
    '''
    быстрый поиcк строки в строке
    O(n)
    '''
    m = prefix(word)
    s = 0
    w = 0
    ans = []
    while s < len(string):
        if string[s] == word[w] and w == len(word)-1:
            ans.append(s)
            s += 1
            w = 0
        elif string[s] == word[w]:
            s += 1
            w += 1
        elif string[s] != word[w] and w != 0:
            w = m[w-1]
        elif string[s] != word[w] and w == 0:
            s += 1
        else:
            print("unexpected encident")
            return
    return ans

print(prefix("aaabaab"))