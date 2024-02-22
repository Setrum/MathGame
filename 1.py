from typing import Tuple
from PIL import Image, ImageTk
import customtkinter as ctk
import game
import time
import webbrowser
import random


ctk.set_appearance_mode("dark")

class MyFrame1(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_name = ctk.CTkLabel(self, text='CALC GAME', font=('Roboto', 18))
        self.label_name.grid(row=0, column=0, padx=60, pady=40)
        
        self.label_discription = ctk.CTkLabel(self, text='Count it.\nAll you need to do is solve problems.\nAnd remember, you have no right to make mistakes.', font=('Roboto', 18))
        self.label_discription.grid(row=1, column=0, padx=60, pady=40)

        self.start_button = ctk.CTkButton(self, text="Let's get started!", command=master.show_game)
        self.start_button.grid(row=2, column=0, padx=60, pady=(30, 5))

        self.exit_button = ctk.CTkButton(self, text="Exit", command=exit)
        self.exit_button.grid(row=3, column=0, padx=60, pady=(5, 30))

        
        
class MyFrame2(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.problem = ctk.CTkLabel(self, text="", font=("Roboto", 30))
        self.problem.grid(row=0, column=0, padx=60, pady=(50, 20))

        self.entry = ctk.CTkEntry(self, corner_radius=5, placeholder_text="Type the answer")
        self.entry.grid(row=2, column=0, padx=60, pady=(20, 10))

        self.answer_button = ctk.CTkButton(self, text="Answer", font=('Roboto', 13), command=master.get_answer)
        self.answer_button.grid(row=3, column=0, padx=60, pady=(0, 10))

        self.score_label = ctk.CTkLabel(self, text='Score: 0')
        self.score_label.grid(row=4, column=0, padx=60, pady=(0, 40))

        self.back_button = ctk.CTkButton(self, 
                                         text="Back to main menu", 
                                         fg_color=self._fg_color, 
                                         border_color=('black', 'white'), 
                                         font=('Roboto', 13), 
                                         border_width=1, 
                                         text_color=('black', 'white'),
                                         hover_color=('white', "#144870"),
                                         command=master.back_to_main_menu)
        self.back_button.grid(row=5, column=0, padx=60, pady=(5, 40))
        master.bind("<Return>", self.answer_button._command)

class App(ctk.CTk):

    theme_mode = 'dark'
    answer = ''
    score = 0

    def __init__(self):
        super().__init__()
        self.geometry('700x550+1000+500')
        self.title("Misha's App")
        self.iconbitmap("assets/icon.ico")
        
        self.start_frame = MyFrame1(self,
                                   width=int(self._current_width*0.8),
                                   height=int(self._current_height*0.8),
                                   fg_color=("#e3e3e3", "#303030"),
                                   corner_radius=10)
        self.frame = MyFrame2(self,
                                   width=int(self._current_width*0.8),
                                   height=int(self._current_height*0.8),
                                   fg_color=("#e3e3e3", "#303030"),
                                   corner_radius=10)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.start_frame.grid(row=0, column=0)

        self.label_author = ctk.CTkLabel(self, text='Made with \u2764 by MishaOvechkin', cursor="hand2")
        self.label_author.grid(row=1, column=0, pady=(0, 20))

        self.label_author.bind("<Enter>", self.underline_link_app)
        self.label_author.bind("<Leave>", self.unrerline_link_disapp)
        self.label_author.bind("<Button-1>", self.callback)

        self.theme_image = ctk.CTkImage(light_image=Image.open("assets/sun2.png"), dark_image=Image.open("assets/moon2.png"))
        self.theme_label = ctk.CTkLabel(self, image=self.theme_image, text="", cursor="hand2")
        self.theme_label.place(x=20, y=20)
        self.theme_label.bind("<Button-1>", self.switch_theme)

    def get_problem(self):
        num1, operation, num2, answer = game.random_problem()
        self.answer = answer
        self.frame.problem.configure(text=f"{num1} {operation} {num2}")

    def get_answer(self, event=None):
        inp = self.frame.entry.get()
        if float(inp) == self.answer:
            self.score += 1
            self.frame.score_label.configure(text=f'Score: {self.score}')
            self.get_problem()
            self.frame.entry.delete(0, "end")
        else:
            self.frame.answer_button.grid_forget()
            self.frame.score_label.configure(text=f"{random.choice(['GOD DAMN!', 'DAMN IT!'])}\nThe correct answer is {int(self.answer)}\nYour score is {self.score}!\nLet's try again", font=("Roboto", 18))
            self.frame.entry.grid_forget()
            # self.frame.try_again_button = ctk.CTkButton(self, text='Try again', command=self.try_again)
            # self.frame.try_again_button.grid(row=1, column=0)


    # def try_again(self):
    #     self.back_to_main_menu()
    #     self.show_game()
    #     self.

    
    def show_game(self):
        self.start_frame.grid_forget()
        self.frame = self.frame = MyFrame2(self,
                                   width=int(self._current_width*0.8),
                                   height=int(self._current_height*0.8),
                                   fg_color=("#e3e3e3", "#303030"),
                                   corner_radius=10)
        self.frame.grid(row=0, column=0)
        self.get_problem()

    def back_to_main_menu(self):
        self.frame.grid_forget()
        self.start_frame.grid(row=0, column=0)
        self.focus()

    def callback(self, event):
        webbrowser.open_new("https://vk.com/mykiil")
    
    def underline_link_app(self, event):
        label_font = ctk.CTkFont(family='Roboto', size=13, underline=True)
        self.configure
        self.label_author.configure(font=label_font)

    def unrerline_link_disapp(self, event):
        label_font = ctk.CTkFont(family='Roboto', size=13, underline=False)
        self.label_author.configure(font=label_font)

    def switch_theme(self, event):
        if self.theme_mode == 'dark':
            ctk.set_appearance_mode("light")
            self.theme_mode = 'light'
        else:
            ctk.set_appearance_mode("dark")
            self.theme_mode = 'dark'
"""
TO DO:
1. ProgressBar (TimeLimit)
2. Зеленая и красная надпись (верно/неверно)
3. Ввод по клавише Enter.
4. Надпись с количеством очков
5. Ввод имени игрока
6. Сохранение очков в бд
"""


if __name__ == '__main__':
    app = App()
    app.mainloop()