"""Elo"""
def main():
    """Elo"""
    reada = float(input())
    readb = float(input())
    choice = input()
    if choice == "A" and reada:
        eloa = 1/(1+(10**((readb-reada)/400)))
        print("%0.2f" % (eloa))
    elif choice == "B" and readb:
        elob = 1/(1+(10**((reada-readb)/400)))
        print("%0.2f" % (elob))
main()
