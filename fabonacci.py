a=1
b=0
n=int(input('Enter the no. of elements must be in fabonacci series'))
for i in range (0,n):
    c=a+b
    a=b
    b=c
    print(c,end=' ')