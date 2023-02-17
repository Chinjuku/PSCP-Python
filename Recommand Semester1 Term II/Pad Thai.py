"""PhadThai"""
def phadthai():
    """Phadthai"""
    ingre = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", \
         "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    delecius = ["Sweet", "Sour", "Salty"]
    while True:
        ingredient = input()
        if ingredient == "Cook":
            break
        lisst1 = []
        more = ""
        lisst1.append(ingredient)
        print(lisst1)
        more += lisst1
    # while True:
    #     taste = input()
    #     if taste == "End":
    #         break
    # if ingredient == ingre and taste == delecius:
    #     print("Delicious!")
    # elif ingredient == ingre or delecius == taste:
    #     print("Not Bad...")
    # else:
    #     print("It's bad")
phadthai()


# def main(request):
#     return request + 10
# x = 10
# print(main(x))
