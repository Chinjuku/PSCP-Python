"""LineSorting"""
def main():
    """LineSorting"""
    num = int(input())
    listt = []
    for _ in range(num):
        listt.append(input())
    listt.sort(key=len)
    print(*listt, sep="\n")
main()