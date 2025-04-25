Algoritmo dota
	n <- -1
	Mientras n<>0 Hacer
		Escribir 'enter number of values'
		Leer n
		Si n=0 Entonces
			Escribir 'exiting program'
		SiNo
			c50_70 <- 0
			c_over_80 <- 0
			c_less_30 <- 0
			Para i<-1 Hasta n Hacer
				Escribir 'enter values'
				valor <- 0
				Leer valor
				Si valor<=50 Y valor<=75 Entonces
					c50_70 <- c50_70+1
				FinSi
				Si valor>80 Entonces
					c_over_80 <- c_over_80+1
				FinSi
				Si valor<30 Entonces
					c_less_30 <- c_less_30+1
				FinSi
			FinPara
			Escribir 'numbers 50-75:', c50_70
			Escribir 'numbers over 80:', c_over_80
			Escribir 'numbers under 30:', c_less_30
		FinSi
	FinMientras
FinAlgoritmo
