a = {4,5,6,89,5}         # it is a set i.e collection of non repetitive element.
print(a)
a = {}  # creates empty dictionary
print(a)
print(type(a))
b = set()           # creates empty set
print(type(b))
# adding elements to the empty set
b.add(4)
b.add(5)
print(b)
b.add((4,78,78))    #tuple can be added to a set
print(b)
#b.add([5,6,7,12])    #list and dict cannot be added to the set since the contents of list and dict can be changed.
#print(b)
#print(len(b))   #Displays the length of the set.
#b.remove(5) #removes the element from the set
#b.remove(15) #returns error
#print(b)
#sets doesn't have index and is unordered.Also, the elements of sets cannot be changed.
#b.pop()    #removes arbitrary element from the set and returns it
#print(b)
#b.clear( )    #empties the set.
#print(b)   
b.intersection({9,6}) 
print(b)





