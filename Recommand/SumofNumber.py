"""sumofnumber"""
def sumall():
    """break the one"""
    numall = int(input())
    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num
        if total == numall:
            break
    print(total)
sumall()
