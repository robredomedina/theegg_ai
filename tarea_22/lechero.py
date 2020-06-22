# Implementación simple recursiva
#
# Devuelve el máximo de litros que se pueden conseguir con un
# camión de tara = "tara"
import time


def lechero(n, tara, pesos, litros):

    if n == 0 or tara == 0:
        return 0


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


