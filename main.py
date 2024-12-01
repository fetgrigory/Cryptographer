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

# Dictionaries for multilingualism
strings = {
    "ru": {
        "title": "Криптограф",
        "enter_password": "Введите пароль:",
        "file_path": "Путь к файлу:",
        "open_file": "Открыть файл",
        "encrypt": "Зашифровать",
        "decrypt": "Расшифровать",
        "about": "О программе",
        "success_encrypt": "Файл успешно зашифрован!",
        "success_decrypt": "Файл успешно расшифрован!",
        "error_file_select": "Выберите файл для шифрования/расшифрования!",
        "error_password": "Введите пароль!",
        "error_password_length": "Пароль должен быть не короче 12 знаков и состоять из латинских букв!",
        "error_encryption": "Ошибка при шифровании:",
        "error_decryption": "Ошибка при расшифровании:",
        "about_text": "Феткулин Григорий - Криптограф, 2022",
        "menu_help": "Справка"

    },
    "en": {
        "title": "Cryptographer",
        "enter_password": "Enter password:",
        "file_path": "File path:",
        "open_file": "Open file",
        "encrypt": "Encrypt",
        "decrypt": "Decrypt",
        "about": "About",
        "success_encrypt": "File successfully encrypted!",
        "success_decrypt": "File successfully decrypted!",
        "error_file_select": "Select a file for encryption/decryption!",
        "error_password": "Enter password!",
        "error_password_length": "Password must be at least 12 characters long and consist of Latin letters!",
        "error_encryption": "Encryption error:",
        "error_decryption": "Decryption error:",
        "about_text": "Grigory Fetkulin - Cryptographer, 2022",
        "menu_help": "Help"
    }
}


class CryptographerApp:
    """AI is creating summary for
    """
    def __init__(self, root, language="ru"):
        self.root = root
        self.language = language
        self.strings = strings[language]
        self.root.title(self.strings["title"])
        self.root.geometry("300x250")
        self.root.resizable(width=False, height=False)
        self.file_path = ""
        self.setup_ui()

    def setup_ui(self):
        """AI is creating summary for setup_ui
        """
        # Create the UI components
        self.label_password = Label(text=self.strings["enter_password"])
        self.label_password.place(x=2, y=100)

        self.pass_field = Entry(show='*', width='37')
        # Moved label above input field
        self.pass_field.place(x=2, y=120)
        self.create_menu()
        # Add file path entry
        self.label_file_path = Label(text=self.strings["file_path"])
        self.label_file_path.place(x=2, y=10)
        self.file_path_entry = Entry(width='37')
        self.file_path_entry.place(x=2, y=30)
        self.open_file_btn = Button(text=self.strings["open_file"], command=self.open_file)
        self.open_file_btn.place(x=2, y=55)

    def create_menu(self):
        """AI is creating summary for create_menu
        """
        # Creating a menu
        self.main_menu = Menu(self.root)
        self.language_menu = Menu(self.main_menu, tearoff=0)
        self.language_menu.add_command(label="Русский", command=lambda: self.change_language("ru"))
        self.language_menu.add_command(label="English", command=lambda: self.change_language("en"))
        self.main_menu.add_cascade(label="Language", menu=self.language_menu)

        self.about_menu = Menu(self.main_menu, tearoff=0)
        self.about_menu.add_command(label=self.strings["about"], command=self.show_info)
        self.main_menu.add_cascade(label=self.strings["menu_help"], menu=self.about_menu)
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
            self.file_path = file_path

    def show_info(self):
        """AI is creating summary for show_info
        """
        mb.showinfo(self.strings["about"], self.strings["about_text"])

    def change_language(self, lang):
        """AI is creating summary for change_language

        Args:
            lang ([type]): [description]
        """
        self.language = lang
        self.strings = strings[lang]
        self.label_password.config(text=self.strings["enter_password"])
        self.label_file_path.config(text=self.strings["file_path"])
        self.open_file_btn.config(text=self.strings["open_file"])
        self.about_menu.entryconfig(0, label=self.strings["about"])
        self.root.title(self.strings["title"])
        self.main_menu.entryconfig(1, label=self.strings["menu_help"])


class Encryptor(CryptographerApp):
    """AI is creating summary for Encryptor

    Args:
        CryptographerApp ([type]): [description]
    """
    def __init__(self, root, language="ru"):
        super().__init__(root, language)
        self.encrypt_btn = Button(text=self.strings["encrypt"], command=self.crypt)
        self.encrypt_btn.place(x=7, y=210)

    # The function of the "Encrypt" button
    def crypt(self):
        """AI is creating summary for crypt
        """
        password = self.pass_field.get()
        if not self.file_path:
            mb.showerror("Ошибка", self.strings["error_file_select"])
            return
        if not password:
            mb.showerror("Ошибка", self.strings["error_password"])
            return
        if not re.match(r"^[a-zA-Z]{12,}$", password):
            mb.showerror("Ошибка", self.strings["error_password_length"])
            return

        try:
            pyAesCrypt.encryptFile(self.file_path, self.file_path + ".aes", password)
            mb.showinfo("Успех", self.strings["success_encrypt"])
        except Exception as e:
            mb.showerror("Ошибка", f"{self.strings['error_encryption']} {e}")


class Decryptor(CryptographerApp):
    def __init__(self, root, language="ru"):
        super().__init__(root, language)
        self.decrypt_btn = Button(text=self.strings["decrypt"], command=self.decrypt)
        self.decrypt_btn.place(x=210, y=210)
        # The function of the "Decrypt" button

    def decrypt(self):
        """AI is creating summary for decrypt
        """
        password = self.pass_field.get()
        if not self.file_path:
            mb.showerror("Ошибка", self.strings["error_file_select"])
            return
        if not password:
            mb.showerror("Ошибка", self.strings["error_password"])
            return

        try:
            pyAesCrypt.decryptFile(self.file_path, self.file_path[:-4], password)
            mb.showinfo("Успех", self.strings["success_decrypt"])
        except Exception as e:
            mb.showerror("Ошибка", f"{self.strings['error_decryption']} {e}")


if __name__ == "__main__":
    root = Tk()
    app = Decryptor(root)
    root.mainloop()
