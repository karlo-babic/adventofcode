with open('3_input.txt') as f:
    banks = f.readlines()

def string_to_ints(s):
    ints = []
    for i in range(len(s)):
        ints.append(int(s[i]))
    return ints

def get_best_number(jolts, digits):
    num_string = ''
    min_i = 0
    for i in range(digits, 0, -1):
        max_i = len(jolts) - i
        part = jolts[min_i:max_i+1]
        biggest_in_part = max(part)
        num_string += str(biggest_in_part)
        min_i = min_i + part.index(biggest_in_part) + 1
    return int(num_string)

total = 0
for bank in banks:
    bank = bank.strip()
    if not bank:
        continue

    jolts = string_to_ints(bank)
    num = get_best_number(jolts, 12)

    total += num

print(total)