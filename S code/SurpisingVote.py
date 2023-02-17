"""Surprisevote"""
def main():
    """Surprise"""
    point_1 = float(input())
    point_2 = float(input())
    point_low = 0
    if point_2 * 2 < point_1:
        point_low = point_1 - point_2 * 2
    if point_2 - point_low > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
