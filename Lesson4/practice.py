import math
from tkinter import *
from tkinter import messagebox


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.label = Label(master, text="Barebones for calculator")
        self.label.grid(row=0, columnspan=3)

        self.addition_button = Button(master, text="Addition", command=self.addition)
        self.addition_button.grid(row=5)

        self.subtraction_button = Button(master, text="Substraction", command=self.subtraction)
        self.subtraction_button.grid(row=5, column=1)

        self.first_number = Entry()
        self.first_number.grid(row=1, column=0)
        self.first_number.insert(0, "1st Number")
        self.first_number.bind("<FocusIn>", lambda args: self.first_number.delete("0", "end"))

        self.second_number = Entry()
        self.second_number.grid(row=2, column=0)
        self.second_number.insert(0, "2nd Number")
        self.first_number.bind("<FocusIn>", lambda args: self.second_number.delete("0", "end"))

    def addition(self):
        first_number = float(self.first_number.get())
        second_number = float(self.second_number.get())

        result = first_number + second_number
        messagebox.showinfo("Results:", str(result))

    def subtraction(self):
        first_number = float(self.first_number.get())
        second_number = float(self.second_number.get())

        if first_number > second_number:
            result = first_number - second_number
            messagebox.showinfo("Results:", result)
        else:
            result = second_number - first_number
            messagebox.showinfo("Results:", result)


app = Tk()
calculator_gui = Calculator(app)
app.mainloop()