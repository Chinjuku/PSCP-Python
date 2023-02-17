"""Frame"""
def main():
    """FrameBig"""
    txt1 = input().strip()
    txt2 = input().strip()
    txt3 = input().strip()
    txt4 = input().strip()
    txt5 = input().strip()
    long1 = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("*"*long1+"****")
    print("* "+txt1+" "*(long1-len(txt1))+" *")
    print("* "+txt2+" "*(long1-len(txt2))+" *")
    print("* "+txt3+" "*(long1-len(txt3))+" *")
    print("* "+txt4+" "*(long1-len(txt4))+" *")
    print("* "+txt5+" "*(long1-len(txt5))+" *")
    print("*"*long1+"****")
main()






























# txt1 = input().strip()
#     txt2 = input().strip()
#     txt3 = input().strip()
#     txt4 = input().strip()
#     txt5 = input().strip()
#     chack1 = len(txt1)
#     chack2 = len(txt2)
#     chack3 = len(txt3)
#     chack4 = len(txt4)
#     chack5 = len(txt5)
#     if chack1 > chack2 and chack1 > chack3 and chack1 > chack4 and chack1 > chack5:
#         ccc2 = chack1-chack2
#         ccc3 = chack1-chack3
#         ccc4 = chack1-chack4
#         ccc5 = chack1-chack5
#         print("**"+"*"*len(txt1)+"**")
#         print("* "+txt1+" *")
#         print("* "+txt2+" "*ccc2+" *")
#         print("* "+txt3+" "*ccc3+" *")
#         print("* "+txt4+" "*ccc4+" *")
#         print("* "+txt5+" "*ccc5+" *")
#         print("**"+"*"*len(txt1)+"**")
#     if chack2 > chack1 and chack2 > chack3 and chack2 > chack4 and chack2 > chack5:
#         vvv1 = chack2-chack1
#         vvv3 = chack2-chack3
#         vvv4 = chack2-chack4
#         vvv5 = chack2-chack5
#         print("**"+"*"*len(txt2)+"**")
#         print("* "+txt1+" "*vvv1+" *")
#         print("* "+txt2+" *")
#         print("* "+txt3+" "*vvv3+" *")
#         print("* "+txt4+" "*vvv4+" *")
#         print("* "+txt5+" "*vvv5+" *")
#         print("**"+"*"*len(txt2)+"**")
#     if chack3 > chack1 and chack3 > chack2 and chack3 > chack4 and chack3 > chack5:
#         ddd1 = chack3-chack1
#         ddd2 = chack3-chack2
#         ddd4 = chack3-chack4
#         ddd5 = chack3-chack5
#         print("**"+"*"*len(txt3)+"**")
#         print("* "+txt1+" "*ddd1+" *")
#         print("* "+txt2+" "*ddd2+" *")
#         print("* "+txt3+" *")
#         print("* "+txt4+" "*ddd4+" *")
#         print("* "+txt5+" "*ddd5+" *")
#         print("**"+"*"*len(txt3)+"**")
#     if chack4 > chack1 and chack4 > chack2 and chack4 > chack3 and chack4 > chack5:
#         ggg1 = chack4-chack1
#         ggg2 = chack4-chack2
#         ggg3 = chack4-chack3
#         ggg5 = chack4-chack5
#         print("**"+"*"*len(txt4)+"**")
#         print("* "+txt1+" "*ggg1+" *")
#         print("* "+txt2+" "*ggg2+" *")
#         print("* "+txt3+" "*ggg3+" *")
#         print("* "+txt4+"*")
#         print("* "+txt5+" "*ggg5+" *")
#         print("**"+"*"*len(txt4)+"**")
#     if chack5 > chack1 and chack5 > chack2 and chack5 > chack3 and chack5 > chack4:
#         rrr1 = chack5-chack1
#         rrr2 = chack5-chack2
#         rrr3 = chack5-chack3
#         rrr4 = chack5-chack4
#         print("**"+"*"*len(txt5)+"**")
#         print("* "+txt1+" "*rrr1+" *")
#         print("* "+txt2+" "*rrr2+" *")
#         print("* "+txt3+" "*rrr3+" *")
#         print("* "+txt4+" "*rrr4+" *")
#         print("* "+txt5+" *")
#         print("**"+"*"*len(txt5)+"**")
