from tkinter import *
from tkinter.ttk import Combobox
import options

def clicked():
    res = "Привет {}".format(txt.get()) # Получаем из txt значение, которое ввел пользователь и записываем его в переменную res (в фигурные скобки)
    lbl.configure(text=res) # Изменяет в виджите lbl текст на значение, которое хранится в переменной res

window = Tk()  # Создание окна window
window.title("Добро пожаловать!") # Название окна
window.geometry("700x700")

lbl = Label(window, text="Привет!", font=("Arial Bold", 30)) # Создание текста (window - окно, где будет текст; font - шрифт и размер шрифта) (font - можно использовать к любому виджету, не только к Lavel)
lbl.grid(column=0, row=0, sticky="nsew", padx=0, pady=0) # Вывод текста (column и row - указывает на ячейку в окне; padx и pady - расположение в этой ячейке; sticky - спользуется для определения того, как виджет распределится в ячейке, если у него есть свободное место в этой ячейке. Значение sticky указывает направления (стороны света), к которым виджет прилипнет. "n" - верх (north), "s" - низ (south), "e" - восток (east), "w" - запад (west).)
# lbl2 = Label(window, text="Пока!", font=("Arial Bold", 50))
# lbl2.grid(column=1, row=0, sticky="nsew", padx=230, pady=0)

btn = Button(window, text="Не нажимать!", font=("Arial Bold", 30), bg = "black", fg= "red", command=clicked) # Создание кнопки (bg - цвет фона; fg - цвет текста; comand - функция, которая вызывается при нажатии на кнопку)
btn.grid(column=2, row=0, sticky="nsew", padx=0, pady=0)

txt = Entry(window, width=30) # Создание поля пользовательского ввода. (width - размер)
txt.grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
txt.focus() # При открытии окна, курсор уже будет стоять в поле ввода txt
# txt = Entry(window, width=30, state="disabled") # Отключение виджета ввода


combo = Combobox(window) # Создаем выпадающий список
combo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Текст") 
combo.current(0)
combo.grid(column=0, row=1)

window.mainloop() # Бесконечный цикл,ожидающий действий от пользователя. Пока он работает - открыто окно
