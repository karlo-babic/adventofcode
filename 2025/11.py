from collections import deque

with open('11_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
connections = {}
for line in lines:
    key = line.split(': ')[0]
    values = line.split(': ')[1].split(' ')
    connections[key] = values

def num_paths(origin, target):
    path_count = 0
    nodes_to_explore = deque([origin])
    
    while nodes_to_explore:
        node = nodes_to_explore.popleft()
        if node == target:
            path_count += 1
            continue
        next_nodes = connections[node]
        nodes_to_explore.extend(next_nodes)

    return path_count

print(num_paths('you', 'out'))