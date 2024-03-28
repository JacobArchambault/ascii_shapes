length = 10
asterisks = "*"
for i in range(length):
    for j in range(length - i):
        print(" ", end='')
    print(asterisks)
    asterisks += "**"
length -= 1
space = 1
asterisk_count = ((length * 2) - 1)
asterisks = "*" * asterisk_count
for i in range(length):
    print(" " + space * " " + asterisks)
    asterisk_count -= 2
    asterisks = "*" * asterisk_count
    space += 1