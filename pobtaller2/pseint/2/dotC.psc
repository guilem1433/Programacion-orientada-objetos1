
	Algoritmo lower2
		Escribir 'Enter values'
		Leer value1, value2, value3
		Mientras value1=value2 O value2=value3 O value1=value3 Hacer
			Escribir 'Values should be different'
			Leer value1, value2, value3
		FinMientras
		Si value1<value2 Y value1<value3 Entonces
			Escribir value1, ' is lower'
		SiNo
			Si value2<value1 Y value2<value3 Entonces
				Escribir value2, ' is lower'
			SiNo
				Escribir value3, ' is lower'
			FinSi
		FinSi
FinAlgoritmo
	
