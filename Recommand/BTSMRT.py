"""BTS"""
def main():
    """MRT"""
    day = input()
    ages = float(input())
    hight = float(input())
    if (day == "Children Day" and ages <= 14 and hight <= 140) or \
       (ages < 14 and hight < 90):
        print("FREE")
    elif day == "Senior Day" and ages >= 60:
        print("FREE")
    else:
        print("PAY")
main()
