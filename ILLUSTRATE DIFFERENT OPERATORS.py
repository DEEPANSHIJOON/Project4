# illustraion of different operator
a = int(input("enter the first no."))
b = int(input("enter the second no."))
Operator = input("What's the operation you want to perform on inputs ")

match Operator:
    case "+":
        print("Addition of given no. is  ", a+b)

    case "-":
        print("Subtraction of given no. is ", a-b)

    case "*":
        print("Multiplication of given no is ", a*b)

    case "/":
        print("division of given no. is ", a/b)

    case "%":
        print("Modulus of given no is ", a % b)
    case _:
        print("The operator you entered is invalid")
