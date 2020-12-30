import re

with open("input.txt") as f:
    blockz = f.read().split('\n\n')


def makefunc(ll, lu, rl, ru):
    return lambda x: ll <= x <= lu or rl <= x <= ru


rules = {}
for rule_str in blockz[0].splitlines():
    groups = re.match(r'([\w\s]+): (\d+-\d+) or (\d+-\d+)', rule_str).groups()
    a = [int(x) for x in groups[1].split('-')]
    b = [int(x) for x in groups[2].split('-')]
    rules[groups[0]] = makefunc(a[0], a[1], b[0], b[1])


def is_valid(numxd: int) -> bool:
    for rule in rules.values():
        if rule(numxd):
            return True
    return False

nearby_tickets = blockz[2].splitlines()[1:]
error_count = 0
for nt in nearby_tickets:
    numberz = [int(x) for x in nt.split(',')]
    for number in numberz:
        if not is_valid(number):
            error_count += number
            nearby_tickets.remove(nt)
            break


# gold
def check_column(current_column, rule):
    for valid_ticket in nearby_tickets:
        if not rule(int(valid_ticket.split(',')[current_column])):
            return False
    return True


def check_cat(cat, rule):
    possible_columns = set()
    for column in range(len(nearby_tickets[0].split(','))):
        if check_column(column, rule):
            possible_columns.add(column)
    return possible_columns


possibilities = {}
for cat, rule in rules.items():
    possibilities[cat] = check_cat(cat, rule)

myticket = [int(x) for x in blockz[1].splitlines()[1].split(',')]

print(possibilities)
print(f"silver: {error_count}")
# print(f"gold: {sum([myticket[x] for x in [0, 9 ,1 ,2 , 12]])}")
