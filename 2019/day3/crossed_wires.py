import sys


def getInt(string):
    return int(string[1:])


def manhattan_dist(tupel):
    a = abs(tupel[0] - 0)
    b = abs(tupel[1] - 0)

    return a + b


f = open("input.txt", "r")
if f.mode == 'r':
    path1 = f.readline()
    path2 = f.readline()
    path1 = path1.split(",")
    path2 = path2.split(",")

path1_points = [(0, 0)]
path1_dist_traveled = []
path1_count = 1
path2_points = [(0, 0)]
path2_dist_traveled = []
path2_count = 1

for instr in path1:
    if instr[0] == 'R':
        diff = abs(getInt(instr))
        last_point = (path1_points[-1][0], path1_points[-1][1])
        for x in range(diff):
            y = x + 1
            path1_points.append((last_point[0] + y, last_point[1]))
            path1_dist_traveled.append(path1_count)
            path1_count += 1
    elif instr[0] == 'L':
        diff = abs(getInt(instr))
        last_point = (path1_points[-1][0], path1_points[-1][1])
        for x in range(diff):
            y = x + 1
            path1_points.append((last_point[0] - y, last_point[1]))
            path1_dist_traveled.append(path1_count)
            path1_count += 1
    elif instr[0] == 'U':
        diff = abs(getInt(instr))
        last_point = (path1_points[-1][0], path1_points[-1][1])
        for x in range(diff):
            y = x + 1
            path1_points.append((last_point[0], last_point[1] + y))
            path1_dist_traveled.append(path1_count)
            path1_count += 1
    elif instr[0] == 'D':
        diff = abs(getInt(instr))
        last_point = (path1_points[-1][0], path1_points[-1][1])
        for x in range(diff):
            y = x + 1
            path1_points.append((last_point[0], last_point[1] - y))
            path1_dist_traveled.append(path1_count)
            path1_count += 1

for instr in path2:
    if instr[0] == 'R':
        diff = abs(getInt(instr))
        last_point = (path2_points[-1][0], path2_points[-1][1])
        for x in range(diff):
            y = x + 1
            path2_points.append((last_point[0] + y, last_point[1]))
            path2_dist_traveled.append(path2_count)
            path2_count += 1
    elif instr[0] == 'L':
        diff = abs(getInt(instr))
        last_point = (path2_points[-1][0], path2_points[-1][1])
        for x in range(diff):
            y = x + 1
            path2_points.append((last_point[0] - y, last_point[1]))
            path2_dist_traveled.append(path2_count)
            path2_count += 1
    elif instr[0] == 'U':
        diff = abs(getInt(instr))
        last_point = (path2_points[-1][0], path2_points[-1][1])
        for x in range(diff):
            y = x + 1
            path2_points.append((last_point[0], last_point[1] + y))
            path2_dist_traveled.append(path2_count)
            path2_count += 1
    elif instr[0] == 'D':
        diff = abs(getInt(instr))
        last_point = (path2_points[-1][0], path2_points[-1][1])
        for x in range(diff):
            y = x + 1
            path2_points.append((last_point[0], last_point[1] - y))
            path2_dist_traveled.append(path2_count)
            path2_count += 1

path2_points = path2_points[1:]
path1_points = path1_points[1:]

duplicates = set(path2_points).intersection(path1_points)
print(duplicates)

min = sys.maxsize

for tuple in duplicates:
    dist = manhattan_dist(tuple)
    if dist < min:
        min = dist

print(min)

min = sys.maxsize

for tuple in duplicates:
    idx1 = path1_points.index(tuple)
    idx2 = path2_points.index(tuple)
    steps = path1_dist_traveled[idx1] + path2_dist_traveled[idx2]
    if ( steps < min):
        min = steps

print(min)