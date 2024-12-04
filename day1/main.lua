values1 = {}
values2 = {}
for line in io.lines("input.txt") do
	v1,v2 = line:match("(%d+)%s+(%d+)")
	table.insert(values1, v1)
	table.insert(values2, v2)
end

table.sort(values1)
table.sort(values2)

sum1 = 0
sum2 = 0
count = {} --hash table that keeps the count of the values in values2

for i=1,#values2 do
	local value = values2[i]
	if not count[value] then count[value] = 1 else count[value] = count[value] + 1 end
end

for i=1,#values1 do
	sum1 = sum1 + math.abs(values1[i] - values2[i])
	if count[values1[i]] ~= nil then
		sum2 = sum2 + (values1[i] * count[values1[i]])
	end
end
print(sum1)
print(sum2)
