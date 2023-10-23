from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser

root = Tk()
root.maxsize(650,650)
root.minsize(650,650)

root.configure(background="blue")

open_img = ImageTk.PhotoImage(Image.open('open.png'))
save_img = ImageTk.PhotoImage(Image.open('save.png'))
run_img = ImageTk.PhotoImage(Image.open('run.png').resize((30,30)))

lbl_file = Label(root, text="File name")
lbl_file.place(relx=0.28, rely=0.03, anchor= CENTER)

input_file = Entry(root)
input_file.place(relx=0.46, rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5, rely=0.55, anchor= CENTER)


name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file.delete(0, END)
    
    file = filedialog.askopenfilename(title=" Open Html File", filetypes=(("HTML Files", "*.html"),))
    print(file)
    name = os.path.basename(file)
    print(name)
    fname = name.split('.')[0]
    print(fname)
    input_file.insert(END, fname)
    root.title(fname)
    html_file = open(name, 'r')
    
    para=html_file.read()
    my_text.insert(END, para)
    html_file.close()
    
def save():
    input_name = input_file.get()
    file = open(input_name+".html", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def run():
    global name
    webbrowser.open(name)
    
save_btn=Button(root,image=save_img, command=save)
save_btn.place(relx=0.11, rely=0.03,anchor=CENTER)

run_btn=Button(root,image=run_img, command=run)
run_btn.place(relx=0.17, rely=0.03,anchor=CENTER)
   

open_btn=Button(root, image=open_img,command = openFile)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)



root.mainloop()