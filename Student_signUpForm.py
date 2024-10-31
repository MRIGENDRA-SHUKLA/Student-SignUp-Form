from tkinter import*

root=Tk()
root.geometry("300x300") 
root.title("Student Sign Up Form") 

Label(root,text="Name:",font=("",10,"bold")).grid(row=0,column=0)

e1=Entry(root)
e1.grid(row=0, column=1)

Label(root,text="DOB:",font=("",10,"bold")).grid(row=1,column=0)

e2=Entry(root)
e2.grid(row=1, column= 1)


###--- Gender RadioButton


Label(root,text="Gender:",font=("",10,"bold")).grid(row=2,column=0)

r1 = Radiobutton(root,text="Male",value=1,font=("",10,"bold")).place(x=60, y= 42)

r2 = Radiobutton(root,text="Female",value=2,font=("",10,"bold")).place(x=115, y= 42)

###--------------------------------------

Label(root,text="Course:",font=("",10,"bold")).grid(row=3,column=0)


##----- *options Button 
def select(n):
    print(var.get(),n)


options=['Data Analytics', 'Data Science', 'Full Stack','Business Analytics','Digital Marketing' ]
var=StringVar()
op=OptionMenu(root,var, *options , command=select).grid(row=3, column= 1)

var.set("Select Your Course:")

###-------------------------------------

Label(root,text="Email:",font=("",10,"bold")).grid(row=5,column=0)

e5=Entry(root)
e5.grid(row=5, column= 1)


### -- Address:/ TEXT FIELD 
Label(root,text="Address:",font=("",10,"bold")).grid(row=6,column=0)

e6=Text(root,height=3,width=15)
e6.grid(row=6, column= 1)

# ####------------------------------------------------

# ## -- MessageBox
from tkinter import messagebox

def Sign_In():
    name = e1.get().strip()
    DOB = e2.get().strip()
    Email= e5.get().strip()
   
    if name and DOB and Email :
        messagebox.showinfo("Info", "Sign In Successfully")
    else:
        messagebox.showerror("Error", "Fill block !!!")

Button(root, text="Sign In",bg="Grey", command=Sign_In, font=("", 10, "bold")).grid(row=7, column=1)

root.mainloop() 

