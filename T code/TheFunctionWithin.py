"""bmi"""
def f_x(num1):
    """fxx"""
    return 2*num1

def g_x(num1):
    """gxx"""
    return 3*num1**4 - num1**3 + 2*num1**2 + 10

def h_xyz(num1, num2, num3):
    """hxyz"""
    return (num3+num1)**2 - num1*num2 + num2**2

def i_abcd(numa, numb, numc, numd):
    """iabcd"""
    return (numa**2 + numb**2 - numc**2) / (numd**2 - 2*numa*numd + 2*numa)

def main():
    """chinjunghome"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numd = float(input())
    fxx = f_x(f_x(numa))
    gxx = g_x(f_x(numa-numb))
    hxx = h_xyz(f_x(numa+numb), f_x(numa+numc), g_x(f_x(numd**2)))
    ixx = i_abcd(h_xyz(f_x(numa+numb), f_x(numa-numc), g_x(f_x(numd**2)))\
        , g_x(f_x(numa-numb)), f_x(f_x(f_x(f_x(f_x(numc))))), numd**8)
    print(fxx)
    print(gxx)
    print(hxx)
    print(ixx)
main()
