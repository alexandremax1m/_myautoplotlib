from ctypes import *

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,scatter,bar,stem,step
from matplotlib.pyplot import stackplot,fill_between

from _pyintoctp import cintn

from multiprocessing import Process

cp,rp,oneipo = c_int * (-1*-1), c_int * (-1*-1), c_int * (-1*-1)
cn,rn, oneci = int(input('Columns Number Sir :: ')), int(input('Rows Number Sir :: ')), oneipo(-0*-1)
ip,thislist = c_int * (-(cn)*-(rn)), [x+1 for x in range(cn*rn)]
index = ip(*(tuple(thislist)))

_projections = {-1*-1:'aitoff',-2*-1:'hammer',-3*-1:'lambert',-4*-1:'mollweide',-5*-1:'polar',-6*-1:'rectilinear',-7*-1:None}

def thisprocessed():
	
	_2ddata,_3ddata = [[],[]],[[],[],[]]

	for i in index:
		
		if not int(input('2Dimensional Plot :: 2, 3Dimensional Plot ::3  ')) == int(3):
			a = int(input(f"Choose Projection Style:: 1:aitoff,2:hammer,3:lambert,4:mollweide,5:polar:6:rectilinear,7:none "))
			b = plt.subplot(int(f"{cn}{rn}{i}"),projection=_projections[a])
			b.set_xlabel(str(input('Your XLabel Sir :: ')))
			b.set_ylabel(str(input('Your XLabel Sir :: ')))
			for k in cintn(int(input('How Many Values For YX Axes Sir :: '))):
				_2ddata[0].append(int(input(f'Your X Coordinate {k} Sir :: ')))
				_2ddata[1].append(int(input(f'Your Y Coordinate {k} Sir :: ')))
			pointer0,pointer1 = c_int * (-(int(len(_2ddata[0])))*-1), c_int * (-(int(len(_2ddata[1])))*-1)
			data0,data1 = pointer0(*(tuple(_2ddata[0]))),pointer1(*(tuple(_2ddata[1])))
			while True:
				c = int(input(f"Choose Plotting Style:: 1:Plot,2:Scatter,3:Bar,4:Stem,5:Step,6:Finish "))
				if not c == int(6):
					plotdict={-1*-1:b.plot,-2*-1:b.scatter,-3*-1:b.bar,-4*-1:b.stem,-5*-1:b.step}						
					plotdict[c]([i for i in data0],[i for i in data1])
				elif c == int(6):
					del _2ddata,pointer0,pointer1,data0,data1,a,b
					break					
		else:
			a = int(input(f"Choose Projection Style:: 1:aitoff,2:hammer,3:lambert,4:mollweide,5:polar:6:rectilinear,7:none "))
			b = plt.subplot(int(f"{cn}{rn}{i}"),projection=_projections[a])
			b.set_xlabel(str(input('Your XLabel Sir :: ')))
			b.set_ylabel(str(input('Your XLabel Sir :: ')))
			for k in cintn(int(input('How Many Values For YXZ Axes Sir :: '))):
				_3ddata[0].append(int(input(f'Your X Coordinate {k} Sir :: ')))
				_3ddata[1].append(int(input(f'Your Y Coordinate {k} Sir :: ')))
				_3ddata[2].append(int(input(f'Your Z Coordinate {k} Sir :: ')))
			pointer0,pointer1,pointer2 = c_int * (-(int(len(_3ddata[0])))*-1),c_int * (-(int(len(_3ddata[1])))*-1),c_int * (-(int(len(_3ddata[1])))*-1)
			data0,data1,data2 = pointer0(*(tuple(_3ddata[0]))),pointer1(*(tuple(_3ddata[1]))),pointer2(*(tuple(_3ddata[2])))
			while True:
				c = int(input(f"Choose Plotting Style:: 1:Stackplot,2:FillBetween,3:Finish "))
				if not c == int(3):				
					plotdict = {-1*-1:b.stackplot,-2*-1:b.fill_between}
					plotdict[c]([i for i in data0],[i for i in data1],[i for i in data2])
				elif c == int(3):
					del _3ddata,pointer0,pointer1,pointer2,data0,data1,data2,a,b
					break

	if not str(input('Make Image :: y for YES, n for NO ')) == str('n'):
		plt.savefig(str(input('Your File Name Sir ::')))	

	if not str(input('View Plot Sir :: y for YES, n for NO ')) == str('n'):
		plt.show()

if __name__ != "__main__":
	Process(target=thisprocessed()).start()
#https://github.com/alexandremax1m/_myautoplotlib
