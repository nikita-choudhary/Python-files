#n= int(input("Enter the no. "))
for i in range(1,4):
    if i%2==0:
        print("*"*(i-1), end="")
        print(" "*(i-1),end="")
        print("*"*(i-1))
    else:
            print("*"*3)

