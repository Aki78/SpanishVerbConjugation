import tkinter as tk
from num2words import num2words
from random import randint

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.number_range = (0, 100)  # Default range, can be changed
        self.number_to_guess = self.generate_random_number()

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        self.info_label = tk.Label(self.main_frame, text="Guess the number in Spanish")
        self.info_label.pack()

        self.number_label = tk.Label(self.main_frame, text=self.number_to_guess)
        self.number_label.pack()

        self.entry = tk.Entry(self.main_frame)
        self.entry.pack()
        self.entry.bind('<Return>', self.check_answer)  # bind Enter key to check_answer function

        self.check_button = tk.Button(self.main_frame, text="Check", command=self.check_answer)
        self.check_button.pack()

    def generate_random_number(self):
        return randint(*self.number_range)

    def check_answer(self, event=None):
        answer = self.entry.get()
        correct_answer = num2words(self.number_to_guess, lang='es')

        if answer.lower() == correct_answer:
            self.number_to_guess = self.generate_random_number()
            self.number_label.config(text=self.number_to_guess)
            self.entry.delete(0, tk.END)
            self.info_label.config(text="Correct! Now guess the next number.", fg='green')
        else:
            self.entry.delete(0, tk.END)
            self.info_label.config(text=f"Incorrect! The correct answer is '{correct_answer}'. Try again.", fg='red')
            self.master.after(2000, self.reset_info_label)  # flash correct answer for 2 seconds

    def reset_info_label(self):
        self.info_label.config(text="Guess the number in Spanish", fg='black')

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

