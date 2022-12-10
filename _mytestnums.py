from ctypes import *

def thismuchto10(oneobject):
	return (c_int * (-1*-int(len(oneobject))))(*(tuple(bytes([x for x in range((-1*-int(len(oneobject))))]))))

def thismuchto10n(n):
	return (c_int * (-1*-int(n)))(*(tuple(bytes([x for x in range(n)]))))
