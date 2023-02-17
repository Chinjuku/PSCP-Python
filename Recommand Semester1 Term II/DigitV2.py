"""digit"""
def digitv2():
    """digital"""
    num = input()
    found = num.split()
    lisst = ["ten", "eleven", "twelve", "thirteen", "fourteen", \
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", \
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    for i in range(len(found)):
        if found[i] == "thousand":
            print(4)
            break
        elif found[i] == "hundred":
            print(3)
            break
        elif found[i] in lisst:
            print(2)
            break
        elif len(found) == 1:
            print(1)
digitv2()
