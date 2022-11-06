import random
import math
import os
from time import perf_counter as pc
import concurrent.futures as future

#Använt list comprehension, lambda, filter
def approx_V_dsphere(n,d): 
    koord_circle = [[(random.uniform(-1,1))**2 for i in range(d)] for j in range(n)]
    r = list(filter(lambda x: x <=1, [sum(koord_circle[l]) for l in range(n)]))

    approx_Vd = (2**d)*(len(r)/n)

    Vd = ((math.pi)**(d/2))/(math.gamma((d/2)+1))

    #return(approx_Vd, Vd)   #För uppgift 1.2
    return(approx_Vd)        #För uppgift 1.3


def main():
    #För uppgift 1.2 
    #print(f'Approximated value for the hyperspehere with dimension 2: {round(approx_V_dsphere(100000,2)[0], 4)}, actual volume: {round(approx_V_dsphere(100000,2)[1], 4)}')
    #print(f'Approximated value for the hyperspehere with dimension 2: {round(approx_V_dsphere(100000,11)[0], 4)}, actual volume: {round(approx_V_dsphere(100000,11)[1], 4)}')
    
    #För uppgift 1.3 
    start = pc()
    approx_V_dsphere(10000000, 11)
    end = pc()
    print(f'Tiden för uppgift 1.2 tog {end-start} sekunder')

    start = pc()
    with future.ProcessPoolExecutor() as ex:
        n = 10**7
        d = 11
        processes = 10
        p = [n//processes for i in range(processes)]
        q = [d for i in range(10)]
        Vd = ((math.pi)**(d/2))/(math.gamma((d/2)+1))

        results = (sum(list(ex.map(approx_V_dsphere, p, q))))/processes

    end = pc()
    print(f'Uträknad volym: {results}')
    print(f'Faktiska volymen: {Vd}')
    print (f'Tiden för uppgift 1.2 med parallellprogrammering tog {end-start} sekunder')
 
    print('Klart!')

if __name__ == "__main__":
    main()


"""
Tiden för uppgift 1.2 tog 40.84667759994045 sekunder
Uträknad volym: 1.890304
Faktiska volymen: 1.8841038793898994
Tiden för uppgift 1.2 med parallellprogrammering tog 10.150740400073119 sekunder
Klart!
"""


