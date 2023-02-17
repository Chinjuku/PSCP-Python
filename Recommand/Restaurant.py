"""Restaurant"""
def main():
    """Restaurant"""
    paid = float(input())
    bill = float(input())
    discount = float(input())
    buy = float(input()) 
    if paid >= bill:
        new_paid = paid*(discount/100)
        print(new_paid)
    elif paid < bill:
        new_paid = paid
    paid_more = paid+buy
    price = paid_more*(discount/100)
    diff_more = (paid_more-price)-paid
    if paid_more-price > paid:
        print("No %0.3f" % abs(diff_more))
    elif paid_more-price < paid:
        print("Yes %0.3f" % abs(diff_more))
main()
