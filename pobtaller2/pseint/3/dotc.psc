Algoritmo dotc
	Suma <- 0
	N <- 0
	summation <- 0
	Mientras N<>300 Hacer
		N <- N+1
		Si N MOD 2=1 Entonces
			Escribir N
			summation <- summation+N
		FinSi
	FinMientras
	Escribir 'Result of summation unpairs: ', summation
FinAlgoritmo
