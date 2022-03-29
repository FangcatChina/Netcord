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
                -users.cfg
                -join.cfg
                -role.cfg
                -Channels
                    -[(Channel Name)blablabla]
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
def Connect(web,username,password):
    try:
        try:
           lanusers = open(web+"/NetcordServices/userlist.cfg",'r')
        except:
            return 404
        if username+"$"+password in lanusers.readlines():
            lanusers.close()
            return 200
        else:
            lanusers.close()
            return 500
    except:
        return 404