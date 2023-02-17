"""iPhone13"""
def mini(num2):
    """iPhone13"""
    if num2 == "128 GB":
        return 25900
    elif num2 == "256 GB":
        return 29900
    elif num2 == "512 GB":
        return 37900
    else:
        return "Not Available"
def sipsam(num2):
    """iPhone13"""
    if num2 == "128 GB":
        return 29900
    elif num2 == "256 GB":
        return 33900
    elif num2 == "512 GB":
        return 41900
    else:
        return "Not Available"
def sipsam_pro(num2):
    """iPhone13"""
    if num2 == "128 GB":
        return 38900
    elif num2 == "256 GB":
        return 42900
    elif num2 == "512 GB":
        return 50900
    elif num2 == "1 TB":
        return 58900
    else:
        return "Not Available"
def sipsam_promax(num2):
    """iPhone13"""
    if num2 == "128 GB":
        return 42900
    elif num2 == "256 GB":
        return 46900
    elif num2 == "512 GB":
        return 54900
    elif num2 == "1 TB":
        return 62900
    else:
        return "Not Available"
def main():
    """iPhone13"""
    num1 = input()
    num2 = input()
    if num1 == "iPhone 13 mini":
        print(mini(num2))
    elif num1 == "iPhone 13":
        print(sipsam(num2))
    elif num1 == "iPhone 13 Pro":
        print(sipsam_pro(num2))
    elif num1 == "iPhone 13 Pro Max":
        print(sipsam_promax(num2))
    else:
        print("Not Available")
main()

# """iPhone"""
# def mini(memo):
#     """13mini"""
#     if memo == "128 GB":
#         return 25900
#     elif memo == "256 GB":
#         return 29900
#     elif memo == "512 GB":
#         return 37900
#     else:
#         print("Not Available")

# def sipsam(memo):
#     """13"""
#     if memo == "128 GB":
#         return 29900
#     elif memo == "256 GB":
#         return 33900
#     elif memo == "512 GB":
#         return 41900
#     else:
#         print("Not Available")
# def sipsampro(memo):
#     """13 Pro"""
#     if memo == "128 GB":
#         return 38900
#     elif memo == "256 GB":
#         return 42900
#     elif memo == "512 GB":
#         return 50900
#     elif memo == "1 TB":
#         return 58900
#     else:
#         print("Not Available")

# def sipsampromax(memo):
#     """13 Pro max"""
#     if memo == "128 GB":
#         return 42900
#     elif memo == "256 GB":
#         return 46900
#     elif memo == "512 GB":
#         return 54900
#     elif memo == "1 TB":
#         return 62900
#     else:
#         print("Not Available")
# def main():
#     """Iphone13"""
#     iphone = input()
#     memo = input()
#     if iphone == "iPhone 13 mini":
#         print(mini(memo))
#     elif iphone == "iPhone 13":
#         print(sipsam(memo))
#     elif iphone == "iPhone 13 Pro":
#         print(sipsampro(memo))
#     elif iphone == "iPhone 13 Pro Max":
#         print(sipsampromax(memo))
#     else:
#         print("Not Available")
# main()
