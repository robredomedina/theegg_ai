import sys
import itertools
import copy

tara  = int(input("Introduzca la capacidad del camion: "))
pesos = input("Introduzca el peso de las vacas(separados por espacios): ").split(" ")
litros = input("Introduzca el numero de litros de cada vacas(separados por espacios): ").split(" ")
vacas = []
listas_vacas = []

mejor_lista = {
	'lista' : '',
	'litros' : 0
}

def lechero(numero_vacas, n, pesos_vacas, litros_vacas):
	
	temp = zip(pesos, litros)
	for vaca in temp:
		vacas.append(vaca)
	global tara
	tara = n
	listas_vacas.append(vacas)
	
def hacer_sub_listas_vacas(lista):
	
	if not lista:
		return
	for item in lista:
		lista_copy = copy.deepcopy(lista)
		lista_copy.remove(item)
		if (lista_copy not in listas_vacas):
			listas_vacas.append(lista_copy)
		hacer_sub_listas_vacas(lista_copy)
	
def comprobar_pesos(listas):
	listas_a_quitar = []
	for lista in listas:
		sum = 0
		for vaca in lista:
			sum += int(vaca[0])
		if (sum > tara):
			listas_a_quitar.append(lista)
	for lista in listas_a_quitar:
		if lista in listas:
			listas.remove(lista)	
				
def elegir_optimo(listas_vacas):
	for lista in listas_vacas:
		litros = 0
		for vaca in lista:
			litros += int(vaca[1])
		if (litros > mejor_lista['litros']):
			mejor_lista['lista'] = lista 
			mejor_lista['litros'] = litros
	print("mejor_lista: ")
	print(mejor_lista['lista'])
	print("total litros: ")
	print(mejor_lista['litros'])
					
lechero(6, tara, pesos, litros)
print(vacas)
hacer_sub_listas_vacas(vacas)

comprobar_pesos(listas_vacas)
elegir_optimo(listas_vacas)

	
