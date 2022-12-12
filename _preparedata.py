from ctypes import *
from _pyintoctp import cintn

def _prepare2d():
	_2dlist = [[],[]]
	for i in cintn(int(input('How Many Values For XY Axes Sir :: '))):
		_2dlist[0].append(int(input(f'Your Values X {i} Sir :: ')))
		_2dlist[1].append(int(input(f'Your Values Y {i} Sir :: ')))
	_2dlist[0],_2dlist[1] = bytes(_2dlist[0]),bytes(_2dlist[1])
	return _2dlist

def _prepare3d():
	_3dlist = [[],[],[]]
	for i in cintn(int(input('How Many Values For XYZ Axes Sir :: '))):
		_3dlist[0].append(int(input(f'Your Values X {i} Sir :: ')))
		_3dlist[1].append(int(input(f'Your Values X {i} Sir :: ')))
		_3dlist[2].append(int(input(f'Your Values X {i} Sir :: ')))
	_3dlist[0],_3dlist[1],_3dlist[2] == bytes(_3dlist[0]),bytes(_3dlist[1]),bytes(_3dlist[2])
	return _3dlist

preparedatadict = {-2*-1:_prepare3d,-1*-1:_prepare2d}
