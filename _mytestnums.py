from ctypes import *

def thismuchto10(oneobject):
	return (c_int * (-1*-int(len(oneobject))))(*(tuple(bytes([x for x in range((-1*-int(len(oneobject))))]))))

def thismuchto10n(n):
	return (c_int * (-1*-int(n)))(*(tuple(bytes([x for x in range(-1*-int(n))]))))

def bign(n):
	return (c_int * (-1*-int(n)))(*(tuple([x for x in range(-1*-int(n))])))

# https://github.com/alexandremax1m/_myautoplotlib
# test,only use if later need to interact with c because of pointers c_int * n and c datatypes supporting
# the return of the function is just a pointer with (n) this much values, and the defined array of length (n)
# main purpose is creating and modifying later on file descriptors for faster data processing with c
# suitable for socket programming,tkinter,matplotlib,..
