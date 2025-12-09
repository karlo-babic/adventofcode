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
        break

sorted_fresh_ranges = sorted(fresh_ranges, key=lambda x: x[0])
merged_ranges = []
for i in range(len(sorted_fresh_ranges)):
    if i == 0:
        merged_ranges.append(sorted_fresh_ranges[i])
    elif sorted_fresh_ranges[i][0] <= merged_ranges[-1][1]:
        if sorted_fresh_ranges[i][1] > merged_ranges[-1][1]:
            merged_ranges[-1] = (merged_ranges[-1][0], sorted_fresh_ranges[i][1])
    else:
        merged_ranges.append(sorted_fresh_ranges[i])

total = 0
for r in merged_ranges:
    total += r[1] - r[0] + 1

print(total)