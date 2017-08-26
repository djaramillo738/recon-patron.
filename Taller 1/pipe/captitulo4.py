
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import re
from sklearn.metrics import confusion_matrix

import numpy as np


weekly=pd.read_csv(r"C:\Users\pipe_\OneDrive\Documents\Matematicas\Maestria\Reconocimiento_de_Patrones\Tarea1\Weekly.csv")

#print (weekly.head())

cuanti= weekly.drop( "Direction", 1)

#print(cuanti.describe())
#### Scatter matrix  AAAAA
##scatter_matrix(cuanti, alpha=0.1)
#plt.show()

#### CCCCC
##print(cuanti.head())

confusion_matrix(cuanti["Year"], cuanti["Lag3"])
plt.show