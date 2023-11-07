from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")

canvas=Canvas(root, width=990, height=490, bg="white",highlightbackground="gray")
fillcolor=["green","yellow","red","blue","pink"]
colour_dropdown=ttk.Combobox(root,state="readonly",values=fillcolor, width=10)
colour_dropdown.place(relx=0.8, rely=0.9, anchor=CENTER)

label=Label(root, text="Choose A Color")
label.place(relx=0.6,rely=0.9, anchor= CENTER)

label_startx=Label(root,text="Choose StartX Point")
label_startx.place(relx = 0.2, rely = 0.9, anchor = CENTER)

coordinates_values = [10,50,100,200,300,400,500,600,700,800,900]
d1 = ttk.Combobox(root, state="readonly", values = coordintaes_values, width=10)
d1.place(relx=0.4, rely=0.9, anchor=CENTER)

label_starty=Label(root,text="Choose StartY Point")
label_starty.place(relx = 0.2, rely = 1, anchor = CENTER)

d2 = ttk.Combobox(root, state="readonly", values = coordintaes_values, width=10)
d2.place(relx=0.4, rely=1, anchor=CENTER)

label_end=Label(root,text="Choose EndX Point")
label_endx.place(relx = 0.01, rely = 0.9, anchor = CENTER)

d3 = ttk.Combobox(root, state="readonly", values = coordintaes_values, width=10)
d3.place(relx=0.1, rely=0.9, anchor=CENTER)

label_starty=Label(root,text="Choose EndY Point")
label_starty.place(relx = 0.01, rely = 1, anchor = CENTER)

d4 = ttk.Combobox(root, state="readonly", values = coordintaes_values, width=10)
d4.place(relx=0.1, rely=1, anchor=CENTER)

direction = ""
oldx=50
oldy=50
newx=50
newy=50
def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy 
    oldx = newx
    oldy = newy
    newx=newx+5
    direction = "right"
    draw(direction, oldx,oldy, newx ,newy)
    
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx=newx-5
    direction = "left"
    draw(direction, oldx,oldy, newx ,newy)
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy-5
    direction = "up"
    draw(direction, oldx,oldy, newx ,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy=newy+5
    direction = "down"
    draw(direction, oldx,oldy, newx ,newy)
    
def draw(direction,oldx,oldy, newx ,newy):
    fill_color = input_box.get()
    if (direction=="right"):
        right_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
    if (direction=="left"):
        left_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
    if(direction=="up"):
        up_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
    if(direction=="down"):
        down_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
canvas.pack()
root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)
root.mainloop()


root.mainloop()