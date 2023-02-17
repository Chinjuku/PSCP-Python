"""IpadAir"""
def ipadair():
    """Ipadair"""
    color = input()
    mem = int(input())
    wifi = input()
    lisst = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    # if color == "Space Gray" or color == "Siver" or color == "Green" or \
    # color == "Rose Gold" or color == "Sky Blue":
    if color in lisst:
        if mem == 64 and wifi == "Wi-Fi":
            print(19900)
        elif mem == 256 and wifi == "Wi-Fi":
            print(24900)
        elif mem == 64 and wifi == "Wi-Fi + Cellular":
            print(24400)
        elif mem == 256 and wifi == "Wi-Fi + Cellular":
            print(29400)
        elif mem != 64 or mem != 256:
            print("Not Available")
        elif wifi != "Wi-Fi + Cellular" or wifi != "Wi-Fi":
            print("Not Available")
        else:
            print("Not Available")
    else:
        print("Not Available")
ipadair()
