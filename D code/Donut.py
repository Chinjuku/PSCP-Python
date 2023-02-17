"""Donut"""
def main():
    """donut"""
    sell = int(input())
    buy = int(input())
    free = int(input())
    want = int(input())
    promo = want // (buy+free)
    donut = promo*(buy+free)
    price = promo*(sell*buy)
    if want % buy+free >= buy:
        donut += buy+free
        price += buy*free
    else: 
        want % buy+free < buy
        more = want-donut
        donut += more
        price += more*sell
    print("%d %d" %(price, donut))
main()
