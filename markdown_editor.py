import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
    

    def create_widgets(self):
        # Create widget one
        self.menu()

        # Create widget two
        self.save_button()

        # Create widget three
        self.save_as()

        #Text field
        self.text_window()

        #Filename field
        self.file_name()
    

    def menu(self):
        button = tk.Button(master=root, text="Menu")
        button.grid(row=0, column=0)
    

    def save_button(self):
        button = tk.Button(master=root, text="Save", command=self._save)
        button.grid(row=0, column=1)
    

    def _save(self):
        pass


    def save_as(self):
        button = tk.Button(master=root, text="Save As", command=self._save_as)
        button.grid(row=0, column=2)
    

    def file_name(self):
        file_name = tk.Entry(master=root).grid(row=0, column=3)
        #file_name.grid(row=0, column=)
    

    def text_window(self):
        field = tk.Text(master=root)
        field.grid(row=1, column=0)
    

    def _save_as(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Markdown Editor")
    app = Application(master=root)
    app.mainloop()