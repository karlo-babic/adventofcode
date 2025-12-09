with open('3_input.txt') as f:
    banks = f.readlines()

def string_to_ints(s):
    ints = []
    for i in range(len(s)):
        ints.append(int(s[i]))
    return ints

def get_best_2(jolts):
    biggest = max(jolts[:-1])
    second_biggest = max(jolts[jolts.index(biggest)+1:])
    return int(str(biggest) + str(second_biggest))

total = 0
for bank in banks:
    bank = bank.strip()
    if not bank:
        continue

    jolts = string_to_ints(bank)
    num = get_best_2(jolts)

    total += num

print(total)