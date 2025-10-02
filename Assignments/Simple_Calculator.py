import os

os.system('cls')

x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))
operation = input("Enter operation (+, -, *, /, ^, %, //)\n>")

class Calculator:
    def add():
        global x, y
        return (x + y)
    def subtract():
        global x, y
        return (x - y)
    def multiply():
        global x, y
        return (x * y)
    def divide():
        global x, y
        return (x / y)
    def pow():
        global x, y
        return (x ** y)
    def mod():
        global x, y
        return (x % y)
    def floor_divide():
        global x, y
        return (x // y)

message = ""
match operation:
    case "+": message = Calculator.add()
    case "-": message = Calculator.subtract()
    case "*": message = Calculator.multiply()
    case "/": message = Calculator.divide()
    case "^": message = Calculator.pow()
    case "%": message = Calculator.mod()
    case "//": message = Calculator.mod()
    case default: print("Invalid operation")

print(message)
