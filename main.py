from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton, Radiobutton, Progressbar, Style
from tkinter import scrolledtext, messagebox
import progressbar_style



def clicked():
    res = "Привет {}".format(txt.get()) # Получаем из txt значение, которое ввел пользователь и записываем его в переменную res (в фигурные скобки)
    # standart_text = lbl.cget("text")
    standart_text = "Привет!"
    if res != "Привет ":
        lbl.configure(text=res) # Изменяет в виджите lbl текст на значение, которое хранится в переменной res
    else:
        lbl.configure(text=standart_text)

def combo_get():
    chainge = combo.get()
    res = "Выбрано: {}".format(chainge)
    lbl.configure(text=res)

def checkbox_chainge():
    if chk_state.get():
        btn.configure(text="Нажимать")
    else:
        btn.configure(text="Не нажимать")
    # print(chk_state.get())

def radio_button(radio_text):
    rad_lbl.configure(text=f"Выбрано: {radio_text}") # Передает в виджет текст - Выбрано {значение выбранной радиокнопки}
    rad_values_lbl.configure(text=selected.get())


window = Tk()  # Создание окна window
window.title("Добро пожаловать!") # Название окна
window.geometry("1000x1000")

lbl = Label(window, text="Привет!", font=("Arial Bold", 30)) # Создание текста (window - окно, где будет текст; font - шрифт и размер шрифта) (font - можно использовать к любому виджету, не только к Lavel)
lbl.grid(column=0, row=0, sticky="nsew", padx=0, pady=0) # Вывод текста (column и row - указывает на ячейку в окне; padx и pady - расположение в этой ячейке; sticky - спользуется для определения того, как виджет распределится в ячейке, если у него есть свободное место в этой ячейке. Значение sticky указывает направления (стороны света), к которым виджет прилипнет. "n" - верх (north), "s" - низ (south), "e" - восток (east), "w" - запад (west), nsew - занимает всю область ячейки.)
# lbl2 = Label(window, text="Пока!", font=("Arial Bold", 50))
# lbl2.grid(column=1, row=0, sticky="nsew", padx=230, pady=0)

btn = Button(window, text="Не нажимать!", font=("Arial Bold", 30), bg = "black", fg= "red", command= lambda: clicked()) # Создание кнопки (bg - цвет фона; fg - цвет текста; comand - функция, которая вызывается при нажатии на кнопку)
btn.grid(column=2, row=0, sticky="nsew", padx=0, pady=0)

txt = Entry(window, width=30) # Создание поля пользовательского ввода. (width - размер)
txt.grid(column=1, row=0, sticky="nsew", padx=0, pady=0)
txt.focus() # При открытии окна, курсор уже будет стоять в поле ввода txt
# txt = Entry(window, width=30, state="disabled") # Отключение виджета ввода


combo = Combobox(window) # Создание выпадающий список
combo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Текст") # Задаю значения, которые будут в выподающем списке
combo.current(0) # Выбираю значение, которое будет стоять по умолчанию (в скобах индекс)
combo.grid(column=0, row=1)
btn_combo_get = Button(window, text="Получить текущее значение из выпадающего списка", font=("Arial Bold", 10), bg ="gray", fg="red", command=combo_get)
btn_combo_get.grid(column=1, row= 1)


chk_state = BooleanVar() # Создаем буллевую переменную (из библиотеки tkinter)
chk_state.set(False) # Задаем ей значение
chk_state_int = IntVar() # Создаем интовую переменную (из библиотеки tkinter)
chk_state_int.set(1) # Задаем ей значение. Теперь, если помемстить эту в var (ниже), то она будет работать также, как и переменная chk_state (При условии, что значения в ней будут 1 или 0 (True или False). Если использовать другое значение, то var будет воспринимать это как false (как 0))
chk = Checkbutton(window, text="Выбрать", width=20, var=chk_state, command= lambda : checkbox_chainge()) # Создание чекбокса (var - значение по умолчанию.)
chk.grid(column=2, row=1)


