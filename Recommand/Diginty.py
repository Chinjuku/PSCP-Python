'''Diginty'''
def main():
    '''Diginty'''
    point = 0
    while True:
        word = input()
        if len(str(word)) > 1:
            for i in str(word):
                point += int(i)
            if word == 0:
                break
        print(point)
        
main()
