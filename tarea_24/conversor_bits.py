##########################################################

# Conversor de numeros enteros en base 10 a binario

# Tarea 2.4 

##########################################################

import math

valor = int(input("Introduce un número entero: "))

# Calculo el número de bits que ocupa el número introducido
numero_bits = math.floor(math.log(valor,2)) + 1

# Inicializo un array de bits puestos a "0"
bits = [0] * numero_bits

n = numero_bits
suma = 0
# Coloco a "1" los bits correspondientes
while (n >= 0):

    if (suma + 2**(n-1) <= valor):
        suma += 2**(n-1)
        bits[-n] = 1
    n -= 1

if __name__ == '__main__':

    print(str(valor) + " en binario es igual a: \n"+ str(bits))
