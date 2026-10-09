from tkinter import *

def numbers(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""


def equals():
    global equation_text

    total = str(eval(equation_text))

    equation_label.set(total)


window = Tk()
window.geometry("300x575")
window.title("calculator")
window.resizable(False, False)
window.config(background="black")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, width=300,
              height=5, fg="blue",
              font=("Arial", 12))
label.pack()

frame = Frame(window)
frame.pack()

but1 = Button(frame, text= "1", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("1"))
but1.grid(row=0, column=0)
but2 = Button(frame, text= "2", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("2"))
but2.grid(row=0, column=1)
but3 = Button(frame, text= 3, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("3"))
but3.grid(row=0, column=2)

but4 = Button(frame, text= 4, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("4"))
but4.grid(row=1, column=0)
but5 = Button(frame, text= 5, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("5"))
but5.grid(row=1, column=1)
but6 = Button(frame, text= 6, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("6"))
but6.grid(row=1, column=2)

but7 = Button(frame, text= 7, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("7"))
but7.grid(row=2, column=0)
but8 = Button(frame, text= 8, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("8"))
but8.grid(row=2, column=1)
but9 = Button(frame, text= 9, width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("9"))
but9.grid(row=2, column=2)

buta = Button(frame, text= "/", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("/"))
buta.grid(row=0, column=3)
butb = Button(frame, text= "*", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("*"))
butb.grid(row=1, column=3)
butc = Button(frame, text= "+", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("+"))
butc.grid(row=2, column=3)
butd = Button(frame, text= "-", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("-"))
butd.grid(row=3, column=3)

bute = Button(frame, text= "0", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("0"))
bute.grid(row=3, column=2)
butr = Button(frame, text= ".", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= lambda : numbers("."))
butr.grid(row=3, column=1)
clear = Button(frame, text= "clear", width=9, height=6, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= clear)
clear.grid(row=3, column=0)
ans = Button(frame, text= "=", width=40, height=4, fg="white", bg="black",
              activebackground="black", activeforeground="white",
              command= equals)
ans.grid(row=4, columnspan=4)



window.mainloop()
