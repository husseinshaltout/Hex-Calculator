from tkinter import *

g = ''#evaluate stirng
d = '' #display value
ld = ''#seprate hex
#Hex to deciaml function
def h2d(h):
    k = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    total = 0
    for i in range(len(h)):
        if (h[i].upper() in k):
            total+= (int(k[h[i].upper()]) * 16**((len(h)-1)-i))
        else:
            total+= (int(h[i]) * 16**((len(h)-1)-i))
            
    return total  
def ev(g):
    g = eval(g)
    if (hex(g)[0] == '-'):
        g = '-'+hex(g)[3:]
    else:    
        g = hex(g)[2:]
    Text1.delete('1.0', END) 
    Text1.insert('1.0',a)
    print(g)
    return g  
  
def ln(i):#Store each seprate hex value
    global ld
    ld += str(i) 
    Text1.insert(END, i)
    
def add():
    global d
    global g
    global ld
    #For display
    b = Text1.get("1.0",END)
    d = b.strip() + '+'
    #Add to evaluation formula
    g += str(h2d(ld.strip()))+'+'
    Text1.delete('1.0', END) 
    Text1.insert('1.0',d)
    print(g)
    ld = ''
    return d,g,ld
def sub():
    global d
    global g
    global ld
    #For display
    b = Text1.get("1.0",END)
    d = b.strip() + '-'
    #Add to evaluation formula
    g += str(h2d(ld.strip()))+'-'
    Text1.delete('1.0', END) 
    Text1.insert('1.0',d)
    print(g)
    ld = ''
    return d,g,ld
def mul():
    global d
    global g
    global ld
    b = Text1.get("1.0",END)
    d = b.strip() + '*'
    #Add to evaluation formula
    g += str(h2d(ld.strip()))+'*'
    Text1.delete('1.0', END) 
    Text1.insert('1.0',d)
    print(g)
    ld = ''
    return d,g,ld
def div():
    global d
    global g
    global ld
    b = Text1.get("1.0",END)
    d = b.strip() + '/'
    #Add to evaluation formula
    g += str(h2d(ld.strip()))+'/'
    Text1.delete('1.0', END) 
    Text1.insert('1.0',d)
    print(g)
    ld = ''
    return d,g,ld    

#Equal button
def eq():
    global d
    global g
    global ld
    b = Text1.get("1.0",END)
    d = b.strip()
    #Add to evaluation formula
    g += str(h2d(ld.strip()))    
    Text1.delete('1.0', END) 
    Text1.insert('1.0',d)
    print(g)    
    ld = ''
    #Calculate formula and change to hex
    k = eval(g)
    k=int(k)
    print("Decimal value: ",k)
    if (hex(k)[0] == '-'):
        k = '-'+hex(k)[3:]
    else:    
        k = hex(k)[2:]
    Text1.delete('1.0', END) 
    Text1.insert('1.0',k)
    g = ''
    print(k)
    return k    

#Clear textbox    
def CE():
    global d
    global g
    global ld
    Text1.delete('1.0', END)
    g = ''
    d=''
    ld=''    
        
#GUI
top = Tk()
top.geometry("336x296+459+196")
top.title("Hex Calculator")
Text1 = Text(top)
Text1.place(relx=0.06, rely=0.034, relheight=0.216, relwidth=0.905)
Button1 = Button(top,text='1',command=lambda:ln('1')).place(relx=0.06, rely=0.305, height=24, width=47)
Button2 = Button(top,text='2',command=lambda:ln('2')).place(relx=0.238, rely=0.305, height=24, width=47)
Button3 = Button(top,text='3',command=lambda:ln('3')).place(relx=0.417, rely=0.305, height=24, width=47)
Button4 = Button(top,text='4',command=lambda:ln('4')).place(relx=0.06, rely=0.405, height=24, width=47)
Button5 = Button(top,text='5',command=lambda:ln('5')).place(relx=0.238, rely=0.405, height=24, width=47)
Button6 = Button(top,text='6',command=lambda:ln('6')).place(relx=0.417, rely=0.405, height=24, width=47)
Button7 = Button(top,text='7',command=lambda:ln('7')).place(relx=0.06, rely=0.505, height=24, width=47)
Button8 = Button(top,text='8',command=lambda:ln('8')).place(relx=0.238, rely=0.505, height=24, width=47)
Button9 = Button(top,text='9',command=lambda:ln('9')).place(relx=0.417, rely=0.505, height=24, width=47)
ButtonA = Button(top,text='A',command=lambda:ln('A')).place(relx=0.06, rely=0.605, height=24, width=47)
ButtonB = Button(top,text='B',command=lambda:ln('B')).place(relx=0.238, rely=0.605, height=24, width=47)
ButtonC = Button(top,text='C',command=lambda:ln('C')).place(relx=0.417, rely=0.605, height=24, width=47)
ButtonD = Button(top,text='D',command=lambda:ln('D')).place(relx=0.06, rely=0.705, height=24, width=47)
ButtonE = Button(top,text='E',command=lambda:ln('E')).place(relx=0.238, rely=0.705, height=24, width=47)
ButtonF = Button(top,text='F',command=lambda:ln('F')).place(relx=0.417, rely=0.705, height=24, width=47)
Buttonadd = Button(top,text='+',command=add).place(relx=0.655, rely=0.372, height=24, width=47)
Buttonsub = Button(top,text='-',command=sub).place(relx=0.833, rely=0.372, height=24, width=47)
Buttonmul = Button(top,text='*',command=mul).place(relx=0.655, rely=0.473, height=24, width=47)
Buttondiv = Button(top,text='/',command=div).place(relx=0.833, rely=0.473, height=24, width=47)
Buttoneq = Button(top,text='=',command=eq).place(relx=0.744, rely=0.574, height=24, width=47)
Buttonce = Button(top,text='CE',command=CE).place(relx=0.744, rely=0.676, height=24, width=47)
top.mainloop()