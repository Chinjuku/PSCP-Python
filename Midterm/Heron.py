"""Heron"""
def main():
    """Heron"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    sss = (num1+num2+num3)/2
    area = (sss*(sss-num1)*(sss-num2)*(sss-num3))**0.5
    print("%.3f"% area)
main()
