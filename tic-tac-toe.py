import os
import random
def clear(): return os.system('clear')


l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

p1 = []
p2 = []

turn = random.randint(0, 1)  # Controls whether X or O move first
win = 0


def get_input(p1, p2, l):  # Get input from user and add it to move list of corresponding player
    global turn
    if turn % 2 == 0:

        move_ahead = 0
        while move_ahead == 0:
            p1_position = int(input("Position for X: "))
            if l[p1_position] != 'X' and l[p1_position] != 'O':
                l[p1_position] = 'X'
                p1.append(p1_position)
                move_ahead = 1
                turn += 1
            else:
                print('Location occupied')
                continue

    else:
        move_ahead = 0
        while move_ahead == 0:
            p2_position = int(input("Position for O: "))
            if l[p2_position] != 'X' and l[p2_position] != 'O':
                l[p2_position] = 'O'
                p2.append(p2_position)
                move_ahead = 1
                turn += 1
            else:
                print('Location occupied')
                continue


def print_board(l):
    clear()

    print("      |     |     ")
    print(f"   {l[7]}  |  {l[8]}  |  {l[9]}  ")
    print("      |     |     ")
    print("------+-----+-------- ")
    print("      |     |     ")
    print(f"   {l[4]}  |  {l[5]}  |  {l[6]}  ")
    print("      |     |     ")
    print("------+-----+-------- ")
    print("      |     |     ")
    print(f"   {l[1]}  |  {l[2]}  |  {l[3]}  ")
    print("      |     |     ")


def check_draw():
    for a in range(1, 10):
        if l[a] != 'X' and l[a] != 'O':
            return 0
        else:
            continue
    print("Draw!")
    return 1


def check_win(l):
    if (l[1] == 'X' and l[2] == 'X' and l[3] == 'X') or (l[4] == 'X' and l[5] == 'X' and l[6] == 'X') or (l[7] == 'X' and l[8] == 'X' and l[9] == 'X') or (l[1] == 'X' and l[4] == 'X' and l[7] == 'X') or (l[2] == 'X' and l[5] == 'X' and l[8] == 'X') or (l[3] == 'X' and l[6] == 'X' and l[9] == 'X') or (l[1] == 'X' and l[5] == 'X' and l[9] == 'X') or (l[3] == 'X' and l[5] == 'X' and l[7] == 'X'):
        print("X won!")
        return 1

    elif (l[1] == 'O' and l[2] == 'O' and l[3] == 'O') or (l[4] == 'O' and l[5] == 'O' and l[6] == 'O') or (l[7] == 'O' and l[8] == 'O' and l[9] == 'O') or (l[1] == 'O' and l[4] == 'O' and l[7] == 'O') or (l[2] == 'O' and l[5] == 'O' and l[8] == 'O') or (l[3] == 'O' and l[6] == 'O' and l[9] == 'O') or (l[1] == 'O' and l[5] == 'O' and l[9] == 'O') or (l[3] == 'O' and l[5] == 'O' and l[7] == 'O'):
        print("O won!")
        return 1


def rungame(turn, p1, p2, l):
    draw = check_draw()
    win = 0
    while win != 1 and draw == 0:
        get_input(p1, p2, l)
        print_board(l)
        win = check_win(l)
        draw = check_draw()


print_board(l)
rungame(0, p1, p2, l)
