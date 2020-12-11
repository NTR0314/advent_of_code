import itertools

sr_silver = [x.strip() for x in open("input.txt")]
sr_gold = sr_silver.copy()
rowsize = len(sr_silver[0])
rows = len(sr_silver)


# Von Stackoverflow geklaut
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def count_gold(seatmap):
    adjacents = [([0] * len(seatmap[0])) for i in range(len(seatmap))]
    adj = 0

    for i in range(rows):
        for j in range(rowsize):
            curr_adj = set()
            # links
            for k in range(1, j + 1):
                if (seatmap[i][j - k]) == 'L':
                    break
                if (seatmap[i][j - k]) == '#':
                    curr_adj.add((i, j - k))
                    break
            # rechts
            for k in range(1, rowsize - j):
                if (seatmap[i][j + k]) == 'L':
                    break
                if (seatmap[i][j + k]) == '#':
                    curr_adj.add((i, j + k))
                    break
            # unten
            for k in range(1, rows - i):
                # print(f"UNTEN: Current Seat: {(i, j)} checking on {i - k, j}:{seatmap[i - k][j]}")
                if (seatmap[i + k][j]) == 'L':
                    break
                if (seatmap[i + k][j]) == '#':
                    curr_adj.add((i + k, j))
                    break
            # oben
            for k in range(1, i + 1):
                # print(f"OBEN: Current Seat: {(i, j)} checking on {i - k, j}:{seatmap[i - k][j]}")
                if (seatmap[i - k][j]) == 'L':
                    break
                if (seatmap[i - k][j]) == '#':
                    curr_adj.add((i - k, j))
                    break
            # unten links
            for k in range(1, min(rows - i, j + 1)):
                if (seatmap[i + k][j - k]) == 'L':
                    break
                if (seatmap[i + k][j - k]) == '#':
                    curr_adj.add((i + k, j - k))
                    break
            # oben links
            for k in range(1, min(i + 1, j + 1)):
                if (seatmap[i - k][j - k]) == 'L':
                    break
                if (seatmap[i - k][j - k]) == '#':
                    curr_adj.add((i - k, j - k))
                    break
            # oben rechts
            for k in range(1, min(i + 1, rowsize - j)):
                if (seatmap[i - k][j + k]) == 'L':
                    break
                if (seatmap[i - k][j + k]) == '#':
                    curr_adj.add((i - k, j + k))
                    break
            for k in range(1, min(rows - i, rowsize - j)):
                if (seatmap[i + k][j + k]) == 'L':
                    break
                if (seatmap[i + k][j + k]) == '#':
                    curr_adj.add((i + k, j + k))
                    break
            adjacents[i][j] = len(curr_adj)
    #         print(f"current Seat:{(i,j)} adj:{curr_adj}")
    #
    # for i in range(len(seatmap)):
    #     print(seatmap[i], "    ", adjacents[i])
    # print("-----------------------")

    return adjacents


def count_silver(seatmap):
    adjacents = [([0] * len(seatmap[0])) for i in range(len(seatmap))]
    adj = 0

    for i in range(len(seatmap)):
        for j in range(len(seatmap[0])):
            if j - 1 >= 0 and (seatmap[i][j - 1]) == '#':
                adj += 1
            if j + 1 < rowsize and (seatmap[i][j + 1]) == '#':
                adj += 1
            if i + 1 < rows and (seatmap[i + 1][j]) == '#':
                adj += 1
            if i - 1 >= 0 and (seatmap[i - 1][j]) == '#':
                adj += 1
            if i - 1 >= 0 and j - 1 >= 0 and (seatmap[i - 1][j - 1] == '#'):
                adj += 1
            if i - 1 >= 0 and j + 1 < rowsize and (seatmap[i - 1][j + 1] == '#'):
                adj += 1
            if i + 1 < rows and j - 1 >= 0 and (seatmap[i + 1][j - 1] == '#'):
                adj += 1
            if i + 1 < rows and j + 1 < rowsize and (seatmap[i + 1][j + 1] == '#'):
                adj += 1

            adjacents[i][j] = adj
            adj = 0
    return adjacents


def apply_rule(seatmap, adj_map, gold=False):
    min_seats_needed = 4
    if gold:
        min_seats_needed = 5

    changed = False
    for i in range(len(seatmap)):
        for j in range(len(seatmap[i])):
            if adj_map[i][j] >= min_seats_needed and seatmap[i][j] == '#':
                seatmap[i] = replacer(seatmap[i], 'L', j, nofail=True)
                changed = True
            if adj_map[i][j] == 0 and seatmap[i][j] == 'L':
                seatmap[i] = replacer(seatmap[i], '#', j, nofail=True)
                changed = True
    return changed


while apply_rule(sr_silver, count_silver(sr_silver)):
    None
while apply_rule(sr_gold, count_gold(sr_gold), gold=True):
    None

print(f"silver: {list(itertools.chain.from_iterable(sr_silver)).count('#')}")
print(f"gold: {list(itertools.chain.from_iterable(sr_gold)).count('#')}")
