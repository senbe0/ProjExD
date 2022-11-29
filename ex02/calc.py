import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

root.title("hello, world!!")
root.geometry("500x200")

label = tk.Label(root, text="This is a label", font=("", 20))
label.pack()

def button_click():
    tkm.showwarning("警告", "おすな！！")
button = tk.Button(root, text="Don't press it", command=button_click)
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()

root.mainloop()


