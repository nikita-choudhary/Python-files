import random
def game(c,b):
    if c=="s" and b=="w":
        return "you are the winner"
    elif c=="s" and b=="g":
        return "you are the winner"
    elif c=="w" and b=="s":
        return "computer is the winner"
    elif c=="w" and b=="g":
        return "computer is the winner"
    elif c=="g" and b=="s":
        return "computer is the winner"
    elif c=="g" and b=="w":
        return "you are the winner"
    else:
        return "tie"
print("computer turn: ")
random_no= random.randint(1,3)
if random_no==1:
    c="s"
    #print(c)
elif random_no==2:
    c="w"
    #print(c)

else:
    c="g"
    #print(c)

b=input("your turn : ")
print(f"computer chose {c}")
print(f"you chose {b}")
print(game(c,b))