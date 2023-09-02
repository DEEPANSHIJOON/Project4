def func(value):
    temp=value[::-1]
    a=0
    b=0
    while(int(value)>0):
        b=int(value)%10
        a=int(temp)%10
        print(a)
        value=0
        return a+b
val=input("enter the value")
print(func(val))