"""ddddd"""
def main():
    """ddddd"""
    second = int(input())
    day = second//86400 
    hour = second//3600
    minute = second//60
    print("%02d", day-hour-minute)
main()
