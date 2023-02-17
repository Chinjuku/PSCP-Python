"""backward"""
def back():
    """back"""
    num = []
    for _ in range(5):
        num.append(int(input()))
    num.sort()
    print(*num, sep="\n")
back()
