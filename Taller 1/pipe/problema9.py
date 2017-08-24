
import pandas as pd 
import matplotlib.pyplot as plt
import re

import numpy as np



auto=pd.read_csv(r"C:\Users\pipe_\OneDrive\Documents\Matematicas\Maestria\Reconocimiento_de_Patrones\Tarea1\Auto.csv")
print (auto)

### SE LIMPIAN LAS FILAS QUE TENGAN UN DATO QUE NO ME SIRVA
### LIMPIAMOS HORSEPOWER
for i in range(len(auto["horsepower"])):

	try:

	
		auto.set_value(i,"horsepower",float(auto["horsepower"][i]))

	except:
		auto.set_value(i,"horsepower", np.NaN)
### LIMPIAMOS MPG		

for i in range(len(auto["mpg"])):

	try:

	
		auto.set_value(i,"mpg",float(auto["mpg"][i]))

	except:
		auto.set_value(i,"mpg", np.NaN)
### LIMPIAMOS DISPLACEMENT		

for i in range(len(auto["displacement"])):

	try:

	
		auto.set_value(i,"displacement",float(auto["displacement"][i]))

	except:
		auto.set_value(i,"displacement", np.NaN)
###LIMPIAMOS WEIGHT		


for i in range(len(auto["weight"])):

	try:

	
		auto.set_value(i,"weight",float(auto["weight"][i]))
		#contador++
		#suma+=float(auto["horsepower"][i])
	except:
		auto.set_value(i,"weight", np.NaN)
### LIMPIAMOS ACCELERATION		


for i in range(len(auto["acceleration"])):

	try:

	
		auto.set_value(i,"acceleration",float(auto["acceleration"][i]))
		#contador++
		#suma+=float(auto["horsepower"][i])
	except:
		auto.set_value(i,"acceleration", np.NaN)
	
auto.dropna(how="any")	

#BBBB El rango de cada variable cuantitativa
rangos=[[min(auto["mpg"]), max(auto["mpg"])],[min(auto["cylinders"]), max(auto["cylinders"])], [min(auto["displacement"]), max(auto["displacement"])],[min(auto["horsepower"]), max(auto["horsepower"])], [min(auto["weight"]), max(auto["weight"])],[min(auto["acceleration"]), max(auto["acceleration"])]]

#CCCC Las medias de todas las columnas cuantitativas		
medias=[np.mean(auto["mpg"]), np.mean(auto["cylinders"]), np.mean(auto["displacement"]), np.mean(auto["horsepower"]), np.mean(auto["weight"]), np.mean(auto["acceleration"])]
#CCCC Desviación estándar de las cuatitativas
print((np.std(np.array(auto["horsepower"]))))
desviaciones=[(np.std(np.array(auto["mpg"]))),(np.std(np.array(auto["cylinders"]))),(np.std(np.array(auto["displacement"]))),(np.std(np.array(auto["horsepower"]))),(np.std(np.array(auto["weight"]))),(np.std(np.array(auto["acceleration"])))]
#DDDD Elimino las filas de la 10 a la 85 y calculo los rangos, medias y desviaciones
auto_nuevo=auto.drop(auto.index[10:85])
rangos_nuevo=[[min(auto_nuevo["mpg"]), max(auto_nuevo["mpg"])],[min(auto_nuevo["cylinders"]), max(auto_nuevo["cylinders"])], [min(auto_nuevo["displacement"]), max(auto_nuevo["displacement"])],[min(auto_nuevo["horsepower"]), max(auto_nuevo["horsepower"])], [min(auto_nuevo["weight"]), max(auto_nuevo["weight"])],[min(auto_nuevo["acceleration"]), max(auto_nuevo["acceleration"])]]
medias_nuevo=[np.mean(auto_nuevo["mpg"]), np.mean(auto_nuevo["cylinders"]), np.mean(auto_nuevo["displacement"]), np.mean(auto_nuevo["horsepower"]), np.mean(auto_nuevo["weight"]), np.mean(auto_nuevo["acceleration"])]
desviaciones_nuevo=[(np.std(np.array(auto_nuevo["mpg"]))),(np.std(np.array(auto_nuevo["cylinders"]))),(np.std(np.array(auto_nuevo["displacement"]))),(np.std(np.array(auto_nuevo["horsepower"]))),(np.std(np.array(auto_nuevo["weight"]))),(np.std(np.array(auto_nuevo["acceleration"])))]

print (desviaciones, desviaciones_nuevo)

print(medias, medias_nuevo)
