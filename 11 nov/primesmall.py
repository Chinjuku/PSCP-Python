"""prime"""
def prime():
    """prime"""
    num = int(input())
    if num == 0 or num == 1:
        print("No")
    for i in range(2, num):
        if num%i == 0:
            print("No")
        elif num%i != 0:
            print("Yes")
prime()
