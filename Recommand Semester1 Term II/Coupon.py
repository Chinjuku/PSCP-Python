"""Coupon"""
def coupon():
    """cOupOn"""
    price = float(input())
    promo1 = input()
    promo2 = input()
    new_promo1 = promo1.split()
    new_promo2 = promo2.split()
    new_price1 = price-float(new_promo1[0]) #ราคาทึ่ถูกลดแล้ว1
    new_price2 = price-price*(float(new_promo2[0])/100) #ราคาทึ่ถูกลดแล้ว2
    if price >= float(new_promo1[1]) and price >= float(new_promo2[1]):
        if new_price1 == new_price2:
            if new_promo1[1] <= new_promo2[1]:
                print("1 %0.1f" %new_price1)
            elif new_promo2[1] <= new_promo1[1]:
                print("2 %0.1f" %new_price2)
        elif new_price1 < new_price2:
            print("1 %0.1f" %new_price1)
        elif new_price2 < new_price1:
            print("2 %0.1f" %new_price2)
    elif price >= float(new_promo1[1]) and price < float(new_promo2[1]):
        print("1 %0.1f" %new_price1)
    elif price >= float(new_promo2[1]) and price < float(new_promo1[1]):
        print("2 %0.1f" %new_price2)
    elif price < float(new_promo1[1]) and price < float(new_promo2[1]):
        print("Nope")
coupon()
