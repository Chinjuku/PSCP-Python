"""allforone"""
def main():
    """allforone"""
    num = int(input())
    newtext = ""
    if num != 0:
        for i in range(1, num+1):
            text = input()
            if i == num:
                newtext += text+ "_" +str(num)
            elif i%2 == 0:
                newtext += text+i*"-"
            elif i%2 != 0:
                newtext += text+i*"*"
        print(newtext)
main()
















# for i in range(1, 8, 3):
#     print(i)

# i = 0
# while i >= -4:
#     print(i)
#     i -= 1

# x = 5
# y = x
# x = 7
# print(y)

# hello = "Hello, World"
# print(hello.index("o",5))

# ax = "FAIL"
# bx = "HELLO"
# print(ax[0:2]+bx[2:5])

# string = "abcDEF"
# string2 = string.upper()
# string3 = string.lower()
# print(string2)
# print(string3)

# mystring = 'This PSIT exam is very easy.'
# x = mystring.index('a')
# print(x)

# string1 = 'Helloworld'
# print(string1[-2:-8:-1])

