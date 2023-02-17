"""LastStand"""
import json
def main():
    """LastStand"""
    text = input()
    listt = json.loads(text)
    for i in listt:
        print(str(i)[-1])
main()
