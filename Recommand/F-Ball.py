"""Forfball"""
def main():
    """XI"""
    ball = input()
    pos_ball = 1
    for i in ball:
        if i == "A" and pos_ball == 1:
            pos_ball = 2
        if i == "A" and pos_ball == 2:
            pos_ball = 1 
        if i == "B" and pos_ball == 2:
            pos_ball = 3
        if i == "B" and pos_ball == 3:
            pos_ball = 2
        if i == "C" and pos_ball == 3:
            pos_ball = 1
        if i == "C" and pos_ball == 1:
            pos_ball = 3
    print(pos_ball)
main()