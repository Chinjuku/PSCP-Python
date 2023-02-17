"""Howlong"""
def long():
    """Howlong"""
    num = str(abs(int(input())))
    k = 0
    for _ in num:
        k += 1
    print(k)
long()
