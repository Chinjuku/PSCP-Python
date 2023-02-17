"""Point Sorting"""
def sort_y(value):
    """sort with y value"""
    return int(value[1])

def sort_sum(value):
    """sort with sum x+y"""
    return int(value[0]) + int(value[1])

def main():
    """Point Sorting"""
    num1 = int(input())
    for _ in range(num1):
        num2 = int(input())
        listt = []
        for _ in range(num2):
            point = input()
            listt.append(point.split())
        listt.sort(key=sort_y, reverse=True)
        listt.sort(key=sort_sum)
        for i in listt:
            print(*i)
main()
