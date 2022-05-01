for x in range(9):
    for y in range(9):
        if int(str(x) + str(y)) - 36 == int(str(y) + str(x)):
            print(x, y, int(str(x) + str(y)) - 36)
