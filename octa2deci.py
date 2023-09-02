def OctalDecimal(num, i):
    if num >=0 and num <= 7:
        return num*pow(8, i)

    last_digit = num % 10
    return (pow(8, i) * last_digit) + OctalDecimal(num // 10, i+1)

def enterno():
    x = input("enter a octal no :")
    y = list(x)
    z=["0","1","2","3","4","5","6","7"]
    n = 0
    for i in y:
        if i in z:
            n+=1
    if n<len(y):
        print("invalid input")
        return(enterno())
    else:
        return int(x)


print('The decimal value is =', OctalDecimal(enterno(), 0))
