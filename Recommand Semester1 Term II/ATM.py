"""ATM"""
def main(num1, total_1):
    """atm"""
    newnum = num1.split()
    if newnum[0] == "D":
        total_1 += int(newnum[1])
    elif newnum[0] == "W":
        if total_1 >= int(newnum[1]):
            total_1 -= int(newnum[1])
        else:
            total_1 -= total_1
    return total_1

def atm():
    """ATM"""
    total = 0
    total = int(input())
    while True:
        num1 = input()
        if num1 == "END":
            break
        total = main(num1, total)
    print(total)
atm()
