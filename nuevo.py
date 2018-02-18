#!/usr/local/bin/python3.6
""" Esto es un mini aplicacion para sistema operativo en la parte de planificacion por prioridad"""
#Importaciones
import numpy as np
import matplotlib.pyplot as plt, matplotlib.backends.backend_tkagg
#import matplotlib as plt
import collections, tkinter, tkinter.filedialog
import numpy.core._methods, numpy.lib.format 
#Fin Importaciones

class Prioridad(object):
	"""Esta Clase Llamada Prioridad lo que hace es guardar los datos minimo y maximo de este script"""
	min = 0
	max = 1

class Proceso(object):
	"""Esta clase se encarga de pedir los datos y guaradalos para luego se usado mas delatnte para sacar los calculos de dicha script"""
	nombre = ""
	prioridad = -1
	tiempoLlegada = -1
	tiempoEjecucion = -1
	tiempoFinalizacion = -1
	def __init__(self, cPrioridad, ultimoProceso):
		self.nombre = str(input("Ingrese Nombre Del Proceso: "))
		while cPrioridad.min > self.prioridad or cPrioridad.max < self.prioridad:
			self.prioridad = int(input("\tIngrese La Prioridad Del Proceso %s (%s - %s):  " % (self.nombre.title(), cPrioridad.min, cPrioridad.max)))	
		while ultimoProceso >= self.tiempoLlegada:
			self.tiempoLlegada = int(input("\tIngrese Instante De LLegada Del Proceso %s: " % (self.nombre.title())))
		self.tiempoEjecucion = int(input("\tIngrese Tiempo De Ejecucion Del Proceso %s: " % (self.nombre.title())))

def ordenardic(dic):
	"""Esta funcion solo retornara el diccionario ordenador de acuerdo al instante de llegada :D"""
	return collections.OrderedDict(sorted(dic.items()))

prioridad = Prioridad();
prioridad.min = int(input("Ingrese Minimo De Prioridad: "))
prioridad.max = int(input("Ingrese Maximo De Prioridad: "))
procesos = int(input("Ingrese Cuanto Procesos Deseas Ejecutar: "))

cola = {}
ultimaLlegada = -1	
acumTiempo = 0		
graf = {"etiquetas": [], "valores": []}
aparte = []
for i in range(procesos):
	print("\t%i.)" % (int(i+1)))
	proceso = Proceso(prioridad, ultimaLlegada)
	ultimaLlegada = proceso.tiempoLlegada
	graf["etiquetas"].append(proceso.nombre)
	acumTiempo += proceso.tiempoEjecucion
	if proceso.prioridad not in cola:
		cola[proceso.prioridad] = []
	cola[proceso.prioridad].append(proceso)
	aparte.append(proceso)
guardarDatos={}
for proc in aparte:
	guardarDatos[proc.tiempoLlegada]={'nombre':proc.nombre, 'prioridad': proc.prioridad, 'te':proc.tiempoEjecucion}

lineaTiempo = 0
tiempoEspera = 0
lista = {}

while lineaTiempo < (acumTiempo + tiempoEspera):
	nomb = None
	for i in range(prioridad.max, prioridad.min-1, -1):
		if i in cola:
			if cola[i]:
				auxProceso = cola[i][0];
				if lineaTiempo >= auxProceso.tiempoLlegada and auxProceso.tiempoEjecucion > 0:
					auxProceso.tiempoEjecucion -= 1
					nomb = auxProceso.nombre
					if(auxProceso.tiempoEjecucion == 0):
						lista[auxProceso.tiempoLlegada]={'if':lineaTiempo+1}
						auxProceso.tiempoFinalizacion = lineaTiempo
						cola[i].pop(0)
					break
	auxValores = []
	if not nomb:
		tiempoEspera += 1
		for i in graf["etiquetas"]:
			auxValores.append(0)
	else:
		for i in graf["etiquetas"]:
			if(i != nomb):
				auxValores.append(0)
			else:
				auxValores.append(1)
	graf["valores"].append(auxValores)
	lineaTiempo +=1

resultado_lista = ordenardic(lista)
resultado_datos = ordenardic(guardarDatos)
print('- '*83)
acu = 1
for key, value in resultado_datos.items():
	iff = resultado_lista[key]['if']
	ts = iff- int(key)
	te = ts - int(value['te'])
	print("* {a}.) Nombre: {b} | Prioridad: {c} | Instante De Llegada: {d} | Tiempo De Ejecucion: {e} | Instante Finalizacion: {f} | Tiempo De Servicio: {g} | Tiempo De Espera: {h}".format(a=acu, b=value['nombre'],c=value['prioridad'], d=key, e=value['te'], f=iff, g=ts, h=te))
	print('- '*83)
	acu+=1

plt.figure("Resultado en Graficos")
N = len(graf["etiquetas"])
ind = np.arange(N)
width = 0.35

for i in range(len(graf["valores"])):
	invertidos=[]
	for sub_i in range(len(graf["valores"][i])):
		if(graf["valores"][i][sub_i]==0):
			invertidos.append(1)
		else:
			invertidos.append(0)
	
	if(i==0):
		acum = np.array(graf["valores"][i])
		plt.bar(ind, graf["valores"][i], width, color='blue')
	else:
		plt.bar(ind, graf["valores"][i], width, bottom=acum, color='blue')
		acum += np.array(graf["valores"][i])
	
	plt.bar(ind, invertidos, width, bottom=acum, color='lightblue')
	acum += np.array(invertidos)	

thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap("ico.ico")		
plt.ylabel('Tiempo de Ejecucion')
plt.title('Politica de Planificacion De Procesos: Por prioridad')
plt.xticks(ind, graf["etiquetas"])
plt.show()

