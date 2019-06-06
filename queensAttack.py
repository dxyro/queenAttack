import os


def read_tex():
    try:
        if os.stat('archivo.txt').st_atime > 0:
            file = open('archivo.txt', 'r')
            list_lines = file.readlines()
            file.close()
            fulfill = validators(list_lines)
            if fulfill['validators']:
                var_format(fulfill['list'])
            else:
                print(fulfill['error_message'])
        else:
            print('The file is empty')
    except Exception as e:
        print('can not read the file, pleace check it '+str(e))


def validators(list_lines):
    validator = True
    list_validator = []
    error_message = ''
    if len(list_lines) >= 2:
        for index, linea in enumerate(list_lines):
            line = linea.split()
            if len(line) == 2:
                if int(line[0]) < 0 or int(line[1]) < 0:
                    error_message = 'the numbers should not be negative'
                    validator = False
                    break
                else:
                    if index == 0:
                        matrix_t = int(line[0])
                        if int(line[1]) != len(list_lines) - 2:
                            error_message = 'the number of obstacles does not match'
                            validator = False
                            break
                    elif matrix_t < int(line[0]) or matrix_t < int(line[1]):
                        error_message = 'The position '+line[0]+', '+line[1]+' it is not found inside the matrix'
                        validator = False
                        break
            else:
                error_message = 'Must enter positions'
                validator = False
                break
            list_validator.append(line)
    else:
        validator = False
        error_message = 'You must enter more data'

    return {'validators': validator, 'error_message': error_message, 'list': list_validator}


def var_format(list_q):
    obs = {}
    queen_p = []
    for idxRow, row in enumerate(list_q):
        obs_tl = []
        if idxRow == 0:
            len_m = int(row[0])
        elif idxRow == 1:
            queen_p.append(int(row[0]))
            queen_p.append(int(row[1]))
        else:
            obs_tl.append(int(row[0]))
            obs_tl.append(int(row[1]))
            obs[idxRow-2] = obs_tl
    fill_matrix(len_m, queen_p, obs)


def fill_matrix(len_m, queen_p, obs):
    board = new_matrix(len_m)
    put_obstacles(board, obs)
    solve(len_m, queen_p, board)


def new_matrix(n):
    chessboard = [[0 for y in range(n)] for x in range(n)]
    return chessboard


def put_obstacles(board, obs):
    for i in obs:
        board[obs[i][0] - 1][obs[i][1] - 1] = 2


def print_board(board):
    for i in board:
        pass
        print(i)


def solve(len_m, queen_p, board):
    x = queen_p[0]-1
    y = queen_p[1]-1
    board[x][y] = 1
    find_way(board, len_m, x, y)
    print_board(board)


def find_way(board, len_m, x, y):
    rx = lx = srx = slx = irx = ilx = x
    ry = ly = sry = sly = iry = ily = y

    count = 0
    if len_m > rx:
        while count_way(board, len_m, rx - 1, y):
            rx = rx-1
            count = count+1
        while count_way(board, len_m, lx + 1, y):
            lx = lx+1
            count = count+1
        while count_way(board, len_m, x, ry - 1):
            ry = ry-1
            count = count+1
        while count_way(board, len_m, x, ly + 1):
            ly = ly+1
            count = count+1
        while count_way(board, len_m, srx + 1, sry + 1):
            srx = srx+1
            sry = sry + 1
            count = count+1
        while count_way(board, len_m, slx - 1, sly - 1):
            slx = slx - 1
            sly = sly - 1
            count = count+1
        while count_way(board, len_m, irx + 1, iry - 1):
            irx = irx + 1
            iry = iry - 1
            count = count+1
        while count_way(board, len_m, ilx - 1, ily + 1):
            ilx = ilx - 1
            ily = ily + 1
            count = count+1

    print(count)


def count_way(board, len_m, x, y):
    if x < 0 or y < 0 or x > len_m-1 or y > len_m-1:
        return False
    if board[x][y] == 0:
        return True
    else:
        return False


read_tex()