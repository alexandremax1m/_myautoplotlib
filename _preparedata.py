from ctypes import *
from _pyintoctp import cintn

def _prepare2d(*_2dlist):
	if not _2dlist:
		_2dlist = [[],[]]
		for i in cintn(int(input('How Many Values For XY Axes Sir :: '))):
			_2dlist[0].append(int(input(f'Your Values X {i} Sir :: ')))
			_2dlist[1].append(int(input(f'Your Values Y {i} Sir :: ')))
		_2dlist[0],_2dlist[1] = bytes(_2dlist[0]),bytes(_2dlist[1])
		return _2dlist
	elif type(_2dlist) == list and len(_2dlist) == 2:
		_2dlist[0],_2dlist[1] = bytes(_2dlist[0]),bytes(_2dlist[1])
		return _2dlist
	elif type(_2dlist) == list and len(_2dlist) != 2:
		f"Expecting an [[1,2,..],[2,1,..]]"

def _prepare3d(*_3dlist):
	if not _3dlist:
		_3dlist = [[],[],[]]
		for i in cintn(int(input('How Many Values For XYZ Axes Sir :: '))):
			_3dlist[0].append(int(input(f'Your Values X {i} Sir :: ')))
			_3dlist[1].append(int(input(f'Your Values X {i} Sir :: ')))
			_3dlist[2].append(int(input(f'Your Values X {i} Sir :: ')))
		_3dlist[0],_3dlist[1],_3dlist[2] == bytes(_3dlist[0]),bytes(_3dlist[1]),bytes(_3dlist[2])
		return _3dlist
	elif type(_3dlist) == list and len(_3dlist) == 3:
		_3dlist[0],_3dlist[1],_3dlist[2] == bytes(_3dlist[0]),bytes(_3dlist[1]),bytes(_3dlist[2])
		return _3dlist
	elif type(_3dlist) == list or type(_3dlist) != list and len(_3dlist) != 3:
		return f'Expecting an [[1,2],[2,1],[1,2]]'

preparedatadict = {-2*-1:_prepare3d,-1*-1:_prepare2d}
