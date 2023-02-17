"""Muddled Menu"""
def main():
    """Muddled Menu"""
    course = []
    while True:
        menu = input()
        if menu == "DONE":
            print("Full Course:", course, end=" ")
            course.reverse()
            print("Reversed:", course)
            return
        if menu == "SOMETHING'S WRONG":
            course = []
            continue
        if menu == "CLOSED":
            return print("Full Course: [] Reversed: []")
        if "Can't do" in menu:
            while menu[10:] in course:
                course.remove(menu[10:])
            continue
        splitt = menu.split(" #")
        if splitt[-1] == "N":
            course.append(splitt[0])
        else:
            course.insert(int(splitt[1])-1, splitt[0])
main()
