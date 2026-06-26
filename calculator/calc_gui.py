import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("500x500")

t1=tk.Label(root,text="CALCULATOR",font=("arial",20))
t1.place(x="165",y="20")


def add():
    a=float(e1.get())
    b=float(e2.get())
    c=a+b
    l3.config(text="ADD IS : " + str(c))
def sub():
    a=float(e1.get())
    b=float(e2.get())
    c=a-b
    l3.config(text="SUB IS "+str(c))
def mul():
    a=float(e1.get())
    b=float(e2.get())
    c=a*b
    l3.config(text="MUL IS "+str(c))
def div():
    a=float(e1.get())
    b=float(e2.get())
    c=a/b
    l3.config(text="DIV IS "+str(c))


l1=tk.Label(root,text="Enter 1st Number ",font=("arial",15))
l1.place(x="10",y="75")
e1=tk.Entry(root,font=("arial",15))
e1.place(x="180",y="75")


l2=tk.Label(root,text="Enter 2nd Number ", font=("arial",15))
l2.place(x="10",y="125")
e2=tk.Entry(root,font=("arial",15))
e2.place(x="180",y="125")


b1=tk.Button(
            root,
            text="ADD",
            font=("arial",15),
            bg="BROWN",
            fg="WHITE",
            command=add
            )
b1.place(x="25",y="175")


b2=tk.Button(
            root,
            text="SUB",
            font=("arial",15),
            bg="BROWN",
            fg="WHITE",
            command=sub
            )
b2.place(x="100",y="175")


b3=tk.Button(
            root,
            text="MUL",
            font=("arial",15),
            bg="BROWN",
            fg="WHITE",
            command=mul
            )
b3.place(x="175",y="175")


b4=tk.Button(
            root,
            text="DIV",
            font=("arial",15),
            bg="BROWN",
            fg="WHITE",
            command=div
            )
b4.place(x="250",y="175")


l3=tk.Label(root,text="...",font=("arial",15))
l3.place(x="180",y="225")


print(root)
root.mainloop()
