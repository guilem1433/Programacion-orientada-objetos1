Algoritmo dotA2
	new_score <- -1
	register <- ''
	Escribir 'Enter 1 to execute, 0 to stop'
	Leer value
	Según value Hacer
		1:
			Escribir 'Ingrese un nuevo puntaje:'
			Leer new_score
			Si 19<=new_score Y new_score<=20 Entonces
				register <- 'The score is A'
			FinSi
			Si 16<=new_score Y new_score<=18 Entonces
				register <- 'The score is B'
			FinSi
			Si 13<=new_score Y new_score<=15 Entonces
				register <- 'The score is C'
			FinSi
			Si 10<=new_score Y new_score<=12 Entonces
				register <- 'The score is D'
			FinSi
			Si 1<=new_score Y new_score<=9 Entonces
				register <- 'The score is F'
			FinSi
		De Otro Modo:
			Escribir 'unown value'
	FinSegún
	Escribir register
FinAlgoritmo
