Algoritmo main13A
	workers <- 50
	Total_Nomina <- 0
	worked_hours <- 0
	Escribir 'Nomina Calculation'
	Para worker<-1 Hasta workers Hacer
		Escribir 'Enter worked hours for worker ', worker, ':'
		Leer worked_hours
		salary <- worked_hours*30000
		Total_Nomina <- Total_Nomina+salary
		Escribir 'Worker ', worker, ': Worked hours = ', worked_hours, ', Salary = ', salary
	FinPara
	Escribir 'Total Nomina: ', Total_Nomina, ' bolívares'
FinAlgoritmo
