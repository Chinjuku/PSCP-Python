"""PlanC"""
def number(num1, num2, num3):
    """PlanC"""
    if num1 <= num2 <= num3:
        return num1, num2, num3
    elif num1 <= num3 <= num2:
        return num1, num3, num2
    elif num2 <= num1 <= num3:
        return num2, num1, num3
    elif num2 <= num3 <= num1:
        return num2, num3, num1
    elif num3 <= num1 <= num2:
        return num3, num1, num2
    elif num3 <= num2 <= num1:
        return num3, num2, num1
    elif num1 == num2 == num3:
        return num3, num2, num3
def number1(num1, num2, num3):
    """PlanC"""
    if num1 >= num2 >= num3:
        return num1, num2, num3
    elif num1 >= num3 >= num2:
        return num1, num3, num2
    elif num2 >= num1 >= num3:
        return num2, num1, num3
    elif num2 >= num3 >= num1:
        return num2, num3, num1
    elif num3 >= num1 >= num2:
        return num3, num1, num2
    elif num3 >= num2 >= num1:
        return num3, num2, num1
    elif num1 == num2 == num3:
        return num3, num2, num1
def main():
    """PlanC"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if text == "Ascend":
        print("%0.2f, %0.2f, %0.2f" %(number(num1, num2, num3)))
    elif text == "Descend":
        print("%0.2f, %0.2f, %0.2f" %(number1(num1, num2, num3)))
main()
