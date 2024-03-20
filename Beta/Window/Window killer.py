import tkinter as tk

root = tk.Tk()
root.title("Window Killer")
#root.wm_resizable(None,None)
root.overrideredirect(True)
canvas = tk.Canvas(root,width=500,height=500)
canvas.pack()

partikel = []

x = 100
y = 100

Up    = False
Down  = False
Left  = False
Rigth = False
def press(event):
    global Up, Down, Rigth, Left
    if (event.keysym == "w"): Up    = True
    if (event.keysym == "s"): Down  = True
    if (event.keysym == "a"): Left  = True
    if (event.keysym == "d"): Rigth = True
def reles(event):
    global Up, Down, Rigth, Left
    if (event.keysym == "w"): Up    = False
    if (event.keysym == "s"): Down  = False
    if (event.keysym == "a"): Left  = False
    if (event.keysym == "d"): Rigth = False
root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", reles)

while True:
    try: canvas.delete("all")
    except: exit()
    
    canvas.create_line(0,25,500,25,fill="black")
    canvas.create_line(475,0,475,25)
    canvas.create_line(450,0,450,25)
    canvas.create_line(425,0,425,25)
    canvas.create_line(25,0,25,25)
    
    y = y + (Down - Up)
    if (y < 0): y = 0
    if (y > root.winfo_screenheight() - 500): y = root.winfo_screenheight() - 500
    x = x + (Rigth - Left)
    if (x < 0): x = 0
    if (x > root.winfo_screenwidth() - 500): x = root.winfo_screenwidth() - 500
    
    root.wm_geometry(f"500x500+{x}+{y}")
    
    canvas.update()
    root.update()