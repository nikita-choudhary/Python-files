"""name=input("enter the name:")

def f1():          #defined the function.
    #print("Hello  "+ name)
    p=print("hello "+name)
    return p  #without mentioning p the result get executed.and
f1()    #calling the function
"""
"""def greet(name):
    print("hello "+name)
greet("nikita")
"""
"""def summ(n1,n2):
    return n1+n2
#s= summ(5,6)
print(summ(5,6))"""

def rec(n):
    if n==1 or n==0 :
        return 1
    else:
        return n* rec(n-1)
print(rec(5))