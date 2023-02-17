"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    k = 0
    for _ in range(1, num+1):
        for _ in range(1, num+1):
            k += 1
            print(k, end=" ")
        print()
main()
