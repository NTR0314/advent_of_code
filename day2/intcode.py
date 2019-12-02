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

    print("initial")
    print(file)

    while (op(file, op_code_ptr) == 1) & (op_code_ptr <= len(file)):
        print("running")
        print(file)
        op_code_ptr += 4

    print(file[0])
