"""Median"""
def main():
    """Median"""
    num = int(input())
    listt = []
    for _ in range(num):
        listt.append(int(input()))
    listt.sort()
    if num%2 == 0:
        first = int((((num+1)/2)-0.5)-1)
        last = int((((num+1)/2)+0.5)-1)
        ans = (listt[first] + listt[last])/2
    else:
        ans = listt[int((num+1)/2)-1]
    print("%.1f" %ans)
main()
