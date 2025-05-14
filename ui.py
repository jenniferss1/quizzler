from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.create_true_button()
        self.create_false_button()
        
        self.window.mainloop()
    
    def create_true_button(self):
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_image, 
            highlightthickness=0, 
            borderwidth=0
        )
        self.true_button.grid(row=0, column=0)
    
    def create_false_button(self):
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image= self.false_image,
            highlightthickness=0,
            borderwidth=0
        )
        self.false_button.grid(row=0, column=1)