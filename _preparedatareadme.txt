## _preparedatausage

from _preparedata import preparedatadict
import matplotlib.pyplot as plt

a = preparedatadict[1]()
plt.plot([i for i in a[0],[i for i in a[1]])
