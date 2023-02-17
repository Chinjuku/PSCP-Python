"""foodgarde"""
def chick():
    """Findchick"""
    wings = int(input())
    if wings >= 50 and wings <= 70:
        return wings
    else:
        return 0
def main():
    """foodgarde"""
    val = list()
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    val.append(chick())
    valx = len(val) - val.count(0)
    print(valx)
main()