Algoritmo dotb
		Suma <- 0
		N <- 0
		summation <- 0
		Mientras N<>100 Hacer
			N <- N+1
			Si N MOD 2=0 Entonces
				Escribir N
				summation <- summation+N
			FinSi
		FinMientras
		Escribir 'Result of summation of pairs: ', summation
FinAlgoritmo
