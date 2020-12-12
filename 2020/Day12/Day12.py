import numpy as np

directions = [(y[0], int(y[1:])) for y in [x.strip() for x in open("input.txt").readlines()]]

compass = ['N', 'E', 'S', 'W']
curr_direction = 'E'
cur_pos_silver = [0, 0]
cur_pos_gold = [0, 0]
waypoint = [10, 1]

new_pos = {
    'N': lambda x: (0, x),
    'E': lambda x: (x, 0),
    'S': lambda x: (0, -x),
    'W': lambda x: (-x, 0),
}

def rotate(winkel, koordz):
    rotation_matrix = np.array([[np.cos(np.deg2rad(winkel)), - np.sin(np.deg2rad(winkel))],
                                [np.sin(np.deg2rad(winkel)), np.cos(np.deg2rad(winkel))]])
    return [round(x) for x in np.matmul(rotation_matrix, np.array(koordz)).tolist()]

def drive_boat(direction, amount):
    global curr_direction
    global cur_pos_silver
    global waypoint
    change_silver = (0, 0)

    if direction == 'L':
        curr_direction = compass[int((compass.index(curr_direction) - amount / 90) % 4)]
        waypoint = rotate(amount, waypoint)
    elif direction == 'R':
        curr_direction = compass[int((compass.index(curr_direction) + amount / 90) % 4)]
        waypoint = rotate(- amount, waypoint)
    elif direction == 'F':
        change_silver = new_pos.get(curr_direction)(amount)
        cur_pos_gold[0] += amount * waypoint[0]
        cur_pos_gold[1] += amount * waypoint[1]
    else:
        change_silver = new_pos.get(direction)(amount)
        waypoint[0] += change_silver[0]
        waypoint[1] += change_silver[1]
    cur_pos_silver[0] += change_silver[0]
    cur_pos_silver[1] += change_silver[1]
    print(f"direction:{direction}, amount:{amount}, current position gold:{cur_pos_gold}, waypoint:{waypoint}")


for d in directions:
    drive_boat(*d)

print(f"silver: {abs(cur_pos_silver[0]) + abs(cur_pos_silver[1])}")
print(f"gold: {abs(cur_pos_gold[0]) + abs(cur_pos_gold[1])}")
