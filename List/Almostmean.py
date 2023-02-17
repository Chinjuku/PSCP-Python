"""Almost"""
def main():
    """mean"""
    num = int(input())
    listt = []
    score = []
    for _ in range(1, num+1):
        txt = input()
        listt.append(txt)
        txt = txt.split("\t")
        score.append(float(txt[1]))
    newscore = sum(score)/num
    rev = sorted(score, reverse=True)
    for i in rev:
        if i < newscore:
            avg = score.index(i)
            print(listt[avg])
            break
main()
