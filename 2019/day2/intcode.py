def op(input, ptr):
    opcode = input[ptr]
    pos1_ptr = input[ptr + 1]
    pos2_ptr = input[ptr + 2]
    res_ptr = input[ptr + 3]

    if opcode == 99:
        return -1
    if opcode == 1:
        input[res_ptr] = input[pos1_ptr] + input[pos2_ptr]
        return 1
    if opcode == 2:
        input[res_ptr] = input[pos1_ptr] * input[pos2_ptr]
        return 1
    return -1


def a1():
    f = open("input.txt", "r")
    if f.mode == 'r':
        file = f.read()
        file = file.split(",")

        #  cast chars to ints
        file = [int(i) for i in file]

        #  restore gravity program xD
        file[1] = 12
        file[2] = 2
        op_code_ptr = 0

        while (op(file, op_code_ptr) == 1) & (op_code_ptr <= len(file)):
            op_code_ptr += 4

        print(file[0])


def a2_help(noun, verb):
    f = open("input.txt", "r")
    if f.mode == 'r':
        file = f.read()
        file = file.split(",")

        #  cast chars to ints
        file = [int(i) for i in file]

        #  restore gravity program xD
        file[1] = noun
        file[2] = verb
        op_code_ptr = 0

        while (op(file, op_code_ptr) == 1) and (op_code_ptr <= len(file)):
            op_code_ptr += 4

        return file[0]


def a2():
    depth = 1
    found = False

    for x in range(100):
        for y in range(100):
            res = a2_help(x, y)
            if res == 19690720:
                print("n1gger")
                print(100 * x + y)


a1()
a2()
