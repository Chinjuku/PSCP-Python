"""backward"""
def back():
    """back"""
    listt = []
    while True:
        text = input()
        if text == "NULL":
            listt.reverse()
            return print(*listt, sep="\n")
        listt.append(text)
back()
