f = open('5_input.txt')
flag_reading_ranges = True
fresh_ranges = []
ids = []
while True:
    line = f.readline()
    if not line:
        break
    line = line.strip()
    if flag_reading_ranges and line == '':
        flag_reading_ranges = False
        continue
    if flag_reading_ranges:
        range_split = line.split('-')
        fresh_ranges.append( (int(range_split[0]), int(range_split[1])) )
    else:  # ids
        ids.append(int(line))

def is_within_range(id, ranges):
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            return True
    return False

count = 0
for id in ids:
    if is_within_range(id, fresh_ranges):
        count += 1

print(count)