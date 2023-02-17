"""metrix"""
def metrix():
    """metrix"""
    ina = int(input())
    inb = int(input())
    matrix = []
    for i in range(ina):
        abc = []
        for j in range(inb):
            abc.append(int(input()))
        matrix.append(abc)
    for i in range(ina):
        for j in range(inb):
            print(matrix[i][j], end=" ")
        print()
metrix()
