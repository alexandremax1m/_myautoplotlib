from ctypes import *

import matplotlib.pyplot as plt

from matplotlib.pyplot import plot,scatter,bar,stem,step
from matplotlib.pyplot import stackplot,fill_between

from _mytestnums import thismuchto10,thismuchto10n

cp,rp,oneipo = c_int * (-1*-1), c_int * (-1*-1), c_int * (-1*-1)
cn,rn, onei = int(input('Columns Number Sir :: ')), int(input('Rows Number Sir :: ')), oneipo(-0*-1)
ip,thislist = c_int * (-(cn)*-(rn)), [x+1 for x in range(cn*rn)]
index = ip(*(tuple(thislist)))

_projections = {-1*-1:'aitoff',-2*-1:'hammer',-3*-1:'lambert',-4*-1:'mollweide',-5*-1:'polar',-6*-1:'rectilinear',-7*-1:None}

for i in index:
	
	_2ddata,_3ddata = [[],[]],[[],[],[]]
	
	if not int(input('2Dimensional Plot :: 2, 3Dimensional Plot ::3  ')) == int(3):
		for j in onei:
			xlab,ylab = str(input('Your XLabel Sir :: ')),str(input('Your YLabel Sir :: '))
			if not _2ddata[j]:
				for k in thismuchto10n(int(input('How Many Values For YX Axes Sir ::'))):
					_2ddata[0].append(int(input(f'Your X Coordinate {k} Sir ::')))
					_2ddata[1].append(int(input(f'Your Y Coordinate {k} Sir ::')))
			pointer0,pointer1 = c_int * (-(int(len(_2ddata[0])))*-1), c_int * (-(int(len(_2ddata[1])))*-1)
			data0,data1 = pointer0(*(tuple(_2ddata[0]))),pointer1(*(tuple(_2ddata[1])))
			b = int(input(f"Choose Projection Style:: 1:aitoff,2:hammer,3:lambert,4:mollweide,5:polar:6:rectilinear,7:none "))
			c = plt.subplot(int(f"{cn}{rn}{i}"),projection=_projections[b])
			c.set_xlabel(xlab)
			c.set_ylabel(ylab)
			while True:
						a = int(input(f"Choose Plotting Style:: 1:Plot,2:Scatter,3:Bar,4:Stem,5:Step,6:Finish "))
						if not a == int(6):							
							plotdict={-1*-1:c.plot,-2*-1:c.scatter,-3*-1:c.bar,-4*-1:c.stem,-5*-1:c.step}
							plotdict[a]([i for i in data0],[i for i in data1])
						elif a == int(6):
							del _2ddata,pointer0,pointer1,data0,data1,a,b
							break
					
	else:
		for j in onei:
			xlab,ylab = str(input('Your XLabel Sir :: ')),str(input('Your YLabel Sir :: '))
			if not _3ddata[j]:
				for k in thismuchto10n(int(input('How Many Values For YXZ Axes Sir :: '))):
					_3ddata[0].append(int(input(f'Your X Coordinate {k} Sir :: ')))
					_3ddata[1].append(int(input(f'Your Y Coordinate {k} Sir :: ')))
					_3ddata[2].append(int(input(f'Your Z Coordinate {k} Sir :: ')))
			pointer0,pointer1,pointer2 = c_int * (-(int(len(_3ddata[0])))*-1),c_int * (-(int(len(_3ddata[1])))*-1),c_int * (-(int(len(_3ddata[1])))*-1)
			data0,data1,data2 = pointer0(*(tuple(_3ddata[0]))),pointer1(*(tuple(_3ddata[1]))),pointer2(*(tuple(_3ddata[2])))
			b = int(input(f"Choose Projection Style:: 1:aitoff,2:hammer,3:lambert,4:mollweide,5:polar:6:rectilinear,7:none "))
			c = plt.subplot(int(f"{cn}{rn}{i}"),projection=_projections[b])
			c.set_xlabel(xlab)
			c.set_ylabel(ylab)
			while True:
						a = int(input(f"Choose Plotting Style:: 1:Stackplot,2:FillBetween,3:Finish "))
						if not a == int(3):				
							plotdict = {-1*-1:c.stackplot,-2*-1:c.fill_between}
							plotdict[a]([i for i in data0],[i for i in data1],[i for i in data2])
						elif a == int(3):
							del _3ddata,pointer0,pointer1,pointer2,data0,data1,data2,a,b
							break

if not str(input('Make Image :: y for YES, n for NO ')) == str('n'):
	plt.savefig(str(input('Your File Name Sir ::')))	

if not str(input('View Plot Sir :: y for YES, n for NO ')) == str('n'):
	plt.show()

#https://github.com/alexandremax1m/_myautoplotlib
