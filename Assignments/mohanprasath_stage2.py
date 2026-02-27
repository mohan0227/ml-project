#Function to check if the number is positive or negative or zero
def result_check(num: int) -> str:
    if(num > 0):
        return f"{num}\nPositive"
    elif(num < 0):
        return f"{num}\nNegative"
    else:
        return f"{num}Zero"

#Function that performs basic calculator operations
def calculator(num1: int, num2: int, operator: str):
    res = 0
    if(operator == "+"):
        res = num1 + num2
    elif(operator == "-"):
        res = num1 - num2
    elif(operator == "*"):
        res = num1 * num2
    elif(operator == "/"):
        try:
            res = num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    return result_check(res)

num1, num2, operator = input().split(", ")
num1 = int(num1)
num2 = int(num2)
print(f"Result = {calculator(num1, num2, operator)}")