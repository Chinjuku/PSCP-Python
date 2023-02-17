"""RPS"""
def main():
    """RPS"""
    txt = input()
    score_a = 0
    score_b = 0
    for i in range(0, len(txt), 2):
        aaa = txt[i]
        bbb = txt[i+1]
        if (aaa == "R" and bbb == "S") or (aaa == "P" and bbb == "R") or \
            (aaa == "S" and bbb == "P"):
            print("A")
            score_a += 1
        elif (aaa == "R" and bbb == "P") or (aaa == "P" and bbb == "S") or \
            (aaa == "S" and bbb == "R"):
            print("B")
            score_b += 1
    if score_a > score_b:
        print("A win %d-%d" (score_a, score_b))
    elif score_b > score_a:
        print("B win", str(score_b)+ "-" + str(score_a))
    else:
        print("DRAW", score_a)
 
main()


# """Rock paper Sissor"""
# def main():
#     """RPS"""
#     txt = input()
#     score_a = 0
#     score_b = 0
#     for i in range(0, len(txt), 2):
#         aaa = txt[i]
#         bbb = txt[i+1]
#         if (aaa == "R" and bbb == "S") or (aaa == "P" and bbb == "R") \
#             or (aaa == "S" and bbb == "P"):
#             score_a += 1
#        elif (aaa == "R" and bbb == "P") or (aaa == "S" and bbb == "R") \
#             or (aaa == "P" and bbb == "S"):
#             score_b += 1
#     if score_a == score_b:
#         print("DRAW", score_a)
#     elif score_a > score_b:
#         print("A win", str(score_a)+"-"+str(score_b))
#     elif score_b > score_a:
#         print("B win", str(score_b)+"-"+str(score_a))
# main()

# """Rock"""
# def main():
#     """Paper"""
#     score = input()
#     score_a = 0
#     score_b = 0
#     for i in range(0, len(score), 2):
#         people_a = score[i]
#         people_b = score[i+1]
#         if (people_a == "R" and people_b == "S") or (people_a == "P" and people_b == "R") \
#             or (people_a == "S" and people_b == "P"):
#             score_a += 1
#         elif (people_b == "R" and people_a == "S") or (people_b == "P" and people_a == "R") \
#             or (people_b == "S" and people_a == "P"):
#             score_b += 1
#     if score_b > score_a:
#         print("B win %d-%d" %(score_b, score_a))
#     elif score_a > score_b:
#         print("A win %d-%d" %(score_a, score_b))
#     else:
#         print("DRAW %d" %score_a)
# main()

