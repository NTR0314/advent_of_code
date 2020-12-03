def isValidSilver(min, max, char, password):
    counter = 0
    for i in range(len(password)):
        if char == password[i]:
            counter += 1

    return min <= counter <= max


def isValidGold(first, second, char, password):
    return (password[first - 1] == char) != (password[second - 1] == char)


with open("input.txt", "r") as input:
    lines = input.readlines()
    correct_count = 0
    gold_count = 0

    for line in lines:
        splitted = line.split(" ")
        valdi_split = splitted[0].split("-")
        min = int(valdi_split[0])
        max = int(valdi_split[1])
        char = splitted[1][0]
        pw = splitted[2][0:-1]

        if isValidSilver(min, max, char, pw):
            correct_count += 1

        if isValidGold(min, max, char, pw):
            gold_count += 1

print("Silver:", correct_count)
print("Gold:", gold_count)
