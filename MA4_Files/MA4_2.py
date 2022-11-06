#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc
from numba import njit 


def main():

	def fib_py(n):
		if n <= 1:
			return n
		else:
			return(fib_py(n-1) + fib_py(n-2))
	
	@njit 
	def fib_numba(n):
		if n <= 1:
			return n
		else:
			return(fib_numba(n-1) + fib_numba(n-2))
	
    
	times_numba = []
	times_cpp = []
	times_py = []
	#x = range(30,45,1)
	#x = range(20,30,1)

    
	'''for i in x:
		start = pc()
		fib_py(i)
		end = pc()
		times_py.append(end-start)

		start = pc()
		fib_numba(i)
		end = pc()
		times_numba.append(end-start)

		start = pc()
		f = Person(i)
		f.fib() 
		end = pc()
		times_cpp.append(end-start)
		hejehje'''

	

	'''plt.plot(x, times_py, label='Python')
	plt.plot(x, times_numba, label='Numba')
	plt.plot(x, times_cpp, label='C++')
	plt.legend(['Python', 'Numba', 'C++']) 
	plt.savefig('plot_MA42_30_45.png')
	print('done')'''

	'''plt.plot(x, times_py, label='Python')
	plt.plot(x, times_numba, label='Numba')
	plt.legend(['Python', 'Numba']) 
	plt.savefig('plot_MA42_20_30.png')
	print('done')'''


	#for n = 47
	print(f'Fibonacci for n = 47, using Numba: ',fib_numba(47))

	f = Person(47)
	print(f'Fibonacci for n = 47, using C++: ',f.fib())
	
	print('done')

    #Fibonacci for n = 47, using Numba:  2971215073
    #Fibonacci for n = 47, using C++:  -1323752223    ???
    #done
	#(quick google search says): For integers larger than 2^31, c++ handles it as a negative value. You can use Bigint data type to solve that problem.


if __name__ == '__main__':
	main()
