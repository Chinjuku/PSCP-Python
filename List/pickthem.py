"""PickThem"""
def pick():
    """ไอแว่นมันเป็นเหี้ยไรวะ"""
    listt = []
    text = input().split()
    for i in text:
        if int(i)%3 == 0 or int(i)%5 == 0:
            listt.append(i)
    if len(listt) == 0:
        return print("Nope")
    listt.reverse()
    print(*listt, sep="\n")
pick()
