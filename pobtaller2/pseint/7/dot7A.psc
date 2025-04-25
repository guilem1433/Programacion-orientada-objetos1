Algoritmo dot7A
	new_score <- -1
	Mientras new_score<>0 Hacer
		Escribir 'enter score'
		Leer new_score
		Si new_score=0 Entonces
			Escribir 'quiting program'
		SiNo
			register <- cadena
			Si 19<=new_score Y new_score<=20 Entonces
				register <- 'the score is A'
			FinSi
			Si 16<=new_score Y new_score<=18 Entonces
				register <- 'the score is B'
			FinSi
			Si 13<=new_score Y new_score<=15 Entonces
				register <- 'the score is C'
			FinSi
			Si 10<=new_score Y new_score<=12 Entonces
				register <- 'the score is D'
			FinSi
			Si 1<=new_score Y new_score<=9 Entonces
				register <- 'the score is F'
			FinSi
			Escribir register
		FinSi
	FinMientras
FinAlgoritmo
