"""Temperature"""
def main():
    """TEMP"""
    temp = float(input())
    first = input()
    last = input()
    if first == "C":
        temp = temp
    elif first == "F":
        temp = (temp-32)*(5/9)
    elif first == "K":
        temp = temp-273.15
    elif first == "R":
        temp = (temp-491.67)*(5/9)
    if last == "C":
        temp = temp
    elif last == "F":
        temp = (temp*(9/5))+32
    elif last == "K":
        temp = temp+273.15
    elif last == "R":
        temp = (temp*(9/5))+491.67
    print("%.2f" %temp)
main()
