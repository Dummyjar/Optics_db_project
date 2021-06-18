from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from tkinter.tix import Balloon
import csv
from ttkbootstrap import Style

import backend
chumu=Style(theme='cyborg')
# win=tix.Tk()
win=chumu.master
win.title('OOE Database')
# win.geometry('1280x720')
win.resizable(width=False,height=False)


def get_element(event):
    pass

def viewall():

    if backend.check() is False:
        messagebox.showwarning("Attention!","Database is EMPTY!")
    else:
    
        for row in backend.show():
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
           
def search(de):
    if de == 'First Name':
        removeall()
        for row in backend.find(fn=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        
    if de == 'Sex':
        removeall()
        for row in backend.find(sex=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            
    if de == 'Last Name':
        removeall()
        for row in backend.find(ln=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                
    if de == 'Registration number':
        removeall()
        for row in backend.find(reg=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                
    if de == 'Roll number':
        removeall()
        for row in backend.find(roll=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                
    if de == 'Phone number':
        removeall()
        for row in backend.find(ph=nebo2.get()):
            tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                
    if de == 'Year':
        if int(nebo2.get()) > 4:
            messagebox.showerror("Error","There are 4 years in B.Tech and you entered 5.")
        else:
            removeall()
            for row in backend.find(year=nebo2.get()):
                tree.insert(parent='',index='end',text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    if de not in choose:
        messagebox.showerror("Error","Select search by condition!")
    


def addinfo():
    
    backend.entrydokha(fname.get(),lname.get(),reg.get(),rol.get(),sex.get(),phone.get(),bochor.get())
    #it will insert values to the database
    tree.insert(parent='',index='end',text='',values=(fname.get(),lname.get(),reg.get(),rol.get(),sex.get(),phone.get(),bochor.get()))
    #it will insert values into the tree 
   

def dell():
    selected = tree.focus()
    value = tree.item(selected,'value')
    backend.Del(value[2])

def updatekor():
    backend.edit(fname.get(),lname.get(),reg.get(),rol.get(),sex.get(),phone.get(),bochor.get())
  


def removeall():
    for record in tree.get_children():
        tree.delete(record)

def clean():
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)

# ------tree view function------------------------------------------------------

def dhor(event):
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    selected = tree.focus()
    value = tree.item(selected,'value')
    e.insert(END,value[0]) #1st name
    e3.insert(END,value[2]) # reg 
    e1.insert(END,value[1]) # last name
    e2.insert(END,value[3])  #roll 
    e5.insert(END,value[5]) #phone
    sex.set(value[4]) #gender
    e4.set(value[6]) #year

# ----------------------------------------------------
def refresh():
    removeall()
    viewall()
# -----------pop up function--for pop up menu----------------------------------------------------
def popup(e):
    menu.tk_popup(e.x_root,e.y_root)

# -----------------------student's marks sheet------------------------------------------
def marks():
    mar=Tk()
    mar.title('Marks Database')
    # -----------------------------------------------------------------
    a=Label(mar,text='University Roll no. :',pady=7,padx=10)
    a.grid(row=0,column=0)
    fname=StringVar() 
    e=ttk.Entry(mar,width=30,textvariable=fname)
    e.grid(row=0,column=1) 


    # -----------------------------------------------------------------
    a2=Label(mar,text='University Reg no. :',pady=7,padx=10)
    a2.grid(row=1,column=0)
    reg=StringVar() 
    e3=ttk.Entry(mar,width=30,textvariable=reg)
    e3.grid(row=1,column=1)
    # -----------------------------------------------------------------

    a4=Label(mar,text='Semester :',pady=7,padx=10)
    a4.grid(row=2,column=0)
    sem= StringVar() 
    e4=ttk.Combobox(mar,value=['B3','B4','B5','B6','B7','B8'],textvariable=sem)
    e4.grid(row=2,column=1)

# -----------saving file as csv------------------------------------------------------


def fun(var):
    with open(var + '.csv','w',newline='') as f:
        chompa = csv.writer(f,dialect='excel')
        for r in backend.show():
            chompa.writerow(r)
    messagebox.showinfo("File Saved","Saved as " + var +".csv")

def  save_file():
    pop =Toplevel(win)
    pop.geometry('200x80')
    var = StringVar()
    ll =Label(pop,text='Save the file name as').pack()
    ent=ttk.Entry(pop,textvariable=var).pack()
    butt=ttk.Button(pop,text='Done',width=20,command=lambda:fun(var.get()))
    butt.pack()

    




# --------------root widgets----------------------------------------------------------------------

a=Label(win,text='First Name :',pady=7,padx=10)
a.grid(row=0,column=0)
fname=StringVar() 
e=ttk.Entry(win,width=30,textvariable=fname)
e.grid(row=0,column=1) 
# -----------------------------------------------------------------

a1=Label(win,text='Last Name :',pady=7,padx=10)
a1.grid(row=0,column=2)
lname=StringVar() 
e1=ttk.Entry(win,width=30,textvariable=lname)
e1.grid(row=0,column=3) 

# -----------------------------------------------------------------
a2=Label(win,text='University Reg Number :',pady=7,padx=10)
a2.grid(row=2,column=2)
reg=StringVar() 
e3=ttk.Entry(win,width=30,textvariable=reg)
e3.grid(row=2,column=3)

# -----------------------------------------------------------------
a3=Label(win,text='University Roll Number :',pady=7,padx=10)
a3.grid(row=2,column=0)
rol=StringVar() 
e2=ttk.Entry(win,width=30,textvariable=rol)
e2.grid(row=2,column=1) 

# -----------------------------------------------------------------
a4=Label(win,text='Current Year :',pady=7,padx=10)
a4.grid(row=1,column=0)
bochor= IntVar() 
e4=ttk.Combobox(win,value=[1,2,3,4],textvariable=bochor)
e4.grid(row=1,column=1)

# def lol(event):
#     print(bochor.get())

# e4.bind("<<ComboboxSelected>>",lol)

# --------------------------------------------------------------------
a7=Label(win,text='Phone no.',pady=7,padx=10)
a7.grid(row=1,column=2)
phone= IntVar()
e5=ttk.Entry(win,width=30,textvariable=phone)
e5.grid(row=1,column=3) 
# --------------------------------------------------------------------
frame =LabelFrame(win,text='Sex')
frame.grid(row=0,rowspan=3,column=4)  

sex=StringVar()
sex.set('F')
ttk.Radiobutton(frame,text='F (Female)',variable=sex,value='F').pack()
ttk.Radiobutton(frame,text='M  (Male)',variable=sex,value='M').pack()
ttk.Radiobutton(frame,text='Others',variable=sex,value='Others').pack()

# --------------tree view------------------------------------------------------
tree=ttk.Treeview(win,height=12)
tree['columns']=('fname','lname','reg','rol','sex','phn','ear')
    # column formatting 
tree.column('#0',width=0,stretch=NO)
tree.column('fname',anchor=W,width=130)
tree.column('lname',anchor=W,width=130)
tree.column('reg',anchor=W,width=150)
tree.column('rol',anchor=W,width=150)
tree.column('ear',anchor=W,width=110)
tree.column('phn',anchor=W,width=130)
tree.column('sex',anchor=W,width=90)
    # tree heading 
tree.heading("#0",text='',anchor=W)
tree.heading("fname",text='First Name',anchor=W)
tree.heading("lname",text='Last Name',anchor=W)
tree.heading("reg",text='University Reg number',anchor=W)
tree.heading("rol",text='University Roll number',anchor=W)
tree.heading("sex",text='Sex',anchor=W)
tree.heading("phn",text='Phone number',anchor=W)
tree.heading("ear",text='Current Year',anchor=W)
tree.grid(row=3,column=0,rowspan=15,columnspan=5)

tree.bind("<ButtonRelease-1>",dhor)

 # ---------------------------BUTTONS----------------------------------------

 #--Search-----
nebo= StringVar()
nebo.set('Search By...')
choose =['First Name','Last Name','Registration number','Roll number','Sex','Phone number','Year']
nebo1=ttk.Combobox(win,value=choose,textvariable=nebo)
nebo1['state']='readonly'

nebo1.grid(row=0,column=5)
nebo0=StringVar()
nebo2=ttk.Entry(win,textvariable=nebo0)
nebo2.grid(row=1,column=5)

nebo3=ttk.Button(win,text='Search',width=20,command=lambda:search(nebo.get()))
nebo3.grid(row=2,column=5)

b=ttk.Button(win,text='Add info',width=20,command=addinfo)
b.grid(row=9,column=5)
b0=ttk.Button(win,text='Refresh',width=20,command=refresh)
b0.grid(row=10,column=5)
b1=ttk.Button(win,text='Delete',width=20,command=dell)
b1.grid(row=16,column=5)
b2=ttk.Button(win,text='Clear text',width=20,command=clean)
b2.grid(row=11,column=5)
b3=ttk.Button(win,text='Update',width=20,command=updatekor)
b3.grid(row=12,column=5)
b4=ttk.Button(win,text='View All',width=20,command=viewall)
b4.grid(row=13,column=5)
b6=ttk.Button(win,text='Enter Marks',width=20,command=marks)
b6.grid(row=14,column=5)
b7=ttk.Button(win,text='Clean Table',width=20,command=removeall)
b7.grid(row=15,column=5)

b5=ttk.Button(win,text='Close',width=20,command=win.destroy)
b5.grid(row=17,column=5)

# --------------------right click popup menu----------

menu=Menu(win,tearoff=False)
menu.add_command(label="Refresh Table",command=refresh)
menu.add_separator()
menu.add_command(label="Clear texts",command=clean)
menu.add_command(label="Remove All",command=removeall)
menu.add_command(label="Insert",command=addinfo)
menu.add_command(label="Show All",command=viewall)
menu.add_separator()
menu.add_command(label="Exit",command=win.destroy)
win.bind("<Button-3>",popup)

# -------------------hover guide-------from tix module--------------------------
# tip= Balloon(win)
# tip.bind_widget(b,balloonmsg="Insert student info into the database")
# tip.bind_widget(b1,balloonmsg="Delete selected row")
# tip.bind_widget(b2,balloonmsg="clear all entry fields")
# tip.bind_widget(b3,balloonmsg="update info to the database")
# tip.bind_widget(b5,balloonmsg="Exit program")
# tip.bind_widget(b7,balloonmsg="Clean Table")
# tip.bind_widget(b4,balloonmsg="Show what's in the database")

# ------file menu---------------------------------------------------------

file= Menu(win)
filemenu=Menu(file,tearoff=0)
filemenu.add_command(label="Create Database")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Export File")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=win.quit)
file.add_cascade(label="File",menu=filemenu)

edit=Menu(file,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
file.add_cascade(label="Edit",menu=edit)

win.config(menu=file)
# ---------------------------------------------------------------

win.mainloop()