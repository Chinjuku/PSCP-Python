"""Phone"""
def main(numphone, typing):
    """Phone"""
    if len(numphone) == 10 and typing == "International":
        print("+66"+numphone[1:2], numphone[2:6], numphone[6:10])
    elif len(numphone) == 9 and typing == "International":
        print("+66", numphone[1:5], numphone[5:9])
    elif len(numphone) == 9 and typing == "Domestic":
        print(numphone[0:1], numphone[1:5], numphone[5:9])
    if len(numphone) == 10 and typing == "Domestic":
        print(numphone[0:2], numphone[2:6], numphone[6:10])
main(input(), input())
