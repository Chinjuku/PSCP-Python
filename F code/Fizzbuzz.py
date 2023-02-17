"""sequence-"""
def main():
    """XI"""
    num1 = int(input())
    for i in range(1, num1 + 1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
main()
