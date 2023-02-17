"""different"""
def main():
    """diff"""
    numa = int(input())
    numb = int(input())
    set_a = set()
    set_b = set()
    for _ in range(numa):
        number_a = int(input())
        set_a.add(number_a)
    for _ in range(numb):
        number_b = int(input())
        set_b.add(number_b)
    set_c = sorted(set_a - set_b)
    print(*set_c)
main()
