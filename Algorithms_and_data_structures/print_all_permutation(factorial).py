def gen_num(range_num:int, range_pos=-1, prefix=None):
    if range_pos == -1:
        range_pos = range_num
    if range_pos == 0:
        print(prefix)
        return None

    prefix = prefix or []
    for number in range(1, range_num+1):
        if number not in prefix:
            prefix.append(number)
            gen_num(range_num, range_pos-1, prefix)
            prefix.pop()

def gen_sym(range_num:set, range_pos=-1, prefix=None):
    if range_pos == -1:
        range_pos = len(range_num)
    if range_pos == 0:
        print(prefix)
        return None

    prefix = prefix or []
    for number in range_num:
        if number not in prefix:
            prefix.append(number)
            gen_sym(range_num, range_pos-1, prefix)
            prefix.pop()

a = {"a", "b", "c"}
gen_sym(a)

