file = open("input.txt").readlines()[0].strip()

decompressed_orig = []
for i,c in enumerate(file):
    if i % 2 == 0:
        decompressed_orig += [i // 2 for _ in range(int(c))]
        #decompressed += int(c) * str((i // 2) % 10)
    else:
        decompressed_orig += [-1 for _ in range(int(c))]


decompressed = decompressed_orig.copy()
empty = 0
last = len(decompressed) - 1
while empty < last:
    if decompressed[empty] != -1:
        empty += 1
        continue
    while decompressed[last] == -1:
        last -= 1
    if empty >= last: break
    decompressed[empty] = decompressed[last]
    decompressed[last] = -1

#print(decompressed)

sum1 = 0
for i,c in enumerate(decompressed):
    if c == -1: break
    sum1 += i*int(c)
print(sum1)

for i in range(len(decompressed_orig) - 1, -1, -1):
    if decompressed_orig[i] != -1:
        highest_id = decompressed_orig[i]
        break

def first_and_length_empty(arr, from_idx):
    length = 0
    first = -1
    for i in range(from_idx, len(arr)):
        if arr[i] != -1: continue
        for j in range(i + 1, len(arr)):
            if arr[j] != -1:
                return (i, j -i)
    return (0, -1)

def print_disk(arr):
    a = ""
    for c in arr:
        if c == -1:
            a += '.'
        else:
            a += str(c)
    print(a)

decompressed = decompressed_orig.copy()
while highest_id >= 1:
    #print(highest_id) #progress tracking
    f_first = decompressed.index(highest_id)
    f_length = decompressed.count(highest_id)
    e_first, e_length = first_and_length_empty(decompressed, 0)
    while e_length != -1:
        if e_length >= f_length and e_first < f_first: #move file over
            decompressed[e_first:e_first+f_length],decompressed[f_first:f_first+f_length] = decompressed[f_first:f_first+f_length],decompressed[e_first:e_first+f_length]
            break
        if e_first > f_first: break
        e_first, e_length = first_and_length_empty(decompressed, e_first + e_length)
    highest_id -= 1
    
#print_disk(decompressed)

sum1 = 0
for i,c in enumerate(decompressed):
    if c == -1: continue
    sum1 += i*int(c)
print(sum1)
