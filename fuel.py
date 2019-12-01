f = open("fuel_input.txt", "r")


def fuel_mass(x):
    return (int(int(x) / 3) - 2)


def mass_fuel_rec(mass):
    result = fuel_mass(mass)
    if fuel_mass(result) > 0:
        result += mass_fuel_rec(result)
    return result


# A1
if f.mode == 'r':
    f1 = f.readlines()
    fuel_a1 = 0
    fuel_a2 = 0
    for x in f1:
        fuel_a1 += fuel_mass(x)
        fuel_a2 += mass_fuel_rec(x)
print(fuel_a1)
print(fuel_a2)
