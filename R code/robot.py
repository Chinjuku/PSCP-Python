"""bot"""
def main():
    """gaeg"""
    name = input()
    old = float(input())
    if 0 < old < 18:
        print(name + ",", "you can pass.")
    else:
        print(name + ",", "you shall not pass.")
main()
