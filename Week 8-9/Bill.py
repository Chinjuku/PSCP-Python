'''bill'''
def main():
    bill = float(input())
    service = bill*(10/100)
    bill2 = bill+service
    vat = bill2*(7/100)
    new_bill = bill + service + vat
    print(new_bill)
    # if bill > 1000:
    #     vat = bill*(7/100)
    #     new_bill = bill  + vat
    # print(new_bill)
main()
