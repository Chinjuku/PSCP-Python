"""123"""
def main():
    """wjfaiof"""
    weight = float(input())
    height = float(input())/100
    bmii = weight/(height*height)
    if bmii < 18.5:
        print("Underweight")
    elif 18.5 <= bmii < 25:
        print("Normal")
    elif 25 <= bmii < 30:
        print("Overweight")
    elif bmii >= 30:
        print("Obese")
main()
