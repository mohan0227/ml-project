#Function that performs basic calculator operations
def calculator(num1: int, num2: int, operator: str):
    if(operator == "+"):
        return num1 + num2
    elif(operator == "-"):
        return num1 - num2
    elif(operator == "*"):
        return num1 * num2
    elif(operator == "/"):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero"

num1, num2, operator = input().split(", ")
num1 = int(num1)
num2 = int(num2)
print(f"Result = {calculator(num1, num2, operator)}")