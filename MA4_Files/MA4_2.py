#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
from time import perf_counter as pc

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())

if __name__ == '__main__':
	main()
