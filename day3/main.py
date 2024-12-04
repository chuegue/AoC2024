import re
import math

muls1 = []
ops2 = []
sum1 = 0
sum2 = 0
with open("input.txt") as file:
    for line in file:
        sum1 += sum([math.prod(list(map(int, pair))) for pair in re.findall(r"mul\((\d+),(\d+)\)", line)])
        ops2 += re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line) 

active = 1
for op in ops2:
    if op == 'do()':
        active = 1
    elif op == 'don\'t()':
        active = 0
    else:
        if active == 1:
            sum2 += math.prod(map(int, re.findall(r"\d{1,3}", op)))

print(sum1)
print(sum2)
