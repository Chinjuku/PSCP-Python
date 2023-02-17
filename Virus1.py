"""Virus I"""
def danger():
    """How virus look like"""
    howlong = input()
    num = 0
    for i in howlong:
        if  i == ("o"):
            num += 1
    print(num)
danger()
