from tkinter import *
root=Tk()
root.geometry("1100x600")
root.title("Calculator")
expression=""

def btn_click(item):
    global expression
    expression=expression+str(item)
    scvalue.set(expression)

def btn_clear():
    global expression
    expression=''
    scvalue.set("")

def evaluate(scvalue):
    global expression
    try:
        result=str(eval(expression))
        scvalue.set(result)
        expression=""
    except:
        expression=""

scvalue=StringVar()
screen=Entry(root,textvariable=scvalue,font="lucida 60 bold").grid(columnspan=4,ipadx=100)

b1=Button(root,text="9",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(9)).grid(row=2,column=0)
b2=Button(root,text="8",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(8)).grid(row=2,column=1)
b3=Button(root,text="7",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(7)).grid(row=2,column=2)

b4=Button(root,text="6",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(6)).grid(row=3,column=0)
b5=Button(root,text="5",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(5)).grid(row=3,column=1)
b6=Button(root,text="4",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(4)).grid(row=3,column=2)

b7=Button(root,text="3",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(3)).grid(row=4,column=0)
b8=Button(root,text="2",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(2)).grid(row=4,column=1)
b9=Button(root,text="1",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(1)).grid(row=4,column=2)

b10=Button(root,text="=",padx=90,pady=20,font="lucida 30 bold",command=lambda:evaluate(scvalue)).grid(row=5,column=0)
b11=Button(root,text="Clear",padx=80,pady=20,font="lucida 30 bold",command=lambda:btn_clear()).grid(row=5,column=1)
b12=Button(root,text="0",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click(0)).grid(row=5,column=2)

plus=Button(root,text="+",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click("+")).grid(row=2,column=3)
subtract=Button(root,text="-",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click("-")).grid(row=3,column=3)
multiply=Button(root,text="*",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click("*")).grid(row=4,column=3)
divide=Button(root,text="/",padx=90,pady=20,font="lucida 30 bold",command=lambda:btn_click("/")).grid(row=5,column=3)

root.mainloop()