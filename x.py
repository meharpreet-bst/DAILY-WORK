import subprocess as sp
import json

dict_client={}
dict_client1={}
def output(val):
    if val=='n':
        with open('reg1.txt', 'w') as file:
            for k,v in dict_client.items():
                file.write(json.dumps(k+ '--'+ v))
        print("file written")
    
    else:
        val='y'
        with open('reg2.txt', 'w') as file:
            for k,v in dict_client1.items():
                file.write(json.dumps(k+ '--'+ v))
        print("file written")	
	
            
def fetch(l):
    if l=='n':  
        type = sp.check_output('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks\Client"')
        type= str(type)
        keys= type.split("\\r\\n")
        a=[]
        b=[]
        for item in keys:
            if 'REG_SZ' in item:
                a= item.split("REG_SZ")
                dict_client[a[0]]=a[1]		

            elif 'REG_DWORD' in item: 
                b= item.split("REG_DWORD")
                dict_client[b[0]]=b[1]
        print("old version \n")
        for k,v in dict_client.items():
            print(k+ '--'+ v)
        return dict_client
		
    if l=='y':
        type = sp.check_output('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks\Client"')
        type= str(type)
        keys= type.split("\\r\\n")
        a=[]
        b=[]
        for item in keys:
            if 'REG_SZ' in item:
                a= item.split("REG_SZ")
                dict_client1[a[0]]=a[1]		

            elif 'REG_DWORD' in item: 
                b= item.split("REG_DWORD")
                dict_client1[b[0]]=b[1]
        print("new version \n")
        for k,v in dict_client1.items():
            print(k+ '--'+ v)
        return dict_client1
		
def difference(a,b):
    for keys in a:
	    for value in b:
          if a[keys][values]!= b[keys][values]:
            print(a[keys][values])
    
	
A={}
B={}
choice=input("updated?? (y/n)")
type(choice)
if choice=='n': 
    A= fetch(choice)
    output(choice)
    choice=input("updated?? (y/n)")
    type(choice)
    if choice=='y':
        B= fetch(choice)
        output(choice)
    else:
        print("finished")
else:
    B= fetch(choice)
    output(choice)
	
difference(A, B)
    

#choice=input("updated?? (y/n)")
#type(choice)

#if choice=='y':	 
    #z= z-1
    #B= fetch(z)
    #output(z)

#else: 
   #print("error")
	



    



