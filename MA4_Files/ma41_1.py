#import matplotlib.pyplot as plt
import random
import math
import os

def M_c_pi(n):
    koordinates_circ_x = []
    koordinates_square_x = []
    koordinates_circ_y = []
    koordinates_square_y = [] 

    for j in range(n):  
        koord = [random.uniform(-1,1), random.uniform(-1,1)]
        if koord[0]**2 + koord[1]**2 <= 1: 
            koordinates_circ_x.append(koord[0])
            koordinates_circ_y.append(koord[1])
        else: 
            koordinates_square_x.append(koord[0])
            koordinates_square_y.append(koord[1])
            
    print(f'Amounth of points inside circle: {len(koordinates_circ_x)}')
    print(f'Approximated pi = {round(4*len(koordinates_circ_x)/n, 3)}')
    print(f'math.pi = {round(math.pi, 3)}')

    #plt.rcParams["figure.figsize"] = (6,6)
    #plt.plot(koordinates_circ_x,koordinates_circ_y,'r.')
    #plt.plot(koordinates_square_x, koordinates_square_y,'b.')
    #plt.savefig()  
    #plt.show()

def main():
    M_c_pi(1000)
    M_c_pi(10000)
    M_c_pi(100000)
    


if __name__ == "__main__":
    main()

