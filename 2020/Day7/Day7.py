class BagRule:
    """ Describes a Rule about what bag can carry what bags"""

    def __init__(self, name, carries):
        self.name = name
        self.carries = carries

    def contains(self, name):
        return name in self.carries


def parse_bag_rule(string):
    name = string.split(" contain ")[0][:-5]
    can_carry_strs = string.split(" contain ")[1].split(", ")
    carries = {}

    for x in can_carry_strs:
        xs = x.split()
        if xs[0] == 'no':
            xs[0] = '0'
        carries.update({" ".join([xs[1], xs[2]]): int(xs[0])})

    return BagRule(name, carries)


def can_contain(name, rules):
    to_check = {name}
    contain = set()

    while len(to_check) != 0:
        elem = to_check.pop()
        for xname, x in rules.items():
            if x.contains(elem):
                to_check.add(x.name)
                contain.add(x.name)

    return contain


def bags_inside(name, rules):
    count = 0

    if rules.get(name) is not None:
        for x, y in rules.get(name).carries.items():
            #print(f"Checking bag: \'{name}\' found rule for: \'{x}\' and adding \'{y}\' bags to count.")
            count += y + y * bags_inside(x, rules)

    return count


rules = {parse_bag_rule(x[:-1]).name: parse_bag_rule(x[:-1]) for x in open("input.txt")}

print("silver:", len(can_contain("shiny gold", rules)))
print("gold:", bags_inside("shiny gold", rules))
