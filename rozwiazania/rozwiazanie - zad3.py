import tkinter


class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("200x200")

        self.greet_button = tkinter.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

    def greet(self):
        self.label = tkinter.Label(self.master, text="hello world")
        self.label.pack()


root = tkinter.Tk()
my_gui = MyGUI(root)
root.mainloop()
