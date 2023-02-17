"""Colour"""
def color():
    """Coulour"""
    color1 = input()
    color2 = input()
    if (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
        print("Orange")
    elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
        print("Violet")
    elif (color1 == "Blue" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Blue"):
        print("Green")
    elif color1 == "Blue" and color2 == "Blue":
        print("Blue")
    elif color1 == "Red" and color2 == "Red":
        print("Red")
    elif color1 == "Yellow" and color2 == "Yellow":
        print("Yellow")
    else:
        print("Error")
color()
