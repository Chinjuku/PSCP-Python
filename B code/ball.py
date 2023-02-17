"""Ball"""
def main():
    """Ball"""
    num = float(input())
    count = 0
    while True:
        num = num*0.6
        if num < 0.01:
            break
        count += 1
    print(count)
main()

# while True:
    #     num = int(input())
    #     if num == 0:
    #         break
    #     if len(str(num)) == 1:
    #         print(num)
    #     elif len(str(num)) > 1:
    #         while True:
    #             count = 0
    #             for i in str(num):
    #                 count += int(i)
    #             if len(str(num)) == 1:
    #                 break
    #         print(count)
    