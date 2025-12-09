import re

with open('6_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [re.sub(r' +', ' ', line) for line in lines]
    lines = [line.split() for line in lines]
nums_m = lines[:-1]
ops = lines[-1]

def transpose(m):
    m_t = []
    for x in range(len(m[0])):
        m_t.append([])
        for y in range(len(m)):
            m_t[x].append(int(m[y][x]))
    return m_t
nums_m = transpose(nums_m)

def prod(nums):
    res = 1
    for val in nums:
        res = res * val
    return res

results = []
for i in range(len(ops)):
    if ops[i] == '+':
        r = sum(nums_m[i])
    else:  # *
        r = prod(nums_m[i])
    results.append(r)

print(sum(results))