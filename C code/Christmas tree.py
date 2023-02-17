"""Christmas tree"""
def main():
    """Christmas tree"""
    bai = int(input())
    lumton = int(input())
    k = 0
    for i in range(1, bai+1):
        for _ in range(1, (bai- i) + 1):
            print(end=" ")
        while k != (2 * i - 1):
            print("*", end="")
            k += 1
        k = 0
        print()
    for _ in range(lumton):
        print('---'.center(bai * 2))
main()
