"""PSCT"""
def main(grade):
    """PSCT"""
    if 95 <= grade <= 100:
        return str("A")
    elif grade >= 90:
        return str("B+")
    elif grade >= 85:
        return str("B")
    elif grade >= 80:
        return str("C+")
    elif grade > 75:
        return str("C")
    elif grade >= 70:
        return str("D+")
    elif grade >= 65:
        return str("D")
    elif grade >= 60:
        return str("F+")
    elif 0 <= grade < 60:
        return str("F")
    else:
        return str("ERR")

print(main(float(input())))
