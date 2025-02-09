def create_board(rows=6, cols=7):
    """Створює порожнє ігрове поле."""
    return [[" " for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    """Виводить ігрове поле."""
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * (len(board[0]) * 4 - 1))


def drop_piece(board, col, piece):
    """Додає фішку до вибраної колонки."""
    for row in reversed(board):
        if row[col] == " ":
            row[col] = piece
            return True
    return False


def is_valid_column(board, col):
    """Перевіряє, чи є обрана колонка допустимою для ходу."""
    return 0 <= col < len(board[0]) and board[0][col] == " "


def check_winner(board, piece):
    """Перевіряє, чи є перемога для гравця з фішкою `piece`."""
    rows, cols = len(board), len(board[0])

    # Перевірка горизонтальних рядів
    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True

    # Перевірка вертикальних стовпців
    for col in range(cols):
        for row in range(rows - 3):
            if all(board[row + i][col] == piece for i in range(4)):
                return True

    # Перевірка діагоналей (зліва направо)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True

    # Перевірка діагоналей (справа наліво)
    for row in range(rows - 3):
        for col in range(3, cols):
            if all(board[row + i][col - i] == piece for i in range(4)):
                return True

    return False


def is_draw(board):
    """Перевіряє, чи всі клітинки заповнені (нічия)."""
    return all(cell != " " for row in board for cell in row)


def play_game():
    """Основна функція гри."""
    rows, cols = 6, 7
    board = create_board(rows, cols)
    print("Гра «Чотири в ряд»!")
    print_board(board)

    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]
        print(f"\nХід гравця {current_player}.")

        try:
            col = int(input(f"Оберіть колонку (0-{cols - 1}): "))
            if not is_valid_column(board, col):
                print("Неприпустимий хід. Спробуйте ще раз.")
                continue

            drop_piece(board, col, current_player)
            print_board(board)

            if check_winner(board, current_player):
                print(f"Гравець {current_player} виграв! Вітаємо!")
                break

            if is_draw(board):
                print("Нічия! Поле заповнене.")
                break

            turn += 1
        except ValueError:
            print("Будь ласка, введіть число.")
        except IndexError:
            print(f"Введіть номер від 0 до {cols - 1}.")


if __name__ == "__main__":
    play_game()
