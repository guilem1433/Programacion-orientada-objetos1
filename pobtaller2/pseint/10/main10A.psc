Algoritmo main10A
	Escribir ' enter number of entries'
	entries <- 0
	price <- 500
	Leer entries
	Si entries>4 Entonces
		Escribir ' limit of 4 entries'
	SiNo
		Escribir entries, ' entries billed'
		Si entries=2 Entonces
			payment <- (entries*500)*0.9
		FinSi
		Si entries=3 Entonces
			payment <- (entries*500)*0.85
		FinSi
		Si entries=4 Entonces
			payment <- (entries*500)*0.8
		FinSi
		Escribir ' bill of ', payment
	FinSi
FinAlgoritmo
