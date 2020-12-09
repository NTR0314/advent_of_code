from itertools import combinations

numbers = [int(x.strip()) for x in open("input.txt").readlines()]


def check_valid(preamble, number):
    return number in map(sum, combinations(preamble, 2))


preamble = numbers[:25]
numbers = numbers[25:]

print(len(preamble))

for number in numbers:
    if check_valid(preamble, number):
        preamble.pop(0)
        preamble.append(number)
    else:
        print(f"silver: {number}")
        break

for x in range(2, len(numbers)):
    seqs = []
    for y in range(len(numbers) - x):
        seqs.append(numbers[y:y + x])
    for y in seqs:
        if sum((gold := y)) == number:
            print(f"gold: {min(gold) + max(gold)}")
            exit()
