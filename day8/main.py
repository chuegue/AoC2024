import math


## Part 1
frequencies = set()
matrix = []
with open("input.txt") as file:
    for line in file:
        for c in line.strip():
            if c not in frequencies and c != '.':
                frequencies.add(c)
        matrix.append(list(line.strip()))

print(frequencies)
antinodes = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

for i,line in enumerate(matrix):
    for j,c in enumerate(line):
        if c in frequencies:
            for u,line2 in enumerate(matrix):
                for v,c2 in enumerate(line2):
                    if c == c2 and (i != u and j != v):
                        vector = [u-i, v-j]
                        an_spot = [u+vector[0], v+vector[1]]
                        if an_spot[0] < 0 or an_spot[0] >= len(matrix) or an_spot[1] < 0 or an_spot[1] >= len(matrix[0]):
                            continue
                        antinodes[u+vector[0]][v+vector[1]] = '#'

sum1 = 0
for line in antinodes:
    sum1 += line.count('#')
    print(''.join(line))

print(sum1)

##Part2
frequencies = set()
matrix = []
with open("input.txt") as file:
    for line in file:
        for c in line.strip():
            if c not in frequencies and c != '.':
                frequencies.add(c)
        matrix.append(list(line.strip()))

print(frequencies)
antinodes = [['.' for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

for i,line in enumerate(matrix):
    for j,c in enumerate(line):
        if c in frequencies:
            for u,line2 in enumerate(matrix):
                for v,c2 in enumerate(line2):
                    if c == c2 and (i != u and j != v):
                        vector = [u-i, v-j]
                        vec_gcd = math.gcd(vector[0], vector[1])
                        vector = [vector[0]//vec_gcd, vector[1]//vec_gcd]
                        an_spot = [u+vector[0], v+vector[1]]
                        while not(an_spot[0] < 0 or an_spot[0] >= len(matrix) or an_spot[1] < 0 or an_spot[1] >= len(matrix[0])):
                            antinodes[an_spot[0]][an_spot[1]] = '#'
                            an_spot = [an_spot[0] + vector[0], an_spot[1] + vector[1]]
                        vector = [-(u-i), -(v-j)]
                        vec_gcd = math.gcd(vector[0], vector[1])
                        vector = [vector[0]//vec_gcd, vector[1]//vec_gcd]
                        an_spot = [u+vector[0], v+vector[1]]
                        while not(an_spot[0] < 0 or an_spot[0] >= len(matrix) or an_spot[1] < 0 or an_spot[1] >= len(matrix[0])):
                            antinodes[an_spot[0]][an_spot[1]] = '#'
                            an_spot = [an_spot[0] + vector[0], an_spot[1] + vector[1]]

sum1 = 0
for line in antinodes:
    sum1 += line.count('#')
    print(''.join(line))

print(sum1)
