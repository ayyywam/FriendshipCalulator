import tkinter as tk
import random
from tkinter.ttk import Label


def calculate():
    random_number = random.randint(1, 101)
    if random_number < 20:
        result.set("not good friends :(")

    elif random_number < 60:
        result.set("Might bloom into something")

    elif random_number < 80:
        result.set("Probably a good friend")

    elif 90 <= random_number <= 100:
        result.set("Best Friends! :)")


window = tk.Tk()

window.title("Friendship calculator")
window.geometry("250x150")
title = tk.Label(text="Enter the name of a person")
title.grid(column=0, row=1)

title2 = tk.Label(text="Enter the name of another person")
title2.grid(column=0, row=3)

button1 = tk.Button(text="Calculate", command=calculate)
button1.grid(column=0, row=6)

result = tk.StringVar()
result.set('')
display = Label(window, textvariable=result)
display.grid(column=0, row=7)
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)
entry_field2 = tk.Entry()
entry_field2.grid(column=0, row=4)
window.mainloop()

