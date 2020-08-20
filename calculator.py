import tkinter as tk

def click(n):
    value = box.get()#get value from entry or display
    box.delete(0,tk.END) #remove value from entry or display
    box.insert(0,str(value) + str(n)) #set new string on display or entry

def ac():
    #remove values on display
    box.delete(0,tk.END)

def add():
    global sign
    sign = "+"
    global number1
    number1 = int(box.get())
    box.delete(0,tk.END)
def sub():
    global sign
    sign = "-"
    global number1
    number1 = int(box.get())
    box.delete(0,tk.END)

def mult():
    global sign
    sign = "*"
    global number1
    number1 = int(box.get())
    box.delete(0,tk.END)

def div():
    global sign
    sign = "/"
    global number1
    number1 = int(box.get())
    box.delete(0,tk.END)

def equal():
    number2 = int(box.get())
    box.delete(0,tk.END)

    if sign == "+":
        result = number1 + number2
        result = str(result)
        box.insert(0,result)

    if sign == "-":
        result = number1 - number2
        result = str(result)
        box.insert(0,result)
        
    if sign == "*":
        result = number1 * number2
        result = str(result)
        box.insert(0,result)
        
    if sign == "/":
        result = number1 / number2
        result = str(result)
        box.insert(0,result)
    
    

win = tk.Tk()

win.title("Calculator")

win.configure(bg = "black")
                        
box = tk.Entry(win, width = 15,font = ("Calibri",30),justify = "right", borderwidth = 5)
box.grid(row = 0, column = 0,columnspan = 4,padx = 3, pady = 3)

sevenButton = tk.Button(win,text = " 7 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(7))
sevenButton.grid(row = 1, column = 0)

eightButton = tk.Button(win,text = " 8 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(8))
eightButton.grid(row =1 , column = 1)

nineButton = tk.Button(win,text = " 9 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(9))
nineButton.grid(row = 1, column = 2)

divisionButton = tk.Button(win,text = " ÷ ",padx = 10, pady = 5,height = 2,width = 4,command = div)
divisionButton.grid(row = 1, column = 3)

fourButton = tk.Button(win,text = " 4 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(4))
fourButton.grid(row = 2, column = 0)

fiveButton = tk.Button(win,text = " 5 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(5))
fiveButton.grid(row = 2, column = 1)

sixButton = tk.Button(win,text = " 6 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(6))
sixButton.grid(row = 2, column = 2)

multButton = tk.Button(win,text = " x ",padx = 10, pady = 5,height = 2,width = 4,command = mult)
multButton.grid(row = 2, column = 3)

oneButton = tk.Button(win,text = " 1 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(1))
oneButton.grid(row = 3, column = 0)

twoButton = tk.Button(win,text = " 2 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(2))
twoButton.grid(row = 3, column = 1)

threeButton = tk.Button(win,text = " 3 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(3))
threeButton.grid(row = 3, column = 2)

subButton = tk.Button(win,text = " - ",padx = 10, pady = 5,height = 2,width = 4,command = sub)
subButton.grid(row = 3, column = 3)

acButton = tk.Button(win,text = " AC ",padx = 10, pady = 5,height = 2,width = 4,command = ac)
acButton.grid(row = 4, column = 0)

zeroButton = tk.Button(win,text = " 0 ",padx = 10, pady = 5,height = 2,width = 4,command = lambda:click(0))
zeroButton.grid(row = 4, column = 1)

equalButton = tk.Button(win,text = " = ",bg = "green",padx = 10, pady = 5,height = 2,width = 4,command = equal)
equalButton.grid(row = 4, column = 2)

sumButton = tk.Button(win,text = " + ",padx = 10, pady = 5,height = 2,width = 4,command = add)
sumButton.grid(row = 4, column = 3)

win.mainloop()
