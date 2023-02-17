"""Difference"""
def main(num_a, num_b):
    """set a - set b"""
    aaa = set()
    bbb = set()
    for _ in range(num_a):
        aaa.add(int(input()))
    for _ in range(num_b):
        bbb.add(int(input()))
    ans = sorted(aaa - bbb)
    print(*ans)
main(int(input()), int(input()))
