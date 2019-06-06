import os


def read_text():
    try:
        if os.stat('archivo.txt').st_atime > 0:
            file = open('archivo.txt', 'r')
            list_lines = file.readlines()
            file.close()
            fulfill = validators(list_lines)
            if fulfill['validators']:
                var_format(fulfill['list'])
            else:
                print(fulfill['message_error'])
        else:
            print('El file esta vacio')
    except Exception as e:
        print('No se puede leer el file, por favor verifiquelo ' + str(e))


def validators(list_lines):
    validator = True
    list_validator = []
    error_message = ''
    if len(list_lines) >= 2:
        for index, linea in enumerate(list_lines):
            line = linea.split()
            if len(line) == 2:
                if int(line[0]) < 0 or int(line[1]) < 0:
                    error_message = 'Los numeros no deben ser negativos'
                    validator = False
                    break
                else:
                    if index == 0:
                        matrix_t = int(line[0])
                        if int(line[1]) != len(list_lines) - 2:
                            error_message = 'La cantidad de obstaculos no concuerda'
                            validator = False
                            break
                    elif matrix_t < int(line[0]) or matrix_t < int(line[1]):
                        error_message = 'La posicion ' + line[0] + ', ' + line[
                            1] + ' no se encuentra dentro de la matriz'
                        validator = False
                        break
            else:
                error_message = 'Debe ingresar posiciones'
                validator = False
                break
            list_validator.append(line)
    else:
        validator = False
        error_message = 'Debe ingresar mas datos'

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
            obs[idxRow - 2] = obs_tl
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
    x = queen_p[0] - 1
    y = queen_p[1] - 1
    board[x][y] = 1
    find_way(board, len_m, x, y)
    print_board(board)


def find_way(board, len_m, x, y):
    count = 0
    movements = {"mov1": [-1, 0], "mov2": [0, -1], "mov3": [1, 0], "mov4": [0, 1], "mov5": [1, 1],
                 "mov6": [-1, -1], "mov7": [1, -1], "mov8": [-1, 1]}
    for values in movements.values():
        count = count_way(board, len_m, x, y, values[0], values[1], count)
    print(count)


def count_way(board, len_m, x, y, var_a, var_b, count):
    x = x + var_a
    y = y + var_b
    if x < 0 or y < 0 or x > len_m - 1 or y > len_m - 1:
        pass
    else:
        if board[x][y] == 0:
            count = count + 1
            count = count_way(board, len_m, x, y, var_a, var_b, count)

    return count


read_text()
