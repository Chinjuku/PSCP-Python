"""Duplicate I"""
def main(num_a, num_b):
    """intersection"""
    aaa = set()
    bbb = set()
    for _ in range(num_a):
        aaa.add(input())
    for _ in range(num_b):
        bbb.add(input())
    ans = sorted(aaa.intersection(bbb))
    ans.reverse()
    if ans == []:
        print("Nope")
    else:
        print(*ans, sep="\n")
main(int(input()), int(input()))
