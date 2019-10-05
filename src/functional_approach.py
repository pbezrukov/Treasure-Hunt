def treasure(table, x=0, y=0):
    value_of_cell = str(table[x][y])
    coordinates = str(x+1) + str(y+1)

    if value_of_cell == coordinates:
        print(value_of_cell, end=' ')

    else:
        x = int(value_of_cell[0]) - 1
        y = int(value_of_cell[1]) - 1
        print(value_of_cell, end=' ')
        treasure(table, x, y)


map_of_treasure = [[34, 21, 32, 41, 25],
                   [14, 42, 43, 14, 31],
                   [54, 45, 52, 42, 23],
                   [33, 15, 51, 31, 35],
                   [21, 52, 33, 13, 23]]

treasure(map_of_treasure)
