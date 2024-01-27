'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/08/20
Ending 2024//

'''
import os
from tkinter import *
from tkinter import Button, Label, Menu
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from typing import List
import pyAesCrypt

# The function of the "Encrypt" button


def crypt(filemass: List[str]):
    """AI is creating summary for crypt

    Args:
        filemass (List[str]): The list of selected files to encrypt
    """
    password = passField.get()
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(filemass[0]), str(
        filemass[0]) + '.aes', password, buffer_size)
    filemass.clear()


# The function of the "Decrypt" button
def decrypt(filemass: List[str]):
    """AI is creating summary for decrypt

    Args:
        filemass (List[str]): The list of selected files to decrypt
    """
    password = passField.get()
    buffer_size = 512*1024
    pyAesCrypt.decryptFile(str(filemass[0]), str(
        os.path.splitext(filemass[0])[0]), password, buffer_size)
    filemass.clear()


def file_dialog():
    """AI is creating summary for file_dialog
    """
    file_name = fd.askopenfilename()
    filemass.append(file_name)


filemass: List[str] = []
# Program interface
root = Tk()
root.title("Криптограф")
root.geometry("300x250")


def show_info():
    """AI is creating summary for show_info
    """
    mb.showinfo("О программе", "Феткулин Григорий - Криптограф, 2022")


label1 = Label(text='Введите пароль:')
label1.place(x=2, y=50)

passField = Entry(show='*', width='37')
passField.place(x=2, y=80)


btn = Button(text='Расшифровать',  command=lambda: decrypt(filemass))
btn.place(x=210, y=210)

btn = Button(text='Зашифровать', command=lambda: crypt(filemass))
btn.place(x=7, y=210)

main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label="Открыть", command=file_dialog)
about_menu = Menu()
about_menu.add_command(label="О программе", command=show_info)
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=about_menu)
root.config(menu=main_menu)
root.mainloop()
