#Netcord
#Author:ZiXian Fang
#A LAN chat app powered by Python 3.6(or upper)
from tkinter import *
from ncore import *
login = Tk()
login.config(bg='black')
logobig = PhotoImage(file='Netcord Dark.png')
lgshow = Label(login,image=logobig,bd=0)
lgshow.grid(row=0,column=0,columnspan=2)
sname = Label(login,text="服务器地址",fg='white',bg='black')
sname.grid(row=1,column=0)
uname = Label(login,text="用户名",fg='white',bg='black')
uname.grid(row=2,column=0)
psd = Label(login,text="登录密码",fg='white',bg='black')
psd.grid(row=3,column=0)
servern = Entry(login,bg='black',fg='white')
servern.grid(row=1,column=1,pady=5)
usern = Entry(login,bg='black',fg='white')
usern.grid(row=2,column=1,pady=5)
passwd = Entry(login,bg='black',fg='white')
passwd.grid(row=3,column=1,pady=5)
def logandconnect():
    global SERVER
    if Connect(servern.get(),usern.get(),passwd.get()) == 200:
        SERVER=servern.get()
        login.destroy()
    else:
        pass
logbutton = Button(login,text="登录",bg='green',command=logandconnect,fg='white',width=20)
logbutton.grid(row=4,column=0,columnspan=2)
login.mainloop()
main = Tk()
srvers = Frame(main)
srvers.pack(side=LEFT)
for i in getServerListOnLAN(SERVER):
    pass
main.mainloop()