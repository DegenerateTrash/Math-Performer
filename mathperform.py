import numpy as np
import os
import math
from decimal import Decimal
from fractions import Fraction
import time

print(len(str(0.45)))

def factorising(a,b,c):
    ### Todo Add support for coefficients
    roots = solvefact(a,b,c)
    print("(x + {0})(x + {1}) | Currently only works with coeffficient of 1".format(roots[0] * -1 , roots[1] * -1 ))

def expandbracket(a,b,c,d):
    #(ax + b)(cx + d)
    #(ax * cx) + (ax * d) + (b * cx) + (b * d)
    print("({}x + {})({}x + {}) is {}x^2 + {}x + {}".format(a,b,c,d,a*c, (a*d)+(b*c), b*d))


def solvefact(a,b,c):

    #ax^2+bx+c
    roots = [0,0]
    x = -30
    """
    -b +- sqrt ( b ^2 - 4ac
                2a
    """
    start = time.time()
    try:
        roots[0], roots[1] = ((-b) + math.sqrt(pow(b,2) - (4*a*c))) / (2*a) , ((-b) - math.sqrt(pow(b,2) - (4*a*c))) / (2*a)
        print(roots)
    except ValueError:
        print("{0}x^2 + {1}x + {2} has no roots.".format(a,b,c)) 
    print("{0:0.10f} seconds".format(time.time() - start ))
    #Looping Table Method Works
    """start = time.time()
    roots = []
    while len(roots) < 2:
        #y = (a*pow(x,2))+(b*x)+(c) 
        x += 0.1
        y = 0
        y += a*float((round(x,10)**2))
        y += b*float(round(x,10))
        y += c

        #print("{0} | {1}".format(round(x,10),y))
        if y == 0:
            roots.append(round(x,10))
        if len(roots) == 2:
            break
    print(roots)
    print("{0:0.10f} seconds".format(time.time() - start ))"""
    print("Roots: {} {}".format(roots[0],roots[1]))
    return roots

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
#d = float(input("d: "))

factorising(a,b,c)
