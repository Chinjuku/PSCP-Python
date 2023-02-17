'''guyu'''
def main():
    '''gg'''
    grade = float(input())
    if grade > 100:
        print("ERR")
    elif grade >= 95:
        print("A")
    elif grade >= 90:
        print("B+")
    elif grade >= 85:
        print("B")
    elif grade >= 80:
        print("C+")
    elif grade > 75:
        print("C")
    elif grade >= 70:
        print("D+")
    elif grade >= 65:
        print("D")
    elif grade >= 60:
        print("F+")
    elif 0 < grade < 60:
        print("F")
    elif grade < 0:
        print("ERR")
main()
