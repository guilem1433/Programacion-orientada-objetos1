Algoritmo main12A
    total <- 0
    counter <- 0
    score <- -1 
	
    Mientras score <> 0 Hacer
        Escribir "enter score:"
        Leer score
		
        Si score <> 0 Entonces
            total <- total + score
            counter <- counter + 1
        FinSi
    FinMientras
	
    // Calcular y mostrar la media
    Si counter > 0 Entonces
        media <- total / counter
        Escribir "media is: ", media
    FinSi
FinAlgoritmo