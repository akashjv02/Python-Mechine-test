#calculator for user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operators:\n"
      "+\n"
      "-\n"
      "*\n"
      "/\n")
operators = input("Enter operator: ")

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cant devide by 0"  

calc = Calculator()  


if operators == "+":
    print("Result :", calc.add(num1, num2))
    
elif operators == "-":
    print("Result :", calc.sub(num1,  num2))  
    
elif operators == "*":
    print("Result :", calc.mul(num1, num2))

elif operators == "/":
    print("Result :", calc.div(num1, num2))      