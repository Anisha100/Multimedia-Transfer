import pickle
import array as arr

def rev(k):

    filecontent=''
    filename=''
    filecontents=''
    for c in k:
        count=0
        count1=0
        count2=0
        while count!=2:
            filecontent=filecontent+k
            if c=="*":
             count+=1
        
        while count1!=2:
            filename=filename+k
            if c=="#":
                count+=1
        while count2!=2:
            file_ext=file_ext+k
            if c=="#":
                count2+=1
    filecontent=filecontent.remove("*")
    filename=filename.remove("#")
    file_ext=file_ext.remove("#")
    m=[filecontent[c:c+3] for c in range(0, len(filecontent), 3)]
    ba=arr.array(int(m))
    n=[filename[b:b+3] for b in range(0, len(filename), 3)]
    ba1=arr.array(int(n))
    o=[filecontent[a:a+3] for a in range(0, len(file_ext), 3)]
    ba2=arr.array(int(o))
    o=pickle.loads(o)
    mn=str(m)
    nm=str(n)
    with open(mn+nm,"wb") as file:
     file.write(o)
 
    return file

        

    