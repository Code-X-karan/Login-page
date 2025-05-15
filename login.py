from tkinter import *
login_page=Tk()
login_page.title("Login Page")
login_page.geometry("570x400")
login_page.minsize(570,400)
login_page.maxsize(570,400)
Label(login_page,text="USER LOGIN",font=("rockwell",18,"bold"),bg="blue",fg="white",).pack(fill="x",pady=50)

##frame declare
frame=Frame(login_page)
frame.pack(anchor="nw",padx=120)

##declare input variables
user_id=StringVar()
password=StringVar()

## declare main points and take inputs
Label(frame,text="USERNAME  ",font=("cosmicssans",11,"bold")).grid(row=0,column=0,pady=10)
Entry(frame,textvariable=user_id).grid(row=0,column=1)
Label(frame,text="PASSWORD  ",font=("cosmicssans",11,"bold")).grid(row=1,column=0)
Entry(frame,textvariable=password,show="*").grid(row=1,column=1)

##declare result label
result_label = Label(frame, font=("cosmicssans", 12, "bold"))
result_label.grid(row=3,column=1)

##button functions
def login():
    acc_id="admin"
    SavePassword="admin"
    if(acc_id==user_id.get() and SavePassword==password.get()):

        result_label.config(text="LOGIN SUCCESSFULLY",fg="green")
    else:
        result_label.config(text="INAVLID ATTEMPT",fg="red")

##make button
Button(frame,text="Login",font=("cosmicssans",11,"bold"),command=login).grid(row=2,column=1,pady=10)
login_page.mainloop()