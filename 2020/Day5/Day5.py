def parseSeat(string):
    row = int(string[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(string[7:].replace('L', '0').replace('R', '1'), 2)

    return row * 8 + column

with open("input.txt", 'r') as input:
    ids = [parseSeat(seat) for seat in input]
    gold = [y + 1 for y in ids for z in ids if y + 2 == z if not y + 1 in set(ids)][0]
    print("silver:", max(ids))
    print("gold:", gold)
