Algoritmo main9
	Escribir 'enter a positive value'
	Leer N
	Si N<2 Entonces
		Escribir N, ' is not a prime number'
	SiNo
		prime <- Verdadero
		j <- 2
		Mientras j<=raiz(N) Y primo Hacer
			Si N MOD j=0 Entonces
				prime <- Falso
			FinSi
			j <- j+1
		FinMientras
		Si prime Entonces
			Escribir N, ' is a prime number'
		SiNo
			Escribir N, ' is not a prime number'
		FinSi
	FinSi
FinAlgoritmo
