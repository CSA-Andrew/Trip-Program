from tkinter import *
from tkinter import ttk
import math
def donothing():
    try:
        file = open("travellog.txt", "a")
        file.write('\n')
        lfirst = (l.curselection())
        file.write(l.get(lfirst, None))
        file.write('\n')
        file.write(shipping.get())
        file.write('\n')
        file.write(spin2.get())
        file.write('\n')
        file.write(notesentry.get())
        file.close()
        filewin = Toplevel(root)
        stuff = Label(filewin, text="Your travel has been logged.")
        stuff.pack()
        button = Button(filewin, text="Close", command=filewin.destroy)
        button.pack()
    except:
        error = Toplevel(root)
        msg = Label(error, text="There was an error with your entry,")
        msg.pack()
        msg2 = Label(error, text="please make sure to fill each box.")
        msg2.pack()
        bb1=Button(error, text="Close", command=error.destroy)
        bb1.pack()
def about():
    aboutb = Toplevel(root)
    description = Label(aboutb, text="This program is an example of a trip guide application.")
    description.pack()
    bb = Button(aboutb, text="Close", command=aboutb.destroy)
    bb.pack()
def clear():
    l.selection_clear(0, END)
    shipping.set("")
    notesentry.delete(0, END)
    spin2.delete(0, END)
root = Tk()
dumbcountrylabelthatisntneeded = Label(text="Countries")
dumbcountrylabelthatisntneeded.grid(row=1, column=0)
menubar = Menu(root) #first menu defined, add all the parts
filemenu = Menu(menubar, tearoff=0) #says it is at the menubar, we have not defined yet
filemenu.add_command(label="Save", command=donothing)
#add separator, usually to focus on something or to make it seem separate from other commands
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#this actually adds the cascade, and you say what is in it. Think of it like a frame
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
shippingitems = "Air", "Foot", "Train", "Bus", "Car", "Water"
shipping = ttk.Combobox(height=1, width=16, value=shippingitems)
shipping.grid(row=0, column=0, sticky=NSEW)
items_lst = ["U.S.A.", "Germany", "China", "India", "Bangladesh", "North Korea", "South Korea", "Japan", "Bermuda", "Somalia", "Haiti", "Uganda", "Wakanda", "Mexico", "Siberia"]
items=StringVar(value=items_lst)
l = Listbox(root, height=10, listvariable=items)
l.grid(column=0, row=2, sticky=NSEW)
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=2, sticky=NSEW)
submit = Button(text="Submit", command=donothing)
submit.grid(column=0, row=4, sticky=NSEW)
clr = Button(text="Clear", command=clear)
clr.grid(column=1, row=4, sticky=NSEW)
l['yscrollcommand'] = s.set
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(10, weight=1)
noteslabel = Label(text="Notes")
noteslabel.grid(column=2, row=1, sticky=NSEW)
notesentry = Entry(text="")
notesentry.grid(column=2, row=2, ipady=70, sticky=NSEW)
pricev=IntVar()
pricelabel= Label(textvariable=pricev)
options1=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
spin2 = Spinbox(root, values=options1, wrap=True)
spin2.delete(0, END)
spin2.grid(row=3, column=0, sticky=NSEW)
g = ttk.Sizegrip(root)
g.grid(row=999, column=999, sticky=SE)


def price():
    pass



root.title("Pricing Calculator")
root.config(menu=menubar)
root.mainloop()