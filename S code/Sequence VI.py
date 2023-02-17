"""sequence Six"""
def main():
    """sequence Sick"""
    value = int(input())
    for line in range(0, value):
        for row in range(1, line+2):
            print(row, end=" ")
        print()
main()
