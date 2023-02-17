"""WeightStation"""
def weight():
    """Weight"""
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = float(input())
    newweight = weight1*4-(weight4+weight3+weight2)
    kilog = newweight+weight4+weight3+weight2
    aver = weight1/2
    if kilog > 15000:
        print("Overweight")
    elif abs(weight1-weight2) >= aver or\
    abs(weight1-weight3) >= aver or abs(weight1-weight4) >= aver or\
    abs(weight1-newweight) >= aver:
        print("Unbalance")
    else:
        print("Pass %0.2f"%newweight)
weight()
