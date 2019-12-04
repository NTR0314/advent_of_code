count = 0

def check_double(strn):
    result = False
    for i in range(len(strn)):
        if i == 0:
            continue
        if (strn[i - 1] == strn[i]):
            result = True
    return result

def check_not_decreasing(strn):
    result = True
    for i in range(len(strn)):
        if i == len(strn) - 1:
            continue
        if int(strn[i + 1]) < int(strn[i]):
            result = False
    return result

for i in range(108457,562041):
    strn = str(i)
    a = check_double(strn)
    b = check_not_decreasing(strn)
    if (a and b):
        count += 1
print(count)
