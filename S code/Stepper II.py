"""Stepper II"""
def main():
    """Stepper II"""
    num = int(input())
    num1 = int(input())
    k = 0
    if num < num1:
        while (num + k) <= num1:
            print(num + k)
            k += 1
    elif num1 < num:
        while (num - k) >= num1:
            print(num - k)
            k += 1
    elif num == num1:
        print(num)
main()
