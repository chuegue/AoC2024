is_rules = 1
rules = {}
updates = {}
forward_star = {}
backward_star = {}

function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

for line in io.lines("input.txt") do
	if #line == 0 then
		is_rules = 0
		goto continue 
	end
	if is_rules == 1 then --rules section
		rule = {}
		for v in line:gmatch("(%d+)") do
			table.insert(rule, tonumber(v))
		end
		table.insert(rules, rule)
		from = rule[1]
		to = rule[2]
		if forward_star[from] == nil then
			forward_star[from] = {}
		end
		forward_star[from][to] = true
		if backward_star[to] == nil then
			backward_star[to] = {}
		end
		backward_star[to][from] = true
	else --updates section
		update = {}
		for v in line:gmatch("(%d+)") do
			table.insert(update, tonumber(v))
		end
		table.insert(updates, update)
	end
	::continue::
end

print "Rules"
for i, r in ipairs(rules) do
	print(i)
	print("\t"..r[1].." "..r[2])
end
print "Updates"
for i, u in ipairs(updates) do
	print(i)
	str = ""
	for _,v in ipairs(u) do str = str..v.." " end
	print("\t"..str)
end
print "Forward Star"
for i, u in pairs(forward_star) do
	str = string.format("%d -> ", i)
	for v,_ in pairs(u) do
		str = str..v.." "
	end
	print(str)
end
print "Backward Star"
for i, u in pairs(backward_star) do
	str = ""
	for v,_ in pairs(u) do
		str = str..v.." "
	end
	str = str.."-> "..i
	print(str)
end

function midpageofincorrect(update)
	b_count = {}
	for i=1,#update do
		b_count[update[i]] = 0
	end
	for i,u in ipairs(update) do
		if backward_star[u] ~= nil then
			for j,v in ipairs(update) do
				if backward_star[u][v] ~= nil then
					b_count[u] = b_count[u] + 1
				end
			end
		end
	end
	target = (#update - 1) / 2
	for i,u in pairs(b_count) do
		if u == target then return i end
	end
end

sum1 = 0
sum2 = 0
for _,update in ipairs(updates) do
	correct = true
	for i,u in ipairs(update) do
		for j,v in ipairs(update) do
			if i < j then
				if forward_star[u] == nil then
					correct = false 
					break
				else
					if forward_star[u][v] == nil then
						correct = false
						break
					end
				end
			elseif j < i then
				if backward_star[u] == nil then
					correct = false 
					break
				else
					if backward_star[u][v] == nil then
						correct = false
						break
					end
				end
			end
		end
		if correct == false then break end
	end
	if correct == true then 
		sum1 = sum1 + update[(#update + 1) / 2] 
	else
		sum2 = sum2 + midpageofincorrect(update)
	end
end

print("\n"..sum1,sum2)
