with open('9_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
coords = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]

areas = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        if coords[i][0] == coords[j][0]:
            areas.append(abs(coords[i][1] - coords[j][1]) + 1)
        elif coords[i][1] == coords[j][1]:
            areas.append(abs(coords[i][0] - coords[j][0]) + 1)
        else:
            areas.append((abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1))

print(max(areas))