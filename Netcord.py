#Netcord
#Author:ZiXian Fang
#A LAN chat app powered by Python
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
    global SERVER,login,USERNAME
    if Connect(servern.get(),usern.get(),passwd.get()) == 200:
        SERVER=servern.get()
        USERNAME = usern.get()
        login.destroy()
    else:
        pass
def chating():
    global sv,c,things,out,send,cserver,svn
    cserver = svn[0]
    c = Toplevel()
    c.configure()
    c.title(cserver)
    things = Text(c)
    things.pack(fill=BOTH, expand=False)
    out = Entry(c,bg='black',fg='white')
    out.pack(side=LEFT)
    send = Button(c,text="发送",bg='black',fg='white',command=sendm)
    send.pack(side=LEFT)
    flash()
def flash():
    global cserver,things
    things.delete(0.0,END)
    things.insert('0.0',FlashMessages(SERVER,cserver))
    things.after(500,flash)
def sendm():
    global out,cserver
    SendMessages(SERVER,cserver,USERNAME+":"+out.get())
    out.delete(0,END)
logbutton = Button(login,text="登录",bg='green',command=logandconnect,fg='white',width=20)
logbutton.grid(row=4,column=0,columnspan=2)
login.mainloop()
main = Tk()
main.geometry("600x600")
srvers = Frame(main)
srvers.pack(side=LEFT)
sv = []
svn = []
for i in range(len(getServerListOnLAN(SERVER))):
    svn.append(getServerListOnLAN(SERVER)[i])
    sv.append(Button(srvers,text=getServerListOnLAN(SERVER)[i],bd=1,bg="black",fg='white',command=chating))
    sv[i].pack(side=LEFT)
main.mainloop()