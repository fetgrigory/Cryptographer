# Installing the necessary libraries
import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from typing import List
import pyAesCrypt
from tkinter import Button, Label, Menu, Entry


class CryptographerApp:
    """AI is creating summary for
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Криптограф")
        self.root.geometry("300x250")
        self.filemass: List[str] = []
        self.setup_ui()

    def setup_ui(self):
        """AI is creating summary for setup_ui
        """
        # Create the UI components
        self.label = Label(text='Введите пароль:')
        self.label.place(x=2, y=50)

        self.pass_field = Entry(show='*', width='37')
        self.pass_field.place(x=2, y=80)
        self.encrypt_btn = Button(text='Зашифровать', command=self.crypt)
        self.encrypt_btn.place(x=7, y=210)

        self.decrypt_btn = Button(text='Расшифровать', command=self.decrypt)
        self.decrypt_btn.place(x=210, y=210)
        self.create_menu()

    def create_menu(self):
        """AI is creating summary for create_menu
        """
        # Creating a menu
        self.main_menu = Menu(self.root)
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label="Открыть", command=self.file_dialog)
        self.about_menu = Menu(self.main_menu, tearoff=0)
        self.about_menu.add_command(label="О программе", command=self.show_info)
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="Справка", menu=self.about_menu)
        self.root.config(menu=self.main_menu)

    # The function of the "Encrypt" button
    def crypt(self):
        """AI is creating summary for crypt
        """
        password = self.pass_field.get()
        buffer_size = 512*1024
        if self.filemass:
            pyAesCrypt.encryptFile(self.filemass[0], self.filemass[0] + '.aes', password, buffer_size)
            self.filemass.clear()

# The function of the "Decrypt" button
    def decrypt(self):
        """AI is creating summary for decrypt
        """
        password = self.pass_field.get()
        buffer_size = 512*1024
        if self.filemass:
            pyAesCrypt.decryptFile(self.filemass[0], os.path.splitext(self.filemass[0])[0], password, buffer_size)
            self.filemass.clear()

    def file_dialog(self):
        """AI is creating summary for file_dialog
        """
        file_name = fd.askopenfilename()
        if file_name:
            self.filemass.append(file_name)

    def show_info(self):
        """AI is creating summary for show_info
        """
        mb.showinfo("О программе", "Феткулин Григорий - Криптограф, 2022")


if __name__ == "__main__":
    root = Tk()
    app = CryptographerApp(root)
    root.mainloop()
