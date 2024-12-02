with open("input.txt") as file:
    reports = [list(map(int, line.split())) for line in file]

def check_ascending(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1] or arr[i] - arr[i-1] > 3:
            return 0
    return 1

def check_descending(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1] or arr[i] - arr[i-1] < -3:
            return 0
    return 1

def check_ascending2(arr):
    if check_ascending(arr) == 0:
        for i in range(len(arr)):
            arrcpy = arr.copy()
            arrcpy.pop(i)
            if check_ascending(arrcpy) == 1:
                return 1
        return 0
    else:
        return 1

def check_descending2(arr):
    if check_descending(arr) == 0:
        for i in range(len(arr)):
            arrcpy = arr.copy()
            arrcpy.pop(i)
            if check_descending(arrcpy) == 1:
                return 1
        return 0
    else:
        return 1

sum1 = 0
sum2 = 0
for report in reports:
    sum1 += check_ascending(report) + check_descending(report)
    sum2 += check_ascending2(report) + check_descending2(report)

print(sum1)
print(sum2)
