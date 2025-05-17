def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Проверка строк
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True

    # Проверка столбцов
    for j in range(3):
        if all([board[i][j] == player for i in range(3)]):
            return True

    # Проверка диагоналей
    if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def play_game():
    board = [[' '] * 3 for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        try:
            move = input(f"{current_player}, введите координаты (строка столбец): ")
            x, y = map(int, move.split())

            if not (0 <= x < 3 and 0 <= y < 3):
                raise ValueError()

            if board[x][y] != ' ':
                print("Это поле занято!")
                continue

            board[x][y] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Победил {current_player}")
                break

            if is_full(board):
                print_board(board)
                print("Ничья")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Ошибка ввода! Попробуйте снова.")


if __name__ == "__main__":
    play_game()