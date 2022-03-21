from tkinter import  *
from tkinter import messagebox
def btn_click():
    k = ent.get()
    if k == 'ПАРОЛЬ':
        root.destroy()
        messagebox.showinfo(title = 'Успех', message = 'macbook разблокирован')

root = Tk()
root.title('macbook заблокирован')
root.geometry('400x200')
root['bg'] = 'red'
Label(root, text = 'Введите пароль', font = 'Arial 25', bg = 'red', fg = 'white').pack()
ent = Entry(root, text = '', font = 'Arial 25', width = 15)
ent.pack()
Button(root, text = 'Разблокировать', font = 'Arial 25', bg = 'purple', fg = 'white', command = btn_click).pack()
root.mainloop()