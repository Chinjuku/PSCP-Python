"""BMI"""
def main():
    """BMI"""
    name = input()
    weight = int(input())
    height = int(input())/100
    bmi = weight/(height*height)
    print("Name:", name)
    print("Weight:", weight, "kg.")
    print("Height: %.2f" %height, "m.")
    print("BMI: %.2f" %bmi)
main()
