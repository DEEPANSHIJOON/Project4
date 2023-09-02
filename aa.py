num=int(input("enter the decimal number  "))
count=0
while(num>0):
    a=num%2
    count+=1
    num=num//2

print("no of bits in the given number are :  ",count)