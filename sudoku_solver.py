board = [
    [0, 5, 0, 0, 8, 7, 3, 1, 0],
    [4, 0, 7, 0, 1, 0, 0, 9, 0],
    [0, 0, 6, 9, 0, 0, 0, 0, 2],
    [0, 0, 0, 6, 5, 4, 0, 3, 0],
    [0, 2, 0, 0, 9, 0, 8, 0, 7],
    [3, 1, 5, 0, 0, 0, 0, 0, 9],
    [8, 0, 0, 0, 0, 1, 9, 0, 4],
    [9, 0, 0, 3, 0, 2, 0, 0, 5],
    [0, 7, 2, 8, 0, 0, 0, 6, 0]
]


def print_board(bd):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('---------------------')

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')

            if j == 8:
                print(bd[i][j])

            else:
                print(str(bd[i][j]) + ' ', end='')

def valid(bd, row, column, number):
    # check for row
    for i in range(9):
        if bd[row][i] == number:
            return False
    # check for column
    for i in range(9):
        if bd[i][column] == number:
            return False

    # check for box(ps:this is a good idea)
    x = (row // 3) * 3
    y = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if bd[x + i][y + j] == number:
                return False

    return True


def solve(bd):
    for row in range(0,9):
        for column in range(0,9):
            if bd[row][column] == 0:
                for number in range(1,10):
                    if valid(bd, row, column, number):
                        bd[row][column] = number
                        solve(bd)
                        bd[row][column] = 0
                return



    print_board(bd)
    input('more possible ways')






solve(board)



