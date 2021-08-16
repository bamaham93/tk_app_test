import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    

    def create_widgets(self):
        # Create widget one
        self._create_widget_one()
        # Create widget two
        self._create_widget_two()
    

    def _create_widget_one(self):
        pass
    

    def _create_widget_two(self):
        pass
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My App")
    photo = tk.PhotoImage(file="python3.jpeg", imgtype='.jpg')
    tk.Label(root, image=photo, bg="black").pack()
    app = Application(master=root)
    app.mainloop()