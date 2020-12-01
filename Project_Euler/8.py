import sys, re


def find(length, num_list):
    s_max = 0
    for i in range(len(num_list)-length):
        s = 1
        for j in num_list[i:i+length]:
            s *= int(j)
        if s > s_max:
            s_max = s
    return(s_max)


length = int(input())
num_list = re.sub(r"\n", "", sys.stdin.read())
print(find(length, num_list))