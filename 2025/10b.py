import pulp

with open('10_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
machines = [{'display': line.split(' ')[0], 'buttons': line.split(' ')[1:-1], 'jolts': line.split(' ')[-1]} for line in lines]
for machine in machines:
    machine['display'] = [-1 if d == '.' else 1 for d in machine['display'][1:-1]]
    machine['buttons'] = [[int(d) for d in button[1:-1].split(',')] for button in machine['buttons']]
    machine['jolts'] = [int(j) for j in machine['jolts'][1:-1].split(',')]

def optimize(machine, map_jolt_buttons):
    model = pulp.LpProblem("Minimize_x", pulp.LpMinimize)
    x = pulp.LpVariable('x', lowBound=0, cat='Integer')
    model += x

    button_presses = []
    for i, button in enumerate(machine['buttons']):
        button_presses.append(pulp.LpVariable(f"bp{i}", lowBound=0, cat='Integer'))
    model += (x == pulp.lpSum(button_presses))
    
    for i, target_value in enumerate(machine['jolts']):
        vars = [button_presses[b] for b in map_jolt_buttons[i]]
        model += (target_value == pulp.lpSum(vars))

    solver = pulp.PULP_CBC_CMD(msg=False)
    status = model.solve(solver)

    if pulp.LpStatus[status] == 'Optimal':
        return int(x.varValue)

total_button_presses = 0
for machine in machines:
    map_jolt_buttons = {}
    for i, button in enumerate(machine['buttons']):
        for j in button:
            if j not in map_jolt_buttons:
                map_jolt_buttons[j] = []
            map_jolt_buttons[j].append(i)

    total_button_presses += optimize(machine, map_jolt_buttons)

print(total_button_presses)
