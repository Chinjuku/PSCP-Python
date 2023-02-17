"""duplicate"""
def duplicates():
    """dup"""
    people = int(input())
    num = int(input())
    set_a = set()
    set_b = set()
    for _ in range(people):
        set_a.add(int(input()))
    for _ in range(num):
        set_b.add(int(input()))
    set_c = sorted(set_a & set_b, reverse=True)
    if set_c == []:
        print("Nope")
    else:
        print(*set_c, sep="\n")
duplicates()
