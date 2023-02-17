"""Hamming"""
def ham():
    """Hammer"""
    txt1 = input()
    txt2 = input()
    list1 = []
    list2 = []
    sums = 0
    for i in txt1:
        list1.append(i)
    for i in txt2:
        list2.append(i)
    for i in range(len(list1)):
        print(list1[i])
        if list1[i] != list2[i]:
            sums += 1
    print(sums)
ham()



