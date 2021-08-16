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
        label = tk.Label(root, text="Enter your name:")
        label.pack()

        name = tk.StringVar()
        name_box = tk.Entry(root, textvariable=name)
        name_box.pack()
        self.name = name
    

    def _create_widget_two(self):
        submit = tk.Button(root, text="Submit", command=self.say_hello)
        submit.pack()
    

    def say_hello(self):
        print(f'Hello, {self.name.get()}')  # must use .get method
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("My App")
    root.minsize(300, 100)
    # photo = tk.PhotoImage(file="python3.jpeg", imgtype='.jpg')
    # tk.Label(root, image=photo, bg="black").pack()
    app = Application(master=root)
    app.mainloop()