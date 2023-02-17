"""ChaChaCha"""
import math
def main():
    """CHACHACHA"""
    day = int(input())
    num = 0
    for _ in range(day):
        hour = math.ceil(float(input()))
        num += hour
    print(int(num*8720))
main()
