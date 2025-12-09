with open('7_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
beam_coords = [lines[0].index('S')]

def propagate(coords, iter):
    new_coords = set()
    splits = 0
    for coord in coords:
        if lines[iter][coord] == '^':
            splits += 1
            new_coords.add(coord - 1)
            new_coords.add(coord + 1)
        else:
            new_coords.add(coord)
    return new_coords, splits

total_splits = 0
for i in range(1, len(lines)):
    beam_coords, splits = propagate(beam_coords, i)
    total_splits += splits
print(total_splits)