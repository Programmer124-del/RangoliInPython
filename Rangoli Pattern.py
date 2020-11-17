import string


alpha = string.ascii_lowercase

num = int(input("Please enter a number: "))

for i in range(num - 1, 0, -1):
    dashes = ['-'] * (num * 2 - 1)
    for x in range(0, num - i):
        dashes[num - 1 - x] = alpha[x + i]
        dashes[num - 1 + x] = alpha[x + i]
    print('-'.join(dashes))


for i in range(0, num):
    dashes = ['-'] * (num * 2 - 1)
    for x in range(0, num - i):
        dashes[num - 1 - x] = alpha[x + i]
        dashes[num - 1 + x] = alpha[x + i]
    print('-'.join(dashes))

