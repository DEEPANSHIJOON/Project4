n =int(input("Enter the no whose factorial is to be find: "))
fact=1
if n>0:
    for x in range(1,n+1):
        fact=fact * x
elif n==0:
    fact=1
else:
    print("Please enter an valid input ")
    exit()
print("The factorialof ", n, "is : ")
print(fact)
