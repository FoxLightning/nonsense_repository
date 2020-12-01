string = "ab"

def permutations(string, prefix=None, h_s=None, list_p=None):
    h_s = string if h_s == None else h_s
    list_p = [] if list_p == None else list_p
    if prefix != None and len(prefix) == len(string):
        list_p.append(prefix)
        return
    used = set()
    for i in range(len(h_s)):
        if h_s[i] not in used:
            used.add(h_s[i])
            tmp_s = h_s[:i] + h_s[i+1:]
            tmp_p = prefix + h_s[i] if prefix != None else h_s[i]
            permutations(string, tmp_p, tmp_s, list_p)

    return list_p

print(permutations(string))
