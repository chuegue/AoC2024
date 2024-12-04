matrix = []
with open("input.txt") as file:
    for line in file:
        matrix += line.split()

def validate_pos1(matrix, pos):
    x = pos[0]
    y = pos[1]
    if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
        return False
    return True

def search1(matrix, i, j):
    sum = 0
    vectors = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    supposed = 'MAS'
    for vector in vectors:
        valid = 1
        for length in range(1,4):
            x = i+vector[0]*length
            y = j+vector[1]*length
            if not validate_pos1(matrix, (x,y)):
                valid = 0
                break
            if matrix[x][y] != supposed[length - 1]:
                valid = 0
                break
        if valid == 1:
            sum += 1
    return sum
            
def search2(m, i ,j):
    validate = lambda m,i,j: i > 0 and j > 0 and i < len(m[0]) - 1 and j < len(m) - 1
    if not validate(m, i, j):
        return 0
    if m[i-1][j-1] == 'M' and m[i-1][j+1] == 'M' and m[i+1][j-1] == 'S' and m[i+1][j+1] == 'S':
        return 1
    if m[i-1][j-1] == 'M' and m[i-1][j+1] == 'S' and m[i+1][j-1] == 'M' and m[i+1][j+1] == 'S':
        return 1
    if m[i-1][j-1] == 'S' and m[i-1][j+1] == 'S' and m[i+1][j-1] == 'M' and m[i+1][j+1] == 'M':
        return 1
    if m[i-1][j-1] == 'S' and m[i-1][j+1] == 'M' and m[i+1][j-1] == 'S' and m[i+1][j+1] == 'M':
        return 1
    return 0



sum1 = 0
sum2 = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        c = matrix[i][j]
        if c == 'X':
            sum1 += search1(matrix, i, j)
        if c == 'A':
            sum2 += search2(matrix, i, j)
print(sum1)
print(sum2)
