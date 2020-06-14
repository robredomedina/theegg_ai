/*1. - Para este prop�sito tienes que definir las siguientes entradas :
	Entrada: N�mero total de vacas en la zona de Tolosa que est�n a la venta.
	Entrada : Peso total que el cami�n puede llevar.
	Entrada : Lista de pesos de las vacas.
	Entrada : Lista de la producci�n de leche por vaca, en litros por d�a.
	2. - El algoritmo que programes tiene que calcular la siguiente salida :
	Salida: Cantidad m�xima de producci�n de leche se puede obtener
*/

#include <iostream>

int max(int a, int b) {
	return (a > b) ? a : b;
}

int lechero(int n, int tara, int pesos[], int litros[]) {

	if (n == 0 || tara == 0) {
		return 0;
	}

	if (pesos[n - 1] > tara) {
		return lechero(n - 1, tara, pesos, litros);
	}

	else {
		return max(
			litros[n - 1] + lechero(n - 1, tara - pesos[n - 1], pesos, litros),
			lechero(n - 1, tara, pesos, litros));
	};
}

int main() {

	int vacas = 6;
	int tara = 700;
	int pesos[] = { 360, 250, 400, 180, 50, 90 };
	int litros[] = { 40, 35, 43, 28, 12, 13 };

	int litros_totales = lechero(vacas, tara, pesos, litros);

	std::cout << "Litros totales: " << litros_totales << std::endl;
}