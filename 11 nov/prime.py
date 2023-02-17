"""isprime_small"""
def main(num):
    """prime"""
    if num == 0 or num == 1:
        return print("No")
    for i in range(2, num):
        if num%i == 0:
            return print("No")
    print("Yes")
main(int(input()))
