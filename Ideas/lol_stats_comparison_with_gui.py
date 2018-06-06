from tkinter import *
from tkinter import messagebox


class Comparison:
    def __init__(self, master):
        self.master = master
        master.title("LoL Stat Comparison")

        self.label = Label(master, text="This program will compare old and new AD and AD Ratio in LoL")
        self.label.grid(row=0)

        self.compare_button = Button(master, text="Compare", command=self.compare)
        self.compare_button.grid(row=5)

        self.old_ad = Entry()
        self.old_ad.grid(row=1, column=0)

        self.old_ad_ratio = Entry()
        self.old_ad_ratio.grid(row=2, column=0)

        self.new_ad = Entry()
        self.new_ad.grid(row=1, column=1)

        self.new_ad_ratio = Entry()
        self.new_ad_ratio.grid(row=2, column=1)

    def compare(self):
        old_ad = float(self.old_ad.get())
        old_ad_ratio = float(self.old_ad_ratio.get())
        new_ad = float(self.new_ad.get())
        new_ad_ratio = float(self.new_ad_ratio.get())
        counter = 1
        while counter < 19:
           # print("Level %.2f: " % counter + "%.2f vs " % old_ad + "%.2f" % new_ad)
            if old_ad > new_ad:
                old_ad = old_ad + old_ad_ratio
                new_ad = new_ad + new_ad_ratio
                counter += 1

            else:
                messagebox.showinfo("Results", "AD and Ratio will be better at level: %.f" % counter +
                        "\nThe new AD will be %.2f" % new_ad)
                break


app = Tk()
compare_gui = Comparison(app)
app.mainloop()
