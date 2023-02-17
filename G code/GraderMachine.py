"""Grader"""
def main():
    """Grader"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    intpass = ''
    if num2 > num1:
        for i in range(num1, num2+1):
            if i % 2 == 0:
                intpass += str(i)+' '
                ans = ans + i
    else:
        for i in range(num1, num2-1, -1):
            if i % 2 == 0:
                intpass += str(i)+' '
                ans = ans + i
    print("pass : %s" %intpass)
    print("Sum : %d" %ans)
main()
