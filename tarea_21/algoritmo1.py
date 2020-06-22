######################################

# Tarea 21 - El algoritmo del biólogo

# Programa pide al usuario que introduzca un número entre el 0.0001 y 0.9999
#
# Devuelve la fracción más simple equivalente a ese número flotante.

######################################
import time

numero = input("Introduce un número entre 0.0001 y 0.9999: ")

try:
    numero = float(numero)
except:
    quit("must me a number")

if (numero <= 0.0001) | (numero > 0.9999):
    quit("Number must be between 0.0001 and 0.9999")
    
numerador = int(numero * 10000)

denominador = 10000

tic = time.perf_counter()

def get_multiplos(numero):
   
    lista = []

    for i in range(1, int(numero) + 1):
        
        if numero % i == 0:

           lista.append(i)

    return lista

lista_numerador = get_multiplos(numerador)

lista_denominador = get_multiplos(denominador)

def encontrar_mcd(lista1, lista2):

    for i in range(len(lista1)-1,0,-1):

        if lista1[i] in lista2:

            return lista1[i]
    
    return 1
        
            

reductor = encontrar_mcd(lista_numerador, lista_denominador)

numerador = numerador/reductor
denominador = denominador/reductor

print("La fracción más reducida de tu número flotante es: ")
print(str(int(numerador)) + '/' + str(int(denominador)))

toc = time.perf_counter()

print(f"Function time is {toc - tic:0.4f} seconds")

