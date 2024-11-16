'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 2022/08/20
Ending 2024//

'''
# Installing the necessary libraries
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from typing import List
import pyAesCrypt
from tkinter import Button, Label, Menu, Entry, END
import re


class CryptographerApp:
    """AI is creating summary for
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Криптограф")
        self.root.geometry("300x250")
        self.root.resizable(width=False, height=False)
        self.filemass: List[str] = []
        self.setup_ui()

    def setup_ui(self):
        """AI is creating summary for setup_ui
        """
        # Create the UI components
        self.label = Label(text='Введите пароль:')
        # Moved label above input field
        self.label.place(x=2, y=100)

        self.pass_field = Entry(show='*', width='37')
        self.pass_field.place(x=2, y=120)
        self.create_menu()
        # Add file path entry
        self.file_path_label = Label(text='Путь к файлу:')
        self.file_path_label.place(x=2, y=10)
        self.file_path_entry = Entry(width='37')
        self.file_path_entry.place(x=2, y=30)
        self.open_file_btn = Button(text='Открыть файл',
                                    command=self.open_file)
        self.open_file_btn.place(x=2, y=55)

    def create_menu(self):
        """AI is creating summary for create_menu
        """
        # Creating a menu
        self.main_menu = Menu(self.root)
        self.file_menu = Menu(self.main_menu, tearoff=0)
        self.about_menu = Menu(self.main_menu, tearoff=0)
        self.about_menu.add_command(label="О программе",
                                    command=self.show_info)
        self.main_menu.add_cascade(label="Справка", menu=self.about_menu)
        self.root.config(menu=self.main_menu)

    def open_file(self):
        """AI is creating summary for open_file
        """
        file_path = fd.askopenfilename(
            initialdir="/",
            title="Выберите файл",
            filetypes=(("all files", "*.*"), ("text files", "*.txt"))
        )
        if file_path:
            self.file_path_entry.delete(0, END)
            self.file_path_entry.insert(0, file_path)

    def show_info(self):
        """AI is creating summary for show_info
        """
        mb.showinfo("О программе", "Феткулин Григорий - Криптограф, 2022")


class Encryptor(CryptographerApp):
    """AI is creating summary for Encryptor

    Args:
        CryptographerApp ([type]): [description]
    """
    def __init__(self, root):
        super().__init__(root)
        self.encrypt_btn = Button(text='Зашифровать', command=self.crypt)
        self.encrypt_btn.place(x=7, y=210)

    # The function of the "Encrypt" button
    def crypt(self):
        """AI is creating summary for crypt
        """
        password = self.pass_field.get()
        file_path = self.file_path_entry.get()
        if not file_path:
            mb.showerror("Ошибка", "Выберите файл для шифрования!")
            return
        if not password:
            mb.showerror("Ошибка", "Введите пароль!")
            return
        if not re.match(r"^[a-zA-Z]{12,}$", password):
            mb.showerror("Ошибка", "Пароль должен быть не короче 12 знаков и состоять из латинских букв!")
            return

        try:
            pyAesCrypt.encryptFile(file_path, file_path + ".aes", password)
            mb.showinfo("Успех", "Файл успешно зашифрован!")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка при шифровании: {e}")


class Decryptor(CryptographerApp):
    """AI is creating summary for Decryptor

    Args:
        CryptographerApp ([type]): [description]
    """
    def __init__(self, root):
        super().__init__(root)
        self.decrypt_btn = Button(text='Расшифровать', command=self.decrypt)
        self.decrypt_btn.place(x=210, y=210)

# The function of the "Decrypt" button
    def decrypt(self):
        """AI is creating summary for decrypt
        """
        password = self.pass_field.get()
        file_path = self.file_path_entry.get()
        if not file_path:
            mb.showerror("Ошибка", "Выберите файл для расшифрования!")
            return
        if not password:
            mb.showerror("Ошибка", "Введите пароль!")
            return

        try:
            pyAesCrypt.decryptFile(file_path, file_path[:-4], password)
            mb.showinfo("Успех", "Файл успешно расшифрован!")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка при расшифровании: {e}")


if __name__ == "__main__":
    root = Tk()
    app = Decryptor(root)
    root.mainloop()
