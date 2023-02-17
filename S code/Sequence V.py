"""Sequence 5"""
def main():
    """Sequence Five"""
    num = int(input())
    while num > 0:
        for _ in range(7):
            print(num, end=" ")
            num -= 1
            if num == 0:
                break
        print()
main()
