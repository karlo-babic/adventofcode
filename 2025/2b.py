with open('2_input.txt') as f:
    line = f.readlines()[0]

ranges = [r for r in line.split(',')]
invalid_ids = []

def repeats(s, r):
    if len(s) % r != 0:
        return False

    part_a = s[:r]
    for i in range(len(s)//r):
        part_b = s[i*r:(i+1)*r]
        if part_a != part_b:
            return False
    return True

for r in ranges:
    beg = int(r.split('-')[0])
    end = int(r.split('-')[1]) + 1
    for id in range(beg, end):
        id = str(id)
        for r in range(1, len(id)//2+1):
            if repeats(id, r):
                invalid_ids.append(int(id))
                break

print(sum(invalid_ids))