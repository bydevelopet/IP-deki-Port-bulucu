#Bydevelopet 28.08.2014
import socket
import thread
import time
import os
_bt=time.time()
IP=""
_port=[1,65535]
_thread=128 # Aynı Anda Port Arıcak İşlem Sayısı
_tpc=[]
i=_port[1]
e=_port[1]/_thread

class _Rophl(object):
    def __init__(self):
        self.bitti=0
        self.Bulunanlar=[]
        self.Threads={}
Rophl=_Rophl()
if i>=_thread:
    for t in range(_thread):
        #e=_port[1]/_thread
        #print e
        ilk=e*t
        son=((t+1)*e)-1
        if t+1==_thread:
            son=_port[1]-1
        _tpc.append([ilk,son])
        
        #print i
##        _tpc.append(i)

##for i,tpc in enumerate(_tpc):
##    ilk=tpc[0]
##    son=tpc[1]
##    print ilk
##    print son
##    print "*"*80
#os._exit(0)
def port_bul(portsayisi,isim):
    for p in range(portsayisi[0],portsayisi[1]):
        #Rophl.ilerleme+=1
        p+=1
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1) # 0.5 yaparsanız daha hızlı biter ama bulmama ihtimali olabilir 1 kesindir
            if True:
                sock.connect((IP,p))
                #print "*"*80
                print "Bulundu : "+str(p)
                #print "*"*80
                Bulunanlar.append(str(p))
        except:#pass
            if p%10000==0:
                pass#print p #her 10000 portda bir gösterir açık portlarla karıştılabilirlir bu yüzden silindi
                
            #print p
    
    Rophl.Threads[isim]=1
    #print (Rophl.Threads)

for i,tpc in enumerate(_tpc):
    #Rophl.Threads["Thread-"+str(i)]=0
    thread.start_new_thread(port_bul, (tpc,"Thread-"+str(i)) )
    
while True:
    time.sleep(5)
    ### Daha Bitmedi
    #if Rophl.bitti==_thread:
    #    print "Bitti"
    #    for i,port in enumerate(Rophl.Bulunanlar):
    #        print str(i+1)+ " - "+port
    #    time.sleep(6000)
    #    break
    
