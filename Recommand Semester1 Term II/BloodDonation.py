"""Bloodd"""
def main():
    """Blood"""
    age = int(input())
    weight = int(input())
    times = int(input())
    if age == 17 or (60 <= age <= 70):
        certificate = input()
        if age == 17 and certificate == "True":
            if weight >= 45:
                print("Yes")
            elif weight < 45:
                print("No")
        elif (age == 17) and certificate == "False":
            print("No")
        if (60 <= age <= 70) and certificate == "True":
            if times > 0 and weight >= 45:
                print("Yes")
            else:
                print("No")
        elif (60 <= age <= 70) and certificate == "False":
            print("No")
    elif (17 <= age <= 59) and weight >= 45:
        if times >= 0 and age <= 55:
            print("Yes")
        elif times > 0 and 55 < age <= 59:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
