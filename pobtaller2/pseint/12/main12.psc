Algoritmo main12
	total <- 0
	counter <- 0
	score <- -1
	Mientras score<>0 Hacer
		Escribir 'enter score'
		Leer score
		Si score<>0 Entonces
			total <- total+score
			counter <- counter+1
		FinSi
	FinMientras
	Si counter>0 Entonces
		average <- total/counter
		Escribir 'average is: ', average
	FinSi
FinAlgoritmo
