def print_towers(towers, n_disks):
    """
    Відображає поточний стан стрижнів.
    """
    max_width = n_disks * 2 + 1
    levels = []

    for level in range(n_disks - 1, -1, -1):
        row = []
        for tower in towers:
            if level < len(tower):
                disk_size = tower[level] * 2 + 1
                disk = "#" * disk_size
                row.append(disk.center(max_width, " "))
            else:
                row.append("|".center(max_width, " "))
        levels.append("   ".join(row))

    base = "=" * max_width
    levels.append(f"{base}   {base}   {base}")
    levels.append(
        "   A   ".center(max_width)
        + "   B   ".center(max_width)
        + "   C   ".center(max_width)
    )

    print("\n".join(levels))


def is_valid_move(towers, from_tower, to_tower):
    """
    Перевіряє, чи є переміщення з одного стрижня на інший дійсним.
    """
    if not towers[from_tower]:
        return False  # Якщо джерело порожнє
    if not towers[to_tower] or towers[from_tower][-1] < towers[to_tower][-1]:
        return True  # Можна перемістити
    return False


def move_disk(towers, from_tower, to_tower):
    """
    Виконує переміщення диска між стрижнями.
    """
    disk = towers[from_tower].pop()
    towers[to_tower].append(disk)


def hanoi_interactive(n_disks):
    """
    Інтерактивна гра в Ханойську вежу.
    """
    towers = [list(range(n_disks, 0, -1)), [], []]
    moves = 0

    print("Початковий стан:")
    print_towers(towers, n_disks)

    while len(towers[2]) != n_disks:
        print(f"\nХід {moves + 1}:")
        try:
            from_tower = (
                input("З якого стрижня перемістити? (A, B, C): ").strip().upper()
            )
            to_tower = (
                input("На який стрижень перемістити? (A, B, C): ").strip().upper()
            )

            # Перетворюємо A, B, C на індекси 0, 1, 2
            from_index = "ABC".index(from_tower)
            to_index = "ABC".index(to_tower)

            if is_valid_move(towers, from_index, to_index):
                move_disk(towers, from_index, to_index)
                moves += 1
                print_towers(towers, n_disks)
            else:
                print(
                    "Неможливий хід. Ви намагаєтеся перемістити більший диск на менший або зі стрижня, де немає дисків."
                )
        except (ValueError, IndexError):
            print("Помилка введення. Введіть A, B або C для вибору стрижнів.")

    print(f"\nВи розв'язали головоломку за {moves} ходів! Вітаємо!")


if __name__ == "__main__":
    print("Гра «Ханойська вежа»")
    try:
        n_disks = int(input("Введіть кількість дисків: "))
        if n_disks > 0:
            hanoi_interactive(n_disks)
        else:
            print("Кількість дисків повинна бути додатною.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
