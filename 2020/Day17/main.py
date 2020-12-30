#!/bin/python3

def neighbours(x, y, z, w=None):
    if w is None:
        return [(a, b, c) for a in range(x - 1, x + 2) for b in range(y - 1, y + 2) for c in range(z - 1, z + 2)
                if (a, b, c) != (x, y, z)]
    else:
        return [(a, b, c, d) for a in range(x - 1, x + 2) for b in range(y - 1, y + 2) for c in range(z - 1, z + 2) for d in range(w - 1, w + 2)
                if (a, b, c, d) != (x, y, z, w)]

def extended_uni_coords(universe: dict):
    coords = set(universe.keys())
    nei_nei_s = set()

    for x in coords:
        nei_nei_s.update(neighbours(*x))

    return coords.union(nei_nei_s)


def active_neighbours(universe, coord):
    active_neineis = 0
    for neighbour in neighbours(*coord):
        if universe.get(neighbour) == '#':
            active_neineis += 1
    return active_neineis


def run_cycles(cycles: int, universe: dict):
    for cycle in range(cycles):
        coords = extended_uni_coords(universe)
        print(f"\nRunde {cycle}")
        update = {}
        for coord in coords:
            status = universe.get(coord, '.')
            if status == '.' and active_neighbours(universe, coord) == 3:
                update[coord] = '#'
                #print(f"ICH WERDE AKTIV: {coord}")
            elif status == '#' and not(active_neighbours(universe, coord) in (2, 3)):
                update[coord] = '.'
                #print(f"ICH SCHLAF EIN: {coord}")
        universe.update(update)


if __name__ == "__main__":
    universe = {}
    hypercube = {}

    with open("input.txt") as f:
        input = f.read().strip().splitlines()

    for y, line in enumerate(input):
        for x, status in enumerate(line):
            universe[(x, y, 0)] = status
            hypercube[(x, y, 0, 0)] = status
    run_cycles(6, universe)
    run_cycles(6, hypercube)
    print(f"silver: {len(list(filter(lambda x: x == '#', universe.values())))}")
    print(f"gold: {len(list(filter(lambda x: x == '#', hypercube.values())))}")
