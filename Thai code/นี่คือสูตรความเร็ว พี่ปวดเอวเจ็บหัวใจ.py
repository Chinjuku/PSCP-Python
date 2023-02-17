"""free"""
def main():
    """free"""
    distance = float(input())
    time = int(input())
    milesea = distance*1852
    millisec = time*0.001
    vvv = milesea/millisec
    print("อัตราเร็วเท่ากับ : %.3f" %vvv, "เมตรต่อวินาที")
main()
