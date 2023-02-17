"""MissingNumber"""
def main():
    """MissingNumber"""
    num = int(input())
    list_num = []
    while True:
        text = int(input())
        if text == 0:
            break
        list_num.append(text)
    for i in range(1, num+1):
        if i not in list_num:
            print(i)
main()
