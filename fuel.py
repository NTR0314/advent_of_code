f = open("fuel_input.txt", "r")
if f.mode == 'r':
    f1 = f.readlines()
    fuel = 0
    for x in f1:
        fuel += (int(int(x) / 3) - 2)
print(fuel)
