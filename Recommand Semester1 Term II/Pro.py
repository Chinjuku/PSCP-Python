"""Pro"""
def pro():
    """Pro"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    people = (num4 // num1) * num2 * num3
    sums = people + (num4 % num1)*num3
    print(sums)
pro()
