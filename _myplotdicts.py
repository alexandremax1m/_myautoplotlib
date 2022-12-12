import matplotlib.pyplot as plt

from matplotlib.pyplot import step,stem,bar,scatter,plot
from matplotlib.pyplot import fill_between,stackplot

_projections = {-7*-1:'aitoff',-6*-1:'hammer',-5*-1:'lambert',-4*-1:'mollweide',-3*-1:'polar',-2*-1:'rectilinear',-1*-1:None}

_pyplotobj = {-2*-1:plt.subplot,-1*-1:plt}
_objmeth2 = {-4*-1:plt.step,-3*-1:plt.stem,-2*-1:plt.bar,-1*-1:plt.scatter,-0*-1:plt.plot}
_objmeth3 = {-1*-1:plt.fill_between,-0*-1:plt.stackplot}

