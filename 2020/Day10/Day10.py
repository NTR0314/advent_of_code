from math import prod, log10

file_path = "bigboy.txt"

adapters = [int(x) for x in open(file_path).readlines()]
adapters.sort()
# Laptop-Adapter
adapters.append(adapters[-1] + 3)

# silver
jdiffs = [0] * 4
prev_adapter = 0

for adapter in adapters:
    jdiffs[adapter - prev_adapter] += 1
    prev_adapter = adapter

print(f"silver: {jdiffs[1] * jdiffs[3]}")

# gold

# hack
adapters.insert(0, 0)


def pre_process(adapters):
    sublists = []
    prev_adapter = 0
    tmp = []
    for adapter in adapters:
        if adapter - prev_adapter >= 3:
            sublists.append(tmp)
            tmp = []
        tmp.append(adapter)
        prev_adapter = adapter

    return list(filter(lambda x: len(x) >= 3, sublists))


def calc_possible(adapters):
    if len(adapters) <= 1:
        return 1
    first = adapters.pop(0)

    possible_next = [x for x in adapters if x - first <= 3]

    return sum([calc_possible(adapters[adapters.index(x):]) for x in possible_next])


print(f"gold: log_10 ~= {log10(prod([calc_possible(x) for x in pre_process(adapters)]))}")
