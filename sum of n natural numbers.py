n = int(input("enter the no till which you want to find the sum of natural no."))
add = 0
for x in range(0, n+1):
    add = add + x
print("sum of first ", n, "natural numbers is ", add)
