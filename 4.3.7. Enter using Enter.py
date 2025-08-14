# 4.3.2. Проект с бронированием
# 4.3.5. Программа с интерфейсом
# 4.3.7. Бронируем нажатием Enter на клавиатуре.

### def book_seat(event=None):
### ...
### seat_entry = Entry()
### seat_entry.pack(pady=10)
### seat_entry.focus()  # Устанавливаем фокус на поле ввода
### # Привязываем событие нажатия Enter к функции book_seat
### seat_entry.bind("<Return>", book_seat)

#Код проекта
#Проект “Бронирование мест”.
from tkinter import *
from tkinter import messagebox as mb

def book_seat(event=None):
    s = seat_entry.get()
    try:
        if seats[s] == "свободно":
            seats[s] = "забронировано"
            update_canvas()
            mb.showinfo("Успех", f"Место {s} успешно забронировано.")
        else:
            mb.showinfo("Ошибка", f"Место {s} уже забронировано или не существует.")
    except KeyError:
        mb.showinfo("Ошибка", f"Место {s} не существует.")

def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)

window = Tk()
window.title("Бронирование мест")
window.geometry("400x200")

canvas = Canvas(width=400, height=60)
canvas.pack(pady=10)

seats = {f"Б{i}": "свободно" for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind("<Return>", book_seat)

Button(text="Забронировать место", command=book_seat).pack(pady=10)

window.mainloop()
