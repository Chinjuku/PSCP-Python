"""Circle"""
import math as a
def main():
    """Circle"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xxn = float(input())
    yyn = float(input())
    circle = a.sqrt((xxn - xxx)**2 + (yyn - yyy)**2)
    if circle <= rrr:
        print("True")
    else:
        print("False")
main()
