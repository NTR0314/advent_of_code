import re

passports = open("input.txt", "r").read()[:-1].split("\n\n")
pass_details = [re.split('\n| ', x) for x in passports]
dicts = []

for liste in pass_details:
    details_dict = {}
    for attribut in liste:
        kek = attribut.split(":")
        details_dict.update({kek[0]: kek[1]})
    dicts.append(details_dict)

silver_count = 0
gold_count = 0

def debug(bool, attr, dict):
    if bool:
        print("VALID", attr + ":", dict.get(attr))
    else:
        print("INVALID", attr + ":", dict.get(attr))

def check_gold(dict):
    byr = 1920 <= int(dict.get('byr')) <= 2002
    #debug(byr, 'byr', dict)

    iyr = 2010 <= int(dict.get('iyr')) <= 2020
    #debug(iyr, 'iyr', dict)

    eyr = 2020 <= int(dict.get('eyr')) <= 2030
    #debug(eyr, 'eyr', dict)

    hgt = False

    hgt_unit = dict.get('hgt')[-2:]
    if not (hgt_unit == 'in' or hgt_unit == 'cm'):
        #print("INVALID FORMAT:", dict.get('hgt'))
        return False
    hgt_number = int(dict.get('hgt')[:-2])
    if hgt_unit == 'in':
        hgt = 59 <= int(dict.get('hgt')[:-2]) <= 76
    elif hgt_unit == 'cm':
        hgt = 150 <= hgt_number <= 193
    #debug(hgt, 'hgt', dict)

    # hcl_pattern = re.compile('#(\d{6}|[a-f]{6})')
    hcl_pattern = re.compile('#(\d|[a-f]){6}')
    hcl = hcl_pattern.match(dict.get('hcl')) is not None
    #debug(hcl, 'hcl', dict)

    ecl_pattern = re.compile('(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)')
    ecl = ecl_pattern.match(dict.get('ecl')) is not None
    #debug(ecl, 'ecl', dict)

    pid_pattern = re.compile('\d{9}')
    pid = pid_pattern.fullmatch(dict.get('pid')) is not None
    #debug(pid, 'pid', dict)

    return pid and ecl and hcl and hgt and eyr and iyr and byr


def check_silver(x):
    return len(x) == 8 or (not 'cid' in x and len(x) == 7)


for x in dicts:
    if check_silver(x):
        silver_count += 1
        if check_gold(x):
            gold_count += 1

print("silver:", silver_count)
print("gold:", gold_count)
