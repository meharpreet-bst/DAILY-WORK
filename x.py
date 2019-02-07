import subprocess as sp
import json
import string

dict_client={}
dict_client1={}
def output(val):
    if val=='n':
        with open('reg1.json', 'a') as file:
            file.write(json.dumps(dict_client))
        print("file written")
    
    else:
        val='y'
        with open('reg2.json', 'a') as file:
                file.write(json.dumps(dict_client1))
        print("file written")	
	
            
def fetch(regp,l):
    if l=='n':  
        type = sp.check_output('REG QUERY '+ regp )
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
        
		
    if l=='y':
        type = sp.check_output('REG QUERY '+ regp )
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
        
		
def difference(a,b):
    for key1 in a:
        for key2 in b:
          if key1== key2:
            if a[key1] == b[key2]:
                key1 = str(key1)
                a[key1] = str(a[key1])
                b[key2] = str(b[key2])
                with open('reg1.txt', 'a') as file:
                    file.write('\n'+ key1.strip()+ '\t')
                    file.write(a[key1].strip())
                    file.write('\t')
                    file.write(b[key2].strip())
                    file.write('\t')
                    file.write("matched \n")
            
            else:
                key1 = str(key1)
                a[key1] = str(a[key1])
                b[key2] = str(b[key2])
                with open('reg1.txt', 'a') as file:
                    file.write('\n'+ key1.strip()+ '\t')
                    file.write(a[key1].strip())
                    file.write('\t')
                    file.write(b[key2].strip())
                    file.write('\t')
                    file.write("No match \n")

def hex(stri):
    hexdec= char(stri)
    dec= int(hecdec, 16)
    d= str(dec)
    print(str(dec))
    return d	
 
	
def webtable(x,y):
    try:
        strtable= '<html><table border="1"><tr><th>KEY</th><th>VALUE1</th><th>VALUE2</th><th>TEST</th></tr>'
        for key1 in x:
            for key2 in y:
                if key1==key2 and "Base64GuidString" in key1:
                    pass
                elif key1==key2:					
                    str= "<tr><td>"
                    str1= "</td><td>"
                    if x[key1]==y[key2]:
                        st= "PASS"
                        xx= '</td><td bgcolor="GREEN">'
                    else:
                        st="FAIL"
                        xx= '</td><td bgcolor= "RED">'
                    strtable= strtable+ str+ key1+ str1+ x[key1]+ str1+ y[key1]+ xx+ st+ "</td></tr>"	
                
                elif key1 in x and key1 not in y and "Base64GuidString" not in key1:
                    str= "<tr><td>"
                    str1= "</td><td>"
                    strtable= strtable+ str+ key1+ str1+ x[key1]+ str1+ ""+ '</td><td bgcolor="RED">'+ ""+ "<td></tr>"
                    break
        for key1 in y:
            for key2 in x:
                if key1 in y and key1 not in x and "Base64GuidString" not in key1:
                    str= "<tr><td>"
                    str1= "</td><td>"
                    strtable= strtable+ str+ key1+ str1+ ""+ str1+ y[key1]+ '</td><td bgcolor="RED">'+ ""+ "<td></tr>"
                break
					
        strtable+= "</table></html>"
        f= open("table.html",'w')
        f.write(strtable)  
        print(strtable)
	
    except Exception as e:
        print("error")

    
	
A={}
B={} 
path=input("Enter path of registry: ")
type(path) 
choice=input("updated?? (y/n)")
type(choice)
if choice=='n': 
    fetch(path,choice)
    #output(choice)
    with open("reg1.json") as f:
        A=json.load(f)
    choice=input("updated?? (y/n)")
    type(choice)
    if choice=='y':
        fetch(path,choice)
        #output(choice)
        with open("reg2.json") as fl:
            B=json.load(fl)
    else:
        print("finished")

#difference(A, B)
webtable(A,B)
    

	



    



