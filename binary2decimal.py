def bin2dec(bina):
    if bina == 0:
        return 0
    else:
        return bina%10 +(2 * bin2dec(bina//10))

def enterno():
    x = input("enter a binary no :")
    y = list(x)
    n = 0
    for i in y:
        if (i=="0") or (i=="1"):
            n+=1
    if n<len(y):
        print("invalid input")
        return(enterno())
    else:
        return int(x)

print("conversion from binary to decimal is : ",bin2dec(enterno()))
