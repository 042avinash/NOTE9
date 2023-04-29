from tkinter import *
from tkinter import filedialog

class Notepad:
    current_file = None

    def __init__(self, master):
        self.master = master
        master.title("Notepad")
        self.textarea = Text(master)
        self.textarea.pack(expand=YES, fill=BOTH)
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

    def new_file(self):
        self.current_file = None
        self.textarea.delete(1.0, END)

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file is not None:
            self.current_file = file.name
            contents = file.read()
            self.textarea.delete(1.0, END)
            self.textarea.insert(END, contents)
            file.close()

    def save_file(self):
        if self.current_file is None:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.current_file is not None:
            file = open(self.current_file, "w")
            file.write(self.textarea.get(1.0, END))
            file.close()

root = Tk()
notepad = Notepad(root)
root.mainloop()
