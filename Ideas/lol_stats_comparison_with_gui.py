from tkinter import *
from tkinter import messagebox


class Comparison:
    def __init__(self, master):
        self.master = master
        master.title("LoL Stat Comparison")

        self.label = Label(master, text="Calculate AD Differene and Max AD")
        self.label.grid(row=0, columnspan=3)

        self.compare_button = Button(master, text="Compare", command=self.compare)
        self.compare_button.grid(row=5)

        self.max_ad_button = Button(master, text="Get Max AD", command=self.maximumAD)
        self.max_ad_button.grid(row=5, column=1)

        self.old_ad = Entry()
        self.old_ad.grid(row=1, column=0)
        self.old_ad.insert(0, 'Old AD')
        self.old_ad.bind("<FocusIn>", lambda args: self.old_ad.delete('0', 'end'))

        self.old_ad_ratio = Entry()
        self.old_ad_ratio.grid(row=2, column=0)
        self.old_ad_ratio.insert(1, 'Old Ratio')
        self.old_ad_ratio.bind("<FocusIn>", lambda args: self.old_ad_ratio.delete('0', 'end'))

        self.new_ad = Entry()
        self.new_ad.grid(row=1, column=1)
        self.new_ad.insert(2, 'New AD')
        self.new_ad.bind("<FocusIn>", lambda args: self.new_ad.delete('0', 'end'))

        self.new_ad_ratio = Entry()
        self.new_ad_ratio.grid(row=2, column=1)
        self.new_ad_ratio.insert(3, 'New Ratio')
        self.new_ad_ratio.bind("<FocusIn>", lambda args: self.new_ad_ratio.delete('0', 'end'))

    def compare(self):
        old_ad = float(self.old_ad.get())
        old_ad_ratio = float(self.old_ad_ratio.get())
        new_ad = float(self.new_ad.get())
        new_ad_ratio = float(self.new_ad_ratio.get())
        counter = 1
        while counter < 19:
            if old_ad > new_ad:
                old_ad = old_ad + old_ad_ratio
                new_ad = new_ad + new_ad_ratio
                counter += 1

            else:
                messagebox.showinfo("Results", "AD and Ratio will be better at level: %.f" % counter +
                        "\nThe new AD will be %.2f" % new_ad)
                break

    def maximumAD(self):
        old_ad = float(self.old_ad.get())
        old_ad_ratio = float(self.old_ad_ratio.get())
        new_ad = float(self.new_ad.get())
        new_ad_ratio = float(self.new_ad_ratio.get())

        old_ad = old_ad + (old_ad_ratio * 17)
        new_ad = new_ad + (new_ad_ratio * 17)
        messagebox.showinfo("Results", "The Champions pure AD at level 18 was %.2f" % old_ad +
                            " before 8.11\nNow it will be %.2f" % new_ad)


app = Tk()
compare_gui = Comparison(app)
app.mainloop()
