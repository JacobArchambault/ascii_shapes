astr = "*"
for i in range(10):
    for j in range(10 - i):
        print(" ", end='')
    print(astr)
    astr += "**"