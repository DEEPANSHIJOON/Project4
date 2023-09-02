def OctalDecimal(num, i):  #user-defined function
    if num >=0 and num <= 7:
        return num*pow(8, i)

    last_digit = num % 10
    return (pow(8, i) * last_digit) + OctalDecimal(num // 10, i+1)

def hex_to_decimal(hex):
    hex_decimal_conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                              'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15}

    p = len(hex) - 1
    decimal = 0

    for c in hex:
        decimal += hex_decimal_conversion[c] * (16 ** p)
        p -= 1

    return decimal

# calling function and display result
num = (input("Enter a hexadecimalnumber: "))
decimal = hex_to_decimal(num)

print(f'Decimal of {num} is {decimal}')
