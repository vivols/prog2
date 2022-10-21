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
	


	'''f = Person(5)
	print(f.get())
	print(f.fib()) 
	
	print(fib_py(8))
	print(fib_numba(7))'''

	times_numba = []
	times_cpp = []
	times_py = []
	x = range(30,45,1)


	for i in range(x):
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

	
	print(times_py, times_numba, times_cpp)

	plt.plot(x, times_py, label='Python')
	plt.plot(x, times_numba, label='Numba')
	plt.plot(x, times_cpp, label='C++')
	plt.savefig('plot_MA42_30_45.png')



if __name__ == '__main__':
	main()
