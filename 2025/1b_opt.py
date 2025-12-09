import math

lines = [line.strip() for line in open('1_input.txt').readlines()]
x, count_0 = 50, 0

for line in lines:
    direction, distance = line[0], int(line[1:])
    d = -1 if direction == 'L' else 1

    count_0 += math.floor(distance / 100)
    remainder = distance % 100

    if (x + remainder*d < 0 or x + remainder*d > 100) and x != 0:
        count_0 += 1
    x += remainder*d
    x = x % 100

    if x == 0:
        count_0 += 1

print(count_0)