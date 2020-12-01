n = int(input())

fn = [1,2]

while True:
    a = fn[-1] + fn[-2]
    if a <= n:
        fn.append(a)
    else:
        break
if n == 2:
    fn = [1,2]
elif n < 2:
    fn = [0]


s = 0
for i in fn:
    if i % 2 == 0:
        s += i


print(s)









