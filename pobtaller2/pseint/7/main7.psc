Algoritmo main7
	Escribir 'enter new score'
	new_score <- 0
	Leer new_score
	register <- texto
	Si new_score>=19 Y new_score<=20 Entonces
		register <- 'the score is A'
	FinSi
	Si new_score>=16 Y new_score<=18 Entonces
		register <- 'the score is B'
	FinSi
	Si new_score>=13 Y new_score<=15 Entonces
		register <- 'the score is C'
	FinSi
	Si new_score>=10 Y new_score<=12 Entonces
		register <- 'the score is D'
	FinSi
	Si new_score>=1 Y new_score<=9 Entonces
		register <- 'the score is E'
	FinSi
	Escribir register
	main7()
FinAlgoritmo
