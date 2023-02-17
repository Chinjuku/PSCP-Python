"""KEy"""
def main():
    """Keyyy"""
    txt = input()
    total = 0
    for score in txt:
        total += int(score)
    ans2 = int(txt[:-3])*10
    ans3 = total + ans2
    if ans3 < 1000:
        print(ans3+1000)
    elif ans3 >= 10000:
        print("%04d" % (ans3 % 10000))
main()
