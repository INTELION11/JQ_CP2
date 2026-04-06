import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.configure(background="#55d3b8")
root.minsize(250,500)
root.maxsize(1500,1500)
root.geometry("300x300+100+100")

start = tk.Label(root,text="This is my first GUI",font=("Times New Roman", 30, "bold"))
start.grid(row=0,column=0)
start.config(fg="#376d2a",background="#9c3434")

label = tk.Label(root,text="This is a label.")
label.grid(row=1,column=0)




# making a counter
root.count = 0

def add():
    root.count += 1
    lbl["text"] = str(root.count)
def sub():
    root.count -= 1
    lbl["text"] = str(root.count)


btn = tk.Button(root,text="ADD",command=add)
btn.grid(row=4,column=0)

btn2 = tk.Button(root,text="Subtract",command=sub)
btn2.grid(row=4,column=1)


lbl = tk.Label(root,text="0")
lbl.grid(row=5,column=0,columnspan=2)

close = tk.Button(root,text="Bye",command=root.destroy)
close.grid(row=6,column=1)

root.mainloop()