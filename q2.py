s1 = int(input("enter marks of sub 1 : "))
s2 = int(input("enter marks of sub 2 : "))
s3 = int(input("enter marks of sub 3 : "))
sum = s1+s2+s3
per = sum/300*100
print(per)
if(per>40):    
    if(s1>35 and s2>35 and s3>35):
        print("pass")
    else:
        print("fail")
elif(per<40):

     print("fail")


