Algoritmo DiagramaDeFlujo
	// Inicialización de variables
	Definir BC, BV, BD, BC2, BM, C, Resto Como Entero
	Definir continuar Como Lógico
	BC <- 0
	BV <- 0
	BD <- 0
	BC2 <- 0
	BM <- 0
	continuar <- Verdadero
	// Entrada de datos
	Escribir 'Ingrese el valor de N (un número entero):'
	Leer N
	C <- N
	// Proceso
	Mientras continuar Hacer
		Si C>=50000 Entonces
			BC <- BC+1
			C <- C-50000
		SiNo
			Si C>=20000 Entonces
				BV <- BV+1
				C <- C-20000
			SiNo
				Si C>=10000 Entonces
					BD <- BD+1
					C <- C-10000
				SiNo
					Si C>=5000 Entonces
						BC2 <- BC2+1
						C <- C-5000
					SiNo
						Si C>=1000 Entonces
							BM <- BM+1
							C <- C-1000
						SiNo
							// Escribir mensaje y salir del bucle
							Escribir 'quit program'
							continuar <- Falso
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
	// Resultado
	Resto <- C
	Escribir 'N: ', N
	Escribir 'BC (>=50000): ', BC
	Escribir 'BV (>=20000): ', BV
	Escribir 'BD (>=10000): ', BD
	Escribir 'BC2 (>=5000): ', BC2
	Escribir 'BM (>=1000): ', BM
	Escribir 'Resto: ', Resto
FinAlgoritmo
