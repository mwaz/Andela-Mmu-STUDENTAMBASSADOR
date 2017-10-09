from math import pi

def pi_approx(n):
    """ Return an approximate value of pi
        calculated from n terms of 4/1 - 4/3 + 4/5 - ...
        >>> pi_approx(1)
        4.0
        >>> pi_approx(100)
        3.1315929035585537
        >>> pi_approx(1000)
        3.1405926538397941
        >>> pi_approx(1e4)
        3.1414926535900345
        """
    result = 0.0
    n = int(n)                       # make sure input is integer
    for i in range(n):               # 0, 1, 2, ..., n-1
        denom = 2.0*i + 1.0          # 1, 3, 5, ..., 2*n-1
        sign  = (-1)**i              # 1, -1, 1, -1, ...
        result = result + sign * 4.0/denom
    return result

def main():
    print " --- pi approximation ---"
    n = input(" How many terms in the series would you like? ")
    answer = pi_approx(n)
    print " Pi is approximately " + str(answer)
    print " which is within " + str(abs(pi - answer)) + " of the true value."

main()
