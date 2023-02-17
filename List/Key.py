"""Key"""
def main():
    """KEY"""
    txt = input()
    num1 = 0
    for score in txt:
        num1 += int(score)
    num2 = (num1[-3:])*10
    num3 = num1 + num2
    if num3 > 9999:
        print("%04d", (num3 % 10000))
    elif num3 < 1000:
        print(num3+1000)
    else:
        print(num3)
main()
