print(' project ')

######################  Imports
import tkinter
import json
islogin=False
login_user=""
dct={"admin":"123456789"}

######################  Functions code
def login():
    global islogin,login_user,result,dct
    username=txt_user.get()
    password=txt_pass.get()
##    print(username,password)
    if(islogin==True):
        result=' You are already log in '
        lbl3.configure(text=result)
        return
    try:
        with open('users.json') as f:
            dct=json.load(f)
    except FileNotFoundError:
        with open('users.json','w') as f:
            json.dump(dct,f)
        print('somthing went wrong,now your backup file is ready')
##        print(dct)
    if((username in dct) and (dct[username]==password)):
        islogin=True
        login_user=username
        result=(username,'welcome to your account')
        lbl3.configure(text=result)
    else:
        result=' Wrong username or password '
        lbl3.configure(text=result)
def submit():
    global islogin,login_user,result,dct
    if(islogin==True):
        result=' You should log out first '
        lbl3.configure(text=result)
        return
    username=txt_user.get()
    password=txt_pass.get()
    if(len(username)<4):
        result="User have to biger than 4char "
        lbl3.configure(text=result)
        return
    if(len(password)<8):
        result="Your password is too short ! "
        lbl3.configure(text=result)
        return
    try:
        with open('users.json') as f:
            dct=json.load(f)
    except FileNotFoundError:
        with open('users.json','w') as f:
            json.dump(dct,f)
        print('somthing went wrong,now your backup file is ready')
        print(dct)
    if(username in dct):
        result=" username already exist!!! "
        lbl3.configure(text=result)
        return
    dct[username]=password
    with open("users.json",'w') as f:
        json.dump(dct,f)
    result="submit succesfully"
    lbl3.configure(text=result)
def logout():
    global islogin,login_user,result,dct,lst
    if(islogin==True):
        islogin=False
        login_user=""
        lstbx.delete(0,tkinter.END)
        result="Have a nice time"
        lbl3.configure(text=result)
    else:
        result="Absolutly but First of all,log in"
        lbl3.configure(text=result)
def delete_account():
    global islogin,login_user,result,dct
    if(islogin==False):
        result="Absolutly but First of all,log in"
        lbl3.configure(text=result)
        return
    if(login_user=="admin"):
        result="Admin account is not removable!"
        lbl3.configure(text=result)
        return
    with open("users.json") as f:
        dct=json.load(f)
    dct.pop(login_user)
##    print(dct)
    with open('users.json','w') as f:
        json.dump(dct,f)
    result='Account have been deleted'
    lbl3.configure(text=result)
    islogin=False
    login_user=""
    return
def users_list():
    global islogin,login_user,result,dct
    if(login_user!="admin"):
        result="Access denied"
        lbl3.configure(text=result)
        return
    with open("users.json") as f:
        dct=json.load(f)
    lst=[]
    for user in dct:
        lst.append(user)
    lstbx.insert('end', lst)
##        result=user
##        lstbx.insert('end',user)
    result='List printed'
    lbl3.configure(text=result)
  
def change_password():
    global islogin,login_user,result,dct
    def Confirmation():
        global islogin,login_user,result,dct
        password=txt_pass.get()
        old_pass=txt_Op.get()
        New_pass=txt_Np.get()
        New_passa=txt_Npa.get()
        if(password!=old_pass):
            result='password incorrect'
            lbl3.configure(text=result)
            return
        if(New_pass!=New_passa):
            result='password incorrect'
            lbl3.configure(text=result)
            return
        with open("users.json") as f:
            dct=json.load(f)
        dct[login_user]=New_passa
        with open('users.json','w') as f:
            json.dump(dct,f)
        result='Password change succesfully'
        lbl3.configure(text=result)
        islogin=False
        login_user=""
        win.destroy()
        return
    if(islogin==False):
        result="Absolutly but First of all,log in"
        lbl3.configure(text=result)
        return
    win=tkinter.Tk()
    win.title('Confirmation')
    win.config(bg="forest green")
    win.geometry('300x300+500+100')
    win.resizable(0,0)
    lbl=tkinter.Label(win,text='Old password : ',bg="black",fg="white",font=("Arial",12))
    lbl.pack()
    txt_Op=tkinter.Entry(win,width=40)
    txt_Op.pack()
    lbl1=tkinter.Label(win,text='New password : ',bg="black",fg="white",font=("Arial",12))
    lbl1.pack()
    txt_Np=tkinter.Entry(win,width=40)
    txt_Np.pack()
    lbl2=tkinter.Label(win,text='New password again : ',bg="black",fg="white",font=("Arial",12))
    lbl2.pack()
    txt_Npa=tkinter.Entry(win,width=40)
    txt_Npa.pack()
    btn=tkinter.Button(win,text="Confirm",width=15,command=Confirmation)
    btn.pack()
    
    win.mainloop()
##    new_pass=input("please enter your new password!")
##    with open("users.json") as f:
##        users=json.load(f)
##    users[login_user]=new_pass
##    with open("users.json",'w') as f:
##        json.dump(users,f)
##    print("your password changed!")

######################  Windows Design
win=tkinter.Tk()
win.title('project')
win.config(bg="powder blue")
win.geometry('1100x650+100+10')
win.resizable(0,0)

######################   Label  Design
lbl=tkinter.Label(win,text='User Name : ',bg="black",fg="white",font=("Arial",12))
lbl.grid(column=1,row=2,padx=10,pady=10)

lbl2=tkinter.Label(win,text='Password : ',bg="black",fg="white",font=("Arial",12))
lbl2.grid(column=1,row=5,padx=10,pady=10)

lbl3=tkinter.Label(win,text="",width=25,bg="black",fg="yellow",font=("Arial",20))
lbl3.grid(column=8,row=2,padx=10,pady=10)

######################  TextBox Design
txt_user=tkinter.Entry(win,width=40)
txt_user.grid(column=2,row=2,padx=10)

txt_pass=tkinter.Entry(win,width=40)
txt_pass.grid(column=2,row=5,padx=10)

######################   Bottun  Design
btn=tkinter.Button(win,text="Log In",width=15,command=login)
btn.grid(column=1,row=10,padx=10,pady=50)

btn2=tkinter.Button(win,text="Submit",width=15,command=submit)
btn2.grid(column=2,row=10,padx=10,pady=50)

btn3=tkinter.Button(win,text="Log Out",width=15,command=logout)
btn3.grid(column=3,row=10,padx=10,pady=50)

btn4=tkinter.Button(win,text="Delete Account",width=15,command=delete_account)
btn4.grid(column=1,row=11,padx=10)

btn5=tkinter.Button(win,text="Users List",width=15,command=users_list)
btn5.grid(column=2,row=11,padx=10)

btn6=tkinter.Button(win,text="Change Password",width=15,command=change_password)
btn6.grid(column=3,row=11,padx=10)

######################   ListBox  Design
lstbx=tkinter.Listbox(win,height=8,width=71,bg="black",fg="white",font=("Arial",20))
lstbx.grid(columnspan=20,padx=10,pady=100)

win.mainloop()
