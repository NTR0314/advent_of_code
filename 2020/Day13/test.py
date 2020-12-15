x = 5
y = 7

result = 0
while True:
    if (result + 1) % 7 == 0 and result % 5 == 0:
        print(result)
        break
    result += 1
