"""f=open("C:/Users/dell/Desktop/Python files/Files/hello.txt","w")
f.write("congratulations for your new job as junior data scientist")
f.close()"""

"""f=open("C:/Users/dell/Desktop/Python files/Files/hello.txt","a")
f.write("Hello nkita!You are such a blessed soul")
f.close()"""

f=open("C:/Users/dell/Desktop/Python files/Files/hello.txt","a")
f.write("Hello nkita!You are such a blessed soul")
f.close()
f1=open("C:/Users/dell/Desktop/Python files/Files/hello.txt","r")
data=f1.read()
print(data)
f.close()
