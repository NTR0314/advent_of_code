from math import prod
from itertools import combinations

xs = [int(x) for x in open("input.txt")]

def solve(n):
    return prod({sum(Y): Y for Y in combinations(xs, n)}[2020])

print("Silver:", solve(2))
print("Gold:", solve(3))
