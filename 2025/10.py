from itertools import combinations

with open('10_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
machines = [{'display': line.split(' ')[0], 'buttons': line.split(' ')[1:-1], 'jolts': line.split(' ')[-1]} for line in lines]
for machine in machines:
    machine['display'] = [-1 if d == '.' else 1 for d in machine['display'][1:-1]]
    machine['buttons'] = [[int(d) for d in button[1:-1].split(',')] for button in machine['buttons']]
    machine['jolts'] = [int(j) for j in machine['jolts'][1:-1].split(',')]

def find_combination(machine, button_presses):
    for button_combo in combinations(machine['buttons'], button_presses):
        display = [-1 for d in machine['display']]
        for button in button_combo:
            for d in button:
                display[d] *= -1
        if display == machine['display']:
            return True
    return False

total_button_presses = 0
for machine in machines:
    for button_presses in range(1, len(machine['buttons']) + 1):
         if find_combination(machine, button_presses):
             total_button_presses += button_presses
             break

print(total_button_presses)
