n=int(input("Enter the no.: "))
a_reverse=range(1,11)
reverse_range=reversed(a_reverse)
for i in reverse_range:
    print(f'{n} X {i} = ',(n*i))

    