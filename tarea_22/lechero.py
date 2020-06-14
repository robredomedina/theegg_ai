# Implementación simple recursiva
#
# Devuelve el máximo de litros que se pueden conseguir con un
# camión de tara = "tara"

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

    numero_vacas = 6
    tara_camion = 700
    pesos_vacas = [360, 250, 400, 180, 50, 90] 
    litros_vacas = [40, 35, 43, 28, 12, 13]
    
    litros_totales = lechero(numero_vacas, tara_camion, pesos_vacas, litros_vacas)

    print(litros_totales)
    
if __name__ == '__main__':

    main()


