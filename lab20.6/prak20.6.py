import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Відкриває файл для редагування."""
    # Відкриваємо діалогове вікно для вибору файлу
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # Якщо файл не вибрано, виходимо з функції
    if not filepath:
        return
    # Очищаємо текстове поле перед завантаженням нового вмісту
    txt_edit.delete("1.0", tk.END)
    # Відкриваємо файл для читання та зчитуємо його вміст
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        # Вставляємо вміст файлу в текстове поле
        txt_edit.insert(tk.END, text)
    # Оновлюємо заголовок вікна, щоб показати ім'я відкритого файлу
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Зберігає поточний файл як новий файл."""
    # Відкриваємо діалогове вікно для вибору місця збереження файлу
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    # Якщо файл не вибрано, виходимо з функції
    if not filepath:
        return
    # Зберігаємо вміст текстового поля у вибраний файл
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    # Оновлюємо заголовок вікна, щоб показати ім'я збереженого файлу
    window.title(f"Simple Text Editor - {filepath}")


# Налаштовуємо основне вікно
window = tk.Tk()
window.title("Simple Text Editor")

# Налаштовуємо розміри вікна
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Створюємо текстове поле для редагування
txt_edit = tk.Text(window)

# Створюємо фрейм для кнопок
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# Створюємо кнопки для відкриття та збереження файлів
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

# Розташовуємо кнопки в фреймі
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Розташовуємо фрейм з кнопками та текстове поле у вікні
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Запускаємо головний цикл додатка
window.mainloop()
