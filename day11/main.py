stones_orig = list(map(int, open("input.txt").readlines()[0].strip().split()))

stones = dict()
for stone in stones_orig:
    if stone not in stones:
        stones[stone] = 1
    else:
        stones[stone] += 1
for _ in range(25):
    #print(_)
    new_stones = dict()
    for stone, num in stones.items():
        if stone == 0:
            if 1 not in new_stones: new_stones[1] = num
            else: new_stones[1] += num
        elif len(str(stone)) % 2 == 0:
            a = int(str(stone)[:len(str(stone))//2])
            b = int(str(stone)[len(str(stone))//2:])
            if a not in new_stones: new_stones[a] = num
            else: new_stones[a] += num
            if b not in new_stones: new_stones[b] = num
            else: new_stones[b] += num
        else:
            if stone * 2024 not in new_stones: new_stones[stone * 2024] = num
            else: new_stones[stone * 2024] += num
    stones = new_stones
print(sum(stones.values()))

stones = dict()
for stone in stones_orig:
    if stone not in stones:
        stones[stone] = 1
    else:
        stones[stone] += 1
for _ in range(75):
    #print(_)
    new_stones = dict()
    for stone, num in stones.items():
        if stone == 0:
            if 1 not in new_stones: new_stones[1] = num
            else: new_stones[1] += num
        elif len(str(stone)) % 2 == 0:
            a = int(str(stone)[:len(str(stone))//2])
            b = int(str(stone)[len(str(stone))//2:])
            if a not in new_stones: new_stones[a] = num
            else: new_stones[a] += num
            if b not in new_stones: new_stones[b] = num
            else: new_stones[b] += num
        else:
            if stone * 2024 not in new_stones: new_stones[stone * 2024] = num
            else: new_stones[stone * 2024] += num
    stones = new_stones
print(sum(stones.values()))
