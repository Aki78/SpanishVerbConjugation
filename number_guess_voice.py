import tkinter as tk
from num2words import num2words
from random import randint
from gtts import gTTS
from playsound import playsound
import os
import threading
import time


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.number_range = [0, 100]  # Default range, can be changed

        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        self.range_frame = tk.Frame(self.main_frame)
        self.range_frame.pack()

        self.min_range_label = tk.Label(self.range_frame, text="Min Range:")
        self.min_range_label.pack(side=tk.LEFT)

        self.min_range_entry = tk.Entry(self.range_frame)
        self.min_range_entry.pack(side=tk.LEFT)

        self.max_range_label = tk.Label(self.range_frame, text="Max Range:")
        self.max_range_label.pack(side=tk.LEFT)

        self.max_range_entry = tk.Entry(self.range_frame)
        self.max_range_entry.pack(side=tk.LEFT)

        self.set_range_button = tk.Button(self.range_frame, text="Set Range", command=self.set_range)
        self.set_range_button.pack(side=tk.LEFT)

        self.number_to_guess = self.generate_random_number()
        self.number_to_guess_spanish = num2words(self.number_to_guess, lang='es')
        self.tts = gTTS(self.number_to_guess_spanish, lang='es')
        self.tts.save("number.mp3")
        threading.Thread(target=self.play_sound).start()

        self.info_label = tk.Label(self.main_frame, text="Type the number you hear in Spanish")
        self.info_label.pack()

        self.entry = tk.Entry(self.main_frame)
        self.entry.pack()
        self.entry.bind('<Return>', self.check_answer)  # bind Enter key to check_answer function

        self.check_button = tk.Button(self.main_frame, text="Check", command=self.check_answer)
        self.check_button.pack()

    def generate_random_number(self):
        return randint(*self.number_range)

    def set_range(self):
        try:
            min_range = int(self.min_range_entry.get())
            max_range = int(self.max_range_entry.get())
            if min_range < max_range:
                self.number_range = [min_range, max_range]
                self.number_to_guess = self.generate_random_number()
                self.number_to_guess_spanish = num2words(self.number_to_guess, lang='es')
                self.tts = gTTS(self.number_to_guess_spanish, lang='es')
                self.tts.save("number.mp3")
                threading.Thread(target=self.play_sound).start()
                self.info_label.config(text="Number range set. Type the number you hear.", fg='black')
            else:
                self.info_label.config(text="Invalid range. Min should be less than Max.", fg='red')
        except ValueError:
            self.info_label.config(text="Please enter valid integers for the range.", fg='red')

#    def check_answer(self, event=None):
#        answer = self.entry.get()
#        print(answer, self.number_to_guess_spanish)
#
#
#        if answer == self.number_to_guess_spanish:
#            self.number_to_guess = self.generate_random_number()
#            self.number_to_guess_spanish = num2words(self.number_to_guess, lang='es')
#            self.tts = gTTS(self.number_to_guess_spanish, lang='es')
#            self.tts.save("number.mp3")
#            threading.Thread(target=self.play_sound).start()
#            self.entry.delete(0, tk.END)
#            self.info_label.config(text="Correct! Now type the next number you hear.", fg='green')
#        else:
#            self.entry.delete(0, tk.END)
#            threading.Thread(target=self.show_correct_answer).start()
    def check_answer(self, event=None):
        try:
            answer = int(self.entry.get())  # Convert input to integer

            if answer == self.number_to_guess:
                self.number_to_guess = self.generate_random_number()
                self.number_to_guess_spanish = num2words(self.number_to_guess, lang='es')
                self.tts = gTTS(self.number_to_guess_spanish, lang='es')
                self.tts.save("number.mp3")
                threading.Thread(target=self.play_sound).start()
                self.entry.delete(0, tk.END)
                self.info_label.config(text="Correct! Now type the next number you hear.", fg='green')
            else:
                self.entry.delete(0, tk.END)
                threading.Thread(target=self.show_correct_answer).start()
        except ValueError:
            self.entry.delete(0, tk.END)
            self.info_label.config(text="Please enter a valid integer.", fg='red')


    def show_correct_answer(self):
        original_text = "Type the number you hear in Spanish"
        self.info_label.config(text=f"Incorrect! The correct answer was {self.number_to_guess}.", fg='red')
        self.master.update()
        time.sleep(2)
        self.info_label.config(text=original_text, fg='black')

    def play_sound(self):
        playsound("number.mp3")
        os.remove("number.mp3")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