selected = IntVar()  
rad1 = Radiobutton(window, text="Первый!", width=20, value=1, var= chk_state_int, variable=selected, command= lambda : radio_button(rad1["text"])) # Создание радио кнопки (var работает также, как и в Checkbutton. Value - это значения, которое ассоциировано с этой радиокнопкой. Когда пользователь выбирает одну из радиокнопок в группе, значение, указанное в value, будет присвоено переменной, связанной с этой группой радиокнопок. Value должно быть уникально для каждой из радиокнопок в группе) В command записана ссылка на функцию radio_button, которая принимает в качестве аргумента значение параметра text текущей радиокнопки.
rad1.grid(column=0, row=2) 
rad2 = Radiobutton(window, text="Второй!", width=20, value=2, var= chk_state_int, variable=selected, command= lambda : radio_button(rad2["text"]))
rad2.grid(column=0, row=3)
rad3 = Radiobutton(window, text="Третий!", width=20, value=3, var= chk_state_int, variable=selected, command= lambda : radio_button(rad3["text"]))
rad3.grid(column=0, row=4)
rad1.invoke()

rad_lbl = Label(window, text=f"Выбрано {rad1['text']}") # В параметр text записал значение по умолчанию
rad_lbl.grid(column=1, row=2, columnspan=3)
rad_values_lbl = Label(window, text=selected.get())
rad_values_lbl.grid(column=2, row=2)


txt_scroll = scrolledtext.ScrolledText(window, width=40, height=5) # Создание текстового поля с прокруткой (wigth - ширина; height - высота)
txt_scroll.grid(column=1, row=5)
txt_scroll.insert(INSERT, "Текстовое поле") # Задаем текст в текстовом поле по умолчанию
# txt_scroll.delete(1.0, END) # Задаем метод очистки текстового поля (можно потом будет использовать с кнопкой)


# messagebox.showinfo("Заголовок", "Текст") # Вызывает окно предупреждения (Пока оно открыто, основное окно блокируется. Почему-то у меня основное окно остается заблокированным даже после закрытия этого окна)
# messagebox.showwarning("Заголовок", "Текст")
# messagebox.showerror("Заголовок", "Текст")
# res = messagebox.askquestion('Заголовок', 'Текст')
# res = messagebox.askyesno('Заголовок', 'Текст')
# res = messagebox.askyesnocancel('Заголовок', 'Текст')
# res = messagebox.askokcancel('Заголовок', 'Текст')
# res = messagebox.askretrycancel('Заголовок', 'Текст')


spin = Spinbox(window, from_=0, to=100, width=20) # Создание спинбокса (from_ и to - диапазон значений, width - размер)
spin.grid(column=0, row=5, sticky="n", padx=0, pady=0)

spin2 = Spinbox(window, values=(1, 3, 5, 10, 14, 16, 25, 28, 30), width=20) # Вместо диапазона значений, указываем конкретные значения
spin2.grid(column=0, row=5, sticky="w", padx=10, pady=0)

var_spin = IntVar()
var_spin.set(5)
spin3 = Spinbox(window, from_=0, to=100, width=20, textvariable=var_spin)
spin3.grid(column=0, row=5, sticky="s", padx=10, pady=0) # Задаем стандартное значение


main_style = Style()
main_style.theme_use('default')  
main_style.configure("Main.Horizontal.TProgressbar", background="#00FF00")
bar = Progressbar(window, length=100, style="Main.Horizontal.TProgressbar", mode="determinate") # Создание прогессбара (length - длина)
bar["value"] = 70 # Значение в прогрессбаре (насколько он заполнен)
bar.grid(column=0, row=6, sticky="w", padx=10, pady=10)


# Создание окна с цветным прогрессбаром
progressbar_button = Button(window, text="Вывести прогрессбар", font=("Arial Bold",20), bg="red", fg="blue", command= lambda : progressbar_style.window_progressbar_function())
progressbar_button.grid(column=0, row=7, sticky="nsew", padx=0, pady=0)



window.mainloop() # Бесконечный цикл,ожидающий действий от пользователя. Пока он работает - открыто окно
