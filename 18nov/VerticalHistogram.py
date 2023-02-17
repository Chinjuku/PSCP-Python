"""VerticalHistogram"""
def sortword(word):
    """sort"""
    if word.isupper():
        return ord(word)+1000
    return ord(word)

def main():
    """HorizontalHistogram"""
    text = input()
    word = set()
    ans = {}
    long = []
    for i in text:
        word.add(i)
    word = list(word)
    word.sort(key=sortword)
    for j in word:
        ans[j] = ""
    for k in text:
        ans[k] += "*"
    for mmm in ans:
        long.append(len(ans[mmm]))
    longest = max(long)
    print(longest)
    for nnn in range(longest, 0, -1):
        print("%03d" %nnn, end=" ")
        wantprint = ""
        for lll in ans:
            printablee = " "
            if len(ans[lll]) >= nnn:
                printablee = "*"
            wantprint += (printablee + " ")
        print(wantprint.rstrip())
    print("   ", *ans)
main()
