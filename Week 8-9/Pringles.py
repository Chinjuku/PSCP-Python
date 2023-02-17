"""Pringles"""
def mainnnnnnnnnn():
    """Pringle"""
    border_top = input()
    pringle = input()
    border_bottom = input()
    value = int(input())

    eat_count = 0
    left_count = 0
    eat = pringle[:value:]
    left = pringle[value::]

    for i in eat:
        if i == ")":
            eat_count = eat_count + 1
    for i in left:
        if i == ")":
            left_count = left_count + 1

    print(eat_count)
    if left_count == 0:
        print("None.")
    else:
        print("There are still some left.")

    print(border_top)
    print("%s%s" %((" "*value), pringle[value:]))
    print(border_bottom)
mainnnnnnnnnn()







# txt1 = input()
    # txt2 = input()
    # txt3 = input()
    # txt4 = input()
    # # if txt4 and txt2 != 0:
    # #     txt4 = txt2.count(")")
    # if txt1 == txt2.count(")"):
    #     print(txt2.count(""))
    #     print("None.")
    #     print(txt1)
    #     print(len(txt1)*""+"|")
    #     print(txt3)
