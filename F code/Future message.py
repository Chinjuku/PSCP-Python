'''Future Message'''
def main():
    '''Future Message'''
    word = input()
    if word.isnumeric() == True:
        print("Number")
    elif word.isupper() == True:
        print("Uppercase")
    elif word.islower() == True:
        print('Lowercase')
    elif word.istitle() == True:
        print("Title")
    elif word.isspace() == True:
        print("Space")
    else:
        print("Other")
main()
