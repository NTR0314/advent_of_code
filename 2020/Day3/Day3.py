from math import prod

linez = [x for x in open("input.txt")]
repeat_length = len(linez[0]) - 1


def trajectory(right, down):
    tree_count = r = d = 0

    while d < len(linez):
        if linez[d][r % repeat_length] == '#':
            tree_count += 1

        r += right
        d += down

    return tree_count


print('### day3 ###')
print("silver:", trajectory(3, 1))
print("gold:", prod([trajectory(x, y) for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))
