# """CoinChangerv1"""
# def main():
#     """ Main function """
#     money = int(input())
 
#     _25coin, coin_left = divmod(money, 25)
#     _10coin, coin_left = divmod(coin_left, 10)
#     _5coin, _1coin = divmod(coin_left, 5)
 
#     print(_25coin + _10coin + _5coin + _1coin)
# main()

import random
fname = ["A", "Cha", "Chin", "Rmin"]
name = sorted(["A", "Cha", "Chin", "Rmin"], key=lambda x : random.randrange(12))
selectcard = []
for i in fname:
    givecard = []
    while True:
        card = random.randrange(1, 30)
        if card not in selectcard:
            givecard.append(card)
            selectcard.append(card)
        if len(givecard) == 3:
            print(i, ":", *givecard)
            break

print(name)
