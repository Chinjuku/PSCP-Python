"""Inverter"""
def main():
    """Inverter"""
    inverter = input()
    total = ""
    for i in inverter:
        print(i)
        if i == "0":
            total += "1"
        elif i == "1":
            total += "0"
    print(total.lstrip("0"))
main()
