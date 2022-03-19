from tkinter import *
from math import pi

root = Tk()
root.geometry('170x198')
inp = Entry(width=50)
out = Entry(width=50)
inp.pack()
out.pack()
def count():
    out.delete(0, len(out.get()))
    i = str(inp.get())
    while '^' in i:
        i = i.replace('^', '**')
    try:
        a = eval(i)
    except:
        a = 'Ошибка'
    out.insert(0, a)

def clear():
    inp.delete(0, len(inp.get()))
    out.delete(0, len(out.get()))

def pi_calc():
    inp.insert('end', 'pi')

def prinp(s: str):
    if s == '<=':
        inp.delete(len(inp.get()) - 1)
    elif s in '/^*+-' and inp.get()[-1] in '/**+-':
        prinp('<=')
        inp.insert('end', s)
    else:
        inp.insert('end', s)

f_top = Frame(root)
f_bottom = Frame(root)
Button(f_top, text="C", command=clear).pack(side=LEFT)
Button(f_top, text="Pi", command=pi_calc).pack(side=LEFT)
Button(f_top, text="<=", command=lambda: prinp('<=')).pack(side=LEFT)
Button(f_top, text="/", command=lambda: prinp('/')).pack(side=LEFT)
f_top.pack(side=TOP)
f_top = Frame(root)

Button(f_top, text="1", command=lambda: prinp('1')).pack(side=LEFT)
Button(f_top, text="2", command=lambda: prinp('2')).pack(side=LEFT)
Button(f_top, text="3", command=lambda: prinp('3')).pack(side=LEFT)
Button(f_top, text="*", command=lambda: prinp('*')).pack(side=LEFT)
f_top.pack(side=TOP)
f_top = Frame(root)

Button(f_top, text="4", command=lambda: prinp('4')).pack(side=LEFT)
Button(f_top, text="5", command=lambda: prinp('5')).pack(side=LEFT)
Button(f_top, text="6", command=lambda: prinp('6')).pack(side=LEFT)
Button(f_top, text="-", command=lambda: prinp('-')).pack(side=LEFT)
f_top.pack(side=TOP)
f_top = Frame(root)

Button(f_top, text="7", command=lambda: prinp('7')).pack(side=LEFT)
Button(f_top, text="8", command=lambda: prinp('8')).pack(side=LEFT)
Button(f_top, text="9", command=lambda: prinp('9')).pack(side=LEFT)
Button(f_top, text="+", command=lambda: prinp('+')).pack(side=LEFT)
f_top.pack(side=TOP)
f_top = Frame(root)

Button(f_top, text="0", command=lambda: prinp('0')).pack(side=LEFT)
Button(f_top, text="^", command=lambda: prinp('^')).pack(side=LEFT)
Button(f_top, text=",", command=lambda: prinp(',')).pack(side=LEFT)
Button(f_top, text="=", command=count).pack(side=LEFT)
f_top.pack(side=TOP)
f_top = Frame(root)

root.mainloop()

# str.isdigit()
