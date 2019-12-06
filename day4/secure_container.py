def check_double(strn):
    result = False
    for i in range(len(strn)):
        if i == 0:
            continue
        if strn[i - 1] == strn[i]:
            result = True
    return result


def check_double2(strn):
    result = False
    bigger_group_char = 'x'
    for i in range(len(strn) - 2):
        if strn[i] == strn[i + 1]:
            if strn[i + 1] != strn[i + 2] and not strn[i] == bigger_group_char:
                result = True
            bigger_group_char = strn[i]
    if strn[-1] == strn[-2] != strn[-3]:
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


def a1():
    count = 0
    for i in range(108457, 562041):
        strn = str(i)
        a = check_double(strn)
        b = check_not_decreasing(strn)
        if a and b:
            count += 1
    print(count)


def a2():
    count = 0
    for i in range(108457, 562041):
        strn = str(i)
        a = check_not_decreasing(strn)
        b = check_double2(strn)
        if a and b:
            count += 1
            #  print(i)
    print(count)


a1()
a2()
