"""Sequence I"""
def main():
    """Sequence I"""
    num = int(input())
    ## Nest Loop
    for _ in range(1, num+1):
        for col in range(1, num+1):
            print(col, end=" ")
        print()
main()
