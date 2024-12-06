matrix = []

with open("input.txt") as file:
    for line in file:
        matrix.append(list(line.split('\n')[0]))


pos_orig = []
direction_orig = 0

for i, line in enumerate(matrix):
    for j, c in enumerate(line):
        if c != '.' and c != '#':
            pos_orig.append(i)
            pos_orig.append(j)
            if c == '^':
                direction_orig = 0
            elif c == '>':
                direction_orig = 1
            elif c == 'v':
                direction_orig = 2
            else:
                direction_orig = 3

def is_inside(matrix, pos):
    x = pos[0]
    y = pos[1]
    lenx = len(matrix)
    leny = len(matrix[0])
    return not (x < 0 or x >= lenx or y < 0 or y >= leny)

vectors = [[-1,0],[0,1],[1,0],[0,-1]]
matrix1 = [line.copy() for line in matrix]
pos = pos_orig.copy()
direction = direction_orig
while True:
    add = lambda a,b: [a[0]+b[0],a[1]+b[1]]
    matrix1[pos[0]][pos[1]] = 'X'
    vector = vectors[direction]
    next_pos = add(pos, vector)
    if not is_inside(matrix1, next_pos):
        break
    if matrix1[next_pos[0]][next_pos[1]] == '#':
        direction = (direction+1)%4
        next_pos = add(pos, vectors[direction])
    pos = next_pos

def next_pos(matrix, pos, direction) -> list[list[int], int]:
    add = lambda a,b: [a[0]+b[0],a[1]+b[1]]
    vector = vectors[direction]
    next_pos = add(pos, vector)
    if not is_inside(matrix, next_pos):
        return [next_pos, direction]
    if matrix2[next_pos[0]][next_pos[1]] == '#':
        direction = (direction+1)%4
        next_pos = add(pos, vectors[direction])
        pos = next_pos
    return [next_pos, direction]



sum2 = 0
nspots = len(matrix)*len(matrix[0])
for i,line in enumerate(matrix):
    for j,c in enumerate(line):
        if c != '.':
            continue
        matrix2 = [line.copy() for line in matrix]
        pos = pos_orig.copy()
        direction = direction_orig
        matrix2[i][j] = '#'
        visited = []
        while True:
            add = lambda a,b: [a[0]+b[0],a[1]+b[1]]
            vector = vectors[direction]
            next_pos = add(pos, vector)
            if not is_inside(matrix, next_pos):
                break
            if matrix2[next_pos[0]][next_pos[1]] == '#':
                if [next_pos, direction] in visited:
                    sum2 += 1
                    break
                visited.append([next_pos, direction])
                direction = (direction+1)%4
                continue
                #next_pos = add(pos, vectors[direction])
            pos = next_pos
            
        print(f"{i*len(matrix[0]) + j} out of {nspots}")

        



sum1 = 0
for line in matrix1:
    sum1 += line.count('X')
    #print(''.join(line))

print(sum1)
print(sum2)
