"""All_Primes"""
def main(num):
    """prime"""
    listt = []
    for i in range(2, num+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            listt.append(i)
    print(len(listt))
main(int(input()))
