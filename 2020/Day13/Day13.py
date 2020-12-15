import time

start_time = time.time()

lines = [x.strip() for x in open("input.txt").readlines()]

timestamp = int(lines[0])
buses = [int(x) for x in lines[1].replace('x,', '').split(',')]

min_bus = 0
min_waiting_time = 9999

for bus in buses:
    waiting_time = bus - (timestamp % bus)
    if waiting_time < min_waiting_time:
        min_waiting_time = waiting_time
        min_bus = bus

print(f"silver: {min_bus * min_waiting_time}")

bus_delays = sorted([(int(x[1]), x[0]) for x in enumerate(lines[1].split(',')) if x[1] != 'x'], key=lambda x: x[0],
                    reverse=True)
print(bus_delays)


def check_time(time, bus_delays):
    result = 1
    tiefe = 0
    print(f"t_gold = {t_gold}")
    for intervall, delay in bus_delays:
        print(f"Checking bus id:{delay} with intervall:{intervall} -> {time} + {delay} mod {intervall} = {(time + delay) % intervall}")
        if not (time + delay) % intervall == 0:
            return result
        tiefe += 1
        result *= intervall
    print("FOUND RESULT")
    return -1


# Because first bus doesn't necesseraly have delay zero
t_gold = 0 - bus_delays[0][1]
#for i in range(10):
#    inc = check_time(t_gold, bus_delays)
while (inc := check_time(t_gold, bus_delays)) > 0:
    t_gold += inc

# for bus in bus_delays:
#     print(f"bus id:{bus[1]}, bus intervall:{bus[0]}, check: {(t_gold + bus[1]) % bus[0]}")

print(f"gold: {t_gold}")
