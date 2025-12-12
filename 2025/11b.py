from collections import deque

with open('11_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
connections = {}
for line in lines:
    key = line.split(': ')[0]
    values = line.split(': ')[1].split(' ')
    connections[key] = values

connections_before = {}
for key in connections:
    for value in connections[key]:
        if value not in connections_before:
            connections_before[value] = set()
        connections_before[value].add(key)

def all_after(node):
    nodes_after = set()
    if node == 'out':
        return nodes_after
    new_nodes = set(connections[node])
    while new_nodes:
        nodes_after.update(new_nodes)
        new_nodes = set()
        for node in nodes_after:
            if node == 'out':
                continue
            nodes_to_add = [node for node in connections[node] if node not in nodes_after]
            new_nodes.update(nodes_to_add)
    return nodes_after

def all_before(node):
    nodes_before = set()
    if node == 'svr':
        return nodes_before
    new_nodes = set(connections_before[node])
    while new_nodes:
        nodes_before.update(new_nodes)
        new_nodes = set()
        for node in nodes_before:
            if node == 'svr':
                continue
            nodes_to_add = [node for node in connections_before[node] if node not in nodes_before]
            new_nodes.update(nodes_to_add)
    return nodes_before

ok_connections = {}
for key in connections:
    after = all_after(key)
    before = all_before(key)
    ffc_after = 'fft' in after
    ffc_before = 'fft' in before
    dac_after = 'dac' in after
    dac_before = 'dac' in before
    if (ffc_after or ffc_before) and (dac_after or dac_before) or key == 'fft' or key == 'dac' or key == 'out' or key == 'svr':
        ok_connections[key] = connections[key]
for key in ok_connections:
    ok_connections[key] = [node for node in ok_connections[key] if node in ok_connections or node == 'out' or node == 'svr']

def num_paths(graph, src, dest):
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    in_degree = {node: 0 for node in all_nodes}
    paths = {node: 0 for node in all_nodes}
    
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            
    q = deque()
    for node in all_nodes:
        if in_degree[node] == 0:
            q.append(node)

    paths[src] = 1
    while q:
        u = q.popleft()
        if u in graph:
            for v in graph[u]:
                paths[v] += paths[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
    return paths[dest]

print(num_paths(ok_connections, 'svr', 'out'))