from copy import copy

instructions = list(map(lambda x: [x[0], int(x[1])], [y.split() for y in open("input.txt")]))


asd = {
    'nop': lambda x: (0, 1),
    'acc': lambda x: (x, 1),
    'jmp': lambda x: (0, x)
}

for i in range(len(instructions)):
    acc = ip = 0
    history = []
    temp_instructions = copy(instructions)
    if temp_instructions[i][0] == 'nop':
        temp_instructions[i][0] = 'jmp'
    elif temp_instructions[i][0] == 'jmp':
        temp_instructions[i][0] = 'nop'
    else:
        continue
    while ip not in history:
        history.append(ip)
        if ip >= len(instructions):
            break
        op, param = temp_instructions[ip]
        ka, kaka = asd[op](param)
        acc += ka
        ip += kaka
        if ip == len(instructions):
            print('cok', acc)
    if temp_instructions[i][0] == 'nop':
        temp_instructions[i][0] = 'jmp'
    elif temp_instructions[i][0] == 'jmp':
        temp_instructions[i][0] = 'nop'

print('hannes'.translate(str.maketrans("S", "P")))
print({ord("n"): ord("p")})
print(str.maketrans("n", "p"))
print(acc)
