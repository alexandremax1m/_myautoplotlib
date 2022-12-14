import json
import matplotlib.pyplot as plt

from pathlib import Path
from os import getcwd

a,aa = [str(x) for x in Path(getcwd()).iterdir() if str(x).endswith('.json')],{}

for x in range(len(a)):
	aa.update({x:a[x]})

jsonfile = json.load(open(aa[int(input(f'{a} Choose File Sir :: {aa} '))],'r'))
keyslist = [key for key in jsonfile]
keys,chosenkeys,data = {},[],[]

for x in range(len(keyslist)):
	keys.update({x:keyslist[x]})
for x in range(2):
	print(keys)
	chosenkeys.append(keys[int(input('Your Key Number Sir :: '))])
	data.append([i for i in jsonfile[chosenkeys[x]]])

datakeys = [key for key in data[0][0]]

plt.plot(
	[data[0][x][datakeys[0]] for x in range(1,len(data[0]))],
	[data[1][x][datakeys[1]] for x in range(1,len(data[0]))])
plt.show()

### foo([data[0]...]) >> apply a function to every variable in data[0]['key'],data[1]['key']

#for x in range(1,len(data[0])):
	#data1.append(int(data[0][x][datakeys[0]]))
	#data2.append(int(data[0][x][datakeys[1]]))	

#plt.plot((data[0])[datakeys[0]],(data[1])[datakeys[1]])
#plt.savefig(str(input('Your File Name Sir ::')))
#plt.show()
