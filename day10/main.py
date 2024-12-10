matrix = [list(map(int, list(line.strip()))) for line in open("input.txt").readlines()]
rows = len(matrix)
cols = len(matrix[0])

    
def bfs(pos):
    Q = []
    Q.append(pos)
    visited = set()
    count = 0
    while len(Q) != 0:
        v = Q.pop(0)
        if matrix[v[0]][v[1]] == 9 and v not in visited:
            count += 1
            visited.add(v)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for r_off, c_off in dirs:
            r,c = v[0]+r_off, v[1]+c_off
            if 0<=r<len(matrix) and 0<=c<len(matrix[0]):
                if matrix[r][c] - matrix[v[0]][v[1]] == 1:
                    Q.append((r,c))
    return count


def bfs2(pos):
    Q = []
    Q.append(pos)
    visited = dict()
    count = 0
    while len(Q) != 0:
        v = Q.pop(0)
        if matrix[v[0]][v[1]] == 9:
            count += 1
            if v not in visited:
                visited[v] = 1
            else:
                visited[v] += 1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for r_off, c_off in dirs:
            r,c = v[0]+r_off, v[1]+c_off
            if 0<=r<len(matrix) and 0<=c<len(matrix[0]):
                if matrix[r][c] - matrix[v[0]][v[1]] == 1:
                    Q.append((r,c))
    return count


count = 0
count2 = 0
for r, row in enumerate(matrix):
    for c, val in enumerate(row):
        if val == 0:
            count += bfs((r,c))
            count2 += bfs2((r,c))

print(count)
print(count2)
