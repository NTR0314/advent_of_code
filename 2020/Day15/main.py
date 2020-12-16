input = [16, 12, 1, 0, 15, 7, 11]
last_said = {}
said_twice = set()

# init
for round, x in enumerate(input, 1):
    last_said[x] = round

curr_num = 0
for x in range(1 + len(input), 30000000):
    # calc next num
    next_num = None
    if curr_num in last_said:
        next_num = x - last_said[curr_num]
    else:
        next_num = 0

    last_said[curr_num] = x

    curr_num = next_num

print(f"silver: {curr_num}")
