import re

regex = re.compile("([\w\s]+)\(contains (\w+(?:, \w+)*)\)")
with open("input.txt") as f:
    matches = [re.match(regex, line) for line in f.readlines()]
tuples = [(x[0].strip().split(), x[1].split(', ')) for x in [y.groups() for y in matches]]
# print(tuples)

possible_allergic_ingrediants = {}
all_ingredients = set()
for ingrediants, allergants in tuples:
    for allergant in allergants:
        if allergant not in possible_allergic_ingrediants:
            possible_allergic_ingrediants[allergant] = set(ingrediants)
        possible_allergic_ingrediants[allergant] = possible_allergic_ingrediants[allergant].intersection(
            set(ingrediants))
        for ingrediant in ingrediants:
            all_ingredients.add(ingrediant)

# print(possible_ingredients)
# print(all_ingredients)
print(possible_allergic_ingrediants)

all_possible = set()
for allergant in possible_allergic_ingrediants:
    all_possible = all_possible.union(possible_allergic_ingrediants[allergant])

non_allergic_ing = all_ingredients - all_possible

# print(non_allergic_ing)

count = 0
for food, _ in tuples:
    for ing in food:
        if ing in non_allergic_ing:
            count += 1

print(f"gold: {count}")

dangerous_list = ""

for x in sorted(possible_allergic_ingrediants, key=lambda x: len(possible_allergic_ingrediants[x])):
    for y in possible_allergic_ingrediants:
        if x == y:
            continue
        possible_allergic_ingrediants[y] = possible_allergic_ingrediants[y] - possible_allergic_ingrediants[x]

for x in sorted(possible_allergic_ingrediants):
    print(x, possible_allergic_ingrediants[x])

# Hab den String geraten xD: vpzxk,bkgmcsx,qfzv,tjtgbf,rjdqt,hbnf,jspkl,hdcj

