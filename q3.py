text = input("enter the text ")
spam = False
if("click now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("make a lot of money" in text):
    spam = True
else:
    spam = False
if(spam):
    print("this is spam")
else:
    print("this is not spam")