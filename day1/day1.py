arr1 = []
arr2 = []

with open("input.txt") as file:
    arr1,arr2 = map(list, zip(*(map(int, line.split()) for line in file)))

arr1.sort()
arr2.sort()

sum1 = 0
sum2 = 0
for i in range(len(arr1)):
    sum1 += abs(arr1[i] - arr2[i])
    sum2 += arr1[i] * arr2.count(arr1[i])

print(sum1)
print(sum2)


