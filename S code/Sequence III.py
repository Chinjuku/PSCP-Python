"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    ## Nest Loop
    for col in range(0, num):
        for row in range(num):
            print(2 + col + row, end=" ")
        print()
main()
