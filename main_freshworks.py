import threading
from threading import*
import time

p_dict={} #dictionary to store the values and keys
def rightnowkeys():
    print("error occcured")


def key_value_create(k,v,presentTime=0):
    if k in p_dict:
        print("existing")
    else:
        if(k.isalpha()):
            if len(p_dict)<(1024*1024*1024) and v<=(16*1024*1024):#should be lessthan 1GB
                if presentTime==0:
                    l=[v,presentTime]
                else:
                    l=[v,time.time()+presentTime]
                if len(k)<=32:
                    p_dict[k]=1
            else:
                print("limit crossed")
        else:
            print("give proper key")

#Threading operations
t1=Thread(target=key_value_create,args=(1,))
t1.start()
time.sleep(2)

