#Ncore
#Author:ZiXian Fang
'''
Codes Returned:
200:OK
404:The server is not available or the server is busy
500:The password is incorrect

The file tree on Netcord Servers:
-NetCord
    -NetcordServices
        -userlist.cfg
        -LANServerList.cfg
        -Servers
            -[(ServerName)blablabla]
                -icon.png   (size must be 100x100)
                -users.cfg  (1.0.5 features)
                -join.cfg   (1.0.5 features)
                -role.cfg   (1.0.5 features)
                -chat.txt
'''
def getServerListOnLAN(web):
    try:
        lanservers = open(web+"/NetcordServices/LANServerList.cfg",'r')
        lst = []
        for i in lanservers.readlines():
            lst.append(i)
        lanservers.close()
        return lst
    except:
        return 404
def joinServer(web,servername,username,psd=None):
    try:
        lanserver = open(web+"/NetcordServices/Servers/"+servername+"/join.cfg",'r')
        if psd == eval(lanserver.readline()):
            av = True
            try:
                j = open(web+"/NetcordServices/Servers/"+servername+"/users.cfg",'a')
            except:
                while av:
                    j = open(web+"/NetcordServices/Servers/"+servername+"/users.cfg",'a')
                    av=False
            j.write(username)
            j.close()
            lanserver.close()
            return 200
        else:
            lanserver.close()
            return 500
    except:
        return 404
def FlashMessages(web,servername):
    #try:
    try:
       chats = open(web+"/NetcordServices/Servers/"+servername+"/chat.txt",'r')
    except:
        a=False
        while a:
            try:
                chats = open(web+"/NetcordServices/Servers/"+servername+"/chat.txt",'r')
                a=True
            except:
                pass
    txt = ''
    for i in chats.readlines():
        txt = txt+i
    chats.close()
    return txt
    #except:
        #return 404
def SendMessages(web,servername,msg):
    try:
        try:
           chats = open(web+"/NetcordServices/Servers/"+servername+"/chat.txt",'a')
        except:
            a=False
            while a:
                try:
                    chats = open(web+"/NetcordServices/Servers/"+servername+"/chat.txt",'a')
                    a=True
                except:
                    pass
        chats.write(msg+"\n")
        chats.close()
    except:
        return 404
def Connect(web,username,password):
    try:
        try:
           lanusers = open(web+"/NetcordServices/userlist.cfg",'r')
        except:
            a=False
            while a:
                try:
                    lanusers = open(web+"/NetcordServices/userlist.cfg",'r')
                    a=True
                except:
                    pass
        if username+"$"+password in lanusers.readlines():
            lanusers.close()
            return 200
        else:
            lanusers.close()
            return 500
    except:
        return 404