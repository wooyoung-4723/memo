from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title("Memo")
window.geometry("500x500")
window.resizable(width=True, height=True)

def new_file():
    text_area.delete("1.0", END)

def save_file():
    f =asksaveasfile(mode = "w", defaultextension = ".txt", filetypes = [("Text File","*.txt")])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()


def maker():
    help_view = Toplevel(window)
    help_view.title("만든사람")
    help_view.resizable(width=True, height=True)
    help_view.geometry("500x500")

    lb = Label(help_view, text = "윤우영이 만든 메모장입니다")
    lb.pack()


menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label = "새파일", command = new_file)
menu_1.add_command(label='저장', command = save_file)
menu_1.add_separator()
menu_1.add_command(label ="종료", command = window.destroy)
menu.add_cascade(label = "파일", menu = menu_1)


menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command = maker)
menu.add_cascade(label= "만든이", menu = menu_2)

text_area = Text(window)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky="nsew")

window.config(menu = menu)
window.mainloop()