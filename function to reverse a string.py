# Reversing a string using slicing
def reverse(st):
    st1=st[::-1]
    return st1

#Reversing a string using for loop
def revfor(str):
    i=len(str)
    j=""
    for x in range(i,0,-1):
        j=j+str[x-1]
    return j


k = "WELCOME Mr. STARK"
print(k)
print(reverse(k))          # Calling the function which used slicing
print(revfor(k))          # Calling a function
