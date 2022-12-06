import tkinter as tk
import maze_maker as mm

# 初期化
id_D = id_L = id_R = id_U = id_E = None

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""

def delete_status():
    canvas.delete(id_f)
    canvas.delete(id_L)
    canvas.delete(id_D)
    canvas.delete(id_R)
    canvas.delete(id_U)
    canvas.delete(id_E)

def main_proc():
    global cx, cy, mx, my
    global id_D, id_L, id_R, id_U, id_E, id_Foot
    if key == "Up": 
        my -= 1
        delete_status()
        id_D = canvas.create_image(cx, cy, image=U, tag="kokaton")
    if key == "Down": 
        my += 1
        delete_status()
        id_D = canvas.create_image(cx, cy, image=D, tag="kokaton")
    if key == "Left": 
        mx -= 1
        delete_status()
        id_D = canvas.create_image(cx, cy, image=L, tag="kokaton")
    if key == "Right": 
        mx += 1
        delete_status()
        id_D = canvas.create_image(cx, cy, image=R, tag="kokaton")
    if maze_lst[mx][my] == 1: # 移動先が壁だったら
        delete_status()
        id_E = canvas.create_image(cx, cy, image=E, tag="kokaton")
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1        
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)

    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    D = tk.PhotoImage(file="fig/1.png")
    L = tk.PhotoImage(file="fig/3.png")
    R = tk.PhotoImage(file="fig/2.png")
    U = tk.PhotoImage(file="fig/6.png")
    E = tk.PhotoImage(file="fig/20.png")
    id_f = canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()