# Write a program (GUI based) which does the same job as Notepad (Windows' application).
#
# It must have a menu Bar and two menus File menu and Help menu.
# Inside the File menu, there should be 3 functions, Open, Save and Close
# 1. Open, which lets user to chose a text file to display in the text area.
# 2. Save, should save the contents of text area in a text file.
# 3. Close, should terminate the application.
#
# Help Menu: upon clicking it should generate a message box to give brief info.
#  e.g. version of the application, probably author name....
import tkinter
from tkinter.filedialog import *
from tkinter.messagebox import *

Screen = tkinter.Tk()
Screen.title("Assignment 3")
Screen.geometry()
WritingSpace = Text(Screen)
TextFile = None


def open_file():
    TextFileTemporary = askopenfilename()
    print(TextFileTemporary)

    if TextFileTemporary:
        TextFile = TextFileTemporary
        WritingSpace.grid()
        WritingSpace.delete(1.0, END)
        file = open(TextFile, "r")
        WritingSpace.insert(1.0, file.read())
        file.close()
        print(TextFile)


def save_file():
    path = asksaveasfilename()
    write = open(path, mode="w")
    write.write(WritingSpace.get("1.0", END))


def close_editor():
    Screen.destroy()


def help_info():
    showinfo("Text Editor 1.0", "Henri Kelder\nhekeld@ttu.ee")


def mordor():
    text = """Three Rings for the Elven-kings under the sky,
Seven for the Dwarf-lords in their halls of stone,
Nine for Mortal Men doomed to die,
One for the Dark Lord on his dark throne
In the Land of Mordor where the Shadows lie.
One Ring to rule them all, One Ring to find them,
One Ring to bring them all and in the darkness bind them,
In the Land of Mordor where the Shadows lie."""
    showinfo("Rings of Power", text)


MenuBar = Menu(Screen)
FileMenu = Menu(MenuBar, tearoff=0)
Screen.config(menu=MenuBar)
MenuBar.add_cascade(label="File", menu=FileMenu)
MenuBar.add_command(label="Help", command=help_info)
MenuBar.add_command(label="???", command=mordor)
FileMenu.add_command(label="Open", command=open_file)
FileMenu.add_command(label="Save", command=save_file)
FileMenu.add_command(label="Exit", command=close_editor)

Screen.mainloop()
