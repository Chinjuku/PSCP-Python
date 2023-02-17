"""Tax"""
def main():
    """Taxi"""
    num = int(input())
    ccc = int(input())
    newc = 0
    newnum = 0
    if 1 <= ccc <= 600:
        newc = ccc * 0.5
    elif 601 <= ccc <= 1800:
        newc = (ccc-600)*1.5 + 300
    elif 1801 <= ccc:
        newc = (ccc-1800)*4 + 2100
    if num == 6:
        newnum = newc - (newc*0.1)
    elif num == 7:
        newnum = newc - (newc*0.2)
    elif num == 8:
        newnum = newc - (newc*0.3)
    elif num == 9:
        newnum = newc - (newc*0.4)
    elif num >= 10:
        newnum = newc*0.5
    if num >= 6:
        print("%0.2f" %newnum)
    elif num < 6:
        print("%0.2f" %newc)
main()
