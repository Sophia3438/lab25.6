from tkinter import Tk, Canvas
from random import shuffle

# Задання констант
BOARD_SIZE = 4  # Розмір ігрового поля (4x4)
SQUARE_SIZE = 80  # Розмір одного блоку у пікселях
EMPTY_SQUARE = BOARD_SIZE**2  # Значення порожнього блоку (16 для поля 4x4)
root = Tk()
root.title("Pythonicway Fifteen")  # Заголовок вікна
canvas = Canvas(
    root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE, bg="#808080"
)
canvas.pack()

# Список для представлення п'ятнашок
board = list(range(1, EMPTY_SQUARE + 1))


# Функція для переміщення блоків
def shuffle_board():
    # Перемішуємо блоки випадковим чином
    shuffle(board)
    # Перевіряємо, чи є розв'язок, і якщо ні — переміщаємо ще раз
    while not is_solvable():
        shuffle(board)


# Список для перевірки перемоги (правильний порядок)
correct_board = board[:]


# Функція для перевірки, чи є рішення
def get_inv_count():
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i + 1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


# Перевірка чи є рішення для головоломки
def is_solvable():
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


# Функція для малювання п’ятнашок
def draw_board():
    canvas.delete("all")
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])
            if index != str(EMPTY_SQUARE):
                canvas.create_rectangle(
                    j * SQUARE_SIZE,
                    i * SQUARE_SIZE,
                    j * SQUARE_SIZE + SQUARE_SIZE,
                    i * SQUARE_SIZE + SQUARE_SIZE,
                    fill="#43ABC9",
                    outline="#FFFFFF",
                )
                canvas.create_text(
                    j * SQUARE_SIZE + SQUARE_SIZE / 2,
                    i * SQUARE_SIZE + SQUARE_SIZE / 2,
                    text=index,
                    font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                    fill="#FFFFFF",
                )


# Функція для обробки натискання на клітинку
def click(event):
    x, y = event.x, event.y
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    board_index = x + (y * BOARD_SIZE)
    empty_index = get_empty_neighbor(board_index)
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    draw_board()
    if board == correct_board:
        show_victory_plate()


# Обробник подій для кліків
canvas.bind("<Button-1>", click)


# Функція для знаходження сусіднього порожнього блоку
def get_empty_neighbor(index):
    empty_index = board.index(EMPTY_SQUARE)
    abs_value = abs(empty_index - index)
    if abs_value == BOARD_SIZE:
        return empty_index
    elif abs_value == 1:
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index


# Функція для виведення повідомлення про перемогу
def show_victory_plate():
    canvas.create_rectangle(
        SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
        BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
        SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
        fill="#000000",
        outline="#FFFFFF",
    )
    canvas.create_text(
        SQUARE_SIZE * BOARD_SIZE / 2,
        SQUARE_SIZE * BOARD_SIZE / 1.9,
        text="Перемога!",
        font="Helvetica {} bold".format(int(10 * BOARD_SIZE)),
        fill="#DC143C",
    )


# Переміщуємо блоки перед малюванням
shuffle_board()

# Малюємо дошку після перемішування
draw_board()

root.mainloop()
