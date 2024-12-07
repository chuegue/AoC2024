import numpy as np

lhs = []
rhs = []
with open("input.txt") as file:
    for line in file:
        lhs.append(int(line.split(':')[0])) 
        rhs.append(list(map(int, line.split(':')[1].strip().split())))

sum1 = 0
for i,r in enumerate(rhs):
    bin_size = len(r) - 1
    max_bin = 2 ** bin_size - 1
    while max_bin >= 0:
        ops = bin(max_bin).split('b')[1]
        if len(ops) < bin_size:
            ops = '0' * (bin_size - len(ops)) + ops
        # 1 is add, 0 is mult
        total = 0
        for o,op in enumerate(ops):
            if op == '1':
                if o == 0:
                    total += r[0] + r[1]
                else:
                    total += r[o + 1]
            elif op == '0':
                if o == 0:
                    total += r[0] * r[1]
                else:
                    total *= r[o + 1]
        if total == lhs[i]:
            sum1+=lhs[i]
            #print(lhs[i], r, ops)
            break
        max_bin -= 1

print(sum1)

sum2 = 0
for i,r in enumerate(rhs):
    ter_size = len(r) - 1
    max_ter = 3 ** ter_size - 1
    while max_ter >= 0:
        ops = np.base_repr(max_ter, base=3)
        if len(ops) < ter_size:
            ops = '0' * (ter_size - len(ops)) + ops
        # 1 is add, 0 is mult, 2 is concat
        total = 0
        for o,op in enumerate(ops):
            if op == '1':
                if o == 0:
                    total += r[0] + r[1]
                else:
                    total += r[o + 1]
            elif op == '0':
                if o == 0:
                    total += r[0] * r[1]
                else:
                    total *= r[o + 1]
            elif op == '2':
                if o == 0:
                    total += int(str(r[0]) + str(r[1]))
                else:
                    total = int(str(total) + str(r[o + 1]))
        if total == lhs[i]:
            sum2+=lhs[i]
            #print(lhs[i], r, ops)
            break
        max_ter -= 1


print(sum2)
