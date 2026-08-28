#Enter Number1
Num1 = int(input("Enter Number1: "))
#Choose Operation type: * / + -
Operation = input("Choose Operation type: * / + - : ")
#Enter Number1
Num2 = int(input("Enter Number2: "))
def calculator(Operation):
    if Operation == "*":
        print(Num1, "*", Num2, "=", Num1 * Num2)
        return Num1 * Num2
    elif Operation == "/":
        if Num2 == 0:
            print("Error: Division by zero is not allowed.")
            return "Error: Division by zero is not allowed."
        else:
            print(Num1, "/", Num2, "=", Num1 / Num2)
            return Num1 / Num2
    elif Operation == "+":
        print(Num1, "+", Num2, "=", Num1 + Num2)
        return Num1 + Num2
    elif Operation == "-":
        print(Num1, "-", Num2, "=", Num1 - Num2)
        return Num1 - Num2
    else:
        return "Invalid operation"
Result = calculator(Operation)
