board = [' ' for _ in range(9)]

for row in range(3):
    print(f'| {board[row*3]} | {board[row*3 + 1]} | {board[row*3 + 2]} |') 
    if row < 2:
        print('-------------')

current_player = 'X'
game_over = False
turn = 0



while not game_over and turn < 9:
    move = input(f'Ход игрока {current_player}. Введите число от 1 до 9: ')

    #корректность ввода
    if not move.isdigit() or int(move) < 1 or int(move) > 9:
        print('Введите число от 1 до 9')
        continue

    move = int(move) - 1

    #проверка ячейки на пустоту
    if board[move] != ' ':
        print('ячейка занята, попробуйте другую')
        continue

    #обновление поля
    board[move] = current_player

    for row in range(3):
        print(f'| {board[row*3]} | {board[row*3 + 1]} | {board[row*3 + 2]} |') 
        if row < 2:
            print('-------------')


    #комбинации для победи
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #горизонтальная победа
        [0, 3, 6], [1, 4, 7], [2, 5, 8], #вертикальная победа
        [0, 4, 8], [2, 4, 6]  #диагональ
    ]

    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current_player:
            print(f'Игрок {current_player} победил!!!')
            game_over = True
            break

    if not game_over:
        current_player = 'O' if current_player == 'X' else 'X'
        turn += 1

if not game_over:
    print('Ничья')

