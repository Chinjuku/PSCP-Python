"""Century"""
import math
def check(num):
    """check ka e hok"""
    num = math.ceil(num/100)
    return num
def main():
    """Century"""
    num = int(input())
    for _ in range(1, num+1):
        word = input()
        if "B.E." in word:
            chris = int(word[5:])
            if chris >= 543:
                chris -= 543
                print(check(chris))
            else:
                print("ERROR")
        if "A.D." in word:
            if int(word[5:]) % 100 == 0:
                print(int(word[5:])//100)
            elif int(word[5:]) % 100 != 0:
                print(int(word[5:])//100 + 1)
            else:
                print("ERROR")
main()
