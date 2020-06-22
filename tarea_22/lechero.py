<<<<<<< HEAD
# Implementación simple recursiva
#
# Devuelve el máximo de litros que se pueden conseguir con un
# camión de tara = "tara"
import time

=======
import sys
import itertools
import copy
>>>>>>> d9660267d13a39f979d66781df7537ed3dd59604

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

<<<<<<< HEAD
    if (pesos[n-1] > tara):
        return lechero(n-1, tara, pesos, litros)

    else:
        return max(
            litros[n-1] + lechero(n-1, tara-pesos[n-1], pesos, litros),
            lechero(n-1, tara, pesos, litros)
        )


def main():

    tara_camion = 2000
    pesos_vacas = [340,355,223,243,130,240,260,155,302,130] 
    litros_vacas = [45,50,34,39,29,40,30,52,31,1]
    numero_vacas = len(pesos_vacas)
    
    tic = time.perf_counter()
    litros_totales = lechero(numero_vacas, tara_camion, pesos_vacas, litros_vacas)
    toc = time.perf_counter()

    print(f"Function run in {toc - tic:0.4f} seconds")

    print(litros_totales)
    
if __name__ == '__main__':

    main()

=======
comprobar_pesos(listas_vacas)
elegir_optimo(listas_vacas)
>>>>>>> d9660267d13a39f979d66781df7537ed3dd59604

	
