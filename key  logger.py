import tkinter as tk

def key_pressed(event):
    print("You pressed:", event.char)

root = tk.Tk()
root.title("Key Press Detector")

root.bind("<Key>", key_pressed)

root.mainloop()

with tk(on_press=lambda tk: tk("log.txt",tk)) as tkinter:
    tkinter.join()