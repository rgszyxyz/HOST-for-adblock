import os

with open("dnsmasq.conf.add") as file:
    for f in file:
        domain=f.split("/")[1]
        #print (domain)
        #flag = os.system('ping -c 2 -w 5 %s'%domain)
        p=os.popen("ping "+domain)
        x=p.read()
        #print(x)
        p.close()
        if x.count('时间<1ms'):
            #print("ping通")
            print(x,end='')

