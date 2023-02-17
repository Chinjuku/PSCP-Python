"""Virus"""
def main():
    """Chrorona"""
    txt = input()
    total = 0
    for number in txt:
        if number == "o":
            total += 1
    print(total)
main()
