with open('1_input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

x = 50
count_0 = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])

    if direction == 'L':
        x -= distance
    elif direction == 'R':
        x += distance
    x = x % 100

    if x == 0:
        count_0 += 1

print(count_0)