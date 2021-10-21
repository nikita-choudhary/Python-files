n = int(input("enter the no. : "))
prime = True
for i in range(2,n):
    fact= n%i
    if(fact==0):
        prime = False

if(prime):
    print("this is a prime no.")
else:
    print("not a prime no.")
