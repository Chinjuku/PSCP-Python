"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    ## Nest Loop
    for _ in range(1):
        for col in range(1, num+1):
            print(col**2, end=" ")
        print()
main()
