with open('2_input.txt') as f:
    line = f.readlines()[0]

ranges = [r for r in line.split(',')]
invalid_ids = []

for r in ranges:
    beg = int(r.split('-')[0])
    end = int(r.split('-')[1]) + 1
    for id in range(beg, end):
        id = str(id)
        if len(id) % 2 != 0:
            continue

        mid = int(len(id)/2)
        first_half = id[:mid]
        second_half = id[mid:]

        if first_half == second_half:
            invalid_ids.append(int(id))

print(sum(invalid_ids))