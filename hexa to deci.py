def hex_to_decimal(hex):
    hex_decimal_conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                              'A': 10, 'B': 11,  'C': 12,  'D': 13, 'E': 14,  'F': 15}

    p = len(hex) - 1
    decimal = 0

    for c in hex:
        decimal += hex_decimal_conversion[c] * (16 ** p)
        p -= 1

    return decimal
def enterno():
    x = input("enter a hexadecimal no :").upper()
    y = list(x)
    z=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    n = 0
    for i in y:
        if i in z:
            n+=1
    if n<len(y):
        print("invalid input")
        return(enterno())
    else:
        return x

hexano=enterno()
#print("no of digits before conersion is :  ",len(hexano))
decimal = hex_to_decimal(hexano)
print(f'conversion from hexadecimal to decimal is {decimal}')