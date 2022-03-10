import pickle
import os

def Operate(demofile):
 file=open(demofile,"rb")
 k=file.read()
 p=pickle.dumps(k)
 ba=bytearray(p)
 filecontent='* '
 sza=0
 for c in ba:
    sza+=1
    k=str(c)
    while len(k)<3:
      k='0'+k
    filecontent=filecontent+k+' '
 filecontent=filecontent+'*'

 filename,file_extension = os.path.splitext(file.name) 
 m=bytearray(filename.encode())
 n=bytearray(file_extension.encode())
 header1='# '
 
 szb=0
 szc=0
 for c in m: # traverse the string 
    szb+=1
    k=str(c)
    while len(k)<3:
      k='0'+k
    header1=header1+k+' '
 header1=header1+'#'
 
 for c in n: # traverse the string 
    szc+=1
    k=str(c)
    while len(k)<3:
      k='0'+k
    header1=header1+k+' '
 header1=header1+'# '
 con=filecontent+header1

 return str(con)
