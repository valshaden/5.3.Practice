# Программа с интерфейсом
from tkinter import *
from tkinter import messagebox as mb

def book_seat():
    s = seat_entry.get().upper()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            update_canvas()
            mb.showinfo("Успех", f"Место '{s}' успешно забронировано.")
        else:
            mb.showerror("Ошибка", f"Место '{s}' уже забронировано.")
    except KeyError:
        mb.showerror("Ошибка", f"Место '{s}' не существует.")

def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20  # Уменьшаем шаг и начальное смещение
        y = 20  # Фиксированное положение по оси Y для одного ряда
        color = "green" if status == 'свободно' else "red"
        canvas.create_rectangle(x, y, x + 30, y + 30, fill=color)  # Уменьшаем размер квадратов
        canvas.create_text(x + 15, y + 15, text=seat)  # Центрируем текст в квадрате


window = Tk()
window.title("Бронирование мест")
window.geometry("400x200")

canvas = Canvas(width=400, height=80)
canvas.pack(pady=10)

# Инициализация мест
seats = {f"Б{i}": 'свободно' for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)

Button(text="Забронировать место", command=book_seat).pack(pady=10)

window.mainloop()
