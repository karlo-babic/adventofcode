with open('9_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
coords = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]

def line_crosses(border_line, diagonal_line):
    right = max(diagonal_line[0][0], diagonal_line[1][0])
    top = max(diagonal_line[0][1], diagonal_line[1][1])
    left = min(diagonal_line[0][0], diagonal_line[1][0])
    bottom = min(diagonal_line[0][1], diagonal_line[1][1])

    within_x_0 = border_line[0][0] < right and border_line[0][0] > left
    within_y_0 = border_line[0][1] < top and border_line[0][1] > bottom
    within_x_1 = border_line[1][0] < right and border_line[1][0] > left
    within_y_1 = border_line[1][1] < top and border_line[1][1] > bottom

    if within_x_0 and within_y_0 or within_x_1 and within_y_1:
        return True

    outside_x = max(border_line[0][0], border_line[1][0]) >= right and min(border_line[0][0], border_line[1][0]) <= left
    outside_y = max(border_line[0][1], border_line[1][1]) >= top and min(border_line[0][1], border_line[1][1]) <= bottom

    if outside_y and within_x_0 and within_x_1:
        return True
    if outside_x and within_y_0 and within_y_1:
        return True
    return False

def legal(coord0, coord1):
    for i in range(len(coords)):
        j = i+1 if i < len(coords) - 1 else 0
        border_line = (coords[i], coords[j])
        if line_crosses(border_line, (coord0, coord1)):
            return False
    return True

areas = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        if not legal(coords[i], coords[j]):
            continue
        if coords[i][0] == coords[j][0]:
            areas.append(abs(coords[i][1] - coords[j][1]) + 1)
        elif coords[i][1] == coords[j][1]:
            areas.append(abs(coords[i][0] - coords[j][0]) + 1)
        else:
            areas.append((abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1))

print(max(areas))