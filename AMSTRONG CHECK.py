num = int(input("enter a no you want to check for an amstrong no."))
sum_ = 0
temp = num
a = 0
while temp > 0:
    a = a+1
    temp //= 10
temp = num
while temp > 0:
    rem = temp % 10
    sum_ += rem ** a
    temp //= 10
if num == sum_:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
