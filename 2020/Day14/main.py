import re


def boss_transformation_90tage(el):
    uff = re.match(r'mem\[(\d+)\] = (\d+)', el)

    return uff.groups()


def lauch_trafo(uff: str) -> str:
    binuff = bin(int(uff))[2:]
    return '0' * (36 - len(binuff)) + binuff


def tim_gabel_trafo(pshh: str) -> str:
    queue_8_koegen = [pshh]

    while queue_8_koegen:
        if not 'X' in queue_8_koegen[0]:
            return queue_8_koegen

        bizepz = queue_8_koegen.pop(0)

        for celaoe, cut36 in enumerate(bizepz):
            if cut36 == 'X':
                mosh37 = list(bizepz)
                mosh37[celaoe] = '0'
                queue_8_koegen.append("".join(mosh37))
                mosh37[celaoe] = '1'
                queue_8_koegen.append("".join(mosh37))
                break

    return queue_8_koegen


input = open("input.txt").read()
uffz = [x.strip() for x in re.split('(mask = (?:\d|X){36}\n)', input)[1:]]
blockz = list(
    zip([x[7:] for x in uffz[::2]], [list(map(boss_transformation_90tage, x.split('\n'))) for x in uffz[1::2]]))

silver_memory = {}
gold_memory = {}
for blokk in blockz:
    mask = blokk[0]
    instructions = blokk[1]

    for i in instructions:
        bin_str = lauch_trafo(i[1])
        bin_adr = lauch_trafo(i[0])
        # print(f"dezimal: {i[1]}, \tbin-convert: {bin_str}, \tlen: {len(bin_str)}")
        result = []
        gold_adr = []
        for ind, bit in enumerate(mask):
            if bit == '0':
                result.append(bit)
                gold_adr.append(bin_adr[ind])
            elif bit == '1':
                result.append(bit)
                gold_adr.append('1')
            else:
                result.append(bin_str[ind])
                gold_adr.append('X')

        gold_adrzszssz = tim_gabel_trafo("".join(gold_adr))
        for x in gold_adrzszssz:
            gold_memory[int(x, 2)] = int(i[1])

        silver_memory[i[0]] = int("".join(result), 2)

print(f"silver: {sum(silver_memory.values())}")
print(f"gold: {sum(gold_memory.values())}")
