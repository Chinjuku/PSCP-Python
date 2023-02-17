"""print"""
def main():
    """print"""
    num = int(input())
    sec = num
    mins = sec//60
    sec = sec%60
    hour = mins//60
    mins = mins%60
    day = hour//24
    hour = hour%24
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" %(day, hour, mins, sec))
main()
