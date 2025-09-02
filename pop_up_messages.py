from tkinter import messagebox

class UserInterface:

    def __init__(self, text):
        self.text = text

    def create_message_info_pop_up(self):
        messagebox.showinfo(self.text)

