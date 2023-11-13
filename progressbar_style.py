from tkinter import Toplevel
from tkinter.ttk import Progressbar, Style


def window_progressbar_function():
    window_progressbar = Toplevel()
    window_progressbar.title("Стиль прогрессбара")
    window_progressbar.geometry("700x700")

    custom_style = Style()
    custom_style.theme_use('default')  
    custom_style.configure("Custom.Horizontal.TProgressbar", background="#FF2C42")

    new_bar = Progressbar(window_progressbar, length=200, style="Custom.Horizontal.TProgressbar", mode='determinate')
    new_bar["value"] = 70
    new_bar.grid(column=0, row=0)

    window_progressbar.mainloop()