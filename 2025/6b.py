with open('6_input.txt') as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
nums_m = lines[:-1]
ops = lines[-1].split()

def transpose(m):
    m_t = [[]]
    for x in range(len(m[0])):
        m_t[-1].append('')
        for y in range(len(m)):
            m_t[-1][-1] += m[y][x]
        if m_t[-1][-1].strip() == '':
            del(m_t[-1][-1])
            m_t.append([])
        else:
            m_t[-1][-1] = int(m_t[-1][-1])
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