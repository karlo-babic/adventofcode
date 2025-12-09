with open('7_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
beam_coords = {lines[0].index('S'): 1}

def propagate(coords, iter):
    new_coords = {}
    for coord, count in coords.items():
        if lines[iter][coord] == '^':
            new_coords[coord-1] = new_coords.get(coord-1, 0) + count
            new_coords[coord+1] = new_coords.get(coord+1, 0) + count
        else:
            new_coords[coord] = new_coords.get(coord, 0) + count
    return new_coords

for i in range(1, len(lines)):
    beam_coords = propagate(beam_coords, i)
print(sum(beam_coords.values()))
