import json
import matplotlib.pyplot as plt

from pathlib import Path
from os import getcwd

a,aa = [str(x) for x in Path(getcwd()).iterdir() if str(x).endswith('.json')],{}
aa.update({x:a[x] for x in range(len(a))})

jsonfile = json.load(open(aa[int(input(f'{a} Choose File Sir :: {aa} '))],'rb'))
keyslist = [key for key in jsonfile]
keys,chosenkeys,data = {},[],[]
keys.update({x:keyslist[x] for x in range(len(keyslist))})
chosenkeys.append(keys[int(input(f'{keys}    Your Key Number Sir :: '))])
chosenkeys.append(keys[int(input(f'{keys}    Your Key Number Sir :: '))])
data.append(([i for i in jsonfile[chosenkeys[0]]]))
data.append(([i for i in jsonfile[chosenkeys[1]]]))
datakeys = [key for key in data[0][0]]

if not len(data[0]) != len(data[1]) == True:
	plt.plot(
		[data[0][x][datakeys[0]] for x in range(1,len(data[0]))],
		[data[1][x][datakeys[1]] for x in range(1,len(data[0]))])
	plt.savefig(str(input('Your File Name Sir ::')))
	plt.show()
else:
	print(f'{len(data[0])} :: {len(data[1])} are not symmetric dimensions to initiate the plot ')
